import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

def get_parquet_raw_neps_cabdata_daily_latest(df):     
    # assign column name to the respective columns
    df.columns =['SEGMENT', 'CAB_ID', 'EXC_ABB', 'CAB_CODE','G3E_FNO', 'G3E_FID', 'FEATURE_STATE',
                 'LATITUDE','LONGITUDE']
   
    schema = pa.schema([
        pa.field('SEGMENT', pa.string()),
        pa.field('CAB_ID', pa.string(), metadata={'req':'sensitive'}),
        pa.field('EXC_ABB', pa.string(), metadata={'req':'sensitive'}),
        pa.field('CAB_CODE', pa.string(), metadata={'req':'sensitive'}),
        pa.field('G3E_FNO', pa.string()),
        pa.field('G3E_FID', pa.string(), metadata={'req':'sensitive'}),
        pa.field('FEATURE_STATE', pa.string()),
        pa.field('LATITUDE', pa.string(), metadata={'req':'sensitive','target_schema':'float64()'}),
        pa.field('LONGITUDE', pa.string(), metadata={'req':'sensitive','target_schema':'float64()'})
        ],
        metadata={'Table_Name':'raw_neps_cabdata_daily_latest'})
    
    # df to parquet  
    tbl = pa.Table.from_pandas(df, schema=schema)
       
    return tbl

def get_parquet_raw_neps_dbdata_daily_latest(df):
    df.columns =['SEGMENT', 'DB_ID', 'FDC_CODE', 'EXC_ABB','DB_CODE', 'FEATURE_STATE', 'LATITUDE', 'LONGITUDE']

    schema = pa.schema([
        pa.field('SEGMENT', pa.string()),
        pa.field('DB_ID', pa.string(), metadata={'req':'sensitive'}),
        pa.field('FDC_CODE', pa.string(), metadata={'req':'sensitive'}),
        pa.field('EXC_ABB', pa.string(), metadata={'req':'sensitive'}),
        pa.field('DB_CODE', pa.string(), metadata={'req':'sensitive'}),
        pa.field('FEATURE_STATE', pa.string()),
        pa.field('LATITUDE', pa.string(), metadata={'req':'sensitive','target_schema':'float64()'}),
        pa.field('LONGITUDE', pa.string(), metadata={'req':'sensitive','target_schema':'float64()'})
        ],
        metadata={'Table_Name':'raw_neps_dbdata_daily_latest'})
    tbl = pa.Table.from_pandas(df, schema=schema)
       
    return tbl
    
def get_parquet_raw_neps_dcbl_daily_latest(df):
    df.columns =['SEGMENT', 'EXC_ABB', 'G3E_FNO', 'G3E_FID','CABLE_CODE', 'CABLE_CLASS', 'TOTAL_LENGTH', 'TOTAL_SIZE']

    df['TOTAL_LENGTH'] = df['TOTAL_LENGTH'].astype(float)
    df['TOTAL_SIZE'] = df['TOTAL_SIZE'].astype(float)
        
    schema = pa.schema([
        pa.field('SEGMENT', pa.string()),
        pa.field('EXC_ABB', pa.string(), metadata={'req':'sensitive'}),
        pa.field('G3E_FNO', pa.string()),
        pa.field('G3E_FID', pa.string(), metadata={'req':'sensitive'}),
        pa.field('CABLE_CODE', pa.string()),
        pa.field('CABLE_CLASS', pa.string()),
        pa.field('TOTAL_LENGTH', pa.float64()),
        pa.field('TOTAL_SIZE', pa.float64())
        ],
        metadata={'Table_Name':'raw_neps_dcbl_daily_latest'})

    tbl = pa.Table.from_pandas(df, schema=schema)
    
    return tbl

    
