import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import geopandas as gpd
from shapely.geometry import Polygon, Point
from rtree import index
import shapely
import fiona
import math
import os
import subprocess
import zipfile
import datetime
from datetime import datetime
import time
import yaml
import warnings
warnings.filterwarnings("ignore")

import sys
sys.path.append("src")
from ndpprep.masked.main import masked_uuid, update_mapping
from ndpprep.secret_key.main import read_secret_key
from ndpprep.encryption.main import encrypt_table
from ndpprep.save_sftp.main import save_to_sftp

"""
# take shpFile.zip from EdgeNode to CDSW 
# unzip file and process to parquet + mask
# parquet send to SFTP
# /edge04_mount/vda_data/ingestion/neps/sourcefiles/
"""
def shp_from_edgenode(remote_user, remote_ip, shp_remote_path, cdsw_direcory):
    # Copy files from remote directory to local
    copy_command = f"scp -r {remote_user}@{remote_ip}:{shp_remote_path} {cdsw_direcory}/"
    try:
        subprocess.run(copy_command, shell=True, check=True)
        print("Files from EdgeNode copied successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while copying files: {e}")
        
def unzip_file(zip_file, extract_to):
    """
    Unzips a ZIP file to the specified directory.

    Args:
        zip_file (str): Path to the ZIP file to be extracted.
        extract_to (str): Directory where the contents of the ZIP file will be extracted.
    """
    # Ensure the extraction directory exists
    os.makedirs(extract_to, exist_ok=True)
    
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

#=========================================================================================
# check the schema exist in schema_config.yaml file and write the schema
# that not exists in the folder and file reports/mygeospatial-failed.txt
#=========================================================================================
def is_schema_exist(fn):
    # Step 1: Read schema_config.yaml file
    with open('/home/cdsw/PIPELINE/schema_config.yaml', 'r') as f:
        config = yaml.safe_load(f)

    found = False
    # Step 2: check the schema element exist or not in the config list
    for schema_name, schema_data in config['schemas'].items():
        if schema_name == fn:
            found = True
            break

    # Step 3: Save failed results to a file in reports directory
    if not found:
        report_file_dir = "/home/cdsw/PIPELINE/OUTPUT/LOG/"
        os.makedirs(report_file_dir, exist_ok=True)
        report_file_path = os.path.join(report_file_dir, "mygeospatial-failed.txt")
        with open(report_file_path, "a") as file:
            current_datetime = datetime.now()
            formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"\n{formatted_datetime} - Failed results: Schema not found\n")
            file.write(f"The schema {fn} does not exist in schema_config.yaml\n")

    return found


#=========================================================================================
# get the schema in schema_config.yaml file
#=========================================================================================
def read_schema(fn):
    # Step 1: Read schema_config.yaml file
    with open('/home/cdsw/PIPELINE/schema_config.yaml', 'r') as f:
        config = yaml.safe_load(f)

    schemas = {}
    # Step 2: get the schema base on the element in the filename 
    for schema_name, schema_data in config['schemas'].items():
        if schema_name == fn:
            print("schema_name : ",schema_name)
            fields = []
            for field_info in schema_data['fields']:
                field_name = field_info['name']
                field_type = field_info['type']
                metadata = {'req': field_info['metadata']} if 'metadata' in field_info else {}
                if field_type == 'string':
                    field_type = pa.string()
                elif field_type == 'float64':
                    field_type = pa.float64()
                elif field_type == 'int32':
                    field_type = pa.int32()
                fields.append(pa.field(field_name, field_type, metadata=metadata))
            schemas[schema_name] = pa.schema(fields)
            break

    return schemas[fn]

def read_parquet(fn):
    df = pd.read_parquet(fn)
    # Convert the "geometry" column from Well-Known Text (WKT) format to a GeoSeries geometry
    df["geometry"] = gpd.GeoSeries.from_wkt(df["geometry"])
    return df

