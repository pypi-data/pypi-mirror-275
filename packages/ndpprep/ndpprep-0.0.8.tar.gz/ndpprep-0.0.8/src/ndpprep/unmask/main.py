import os
import pyarrow.parquet as pq
import pyarrow as pa
import pandas as pd
import sys
sys.path.append("src")
from ndpprep.decryption.main import decrypt_table

def load_mapping_table(mapping_table_folder):
    mapping_table = pd.DataFrame()
    for file in os.listdir(mapping_table_folder):
        if file.endswith(".parquet"):
            file_path = os.path.join(mapping_table_folder, file)
            mapping_table = pd.concat([mapping_table, pq.read_table(file_path).to_pandas()])
    return mapping_table

#with dbname folder
def unmask_sensitive(decrypted_tables, decrypted_files, mapping_table_folder):
    unmasked_tables = []
    mapping_table = load_mapping_table(mapping_table_folder)
    
    for table in decrypted_tables:
        schema = table.schema
        modified_columns = {}
        
        for col in schema.names:
            if schema.field(col).metadata and schema.field(col).metadata.get(b"req") == b"sensitive":
                original_values = table[col].to_pandas().map(mapping_table.set_index("MASKED_VALUE").to_dict()["ORIGINAL_VALUE"])
                modified_columns[col] = original_values
            else:
                modified_columns[col] = table[col]
        
        unmasked_table = pa.Table.from_pandas(pd.DataFrame(modified_columns))
        unmasked_tables.append(unmasked_table)
        print(unmasked_tables)

    for table, file_path in zip(unmasked_tables, decrypted_files):
        output_folder = os.path.dirname(file_path)  # Use the directory of the original file
        original_filename = os.path.basename(file_path)
        new_filename = os.path.splitext(original_filename)[0] + "_unmasked.parquet"
        output_file = os.path.join(output_folder, new_filename)
        pq.write_table(table, output_file)
    
    return unmasked_tables