def get_parquet_raw_neps_ddpdata_daily_latest(df):
    df.columns =['SEGMENT', 'DDP_ID', 'EXC_ABB','DDP_CODE', 'G3E_FNO', 'G3E_FID', 'FEATURE_STATE', 'LATITUDE','LONGITUDE']
  
    schema = pa.schema([
        pa.field('SEGMENT', pa.string()),
        pa.field('DDP_ID', pa.string(), metadata={'req':'sensitive'}),
        pa.field('EXC_ABB', pa.string(), metadata={'req':'sensitive'}),
        pa.field('DDP_CODE', pa.string(),metadata={'req':'sensitive'}),
        pa.field('G3E_FNO', pa.string()),
        pa.field('G3E_FID', pa.string(), metadata={'req':'sensitive'}),
        pa.field('FEATURE_STATE', pa.string()),
        pa.field('LATITUDE', pa.string(), metadata={'req':'sensitive','target_schema':'float64()'}),
        pa.field('LONGITUDE', pa.string(), metadata={'req':'sensitive','target_schema':'float64()'})
        ],
        metadata={'Table_Name':'raw_neps_ddpdata_daily_latest'})
    
    tbl = pa.Table.from_pandas(df, schema=schema)
    
    return tbl
    
def get_parquet_raw_neps_dpdata_daily_latest(df):
    df.columns =['SEGMENT', 'DP_ID', 'EXC_ABB','DP_CODE', 'FEATURE_STATE', 'LATITUDE', 'LONGITUDE']

    schema = pa.schema([
        pa.field('SEGMENT', pa.string()),
        pa.field('DP_ID', pa.string(), metadata={'req':'sensitive'}),
        pa.field('EXC_ABB', pa.string(), metadata={'req':'sensitive'}),
        pa.field('DP_CODE', pa.string(), metadata={'req':'sensitive'}),
        pa.field('FEATURE_STATE', pa.string()),
        pa.field('LATITUDE', pa.string(), metadata={'req':'sensitive','target_schema':'float64()'}),
        pa.field('LONGITUDE', pa.string(), metadata={'req':'sensitive','target_schema':'float64()'})
        ],
        metadata={'Table_Name':'raw_neps_dpdata_daily_latest'})
    
    tbl = pa.Table.from_pandas(df, schema=schema)
    
    return tbl
    
def get_parquet_raw_neps_dslamdata_daily_latest(df):
    df.columns =['SEGMENT', 'DSLAM_ID', 'EXC_ABB','DSLAM_CODE','G3E_FNO', 'G3E_FID', 'FEATURE_STATE', 
                       'LATITUDE','LONGITUDE']

    schema = pa.schema([
        pa.field('SEGMENT', pa.string()),
        pa.field('DSLAM_ID', pa.string(), metadata={'req':'sensitive'}),
        pa.field('EXC_ABB', pa.string(), metadata={'req':'sensitive'}),
        pa.field('DSLAM_CODE', pa.string(), metadata={'req':'sensitive'}),
        pa.field('G3E_FNO', pa.string()),
        pa.field('G3E_FID', pa.string(), metadata={'req':'sensitive'}),
        pa.field('FEATURE_STATE', pa.string()),
        pa.field('LATITUDE', pa.string(), metadata={'req':'sensitive','target_schema':'float64()'}),
        pa.field('LONGITUDE', pa.string(), metadata={'req':'sensitive','target_schema':'float64()'})
        ],
        metadata={'comment':'raw_neps_dslamdata_daily_latest'})
    
    tbl = pa.Table.from_pandas(df, schema=schema)
    
    return tbl

def get_parquet_raw_neps_ecbl_daily_latest(df):
    df.columns =['SEGMENT', 'EXC_ABB', 'G3E_FNO', 'G3E_FID','CABLE_CODE', 'CABLE_CLASS', 'TOTAL_LENGTH', 'TOTAL_SIZE']

    schema = pa.schema([
        pa.field('SEGMENT', pa.string()),
        pa.field('EXC_ABB', pa.string(), metadata={'req':'sensitive'}),
        pa.field('G3E_FNO', pa.string()),
        pa.field('G3E_FID', pa.string(), metadata={'req':'sensitive'}),
        pa.field('CABLE_CODE', pa.string()),
        pa.field('CABLE_CLASS', pa.string()),
        pa.field('TOTAL_LENGTH', pa.string()),
        pa.field('TOTAL_SIZE', pa.string())
        ],
        metadata={'comment':'raw_neps_ecbl_daily_latest'})
    
    tbl = pa.Table.from_pandas(df, schema=schema)
    
    return tbl