#=========================================================================================
# convert shape file to parquet file and call is_schema_exist function
# to check the schema exist in schema_config.yaml file and call
# read_schema function to get the schema in schema_config.yaml file
# and write the successfull generate parquet file into reports/mygeospatial-success.txt
#=========================================================================================
def convert_shapefile_to_parquet(fn, sch, pfn,  dbname, dataset_name, private_key, target_user, target_ip, target_path):
    # Step 1: Read the shapefile into a GeoDataFrame
    dbname = "raw_neps.db"
    colint = ["G3E_FNO","G3E_FID","VGC_BND_P_"]
    colfloat = ["GC_DDP_BND","GC_FDC_BND"]
    read_start = time.time()
    gdf = gpd.read_file(fn)
    read_duration = time.time() - read_start
 
    # Step 2a: Convert the geometry column to Well-Known Text (WKT) format
    gdf['geometry'] = gdf.geometry.apply(lambda x: shapely.wkt.dumps(x))
    # Step 2b: Convert the int64 format column to string format
    for column_name in gdf.columns:
        if column_name in colint:
            gdf[column_name] = gdf[column_name].astype('int64').astype('string')
    # Step 2c: Convert the float64 format column to string format
    for column_name in gdf.columns:
        if column_name in colfloat:
            gdf[column_name] = gdf[column_name].astype('float64').astype('string')

    df = pd.DataFrame()
    if is_schema_exist(sch):
        schemaShp = read_schema(sch)
        # Step 3: Convert GeoDataFrame to PyArrow Table
        tbl = pa.Table.from_pandas(gdf, schema=schemaShp)

        # Step 4: Write PyArrow Table to Parquet file with metadata
        #parquet_file_path = 'data/myshapefile.parquet'
        pq.write_table(tbl, pfn)
        print('The Parquet file written into : ',pfn)
        
        # Step 5: Read Parquet into dataframe
        df = pd.read_parquet(pfn)
        
        # Step 6: Masking data
        modified_columns = []
        masked_start = time.time()
        cnt_column_masked = 0
        masked_columns = []
        original_columns = []
                    
        for col_name in tbl.schema.names:
            if tbl.schema.field(col_name).metadata and tbl.schema.field(col_name).metadata.get(b"req") == b"sensitive":
                print(f"(MASKED) Processing sensitive column '{col_name}' with metadata: {tbl.schema.field(col_name).metadata}")
                original_columns.append(tbl[col_name])
                cnt_column_masked += 1
                modified_column = [masked_uuid(str(val)) for val in tbl[col_name]]
                masked_columns.append(modified_column)
            else:
                #print(f"Processing column '{col_name}' with metadata: {tbl.schema.field(col_name).metadata}")
                modified_column = tbl[col_name]

            modified_columns.append(modified_column)

        update_mapping(original_columns, masked_columns, dbname)

        tbl = pa.table(modified_columns, schema=tbl.schema)
        masked_duration = time.time() - masked_start
        total_row_count = len(tbl)

        # Step 7: Encrypting data
        output_folder = f'{dbname}/{dataset_name}'
        os.makedirs(output_folder, exist_ok=True)
        output_file = os.path.join(output_folder, pfn)
        # print(output_file)
        
        encrypt_start = time.time()
        encrypt_table(tbl, output_file, private_key)
        encrypt_duration = time.time() - encrypt_start
        memory_size_mb = tbl.nbytes / (1024 * 1024)
        #logging.info(output_file)
        
        # Step 8: Uploading encrypted data to SFTP    
        sftp_start = time.time()
        save_to_sftp(output_file, target_user, target_ip, target_path)
        sftp_upload_duration = time.time() - sftp_start
        
        # Step 9: Save success results to a file in reports directory
        report_file_dir = "/home/cdsw/PIPELINE/OUTPUT/LOG/"
        os.makedirs(report_file_dir, exist_ok=True)
        report_file_path = os.path.join(report_file_dir, "mygeospatial-success.txt")
        with open(report_file_path, "a") as file:
            current_datetime = datetime.now()
            formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"\n{formatted_datetime} - Success results: {sch} Schema\n")
            file.write(f"The Shape file from :  {fn} \n")
            file.write(f"The Parquet file written into :  {output_file} \nTotal Record : {gdf.shape[0]}\n")
        
        # Logging durations
        with open(log_file_path, "a") as log_file:
            log_file.write(f"{output_file}: \nread_duration: {read_duration:.2f} seconds,\nmasked_duration: {masked_duration:.2f} seconds, \nencrypt_duration: {encrypt_duration:.2f} seconds, \nupload_to_sftp_duration: {sftp_upload_duration:.2f} seconds, \ncount masked column: {cnt_column_masked}, \nmemory size (mb): {memory_size_mb}\n\n")
            
    else:
        print('The schema '+str(sch)+' for file '+str(fn)+' not exists in schema_config.yaml')

    return df

