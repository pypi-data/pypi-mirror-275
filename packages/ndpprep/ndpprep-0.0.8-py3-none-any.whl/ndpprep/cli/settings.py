import os, sys
sys.path.append("src")
from ndpprep.secret_key.main import read_secret_key
from ndpprep.secret_key import *

target_user = "ndp"
target_ip = "172.20.100.213"
target_path = "/data"
default_secret_path = "/home/cdsw/PIPELINE/secret_key.txt"

if os.environ.get("NDPPREP_MODE") == "development":
    secret_key = "randomsecretkey"
else:
    secret_key = read_secret_key(default_secret_path)

#mapping_table_folder = f"/home/cdsw/PIPELINE/OUTPUT/mapping_table/{db}"