def get_parquet_raw_neps_fcbl_daily_latest(df):
    df.columns =['SEGMENT', 'EXC_ABB', 'G3E_FNO', 'G3E_FID','CABLE_CODE','CABLE_TYPE', 'INSTALL_TYPE', 
                      'CABLE_LENGTH', 'CABLE_SIZE']

    # Convert lat long column to float type
    df['CABLE_LENGTH'] = df['CABLE_LENGTH'].astype(float)
    df['CABLE_SIZE'] = df['CABLE_SIZE'].astype(float)
    
    schema = pa.schema([
        pa.field('SEGMENT', pa.string()),
        pa.field('EXC_ABB', pa.string(), metadata={'req':'sensitive'}),
        pa.field('G3E_FNO', pa.string()),
        pa.field('G3E_FID', pa.string(), metadata={'req':'sensitive'}),
        pa.field('CABLE_CODE', pa.string()),
        pa.field('CABLE_TYPE', pa.string()),
        pa.field('INSTALL_TYPE', pa.string()),
        pa.field('CABLE_LENGTH', pa.float64()),
        pa.field('CABLE_SIZE', pa.float64())
        ],
        metadata={'comment':'raw_neps_fcbl_daily_latest'})
    tbl = pa.Table.from_pandas(df, schema=schema)
    
    return tbl
    
def get_parquet_raw_neps_fdcbl_daily_latest(df):
    df.columns =['SEGMENT', 'EXC_ABB', 'G3E_FNO', 'G3E_FID','FCABLE_CODE', 'CABLE_TYPE','INSTALL_TYPE', 
                       'CABLE_LENGTH', 'CABLE_SIZE']

    # Convert lat long column to float type
    df['CABLE_LENGTH'] = df['CABLE_LENGTH'].astype(float)
    df['CABLE_SIZE'] = df['CABLE_SIZE'].astype(float)
    
    schema = pa.schema([
        pa.field('SEGMENT', pa.string()),
        pa.field('EXC_ABB', pa.string(), metadata={'req':'sensitive'}),
        pa.field('G3E_FNO', pa.string()),
        pa.field('G3E_FID', pa.string(), metadata={'req':'sensitive'}),
        pa.field('FCABLE_CODE', pa.string()),
        pa.field('CABLE_TYPE', pa.string()),
        pa.field('INSTALL_TYPE', pa.string()),
        pa.field('CABLE_LENGTH', pa.float64()),
        pa.field('CABLE_SIZE', pa.float64())
        ],
        metadata={'comment':'raw_neps_fdcbl_daily_latest'})
    tbl = pa.Table.from_pandas(df, schema=schema)
    
    return tbl
    
def get_parquet_raw_neps_fdcdata_daily_latest(df):
    df.columns =['SEGMENT', 'FDC_ID', 'EXC_ABB','FDC_CODE', 'FEATURE_STATE', 'LATITUDE', 'LONGITUDE']

    schema = pa.schema([
        pa.field('SEGMENT', pa.string()),
        pa.field('FDC_ID', pa.string(), metadata={'req':'sensitive'}),
        pa.field('EXC_ABB', pa.string(), metadata={'req':'sensitive'}),
        pa.field('FDC_CODE', pa.string(), metadata={'req':'sensitive'}),
        pa.field('FEATURE_STATE', pa.string()),
        pa.field('LATITUDE', pa.string(), metadata={'req':'sensitive','target_schema':'float64()'}),
        pa.field('LONGITUDE', pa.string(), metadata={'req':'sensitive','target_schema':'float64()'})
        ],
        metadata={'comment':'raw_neps_fdcdata_daily_latest'})
    tbl = pa.Table.from_pandas(df, schema=schema)
    
    return tbl
    