#=========================================================================================
# function used by convert_shapefile function to convert coordinates
# from EPSG:3857 to EPSG:4326
#=========================================================================================
def mercator_to_lonlat(x, y):
    '''
    The provided mercator_to_lonlat function converts coordinates from the 
    Web Mercator projection (EPSG:3857) to latitude and longitude in the 
    WGS84 coordinate system (EPSG:4326). 
    Here's a breakdown of how it works:

    1)It first converts the X-coordinate (longitude) from meters to degrees 
    using the formula (x / 20037508.34) * 180. 
    This formula scales the X-coordinate by the circumference of the Earth 
    at the Equator (approximately 40,075,008.34 meters) to get a value in degrees.

    2)It then converts the Y-coordinate (latitude) from meters to degrees using 
    a series of calculations involving the natural logarithm and the arctangent 
    function. This process is based on the inverse Mercator projection formula. 
    The detailed explanation is as follows:
    - Divide the Y-coordinate by the Earth's radius (20037508.34) to get a value between -1 and 1.
    - Multiply by 180 to convert from radians to degrees.
    - Calculate the latitude using the formula 2 * atan(exp(y * pi / 180)) - pi / 2, 
      where exp is the exponential function and atan is the arctangent function.
    - Convert the latitude from radians to degrees using the formula 180 / pi.

    3)The function returns the resulting longitude and latitude as a tuple (lon, lat).
    '''
    lon = (x / 20037508.34) * 180
    lat = (y / 20037508.34) * 180
    lat = 180 / math.pi * (2 * math.atan(math.exp(lat * math.pi / 180)) - math.pi / 2)
    return lon, lat

#=========================================================================================
# convert shape file and call function mercator_to_lonlat to convert coordinates 
#=========================================================================================
def convert_shapefile(fn):
    gdf = gpd.read_file(fn)
    # Iterate over each row in the GeoDataFrame
    for index, row in gdf.iterrows():
        # Access the geometry of the current row
        geometry = row['geometry']
        if isinstance(geometry, Polygon):
            # Divide each coordinate of the Polygon in mercator_to_lonlat function
            new_coords = [mercator_to_lonlat(x, y) for x, y in geometry.exterior.coords]
            new_polygon = Polygon(new_coords)
            # Update the geometry column with the new Polygon
            gdf.at[index, 'geometry'] = new_polygon
    
    return gdf

#=========================================================================================
# function used to find boundary
#=========================================================================================
def find_myboundary(point, polygon_gdf):
    point_geom = Point(point)
    inout_boundry = "out_of_boundry"

    for index, row in polygon_gdf.iterrows():
        if point_geom.within(row['geometry']):
            inout_boundry = "in_the_boundry" #row['BND_ID']
            break
    
    # If the point is not inside any polygon, return out_of_boundry value
    return inout_boundry

#=========================================================================================
# function used to check if in the boundary
#=========================================================================================
def point_inside_polygon(point, polygon_gdf):
    point_geom = Point(point)
    inside_boundry = False

    for _, polygon in polygon_gdf.iterrows():
        if point_geom.within(polygon['geometry']):
            inside_polygon = True
            break
    
    # If the point is not inside any polygon, return False value
    return inside_boundry

  
log_file_path = "/home/cdsw/PIPELINE/OUTPUT/LOG/runtime_log.txt"
