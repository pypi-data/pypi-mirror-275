## ignore this code
import os
from glob import glob

def get_datasets_in_scope(filepath: str = "datasets_in_scope.txt") -> dict:
    """Read file to get datasets in scope."""
    datasets = {}
    with open(filepath, "r") as f:
        for line in f:
            if line[0] == "#":
                continue
            else:
                dbname, dataset_name = line.strip().split('/')
                try:
                    datasets[dbname].add(dataset_name)
                except KeyError:
                    datasets[dbname] = {dataset_name}
    return datasets

def get_list_of_files_in_source_location(ds, sourcepath):
    """Get list of files in source location."""

    # process datasets_in_scope key-value pairs
    files = glob(f"{sourcepath}/**/*.parquet", recursive=True)
    srcfiles = []
    for file in files:
        dbname, dataset_name, batch, filename = file.split('\\')[-4:]
        # proceed if data is in scope, otherwise skip
        if dbname in ds.keys():
            if dataset_name in ds[dbname]:
                pass
            else:
                continue
        else:
            continue

        srcfiles.append(file.replace(sourcepath + '\\', ''))

    print(srcfiles)
    return srcfiles

def get_list_of_files_processed():
    """Get list of files processed from 'LOG/runtime_log.txt'."""
    processed_files = []
    log_file_path = 'LOG/runtime_log.txt'
    if os.path.exists(log_file_path):
        with open(log_file_path, 'r') as log_file:
            for line in log_file:
                dbname, dataset_name, batch, filename = line.strip().split('/')
                processed_files.append((dbname, dataset_name, batch, filename))
    else:
        print(f"Error: Log file '{log_file_path}' not found.")
    return processed_files


def get_list_of_files_to_process(dbname, dataset_name):
    """Get list of files to process."""
    print("This is a placeholder for the function get_list_of_files_to_process() in the main module.")

def get_list_of_files_to_process(db, ds, sourcepath):
    srcfiles = get_list_of_files_in_source_location(ds, sourcepath)
    processed_files = get_list_of_files_processed()
    files_to_process = [file for file in srcfiles if file not in processed_files]
    return files_to_process
