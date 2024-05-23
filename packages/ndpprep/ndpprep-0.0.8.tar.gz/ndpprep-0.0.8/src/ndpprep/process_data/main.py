import pyarrow as pa
import pyarrow.parquet as pq
from importlib import import_module
import re
import os
import time
from datetime import datetime
import pandas as pd
from io import StringIO 

import sys
sys.path.append("src")
from ndpprep.masked.main import masked_uuid, update_mapping
from ndpprep.target_schema.granite import *
from ndpprep.target_schema.nis import *
from ndpprep.target_schema.neps import *
from ndpprep.secret_key.main import read_secret_key
from ndpprep.encryption.main import encrypt_table
from ndpprep.save_sftp.main import save_to_sftp

if not os.environ.get("NDPPREP_MODE") == "development":
    import pydoop.hdfs as hdfs

#granite & nis
def process_dataset(dbname, dataset_name, extraction_date, secret_path, target_user, target_ip, target_path):
    hivepath = "hdfs://nerveprdha/warehouse/tablespace/external/hive"
    folder = f"{hivepath}/{dbname}/{dataset_name}"
    job_id = "cli"

    datasets = hdfs.ls(folder)
    secret_key = read_secret_key(secret_path)

    for dataset in datasets:
        parquet_files = hdfs.ls(dataset)

        for parquet_file in parquet_files:
            if extraction_date in parquet_file:
                try: 
                    read_start = time.time()
                    
                    with hdfs.open(parquet_file) as f:
                        metadata = pq.read_metadata(f)
                        tbl = pq.read_table(f)
                        schema = metadata.schema
                        tbl = tbl.rename_columns([col.upper() for col in tbl.schema.names])
                        read_duration = time.time() - read_start
                        
                        target_schema_function_name = f"get_target_schema_{dataset_name}"
                        if target_schema_function_name in globals():
                            target_schema_function = globals()[target_schema_function_name]
                            target_schema = target_schema_function(tbl.schema.names)
                        else:
                            target_schema = tbl.schema  # Use original schema

                        tbl = tbl.cast(target_schema)

                        modified_columns = []
                        masked_start = time.time()
                        cnt_column_masked = 0
                        masked_columns = []
                        original_columns = []
                    
                        for col_name in tbl.schema.names:
                            if tbl.schema.field(col_name).metadata and tbl.schema.field(col_name).metadata.get(b"req") == b"sensitive":
                                print(f"Column '{col_name}' metadata:")
                                print(f"(MASKED) Processing sensitive column '{col_name}' with metadata: {tbl.schema.field(col_name).metadata}")
                                original_columns.append(tbl[col_name])
                                cnt_column_masked += 1
                                modified_column = [masked_uuid(str(val)) for val in tbl[col_name]]
                                masked_columns.append(modified_column)
                                modified_columns.append(modified_column)
                            else:
                                modified_column = tbl[col_name]
                                modified_columns.append(modified_column)

                        update_mapping(original_columns, masked_columns, job_id)
                            
                        tbl = pa.table(modified_columns, schema=tbl.schema)
                        masked_duration = time.time() - masked_start
                        total_row_count = len(tbl)

                        extraction_date = re.search(r"(\d{4}-\d{2}-\d{2})", extraction_date).group(1)

                        output_folder = f'{dbname}/{dataset_name}/extraction_date={extraction_date}'
                        os.makedirs(output_folder, exist_ok=True)
                        output_file = os.path.join(output_folder, os.path.basename(parquet_file))    
                                    
                        # Encrypting data
                        encrypt_start = time.time()
                        encrypt_table(tbl, output_file, secret_key)
                        encrypt_duration = time.time() - encrypt_start
                        memory_size_mb = tbl.nbytes / (1024 * 1024)

                        # Uploading encrypted data to SFTP
                        sftp_start = time.time()
                        save_to_sftp(output_file, target_user, target_ip, target_path)
                        sftp_upload_duration = time.time() - sftp_start

                        # Logging durations
                        with open(log_file_path, "a") as log_file:
                            log_file.write(f"{parquet_file}: \nread_duration: {read_duration:.2f} seconds,\nmasked_duration: {masked_duration:.2f} seconds, \nencrypt_duration: {encrypt_duration:.2f} seconds, \nupload_to_sftp_duration: {sftp_upload_duration:.2f} seconds, \ncount masked column: {cnt_column_masked}, \nmemory size (mb): {memory_size_mb}\n\n")

                except pa.ArrowInvalid as e:
                    print(f"Error while processing file '{parquet_file}': {e}")
                    with open(processed_file, "a") as fail:
                        fail.write(f"Error processing dataset '{dataset_name}' in database '{dbname}'\n")
                    # Move to the next dataset
                    break  # Break out of the inner loop and proceed to the next dataset
                print(f"File found for extraction date '{extraction_date}' in '{dataset}'")
            else:
                continue
            