def get_parquet_raw_neps_fdpdata_daily_latest(df):
    df.columns =['SEGMENT', 'FDP_ID', 'EXC_ABB','FDC_CODE', 'FDP_CODE', 'FEATURE_STATE', 'LATITUDE', 'LONGITUDE']

    schema = pa.schema([
        pa.field('SEGMENT', pa.string()),
        pa.field('FDP_ID', pa.string(), metadata={'req':'sensitive'}),
        pa.field('EXC_ABB', pa.string(), metadata={'req':'sensitive'}),
        pa.field('FDC_CODE', pa.string(), metadata={'req':'sensitive'}),
        pa.field('FDP_CODE', pa.string(), metadata={'req':'sensitive'}),
        pa.field('FEATURE_STATE', pa.string()),
        pa.field('LATITUDE', pa.string(), metadata={'req':'sensitive','target_schema':'float64()'}),
        pa.field('LONGITUDE', pa.string(), metadata={'req':'sensitive','target_schema':'float64()'})
        ],
        metadata={'comment':'raw_neps_fdpdata_daily_latest'})
    tbl = pa.Table.from_pandas(df, schema=schema)
    
    return tbl

    
def get_parquet_raw_neps_fsplicedata_daily_latest(df): 
    df.columns =['REGION', 'SEGMENT', 'EXC_ABB', 'G3E_ID', 'G3E_FNO', 'G3E_FID',
             'G3E_CNO', 'G3E_CID', 'BRANCH_TYPE', 'CABLE_CLASS', 'CLOSURE_SIZE',
             'CONTRACTOR', 'CREATED_BY', 'CREATED_DATE', 'CREATED_HOST',
             'CREATED_IP_ADDRESS', 'CREATED_OS_USER', 'CUST_NETWORK', 'DESCRIPTION','FSPLICE_CLASS', 
             'LOCATION', 'LOCATION_FID', 'LOC_TYPE', 'MANUFACTURER','MODEL', 'MODIFIED_BY', 
             'MODIFIED_DATE', 'MODIFIED_HOST','MODIFIED_IP_ADDRESS', 'MODIFIED_OS_USER', 
             'NETWORK_TYPE', 'NUMBERING','SPLICE_CODE', 'LATITUDE', 'LONGITUDE']
    
    schema = pa.schema([
        pa.field('REGION', pa.string()),
        pa.field('SEGMENT', pa.string()),
        pa.field('EXC_ABB', pa.string(), metadata={'req':'sensitive'}),
        pa.field('G3E_ID', pa.string(), metadata={'req':'sensitive'}),
        pa.field('G3E_FNO', pa.string()),
        pa.field('G3E_FID', pa.string(), metadata={'req':'sensitive'}),
        pa.field('G3E_CNO', pa.string()),
        pa.field('G3E_CID', pa.string()),
        pa.field('BRANCH_TYPE', pa.string()),
        pa.field('CABLE_CLASS', pa.string()),
        pa.field('CLOSURE_SIZE', pa.string()),
        pa.field('CONTRACTOR', pa.string()),
        pa.field('CREATED_BY', pa.string(), metadata={'req':'sensitive'}),
        pa.field('CREATED_DATE', pa.string()),
        pa.field('CREATED_HOST', pa.string(), metadata={'req':'sensitive'}),
        pa.field('CREATED_IP_ADDRESS', pa.string(), metadata={'req':'sensitive'}),
        pa.field('CREATED_OS_USER', pa.string(), metadata={'req':'sensitive'}),
        pa.field('CUST_NETWORK', pa.string()),
        pa.field('DESCRIPTION', pa.string(), metadata={'req':'sensitive'}),
        pa.field('FSPLICE_CLASS', pa.string()),
        pa.field('LOCATION', pa.string()),
        pa.field('LOCATION_FID', pa.string()),
        pa.field('LOC_TYPE', pa.string()),
        pa.field('MANUFACTURER', pa.string(), metadata={'req':'sensitive'}),
        pa.field('MODEL', pa.string()),
        pa.field('MODIFIED_BY', pa.string(), metadata={'req':'sensitive'}),
        pa.field('MODIFIED_DATE', pa.string()),
        pa.field('MODIFIED_HOST', pa.string()),
        pa.field('MODIFIED_IP_ADDRESS', pa.string(), metadata={'req':'sensitive'}),
        pa.field('MODIFIED_OS_USER', pa.string(), metadata={'req':'sensitive'}),
        pa.field('NETWORK_TYPE', pa.string()),
        pa.field('NUMBERING', pa.string()),
        pa.field('SPLICE_CODE', pa.string(), metadata={'req':'sensitive'}),
        pa.field('LATITUDE', pa.string(), metadata={'req':'sensitive','target_schema':'float64()'}),
        pa.field('LONGITUDE', pa.string(), metadata={'req':'sensitive','target_schema':'float64()'})
        ],
        metadata={'req':'raw_neps_fsplicedata_daily_latest'})
    
    # df to parquet
    tbl = pa.Table.from_pandas(df, schema=schema)
    
    return tbl

