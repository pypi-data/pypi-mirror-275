import uuid
import os
import pandas as pd
      
def masked_uuid(data):
    randno = "1x7h3"
    # Generate a UUID based on the input data
    uuid_val = str(uuid.uuid5(uuid.NAMESPACE_X500, randno + str(data)))
    # Take the first 8 characters of the UUID and remove hyphens
    shortened_uuid = uuid_val[:8].replace('-', '')
    return shortened_uuid

#with folder dbname
def update_mapping(original_columns, masked_columns, job_id, dbname):
    try:
        data_dict = {"ORIGINAL_VALUE": [], "MASKED_VALUE": []}
        existing_combinations = set()

        for original_column, masked_column in zip(original_columns, masked_columns):
            for original_val, masked_val in zip(original_column, masked_column):
                # Check if the combination already exists
                if (original_val, masked_val) not in existing_combinations:
                    data_dict["ORIGINAL_VALUE"].append(original_val)
                    data_dict["MASKED_VALUE"].append(masked_val)
                    existing_combinations.add((original_val, masked_val))

        df = pd.DataFrame(data_dict)
        
        # Define the folder path based on dbname
        mapping_table_folder = f"PIPELINE/OUTPUT/mapping_table/{dbname}"
        os.makedirs(mapping_table_folder, exist_ok=True)

        output_file_path = f"{mapping_table_folder}/mapping_table_{job_id}.parquet"
        if os.path.exists(output_file_path):
            existing_df = pd.read_parquet(output_file_path)
            existing_combinations = set(zip(existing_df["ORIGINAL_VALUE"], existing_df["MASKED_VALUE"]))
            # Find and remove duplicates
            df_no_duplicates = pd.concat([existing_df, df]).drop_duplicates(subset=["MASKED_VALUE"]).reset_index(drop=True)
        else:
            # If the file doesn't exist, use the original dataframe
            df_no_duplicates = df

        df_no_duplicates.to_parquet(output_file_path, index=False)
        
        print(f"mapping_table_{job_id}.parquet updated successfully.")

    except Exception as e:
        print(f"Error while updating mapping_table_{job_id}.parquet: {e}")