#raw_neps.db
def process_neps_dataset(dbname, dataset_name, extraction_date, secret_path, target_user, target_ip, target_path):  
    if dbname == "raw_neps.db":
        source_db = "nia_reference_dev.db"
    else:
        source_db = dbname
        dbname = "raw_neps.db"
    
    hivepath = "hdfs://nerveprdha/warehouse/tablespace/managed/hive"
    folder = f"{hivepath}/{source_db}/{dataset_name}"

    data = hdfs.ls(folder)
    secret_key = read_secret_key(secret_path)

    for data_csv in data:
        #filename = os.path.basename(data_csv)
        filename = os.path.splitext(os.path.basename(data_csv))[0]
        try:
            read_start = time.time()
            # Read the text or CSV file from HDFS
            with hdfs.open(data_csv, 'rt', encoding='utf-8') as file:
                file.seek(0)  # Reset file pointer to the beginning
                csv_content = StringIO(file.read())  # Use StringIO to create a file-like object
                if dataset_name == "raw_neps_fsplicedata_daily_latest":
                    df = pd.read_csv(csv_content, sep='|', header=None, dtype=str)
                else:
                    df = pd.read_csv(csv_content, header=None, dtype=str) 
                
            read_duration = time.time() - read_start
            
            target_schema_function_name = f"get_parquet_{dataset_name}"
            if target_schema_function_name in globals():
                target_schema_function = globals()[target_schema_function_name]
                tbl = target_schema_function(df) # csv -> pq
            else:
                print(f"Target parquet function '{target_schema_function_name}' not found. Falling back to original schema.")
            
            # masking
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

            update_mapping(original_columns, masked_columns, job_id)
                            
            tbl = pa.table(modified_columns, schema=tbl.schema)
            masked_duration = time.time() - masked_start
            total_row_count = len(tbl)

            output_folder = f'{dbname}/{dataset_name}/extraction_date={extraction_date}'
            os.makedirs(output_folder, exist_ok=True)
            today_date = str(extraction_date).replace("-", "")
            output_file = os.path.join(output_folder, f'{dataset_name}_{today_date}_{filename}.parquet')

            # Encrypting data
            encrypt_start = time.time()
            encrypt_table(tbl, output_file, secret_key)
            encrypt_duration = time.time() - encrypt_start
            memory_size_mb = tbl.nbytes / (1024 * 1024)

            # Uploading encrypted data to SFTP
            sftp_start = time.time()
            save_to_sftp(output_file, target_user, target_ip, target_path)
            sftp_upload_duration = time.time() - sftp_start

            # Logging durations
            with open(log_file_path, "a") as log_file:
                log_file.write(f"{today_date}_{data_csv}: read_duration: {read_duration:.2f} seconds, masked_duration: {masked_duration:.2f} seconds, encrypt_duration: {encrypt_duration:.2f} seconds, upload_to_sftp_duration: {sftp_upload_duration:.2f} seconds, count masked column: {cnt_column_masked}, memory size (mb): {memory_size_mb}\n")

        except pa.ArrowInvalid as e:
            print(f"Error while processing file '{data_csv}': {e}")

log_file_path = "PIPELINE/OUTPUT/LOG/runtime_log.txt"
processed_file = "PIPELINE/OUTPUT/LOG/processed_files.txt"