def get_parquet_raw_neps_jnt_daily_latest(df):
    df.columns =['SEGMENT', 'EXC_ABB', 'G3E_FNO', 'G3E_FID','CABLE_CODE','CABLE_TYPE','INSTALL_TYPE', 
                     'CABLE_LENGTH', 'CABLE_SIZE']

    # Convert lat long column to float type
    df['CABLE_LENGTH'] = df['CABLE_LENGTH'].astype(float)
    df['CABLE_SIZE'] = df['CABLE_SIZE'].astype(float)
    
    schema = pa.schema([
        pa.field('SEGMENT', pa.string()),
        pa.field('EXC_ABB', pa.string(), metadata={'req':'sensitive'}),
        pa.field('G3E_FNO', pa.string()),
        pa.field('G3E_FID', pa.string(), metadata={'req':'sensitive'}),
        pa.field('CABLE_CODE', pa.string()),
        pa.field('CABLE_TYPE', pa.string()),
        pa.field('INSTALL_TYPE', pa.string()),
        pa.field('CABLE_LENGTH', pa.float64()),
        pa.field('CABLE_SIZE', pa.float64())
        ],
        metadata={'comment':'raw_neps_jnt_daily_latest'})
    # df to parquet
    tbl = pa.Table.from_pandas(df, schema=schema)
    
    return tbl

    
def get_parquet_raw_neps_manhldata_daily_latest(df):
    df.columns = ['REGION', 'SEGMENT', 'EXC_ABB', 'G3E_FNO', 'G3E_FID', 'FEATURE_TYPE','LATITUDE', 'LONGITUDE']
    
    schema = pa.schema([
        pa.field('REGION', pa.string()),
        pa.field('SEGMENT', pa.string()),
        pa.field('EXC_ABB', pa.string(), metadata={'req':'sensitive'}),
        pa.field('G3E_FNO', pa.string()),
        pa.field('G3E_FID', pa.string(), metadata={'req':'sensitive'}),
        pa.field('FEATURE_TYPE', pa.string()),
        pa.field('LATITUDE', pa.string(), metadata={'req':'sensitive','target_schema':'float64()'}),
        pa.field('LONGITUDE', pa.string(), metadata={'req':'sensitive','target_schema':'float64()'})
        ],
        metadata={'comment':'raw_neps_manhldata_daily_latest'})
    # df to parquet
    tbl = pa.Table.from_pandas(df, schema=schema)
    
    return tbl
    
    
def get_parquet_raw_neps_msandata_daily_latest(df):
    df.columns =['SEGMENT', 'MSAN_ID', 'EXC_ABB','RT_CODE', 'G3E_FNO', 'G3E_FID', 'FEATURE_STATE', 
                      'LATITUDE', 'LONGITUDE']

    schema = pa.schema([
        pa.field('SEGMENT', pa.string()),
        pa.field('MSAN_ID', pa.string(), metadata={'req':'sensitive'}),
        pa.field('EXC_ABB', pa.string(), metadata={'req':'sensitive'}),
        pa.field('RT_CODE', pa.string(), metadata={'req':'sensitive'}),
        pa.field('G3E_FNO', pa.string()),
        pa.field('G3E_FID', pa.string(), metadata={'req':'sensitive'}),
        pa.field('FEATURE_STATE', pa.string()),
        pa.field('LATITUDE', pa.string(), metadata={'req':'sensitive','target_schema':'float64()'}),
        pa.field('LONGITUDE', pa.string(), metadata={'req':'sensitive','target_schema':'float64()'})
        ],
        metadata={'comment':'raw_neps_msandata_daily_latest'})
    # df to parquet
    tbl = pa.Table.from_pandas(df, schema=schema)
    
    return tbl
    
        
