import re
import os
import time
import datetime
import pandas as pd
from io import StringIO 

import sys
sys.path.append("src")
from ndpprep.secret_key.main import read_secret_key
from ndpprep.shp_file.mygeospatial import convert_shapefile_to_parquet, shp_from_edgenode, unzip_file

extraction_date = datetime.date.today()

def refresh_shapefile(extraction_date, secret_path, target_user, target_ip, target_path):
    # EdgeNode -> CDSW
    local_directory = "/home/cdsw/CODE/SHAPEFILE"
    remote_user = "ndp"
    remote_ip = "172.21.131.36"
    shp_remote_path = "/edge04_mount/vda_data/ingestion/neps/sourcefiles/shpFiles.zip"

    shp_from_edgenode(remote_user, remote_ip, shp_remote_path, local_directory)

    # unzip
    zip_file = "/home/cdsw/PIPELINE/SHAPEFILE/shpFiles.zip"
    extract_to = local_directory
    unzip_file(zip_file, extract_to)

    # CDSW -> SFTP
    dbname = "raw_neps.db"
    dataset_name = "SHAPEFILE"
    secret_key = read_secret_key(secret_path)

    shp_folder_path = local_directory + "/shp/"

    for filename in os.listdir(shp_folder_path):
        if filename.endswith(".shp"):
            pqFile = filename.replace(".shp","")+".parquet"
            region = filename.split('_')[0]
            element = filename.replace(region+"_","").replace("_BND","").replace("_DATA","").replace(".shp","")
            print("\n======= START CONVERT SHAPE FILE ["+str(filename)+"] to PARQUET=======")
            dfParquet = convert_shapefile_to_parquet(shp_folder_path + filename, element, pqFile, dbname, dataset_name, secret_key, target_user, target_ip, target_path)
            print("Parquet data : \n",dfParquet.shape[0])
            
            
