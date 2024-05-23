import os
import paramiko
import pyarrow.parquet as pq
import sys
sys.path.append("src")
from ndpprep.encryption.main import InMemoryKmsClient, pe
from ndpprep.secret_key.main import read_secret_key

def decrypt_table(dbname, dataset_name, extraction_date, secret_path, target_user, target_ip):
    decrypted_tables = []
    decrypted_files = []

    # Construct the SFTP path
    sftp_path = f"/data/{dbname}/{dataset_name}/extraction_date={extraction_date}"
    secret_key = read_secret_key(secret_path)

    # KMS connection configuration
    kms_connection_config = pe.KmsConnectionConfig(
        custom_kms_conf={
            "footer": secret_key.decode("UTF-8"),
            "columns": secret_key.decode("UTF-8"),
        }
    )

    # Crypto factory
    def kms_factory(kms_connection_configuration):
        return InMemoryKmsClient(kms_connection_configuration)

    crypto_factory = pe.CryptoFactory(kms_factory)

    # Decryption properties
    decryption_properties = crypto_factory.file_decryption_properties(kms_connection_config)

    # Connect to the SFTP server
    try:
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.connect(target_ip, username=target_user)
        sftp = ssh.open_sftp()
        
        files = sftp.listdir(sftp_path)
        first_table_printed = False 
        
        for filename in files:
            print(filename)
            remote_path = os.path.join(sftp_path, filename)
            local_basename = os.path.basename(remote_path)
            output_folder = f'DECRYPTED/{dbname}/{dataset_name}/extraction_date={extraction_date}'
            local_path = os.path.join(output_folder, local_basename)
            os.makedirs(output_folder, exist_ok=True)

            # Download the file from SFTP
            sftp.get(remote_path, local_path)
            decrypted_files.append(local_path)

            # Decrypt the downloaded Parquet file
            encrypted_parquet_file = pq.ParquetFile(local_path, decryption_properties=decryption_properties)
            table = encrypted_parquet_file.read()
            decrypted_tables.append(table)
            #print(decrypted_tables)

            # Print full column names with sample values
            if not first_table_printed:
                schema = table.schema
                first_table_printed = False
                for i, field in enumerate(schema):
                    column_name = field.name
                    column_values = table[column_name].to_pylist()[:5]  # The first 5 values as sample
                    print(f"{column_name}: {column_values}")
                first_table_printed = True

             # Generate path for decrypted file
            decrypted_file_path = os.path.splitext(local_path)[0] + "_decrypted.parquet"
            # Save decrypted Parquet file
            pq.write_table(table, decrypted_file_path)
            
        sftp.close()
        ssh.close()
    
    except Exception as e:
        print(f"Error occurred while decrypting files from SFTP: {e}")

    return decrypted_tables, decrypted_files

def decrypt_shp(dbname, dataset_name, shp, secret_path, target_user, target_ip):
    decrypted_tables = []
    #decrypted_files = []

    # Construct the SFTP path
    sftp_path = f"/data/{dbname}/{dataset_name}"
    secret_key = read_secret_key(secret_path)

    # KMS connection configuration
    kms_connection_config = pe.KmsConnectionConfig(
        custom_kms_conf={
            "footer": secret_key.decode("UTF-8"),
            "columns": secret_key.decode("UTF-8"),
        }
    )

    # Crypto factory
    def kms_factory(kms_connection_configuration):
        return InMemoryKmsClient(kms_connection_configuration)

    crypto_factory = pe.CryptoFactory(kms_factory)

    # Decryption properties
    decryption_properties = crypto_factory.file_decryption_properties(kms_connection_config)

    # Connect to the SFTP server
    try:
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.connect(target_ip, username=target_user)
        sftp = ssh.open_sftp()
        
        files = sftp.listdir(sftp_path)
        first_table_printed = False 
        
        for filename in files:
            if filename.startswith(shp):
                print(filename)
                remote_path = os.path.join(sftp_path, filename)
                local_basename = os.path.basename(remote_path)
                output_folder = f'DECRYPTED/{dbname}/{dataset_name}'
                local_path = os.path.join(output_folder, local_basename)
                os.makedirs(output_folder, exist_ok=True)

                # Download the file from SFTP
                sftp.get(remote_path, local_path)
                #decrypted_files.append(local_path)

                # Decrypt the downloaded Parquet file
                encrypted_parquet_file = pq.ParquetFile(local_path, decryption_properties=decryption_properties)
                table = encrypted_parquet_file.read()
                decrypted_tables.append(table)

                # Print full column names with sample values
                if not first_table_printed:
                    schema = table.schema
                    first_table_printed = False
                    for i, field in enumerate(schema):
                        column_name = field.name
                        column_values = table[column_name].to_pylist()[:5]  # The first 5 values as sample
                        print(f"{column_name}: {column_values}")
                    first_table_printed = True

                # Generate path for decrypted file
                decrypted_file_path = os.path.splitext(local_path)[0] + "_decrypted.parquet"
                # Save decrypted Parquet file
                pq.write_table(table, decrypted_file_path)
            
        sftp.close()
        ssh.close()
    
    except Exception as e:
        print(f"Error occurred while decrypting files from SFTP: {e}")

    return decrypted_tables, #decrypted_files