def get_parquet_raw_neps_odfdata_daily_latest(df):
    df.columns =['SEGMENT', 'ODF_ID', 'EXC_ABB','FDC_CODE', 'FEATURE_STATE', 'LATITUDE', 'LONGITUDE']

    schema = pa.schema([
        pa.field('SEGMENT', pa.string()),
        pa.field('ODF_ID', pa.string(), metadata={'req':'sensitive'}),
        pa.field('EXC_ABB', pa.string(), metadata={'req':'sensitive'}),
        pa.field('FDC_CODE', pa.string(), metadata={'req':'sensitive'}),
        pa.field('FEATURE_STATE', pa.string()),
        pa.field('LATITUDE', pa.string(), metadata={'req':'sensitive','target_schema':'float64()'}),
        pa.field('LONGITUDE', pa.string(), metadata={'req':'sensitive','target_schema':'float64()'})
    ],
    metadata={'req':'raw_neps_odfdata_daily_latest'})

    tbl = pa.Table.from_pandas(df, schema=schema)
    
    return tbl

def get_parquet_raw_neps_poledata_daily_latest(df):
    df.columns = ['REGION', 'SEGMENT', 'EXC_ABB', 'G3E_FNO', 'G3E_FID', 'FEATURE_TYPE', 'POLE_TYPE',
                   'LATITUDE', 'LONGITUDE']
    
    schema = pa.schema([
        pa.field('REGION', pa.string()),
        pa.field('SEGMENT', pa.string()),
        pa.field('EXC_ABB', pa.string(), metadata={'req':'sensitive'}),
        pa.field('G3E_FNO', pa.string()),
        pa.field('G3E_FID', pa.string(), metadata={'req':'sensitive'}),
        pa.field('FEATURE_TYPE', pa.string()),
        pa.field('POLE_TYPE', pa.string()),
        pa.field('LATITUDE', pa.string(), metadata={'req':'sensitive','target_schema':'float64()'}),
        pa.field('LONGITUDE', pa.string(), metadata={'req':'sensitive','target_schema':'float64()'})
        ],
        metadata={'comment':'raw_neps_poledata_daily_latest'})
    
    tbl = pa.Table.from_pandas(df, schema=schema)
    
    return tbl
    
def get_parquet_raw_neps_rtdata_daily_latest(df):
    df.columns =['SEGMENT', 'RT_ID', 'EXC_ABB','RT_CODE', 'G3E_FNO', 'G3E_FID', 'FEATURE_STATE', 
                    'LATITUDE', 'LONGITUDE']

    schema = pa.schema([
        pa.field('SEGMENT', pa.string()),
        pa.field('RT_ID', pa.string(), metadata={'req':'sensitive'}),
        pa.field('EXC_ABB', pa.string(), metadata={'req':'sensitive'}),
        pa.field('RT_CODE', pa.string(), metadata={'req':'sensitive'}),
        pa.field('G3E_FNO', pa.string()),
        pa.field('G3E_FID', pa.string(), metadata={'req':'sensitive'}),
        pa.field('FEATURE_STATE', pa.string()),
        pa.field('LATITUDE', pa.string(), metadata={'req':'sensitive','target_schema':'float64()'}),
        pa.field('LONGITUDE', pa.string(), metadata={'req':'sensitive','target_schema':'float64()'})
        ],
        metadata={'comment':'raw_neps_rtdata_daily_latest'})
    
    tbl = pa.Table.from_pandas(df, schema=schema)
    
    return tbl
    
def get_parquet_raw_neps_sdfdata_daily_latest(df):
    df.columns =['SEGMENT', 'SDF_ID', 'EXC_ABB','SDF_CODE', 'G3E_FNO', 'G3E_FID', 'FEATURE_STATE', 'LATITUDE', 'LONGITUDE']

    schema = pa.schema([
        pa.field('SEGMENT', pa.string()),
        pa.field('SDF_ID', pa.string(), metadata={'req':'sensitive'}),
        pa.field('EXC_ABB', pa.string(), metadata={'req':'sensitive'}),
        pa.field('SDF_CODE', pa.string(), metadata={'req':'sensitive'}),
        pa.field('G3E_FNO', pa.string()),
        pa.field('G3E_FID', pa.string(), metadata={'req':'sensitive'}),
        pa.field('FEATURE_STATE', pa.string()),
        pa.field('LATITUDE', pa.string(), metadata={'req':'sensitive','target_schema':'float64()'}),
        pa.field('LONGITUDE', pa.string(), metadata={'req':'sensitive','target_schema':'float64()'})
        ],
        metadata={'comment':'raw_neps_sdfdata_daily_latest'})
    
    tbl = pa.Table.from_pandas(df, schema=schema)
    
    return tbl

def get_parquet_raw_neps_trunk_daily_latest(df):
    df.columns =['SEGMENT', 'EXC_ABB', 'G3E_FNO', 'G3E_FID','CABLE_CODE', 
                  'CABLE_TYPE','INSTALL_TYPE', 'CABLE_LENGTH', 'CABLE_SIZE']

    # Convert lat long column to float type
    df['CABLE_LENGTH'] = df['CABLE_LENGTH'].astype(float)
    df['CABLE_SIZE'] = df['CABLE_SIZE'].astype(int)
    
    schema = pa.schema([
        pa.field('SEGMENT', pa.string()),
        pa.field('EXC_ABB', pa.string(), metadata={'req':'sensitive'}),
        pa.field('G3E_FNO', pa.string()),
        pa.field('G3E_FID', pa.string(), metadata={'req':'sensitive'}),
        pa.field('CABLE_CODE', pa.string()),
        pa.field('CABLE_TYPE', pa.string()),
        pa.field('INSTALL_TYPE', pa.string()),
        pa.field('CABLE_LENGTH', pa.float64()),
        pa.field('CABLE_SIZE', pa.uint8())
        ],
        metadata={'comment':'raw_neps_trunk_daily_latest'})
    
    tbl = pa.Table.from_pandas(df, schema=schema)
    
    return tbl
    
def get_parquet_raw_neps_upedata_daily_latest(df):
    df.columns = ['REGION', 'SEGMENT', 'EXC_ABB', 'G3E_FNO', 'G3E_FID', 'UPE_CODE',
                  'LATITUDE', 'LONGITUDE']
    
    schema = pa.schema([
        pa.field('REGION', pa.string()),
        pa.field('SEGMENT', pa.string()),
        pa.field('EXC_ABB', pa.string(), metadata={'req':'sensitive'}),
        pa.field('G3E_FNO', pa.string()),
        pa.field('G3E_FID', pa.string(), metadata={'req':'sensitive'}),
        pa.field('UPE_CODE', pa.string()),
        pa.field('LATITUDE', pa.string(), metadata={'req':'sensitive','target_schema':'float64()'}),
        pa.field('LONGITUDE', pa.string(), metadata={'req':'sensitive','target_schema':'float64()'})
        ],
        metadata={'comment':'raw_neps_upedata_daily_latest'})
    
    tbl = pa.Table.from_pandas(df, schema=schema)
    
    return tbl
    
def get_parquet_raw_neps_vdsl2data_daily_latest(df):
    df.columns =['SEGMENT', 'VDSL2_ID', 'EXC_ABB','RT_CODE', 'FEATURE_STATE', 'LATITUDE', 'LONGITUDE']

    schema = pa.schema([
        pa.field('SEGMENT', pa.string()),
        pa.field('VDSL2_ID', pa.string(), metadata={'req':'sensitive'}),
        pa.field('EXC_ABB', pa.string(), metadata={'req':'sensitive'}),
        pa.field('RT_CODE', pa.string(), metadata={'req':'sensitive'}),
        pa.field('FEATURE_STATE', pa.string()),
        pa.field('LATITUDE', pa.string(), metadata={'req':'sensitive','target_schema':'float64()'}),
        pa.field('LONGITUDE', pa.string(), metadata={'req':'sensitive','target_schema':'float64()'}          )
        ],
        metadata={'comment':'raw_neps_vdsl2data_daily_latest'})
    
    tbl = pa.Table.from_pandas(df, schema=schema)
    
    return tbl