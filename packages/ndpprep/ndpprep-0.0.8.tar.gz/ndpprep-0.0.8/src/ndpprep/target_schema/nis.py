import pyarrow as pa

def preprocess_uint(value):
    if value == 'N/A':
        return None
    else:
        return int(value)
      
def cast_columns_to_target_types(tbl, target_schema):
    tbl_column_names = tbl.schema.names
    casted_columns = []
    for field in target_schema:
        field_name = field.name
        field_index = tbl_column_names.index(field_name) if field_name in tbl_column_names else -1

        if field_index >= 0:
            original_field_type = tbl.schema[field_index].type
            target_field_type = field.type

            # If the original type is different from the target type, cast it
            if original_field_type != target_field_type:
                casted_columns.append((field_name, target_field_type))
            else:
                casted_columns.append((field_name, tbl.schema[field_index].type))
    return tbl.cast(pa.schema(casted_columns), safe=False)
  
''' 
def float_to_string_without_trailing_zeros(value):
    if '.' in value:
        # Match and remove trailing zeros after the decimal point
        return re.sub(r'(?:(\.\d*?[1-9])|(\.0*))$', r'\1', value)
    else:
        return value   
'''


def get_target_schema_daa_clarity_accounts_p(column_names):
    target_schema = pa.schema([
        pa.field('ACCT_NUMBER', pa.string(), metadata={"req":"sensitive"}),
        pa.field('ACCT_STATUS', pa.string()),
        pa.field('ACCT_CUSR_ABBREVIATION', pa.string()),
        pa.field('ACCT_LOCN_ID', pa.decimal128(16, 0)),
        pa.field('ACCT_ESTIMATEDREVENUE', pa.string(),  metadata={'target_schema':'float64()'}),
        pa.field('ACCT_ACCM_ID', pa.decimal128(16, 0)),
        pa.field('ACCT_SALESCHANNEL', pa.string()),
        pa.field('ACCT_DATECREATED', pa.timestamp('ns')),
        pa.field('ACCT_USERCREATED', pa.string(), metadata={"req":"sensitive"}),
        pa.field('ACCT_ACCT_NUMBER', pa.string()),
        pa.field('ACCT_ADDE_ID', pa.decimal128(16, 0)),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
        metadata={
            "Table_Name": "daa_clarity_accounts_p",
            "Classification": "Confidential"
    })
    return target_schema
    
def get_target_schema_daa_clarity_address_serviceability_p(column_names):
    target_schema = pa.schema([
        pa.field('ADDS_FRAC_ID', pa.decimal128(16, 0)),
        pa.field('ADDS_ADDE_ID', pa.decimal128(16, 0)),
        pa.field('ADDS_PRIORITY', pa.string()),
        pa.field('ADDS_DISTANCE', pa.float64()),
        pa.field('ADDS_EQUP_ID', pa.decimal128(16, 0)),
        pa.field('EXTRACTION_TIMESTAMP', pa.string(),  metadata={"target_schema":"timestamp('ns')"})
    ],
    metadata={
        "Classification": "Confidential"
    })
    return target_schema
    
def get_target_schema_daa_clarity_addresses_p(column_names):
    target_schema = pa.schema([
        pa.field('ADDE_ID', pa.decimal128(16, 0)),
        pa.field('ADDE_STAT_ABBREVIATION', pa.string()),
        pa.field('ADDE_STREETNUMBER', pa.string(),metadata={"req":"sensitive"}),
        pa.field('ADDE_POSC_CODE', pa.string()),
        pa.field('ADDE_SUBURB', pa.string(),metadata={"req":"sensitive"}),
        pa.field('ADDE_CITY', pa.string()),
        pa.field('ADDE_COUNTRY', pa.string()),
        pa.field('ADDE_POCS_ID', pa.decimal128(10, 0)),
        pa.field('ADDE_STRN_NAMEANDTYPE', pa.string(), metadata={"req":"sensitive"}),
        pa.field('ADDE_FIELD_1', pa.string(), metadata={"req":"sensitive"}),
        pa.field('ADDE_FIELD_2', pa.string(), metadata={"req":"sensitive"}),
        pa.field('ADDE_FIELD_3', pa.string(), metadata={"req":"sensitive"}),
        pa.field('ADDE_FIELD_4', pa.string(), metadata={"req":"sensitive"}),
        pa.field('ADDE_FIELD_5', pa.string(), metadata={"req":"sensitive"}),
        pa.field('ADDE_FIELD_6', pa.string(), metadata={"req":"sensitive"}),
        pa.field('ADDE_FIELD_7', pa.string(), metadata={"req":"sensitive"}),
        pa.field('ADDE_FIELD_8', pa.string(), metadata={"req":"sensitive"}),
        pa.field('ADDE_FIELD_9', pa.string(), metadata={"req":"sensitive"}),
        pa.field('ADDE_DATECREATED', pa.timestamp('ns')),
        pa.field('ADDE_USERCREATED', pa.string(),metadata={"req":"sensitive"}),
        pa.field('ADDE_DATEMODIFIED', pa.timestamp('ns')),
        pa.field('ADDE_USERMODIFIED', pa.string(),metadata={"req":"sensitive"}),
        pa.field('ADDE_STREETNAME', pa.string(),metadata={"req":"sensitive"}),
        pa.field('ADDE_STRE_TYPE', pa.string()),
        pa.field('ADDRESS_FULL', pa.string(),metadata={"req":"sensitive"}),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Classification": "Confidential"
    })
    return target_schema
    
def get_target_schema_daa_clarity_areas_p(column_names):
    target_schema = pa.schema([
        pa.field('AREA_CODE', pa.string()),
        pa.field('AREA_PREFIX', pa.decimal128(38, 10), metadata={'target_schema':'string()'}),
        pa.field('AREA_RANGEEND', pa.decimal128(38, 10)),
        pa.field('AREA_RANGESTART', pa.decimal128(38, 10)),
        pa.field('AREA_DESCRIPTION', pa.string(),metadata={"req":"sensitive"}),
        pa.field('AREA_AREA_CODE', pa.string()),
        pa.field('AREA_ARET_CODE', pa.string()),
        pa.field('AREA_AUTOPROVISION', pa.string()),
        pa.field('AREA_STAT_ABBREVIATION', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Classification": "Confidential"
    })

    return target_schema

def get_target_schema_daa_clarity_cable_core_ends_p(column_names):
    target_schema = pa.schema([
        pa.field('CACE_CABC_ID', pa.string(), metadata={"req":"sensitive"}),
        pa.field('CACE_CSAP_ID', pa.decimal128(16, 0)),
        pa.field('CACE_COREGROUPID', pa.decimal128(16, 0)),
        pa.field('CACE_FRAA_ID', pa.decimal128(20, 0)),
        pa.field('CACE_SPLP_ID', pa.decimal128(16, 0)),
        pa.field('CACE_CACC_ID', pa.decimal128(16, 0)),
        pa.field('CACE_ID', pa.decimal128(16, 0)),
        pa.field('CACE_LEFL_ID', pa.decimal128(16, 0)),
        pa.field('CACE_DIRECTION', pa.string()),
        pa.field('CACE_PHYC_ID', pa.decimal128(16, 0)),
        pa.field('CACE_ACPO_ID', pa.decimal128(16, 0)),
        pa.field('EXTRACTION_TIMESTAMP',pa.timestamp('ns'))],
    metadata={
        "Classification": "Confidential"
    })

    return target_schema

def get_target_schema_daa_clarity_cable_core_p(column_names):
    target_schema = pa.schema([
        pa.field('CABC_ID', pa.string(), metadata={"req":"sensitive"}),
        pa.field('CABC_CABS_ID', pa.string(), metadata={"req":"sensitive"}),
        pa.field('CABC_LEAF_ID', pa.decimal128(16, 0)),
        pa.field('CABC_NUMBER', pa.string()),
        pa.field('CABC_STATE', pa.string()),
        pa.field('CABC_CCCT_ID', pa.decimal128(16, 0)),
        pa.field('CABC_TYPE', pa.string()),
        pa.field('CABC_BUFFER', pa.string()),
        pa.field('CABC_PHCT_ID', pa.decimal128(16, 0)),
        pa.field('CABC_SEQUENCE', pa.string()),
        pa.field('CABC_CREATED_BY', pa.string(), metadata={"req":"sensitive"}),
        pa.field('CABC_STATUS', pa.string()),
        pa.field('CABC_OLDSTATUS', pa.string()),
        pa.field('CABC_MEASUREDLENGTH', pa.decimal128(38, 10), metadata={'target_schema':'uint16()'}),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
        metadata={
            "Table_Name": "daa_clarity_cable_core_p",
            "Classification": "Confidential"
        })
    
    return target_schema


def get_target_schema_daa_clarity_cable_sheaths_p(column_names):
    target_schema = pa.schema([
        pa.field('CABS_ID', pa.decimal128(16, 0)),
        pa.field('CABS_NAME', pa.string(), metadata={"req": "sensitive"}),
        pa.field('CABS_CAST_TYPE', pa.string()),
        pa.field('CABS_CSPT_ID', pa.decimal128(16, 0)),
        pa.field('CABS_CALCULATEDLENGTH', pa.decimal128(38, 10), metadata={'target_schema':'float64()'}),
        pa.field('CABS_MEASUREDLENGTH', pa.decimal128(38, 10), metadata={'target_schema':'float64()'}),
        pa.field('CABS_ESTIMATEDLOSS', pa.decimal128(38, 10), metadata={'target_schema':'float64()'}),
        pa.field('CABS_STATUS', pa.string()),
        pa.field('CABS_NOTES', pa.string(), metadata={"req": "sensitive"}),
        pa.field('CABS_DIVISION', pa.string()),
        pa.field('CABS_CASR_REELID', pa.string()),
        pa.field('CABS_OLDSTATUS', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
        metadata={
            "Table_Name": "daa_clarity_cable_sheaths_p",
            "Classification": "Confidential"
        })
    
    return target_schema


def get_target_schema_daa_clarity_cards_p(column_names):
    target_schema = pa.schema([
        pa.field('CARD_EQUP_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('CARD_SLOT', pa.string()),
        pa.field('CARD_NAME', pa.string()),
        pa.field('CARD_LOCN_TTNAME', pa.string(), metadata={"req": "sensitive"}),
        pa.field('CARD_MODEL', pa.string()),
        pa.field('CARD_REVISION', pa.string()),
        pa.field('CARD_SERIAL', pa.string()),
        pa.field('CARD_DEVIATION', pa.string()),
        pa.field('CARD_STATUS', pa.string()),
        pa.field('CARD_UNITSTATUS', pa.string()),
        pa.field('CARD_OLD_STATUS', pa.string()),
        pa.field('CARD_MODE', pa.string()),
        pa.field('CARD_NEMSNAME', pa.string()),
        pa.field('PARENT_CARD_SLOT', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
        metadata={
            "Table_Name": "daa_clarity_cards_p",
            "Classification": "Confidential"
        })
      
    return target_schema
  


def get_target_schema_daa_clarity_circuit_addresses_p(column_names):
    target_schema = pa.schema([
        pa.field('CIRA_CIRT_NAME', pa.string()),
        pa.field('CIRA_ADDE_ID', pa.decimal128(16, 0)),
        pa.field('CIRA_TERMINATIONPOINT', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
        metadata={
            "Table_Name": "daa_clarity_circuit_addresses_p",
            "Classification": "Confidential"
        })
    
    return target_schema

def get_target_schema_daa_clarity_circuit_detail_instance_p(column_names):
    target_schema = pa.schema([
        pa.field('CIDI_ID', pa.decimal128(16, 0)),
        pa.field('CIDI_SERO_ID', pa.string()),
        pa.field('CIDI_NAME', pa.string()),
        pa.field('CIDI_VALUE', pa.string(), metadata={"req": "sensitive"}),
        pa.field('CIDI_OPTIONALITY', pa.string()),
        pa.field('CIDI_INOUT', pa.string()),
        pa.field('CIDI_OWNER', pa.string()),
        pa.field('CIDI_VALR_ID', pa.decimal128(16, 0)),
        pa.field('CIDI_DATATYPE', pa.string()),
        pa.field('CIDI_SERVICEKEY', pa.decimal128(8, 0), metadata={'target_schema':'uint8()'}),
        pa.field('CIDI_CIRT_NAME', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
        metadata={
            "Table_Name": "daa_clarity_circuit_detail_instance_p",
            "Classification": "Confidential"
        })
    
    return target_schema


def get_target_schema_daa_clarity_circuit_hierarchy_p(column_names):
    target_schema = pa.schema([
        pa.field('CIRH_PARENT', pa.string()),
        pa.field('CIRH_CHILD', pa.string()),
        pa.field('CIRH_TRIBUTARY', pa.string()), 
        pa.field('CIRH_PARENTORDER', pa.decimal128(38, 10), metadata={'target_schema':'uint16()'}),
        pa.field('CIRH_PATH', pa.string()), 
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
        metadata={
            "Table_Name": "daa_clarity_circuit_hierarchy_p",
            "Classification": "Confidential"
        })
    
    return target_schema


def get_target_schema_daa_clarity_circuits_p(column_names):
    target_schema = pa.schema([
        pa.field('CIRT_NAME', pa.string()),
        pa.field('CIRT_INSERVICE', pa.timestamp('ns')),
        pa.field('CIRT_CUSR_ABBREVIATION', pa.string()),
        pa.field('CIRT_SPED_ABBREVIATION', pa.string()),
        pa.field('CIRT_SERE_ID', pa.string()),
        pa.field('CIRT_STATUS', pa.string()),
        pa.field('CIRT_EXPIRYDATE', pa.timestamp('ns')),
        pa.field('CIRT_TYPE', pa.string()),
        pa.field('CIRT_ARING_ABBREVIATION', pa.string()),
        pa.field('CIRT_BRING_ABBREVIATION', pa.string()),
        pa.field('CIRT_EMPE_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('CIRT_COMMENT', pa.string(), metadata={"req": "sensitive"}),
        pa.field('CIRT_DECOMMISSIONED', pa.timestamp('ns')),
        pa.field('CIRT_SERT_ABBREVIATION', pa.string()),
        pa.field('CIRT_ACCT_NUMBER', pa.string(), metadata={"req": "sensitive"}),
        pa.field('CIRT_LOCN_AEND', pa.string(), metadata={"req": "sensitive"}),
        pa.field('CIRT_LOCN_BEND', pa.string(), metadata={"req": "sensitive"}),
        pa.field('CIRT_COMPLIANCE', pa.string()),
        pa.field('CIRT_PREFIX', pa.string()),
        pa.field('CIRT_SUFFIX', pa.string()),
        pa.field('CIRT_SERIALNO', pa.string()),
        pa.field('CIRT_CLCISVCCODE', pa.string()),
        pa.field('CIRT_CLCISVCMOD', pa.string()),
        pa.field('CIRT_CLCICOMPANY', pa.string()),
        pa.field('CIRT_CLCISEGMENT', pa.string()),
        pa.field('CIRT_OUTSERVICE', pa.timestamp('ns')),
        pa.field('CIRT_SLRL_NAME', pa.string()),
        pa.field('CIRT_DISPLAYNAME', pa.string()),
        pa.field('CIRT_NOTIFYDATE', pa.timestamp('ns')),
        pa.field('CIRT_SERV_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('CIRT_RESERVATIONID', pa.string()),
        pa.field('CIRT_RELM_NAME', pa.string()),
        pa.field('CIRT_REALM', pa.string()),
        pa.field('CIRT_EQUT_LEVEL', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
        metadata={
            "Table_Name": "daa_clarity_circuits_p",
            "Classification": "Confidential"
        })
    
    return target_schema

#kena delete yg lama sbb cust name tak masked.
def get_target_schema_daa_clarity_customer_p(column_names):
    target_schema = pa.schema([
        pa.field('CUSR_ABBREVIATION', pa.string()),
        pa.field('CUSR_NAME', pa.string(), metadata={"PII":"Yes"}),
        pa.field('CUSR_CUTP_TYPE', pa.string()),
        pa.field('CUSR_STAS_ABBREVIATION', pa.string()),
        pa.field('CUSR_ACN', pa.string()),
        pa.field('CUSR_INDC_CODE', pa.string()),
        pa.field('CUSR_DATECREATED', pa.timestamp('ns')),
        pa.field('CUSR_USERCREATED', pa.string()),
        pa.field('CUSR_DATEMODIFIED', pa.timestamp('ns')),
        pa.field('CUSR_USERMODIFIED', pa.string()),
        pa.field('CUSR_WEBUSERNAME', pa.string(), metadata={"req": "sensitive"}),
        pa.field('CUSR_WEBPASSWORD', pa.string(), metadata={"req": "sensitive"}),
        pa.field('CUSR_FEEDBACK', pa.string()),
        pa.field('CUSR_COMMENTS', pa.string(), metadata={"req": "sensitive"}),
        pa.field('CUSR_MEGA_IDENTIFIER', pa.string()),
        pa.field('CUSR_EXTERNAL_CUSTOMER_REF', pa.string()),
        pa.field('CUSR_MARS_ABBREVIATION', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
        metadata={
            "Table_Name": "daa_clarity_customer_p",
            "Classification": "Confidential"
        })

    return target_schema


def get_target_schema_daa_clarity_employees_p(column_names):
    target_schema = pa.schema([
        pa.field('EMPE_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('EMPE_NAME', pa.string(), metadata={"req": "sensitive", "PII":"Yes"}),
        pa.field('EMPE_USERID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('EMPE_ACCP_GROUP', pa.string()),
        pa.field('EMPE_UNIXID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('EMPE_ENDDATE', pa.timestamp('ns')),
        pa.field('EMPE_DESCRIPTION', pa.string(), metadata={"req": "sensitive"}),
        pa.field('EMPE_NOTIFICATION_PREF', pa.string()),
        pa.field('EMPE_LANGUAGE', pa.string()),
        pa.field('EMPE_TERRITORY', pa.string()),
        pa.field('EMPE_EMAIL', pa.string(), metadata={"req": "sensitive"}),
        pa.field('EMPE_FAX', pa.string(), metadata={"req": "sensitive"}),
        pa.field('EMPE_STATUS', pa.string()),
        pa.field('EMPE_SYSTEM_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('EMPE_MOBILE', pa.string(), metadata={"req": "sensitive","PII":"Phone Number"}),
        pa.field('EMPE_TEL', pa.string(), metadata={"req": "sensitive", "PII":"Phone Number"}),
        pa.field('EMPE_EMAILPW', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
        metadata={
            "Table_Name": "daa_clarity_employees_p",
            "Classification": "Confidential"
        })

    return target_schema

def get_target_schema_daa_clarity_equipment_detail_instance_p(column_names):
    target_schema = pa.schema([
        pa.field('EQDI_EQUP_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('EQDI_NAME', pa.string()),
        pa.field('EQDI_VALUE', pa.string(), metadata={"req": "sensitive"}),
        pa.field('EQDI_OPTIONALITY', pa.string()),
        pa.field('EQDI_OWNER', pa.string()),
        pa.field('EQDI_VALR_ID', pa.decimal128(16, 0)),
        pa.field('EQDI_DATATYPE', pa.string()),
        pa.field('EQDI_EQDT_ID', pa.decimal128(16, 0)),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
        metadata={
            "Table_Name": "daa_clarity_equipment_detail_instance_p",
            "Classification": "Confidential"
        })
    
    return target_schema


def get_target_schema_daa_clarity_equipment_p(column_names):
    target_schema = pa.schema([
        pa.field('EQUP_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('EQUP_EQUT_ABBREVIATION', pa.string()),
        pa.field('EQUP_INDEX', pa.string()),
        pa.field('EQUP_LOCN_TTNAME', pa.string(), metadata={"req": "sensitive"}),
        pa.field('EQUP_POSITION', pa.string(), metadata={"req": "sensitive"}),
        pa.field('EQUP_STATUS', pa.string()),
        pa.field('EQUP_MANS_NAME', pa.string()),
        pa.field('EQUP_NODEID', pa.string()),
        pa.field('EQUP_IPADDRESS', pa.string(), metadata={"req": "sensitive"}),
        pa.field('EQUP_CUSR_ABBREVIATION', pa.string()),
        pa.field('EQUP_MANR_ABBREVIATION', pa.string()),
        pa.field('EQUP_EQUM_MODEL', pa.string()),
        pa.field('EQUP_SERIALNUMBER', pa.string(), metadata={"req": "sensitive"}),
        pa.field('EQUP_INSERVICE', pa.timestamp('ns')),
        pa.field('EQUP_SUPPLIER', pa.string()),
        pa.field('EQUP_DEALER', pa.string()),
        pa.field('EQUP_MAINTAINER', pa.string()),
        pa.field('EQUP_COMMENTS', pa.string(), metadata={"req": "sensitive"}),
        pa.field('EQUP_WORG_NAME', pa.string()),
        pa.field('EQUP_EXCC_CODE', pa.string(), metadata={"req": "sensitive"}),
        pa.field('EQUP_RELM_NAME', pa.string()),
        pa.field('EQUP_DISCSTATUS', pa.string()),
        pa.field('EQUP_DISCSTATUSDATE', pa.timestamp('ns')),
        pa.field('EQUP_DISC_STATUS', pa.string()),
        pa.field('EQUP_IPREGION', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
        metadata={
            "Table_Name": "daa_clarity_equipment_p",
            "Classification": "Confidential"
        })

    return target_schema

def get_target_schema_daa_clarity_equipment_types_p(column_names):
    target_schema = pa.schema([
        pa.field('EQUT_ABBREVIATION', pa.string()),
        pa.field('EQUT_DESCRIPTION', pa.string(), metadata={"req": "sensitive"}),
        pa.field('EQUT_GROUP', pa.string()),
        pa.field('EQUT_TECHNOLOGY', pa.string()),
        pa.field('EQUT_FUNC_ID', pa.decimal128(16, 0)),
        pa.field('EQUT_LEVEL', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
        metadata={
            "Table_Name": "daa_clarity_equipment_types_p",
            "Classification": "Confidential"
        })

    return target_schema

def get_target_schema_daa_clarity_fileattachment_links_p(column_names):
    target_schema = pa.schema([
        pa.field('FIAL_ID', pa.decimal128(16, 0)),
        pa.field('FIAL_FILT_ID', pa.decimal128(16, 0)),
        pa.field('FIAL_FOREIGNID', pa.string()),
        pa.field('FIAL_TABLENAME', pa.string()),
        pa.field('FIAL_USERATTACHED', pa.string(), metadata={"req": "sensitive"}),
        pa.field('FIAL_DATEATTACHED', pa.timestamp('ns')),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
        metadata={
            "Table_Name": "daa_clarity_fileattachment_links_p",
            "Classification": "Confidential"
        })

    return target_schema

def get_target_schema_daa_clarity_flash_core_cable_p(column_names):
    target_schema = pa.schema([
        pa.field('CABLE_NAME', pa.string(), metadata={"req": "sensitive"}),
        pa.field('TOTAL_CORE', pa.decimal128(38, 10), metadata={"target_schema": "int32()"}),
        pa.field('CABLE_TYPE', pa.string()),
        pa.field('CONNECTION', pa.string()),
        pa.field('NODE_A', pa.string(), metadata={"req": "sensitive"}),
        pa.field('NODE_B', pa.string(), metadata={"req": "sensitive"}),
        pa.field('FRAME_TYPE', pa.string()),
        pa.field('CON_TYPE', pa.string()),
        pa.field('ROW_A', pa.string()),
        pa.field('PORT_A', pa.string()),
        pa.field('CORE_A',pa.decimal128(38, 10), metadata={"target_schema": "uint8()"}),
        pa.field('ROW_B', pa.string()),
        pa.field('PORT_B', pa.string()),
        pa.field('CORE_B', pa.decimal128(38, 10), metadata={"target_schema": "uint8()"}),
        pa.field('CORE_STATUS', pa.string()),
        pa.field('NE_ID_A', pa.string(), metadata={"req": "sensitive"}),
        pa.field('NE_ID_B', pa.string(), metadata={"req": "sensitive"}),
        pa.field('CCT_NAME', pa.string(), metadata={"req": "sensitive"}),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
        metadata={
            "Table_Name": "daa_clarity_flash_core_cable_p",
            "Classification": "Confidential"
        })
    return target_schema

def get_target_schema_daa_clarity_flash_nis_t_n_j_load_p(column_names):
    target_schema = pa.schema([
        pa.field('CABS_ID', pa.decimal128(16, 0)),
        pa.field('CABLE_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('TOTAL_CORE', pa.decimal128(38, 10), metadata={"target_schema": "int32()"}),
        pa.field('CABLE_TYPE', pa.string()),
        pa.field('CONNECTION', pa.string()),
        pa.field('TM_NODE_A', pa.string(), metadata={"req": "sensitive"}),
        pa.field('TM_NODE_B', pa.string(), metadata={"req": "sensitive"}),
        pa.field('FRAME_TYPE', pa.string()),
        pa.field('CON_TYPE', pa.string()),
        pa.field('ROW_A', pa.string()),
        pa.field('ODF_A', pa.string(), metadata={"req": "sensitive"}),
        pa.field('SHELF_A', pa.string()),
        pa.field('PORT_A', pa.string()),
        pa.field('CORE_A', pa.decimal128(38, 10), metadata={"target_schema": "uint8()"}),
        pa.field('ROW_B', pa.string()),
        pa.field('ODF_B', pa.string(), metadata={"req": "sensitive"}),
        pa.field('SHELF_B', pa.string()),
        pa.field('PORT_B', pa.string()),
        pa.field('CORE_B', pa.decimal128(38, 10), metadata={"target_schema": "uint8()"}),
        pa.field('CORE_STATUS', pa.string()),
        pa.field('NE_ID_A', pa.string()),
        pa.field('NE_ID_B', pa.string()),
        pa.field('CCT_NAME', pa.string(), metadata={"req": "sensitive"}),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
        metadata={
            "Table_Name": "daa_clarity_flash_nis_t_n_j_load_p",
            "Classification": "Confidential"
        })

    return target_schema

def get_target_schema_daa_clarity_frame_appearances_p(column_names):
    target_schema = pa.schema([
        pa.field('FRAA_ID', pa.decimal128(20, 0)),
        pa.field('FRAA_FRAU_ID', pa.decimal128(16, 0)),
        pa.field('FRAA_POSITION', pa.string()), 
        pa.field('FRAA_USAGE', pa.string()),
        pa.field('FRAA_POSITIONGROUPID', pa.string()),
        pa.field('FRAA_SIDE', pa.string()),
        pa.field('FRAA_PHYC_ID', pa.decimal128(16, 0)),
        pa.field('FRAA_CACE_ID', pa.decimal128(16, 0)),
        pa.field('FRAA_CIRT_NAME', pa.string()),
        pa.field('FRAA_STATUS', pa.string()),
        pa.field('FRAA_OLDSTATUS', pa.string()),
        pa.field('FRAA_DETAILS', pa.string()),
        pa.field('FRAA_ADDE_ID', pa.decimal128(16, 0)),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
        metadata={
            "Table_Name": "daa_clarity_frame_appearances_p",
            "Classification": "Confidential"
        })

    return target_schema

def get_target_schema_daa_clarity_frame_container_detailinstance_p(column_names):
    target_schema = pa.schema([
        pa.field('FCDI_ID', pa.decimal128(16, 0)),
        pa.field('FCDI_NAME', pa.string(), metadata={"req": "sensitive"}),
        pa.field('FCDI_VALUE', pa.string()), 
        pa.field('FCDI_OPTIONALITY', pa.string()),
        pa.field('FCDI_OWNER', pa.string()),
        pa.field('FCDI_VALR_ID', pa.decimal128(16, 0)),
        pa.field('FCDI_DATATYPE', pa.string()),
        pa.field('FCDI_FRAC_ID', pa.decimal128(16, 0)),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
        metadata={
            "Table_Name": "daa_clarity_frame_container_detailinstance_p",
            "Classification": "Confidential"
        })

    return target_schema

def get_target_schema_daa_clarity_frame_container_service_types_p(column_names):
    target_schema = pa.schema([
        pa.field('FCST_FRAC_ID', pa.decimal128(16, 0)),
        pa.field('FCST_SERT_ABBREVIATION', pa.string()),
        pa.field('FCST_PRIORITY', pa.decimal128(38, 10), metadata={"target_schema": "uint8()"}), 
        pa.field('FCST_BATCH_ID', pa.decimal128(16, 0)),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
        metadata={
            "Table_Name": "daa_clarity_frame_container_service_types_p",
            "Classification": "Confidential"
        })

    return target_schema

def get_target_schema_daa_clarity_frame_containers_p(column_names):
    target_schema = pa.schema([
        pa.field('FRAC_ID', pa.decimal128(16, 0)),
        pa.field('FRAC_NAME', pa.string()),
        pa.field('FRAC_TYPE', pa.string()),
        pa.field('FRAC_LOCN_TTNAME', pa.string(), metadata={"req": "sensitive"}),
        pa.field('FRAC_FLOOR', pa.string(), metadata={"req": "sensitive"}),
        pa.field('FRAC_FLOORLOCATION', pa.string()),
        pa.field('FRAC_FRAN_NAME', pa.string()),
        pa.field('FRAC_INDEX', pa.string()),
        pa.field('FRAC_DESCRIPTION', pa.string(), metadata={"req": "sensitive"}),
        pa.field('FRAC_MANR_ABBREVIATION', pa.string()),
        pa.field('FRAC_STATUS', pa.string()),
        pa.field('FRAC_OLDSTATUS', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
        metadata={
            "Table_Name": "daa_clarity_frame_containers_p",
            "Classification": "Confidential"
        })

    return target_schema

def get_target_schema_daa_clarity_frame_units_p(column_names):
    target_schema = pa.schema([
        pa.field('FRAU_ID', pa.decimal128(16, 0)),
        pa.field('FRAU_FRAC_ID', pa.decimal128(16, 0)),
        pa.field('FRAU_FUPT_ID', pa.decimal128(16, 0)),
        pa.field('FRAU_NAME', pa.string()),
        pa.field('FRAU_DESCRIPTION', pa.string()),
        pa.field('FRAU_POSITION', pa.string()),
        pa.field('FRAU_DISTANCE', pa.decimal128(38, 10), metadata={"target_schema": "float64()"}),
        pa.field('FRAU_WORG_NAME', pa.string()),
        pa.field('FRAU_MANR_ABBREVIATION', pa.string()),
        pa.field('FRAU_FRUT_NAME', pa.string()),
        pa.field('FRAU_DIRECTION', pa.string()),
        pa.field('FRAU_STATUS', pa.string()),
        pa.field('FRAU_OLDSTATUS', pa.string()),
        pa.field('FRAU_ZONENAME', pa.string()),
        pa.field('FRAU_USAGE', pa.string()),
        pa.field('FRAU_RADIALDISTANCE', pa.decimal128(38, 10), metadata={"target_schema": "float64()"}),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
        metadata={
            "Table_Name": "daa_clarity_frame_units_p",
            "Classification": "Confidential"
        })
    return target_schema

def get_target_schema_daa_clarity_locations_p(column_names):
    target_schema = pa.schema([
        pa.field('LOCN_LOCN_ID', pa.decimal128(16, 0)),
        pa.field('LOCN_LOCT_ABBREVIATION', pa.string()),
        pa.field('LOCN_AREA_CODE', pa.string(), metadata={"req": "sensitive"}),
        pa.field('LOCN_ID', pa.decimal128(16, 0)),
        pa.field('LOCN_TTNAME', pa.string(), metadata={"req": "sensitive"}),
        pa.field('LOCN_TTNAME_DESCRIPTION', pa.string(), metadata={"req": "sensitive"}),
        pa.field('LOCN_OWNER', pa.string()),
        pa.field('LOCN_DETAILS', pa.string()),
        pa.field('LOCN_NODE', pa.string()),
        pa.field('LOCN_X', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('LOCN_Y', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('LOCN_REGN_CODE', pa.string()),
        pa.field('LOCN_SHORT_CODE', pa.string()),
        pa.field('LOCN_BUILDING_NAME', pa.string(), metadata={"req": "sensitive"}),
        pa.field('LOCN_STAS_ABBREVIATION', pa.string()),
        pa.field('LOCN_SERV_ID', pa.string()),
        pa.field('LOCN_GEOHASH', pa.string(), metadata={"req": "sensitive"}),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
        metadata={
            "Table_Name": "daa_clarity_locations_p",
            "Classification": "Confidential"
        })

    return target_schema


def get_target_schema_daa_clarity_mamz_dwh_stat_p(column_names):
    target_schema = pa.schema([
        pa.field('CUST_SERVICE_NUMBER', pa.string()),
        pa.field('HAS_DSL', pa.string()),
        pa.field('DP_ACTUAL_NAME', pa.string()),
        pa.field('CABLEONCABINET', pa.decimal128(38, 10)),
        pa.field('CABLEONEXCHANGE', pa.decimal128(38, 10)),
        pa.field('DP_ACTUAL_ID', pa.decimal128(16, 0)),
        pa.field('CURRENT_DSLAM_TYPE', pa.string()),
        pa.field('CURRENT_DSLAM_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('RDSLAM_LESS_2M', pa.string()), 
        pa.field('RDSLAM_MORE_2M', pa.string()),
        pa.field('ADSLAM_LESS_2M', pa.string()), 
        pa.field('ADSLAM_MORE_2M', pa.string()),
        pa.field('CABINET_ACTUAL_ID', pa.decimal128(16, 0)),
        pa.field('ATTAINABLE_RATE', pa.string()), #uint8
        pa.field('CUST_ATTAINABLE_RATE', pa.string()),
        pa.field('DSL_SERVICE_TYPE', pa.string()), 
        pa.field('DATA_UPDATED', pa.string()),
        pa.field('ACCOUNT_NUM', pa.string()),
        pa.field('CONNECT_DATE', pa.timestamp('ns')),
        pa.field('ACCESS_IND', pa.string()),
        pa.field('IP_ADDR_NUM', pa.string(), metadata={"req": "sensitive"}),
        pa.field('SUBNET_MASK_NUM', pa.string(), metadata={"req": "sensitive"}),
        pa.field('SERVICE_TYPE_CODE', pa.string()),
        pa.field('SERVICE_STATUS', pa.string()),
        pa.field('DSL_SERVICE_ID', pa.string()), #
        pa.field('PSTN_SERV_ID', pa.string()), #
        pa.field('MDF_ID', pa.decimal128(16, 0)),
        pa.field('BRAS_PORT_ID', pa.decimal128(16, 0)),
        pa.field('ATM_PORT_ID', pa.decimal128(16, 0)),
        pa.field('HOST_PORT_ID', pa.decimal128(16, 0)),
        pa.field('METRO_PORT_ID', pa.decimal128(16, 0)),
        pa.field('DSLAM_PORT_ID', pa.decimal128(16, 0)),
        pa.field('SERV_SPEED', pa.string()),
        pa.field('DOWNSTREAM_SPEED', pa.string()),
        pa.field('UPSTREAM_SPEED', pa.string()),
        pa.field('SERVICE_SPEED_NUM', pa.string()),
        pa.field('CUST_TAGGED_DATE', pa.string()),
        pa.field('EXCHANGE_CODE', pa.string(), metadata={"req": "sensitive"}),
        pa.field('PTT_NAME', pa.string()),
        pa.field('STATE_CODE', pa.string()),
        pa.field('MAX_POSSIBLE_SPEED', pa.string()),
        pa.field('DSLAM_MANUFACTURER', pa.string()),
        pa.field('EXCHANGE_PORT', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
        metadata={
            "Table_Name": "daa_clarity_mamz_dwh_stat_p",
            "Classification": "Confidential"
        })
    return target_schema

def get_target_schema_daa_clarity_mit_region_state_ptt_p(column_names):
    target_schema = pa.schema([
        pa.field('BUILDING_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('BUILDING_DESCRIPTION', pa.string(), metadata={"req": "sensitive"}),
        pa.field('PTT', pa.string(), metadata={"req": "sensitive"}),
        pa.field('STATE', pa.string()),
        pa.field('REGION', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
        metadata={
            "Table_Name": "daa_clarity_mit_region_state_ptt_p",
            "Classification": "Confidential"
        })

    return target_schema

def get_target_schema_daa_clarity_number_status_p(column_names):
    target_schema = pa.schema([
        pa.field('NUMS_BEFORE_CODE', pa.string()),
        pa.field('NUMS_DESCRIPTION', pa.string()),
        pa.field('NUMS_ID', pa.decimal128(38, 10)),
        pa.field('NUMS_AFTER_CODE', pa.string()), 
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
        metadata={
            "Table_Name": "daa_clarity_number_status_p",
            "Classification": "Confidential"
        })

    return target_schema

def get_target_schema_daa_clarity_numbers_p(column_names):
    target_schema = pa.schema([
        pa.field('NUMB_ID', pa.decimal128(16, 0)),
        pa.field('NUMB_AREA_CODE', pa.string(), metadata={"req": "sensitive"}),
        pa.field('NUMB_NUMBER', pa.string(), metadata={"req": "sensitive"}),
        pa.field('NUMB_STATUSCHG_DATE', pa.timestamp('ns')),
        pa.field('NUMB_NUMT_TYPE', pa.string()),
        pa.field('NUMB_REDIRECTION_NUMBER', pa.string()),
        pa.field('NUMB_REDIRECTION_DATE', pa.timestamp('ns')),
        pa.field('NUMB_SERV_ID', pa.string()), #
        pa.field('NUMB_RESERVE_ID', pa.string()), #
        pa.field('NUMB_NUSS_SET', pa.decimal128(16, 0)),
        pa.field('NUMB_NUCC_CODE', pa.string()),
        pa.field('NUMB_NUTE_TECHNOLOGY', pa.string()),
        pa.field('NUMB_NUMS_ID', pa.decimal128(38, 10), metadata={"target_schema": "decimal128(10, 0)"}), 
        pa.field('NUMB_COUNTRY_NUCC_CODE', pa.string()),
        pa.field('NUMB_NETMASK', pa.decimal128(2, 0)), 
        pa.field('NUMB_DNSS_ID', pa.decimal128(16, 0)),
        pa.field('NUMB_WORG_NAME', pa.string()),
        pa.field('NUMB_NUNE_NETNAME', pa.string()),
        pa.field('NUMB_IPCONTROL', pa.string()),
        pa.field('NUMB_REMARK', pa.string(), metadata={"req": "sensitive"}),
        pa.field('NUMB_IPCONTINUITY', pa.string()),
        pa.field('NUMB_NUMT_SUBTYPE', pa.string()),
        pa.field('NUMB_NAT', pa.string()),
        pa.field('NUMB_SUBBEDNET_ID', pa.decimal128(16, 0)),
        pa.field('NUMB_USAGE', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
        metadata={
            "Table_Name": "daa_clarity_numbers_p",
            "Classification": "Confidential"
        })

    return target_schema

def get_target_schema_daa_clarity_other_names_p(column_names):
    target_schema = pa.schema([
        pa.field('OTHN_CIRT_NAME', pa.string()),
        pa.field('OTHN_NAME', pa.string(), metadata={"req": "sensitive"}),
        pa.field('OTHN_NAMETYPE', pa.string()),
        pa.field('OTHN_WORG_NAME', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
        metadata={
            "Table_Name": "daa_clarity_other_names_p",
            "Classification": "Confidential"
        })
    return target_schema

def get_target_schema_daa_clarity_planned_event_centers_p(column_names):
    target_schema = pa.schema([
        pa.field('PLEE_ABBREVIATION', pa.string()),
        pa.field('PLEE_DESCRIPTION', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
        metadata={
            "Table_Name": "daa_clarity_planned_event_centers_p",
            "Classification": "Confidential"
        })

    return target_schema

def get_target_schema_daa_clarity_planned_event_contacts_p(column_names):
    target_schema = pa.schema([
        pa.field('PLEC_PLAE_NUMBER', pa.string()),
        pa.field('PLEC_CONP_ID', pa.decimal128(16, 0)),
        pa.field('PLEC_EMPE_USERID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
        metadata={
            "Table_Name": "daa_clarity_planned_event_contacts_p",
            "Classification": "Confidential"
        })

    return target_schema

def get_target_schema_daa_clarity_planned_event_impact_p(column_names):
    target_schema = pa.schema([
        pa.field('PLEI_PLAE_NUMBER', pa.string()),
        pa.field('PLEI_OBJECT_ID', pa.string()),
        pa.field('PLEI_CUSR_ABBREVIATION', pa.string()),
        pa.field('PLEI_SERE_ID', pa.string()),
        pa.field('PLEI_IMPACT', pa.string()),
        pa.field('PLEI_SERT_ABBREVIATION', pa.string()),
        pa.field('PLEI_OBJECT_TYPE', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
        metadata={
            "Table_Name": "daa_clarity_planned_event_impact_p",
            "Classification": "Confidential"
        })

    return target_schema

def get_target_schema_daa_clarity_planned_event_notes_p(column_names):
    target_schema = pa.schema([
        pa.field('PLEN_SEQUENCE', pa.uint8()),
        pa.field('PLEN_PLAE_NUMBER', pa.string()),
        pa.field('PLEN_USERNAME', pa.string(), metadata={"req": "sensitive"}),
        pa.field('PLEN_DATECREATED', pa.timestamp('ns')),
        pa.field('PLEN_CATEGORY', pa.string()),
        pa.field('PLEN_TITLE', pa.string()),
        pa.field('PLEN_DETAILS', pa.string(), metadata={"req": "sensitive"}),
        pa.field('PLEN_LONGDESCRIPTION', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
        metadata={
            "Table_Name": "daa_clarity_planned_event_notes_p",
            "Classification": "Confidential"
        })

    return target_schema

def get_target_schema_daa_clarity_planned_event_targets_p(column_names):
    target_schema= pa.schema([
        pa.field('PETA_PLAE_NUMBER', pa.string()),
        pa.field('PETA_FOREIGNID', pa.string()),
        pa.field('PETA_FOREIGNTYPE', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
        metadata={
            "Table_Name": "daa_clarity_planned_event_targets_p",
            "Classification": "Confidential"
        })

    return target_schema

def get_target_schema_daa_clarity_planned_event_tasks_p(column_names):
    target_schema = pa.schema([
        pa.field('PLET_ID', pa.decimal128(16, 0)),
        pa.field('PLET_PLAE_NUMBER', pa.string()),
        pa.field('PLET_DESCRIPTION', pa.string(), metadata={"req": "sensitive"}),
        pa.field('PLET_SEQUENCE', pa.string()),
        pa.field('PLET_LOCN_TTNAME', pa.string()),
        pa.field('PLET_TARGETDATE', pa.timestamp('ns')),
        pa.field('PLET_COMPLETED', pa.string()),
        pa.field('PLET_ASSIGNEDTO', pa.string()), # 'AND JU'
        pa.field('PLET_EMPE_USERID', pa.string()),
        pa.field('PLET_PTAS_CODE', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
        metadata={
            "Table_Name": "daa_clarity_planned_event_tasks_p",
            "Classification": "Confidential"
        })

    return target_schema

def get_target_schema_daa_clarity_planned_events_jn_p(column_names):       
    target_schema = pa.schema([
        pa.field('PLAE_NUMBER', pa.string()),
        pa.field('PLAE_PLANNEDSTART', pa.timestamp('ns')),
        pa.field('PLAE_PLANNEDEND', pa.timestamp('ns')),
        pa.field('PLAE_ACTUALSTART', pa.timestamp('ns')),
        pa.field('PLAE_ACTUALEND', pa.timestamp('ns')),
        pa.field('PLAE_TITLE', pa.string()),
        pa.field('PLAE_OBJECTIVE', pa.string(), metadata={"req": "sensitive"}),
        pa.field('PLAE_IMPACTTYPE', pa.string()),
        pa.field('PLAE_ACTT_ABBREVIATION', pa.string(), metadata={"req": "sensitive"}),
        pa.field('PLAE_APPROVEDBY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('PLAE_ENTEREDBY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('PLAE_USERNAME', pa.string(), metadata={"req": "sensitive"}),
        pa.field('PLAE_CREATED', pa.timestamp('ns')),
        pa.field('PLAE_REQUESTOR', pa.string(), metadata={"req": "sensitive"}),
        pa.field('PLAE_REQA_ABBREVIATION', pa.string()),
        pa.field('PLAE_STATE', pa.string()),
        pa.field('PLAE_SUCCEEDED', pa.string()),
        pa.field('PLAE_PROJECT', pa.string()),
        pa.field('PLAE_FALLBACKTIME', pa.timestamp('ns')),
        pa.field('PLAE_RESCHEDULESTATE', pa.timestamp('ns')),
        pa.field('PLAE_RESCHEDULEPLANDATE', pa.timestamp('ns')),
        pa.field('PLAE_PLATRECOMMENDED', pa.string()),
        pa.field('PLAE_COMMENTS', pa.string()),
        pa.field('PLAE_CREATEDCENTER', pa.string()),
        pa.field('PLAE_WORG_NAME', pa.string(), metadata={"req": "sensitive"}),
        pa.field('PLAE_CRMNOTIFIED', pa.string()), 
        pa.field('PLAE_OUTAGESTART', pa.timestamp('ns')),
        pa.field('PLAE_OUTAGEEND', pa.timestamp('ns')),
        pa.field('PLAE_RING', pa.string()),
        pa.field('PLAE_PLAE_NUMBER', pa.string()), # newly added
        pa.field('PLAE_JN_OPERATION', pa.string(), metadata={"req": "sensitive"}),
        pa.field('PLAE_JN_ORACLEUSER', pa.string(), metadata={"req": "sensitive"}),
        pa.field('PLAE_JN_DATETIME', pa.timestamp('ns')),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
        metadata={
            "Table_Name": "daa_clarity_planned_events_jn_p",
            "Classification": "Confidential"
        })

    return target_schema

def get_target_schema_daa_clarity_planned_events_p(column_names):
    target_schema = pa.schema([
        pa.field('PLAE_NUMBER', pa.string()),
        pa.field('PLAE_PLANNEDSTART', pa.timestamp('ns')),
        pa.field('PLAE_PLANNEDEND', pa.timestamp('ns')),
        pa.field('PLAE_ACTUALSTART', pa.timestamp('ns')),
        pa.field('PLAE_ACTUALEND', pa.timestamp('ns')),
        pa.field('PLAE_TITLE', pa.string(), metadata={"req": "sensitive"}),
        pa.field('PLAE_OBJECTIVE', pa.string(), metadata={"req": "sensitive"}),
        pa.field('PLAE_IMPACTTYPE', pa.string()),
        pa.field('PLAE_ACTT_ABBREVIATION', pa.string()),
        pa.field('PLAE_APPROVEDBY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('PLAE_ENTEREDBY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('PLAE_USERNAME', pa.string(), metadata={"req": "sensitive"}),
        pa.field('PLAE_CREATED', pa.timestamp('ns')),
        pa.field('PLAE_REQUESTOR', pa.string(), metadata={"req": "sensitive"}),
        pa.field('PLAE_REQA_ABBREVIATION', pa.string()),
        pa.field('PLAE_STATE', pa.string()),
        pa.field('PLAE_SUCCEEDED', pa.string()),
        pa.field('PLAE_PROJECT', pa.string()),
        pa.field('PLAE_FALLBACKTIME', pa.timestamp('ns')),
        pa.field('PLAE_RESCHEDULESTATE', pa.timestamp('ns')),
        pa.field('PLAE_RESCHEDULEPLANDATE', pa.timestamp('ns')),
        pa.field('PLAE_PLATRECOMMENDED', pa.string()),
        pa.field('PLAE_COMMENTS', pa.string(), metadata={"req": "sensitive"}),
        pa.field('PLAE_CREATEDCENTER', pa.string()),
        pa.field('PLAE_WORG_NAME', pa.string()),
        pa.field('PLAE_CRMNOTIFIED', pa.string()),
        pa.field('PLAE_OUTAGESTART', pa.timestamp('ns')),
        pa.field('PLAE_OUTAGEEND', pa.timestamp('ns')),
        pa.field('PLAE_RING', pa.string(), metadata={"req": "sensitive"}),
        pa.field('PLAE_PLAE_NUMBER', pa.string()),
        pa.field('PLAE_PEPR_CODE', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
        metadata={
            "Table_Name": "daa_clarity_planned_events_p",
            "Classification": "Confidential"
        })
    
    return target_schema

  
def get_target_schema_daa_clarity_pmt_financial_temp_p(column_names):
    target_schema = pa.schema([
        pa.field('ACT_DESCRIPTION', pa.string()),
        pa.field('ANDGROUP', pa.string()),
        pa.field('AR_APPROVED_DATE', pa.timestamp('ns')),
        pa.field('AR_NO', pa.string()),
        pa.field('ASSETIZATION_TECO', pa.string()),
        pa.field('ASSET_ASSETIZATION', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('ASSET_IN_CWIP', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('DESCRIPTION', pa.string(), metadata={"req": "sensitive"}),
        pa.field('GEMS_ACTIVITIES_TYPE', pa.string()),
        pa.field('INCIDENTAL_COST', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('LABOUR_COST', pa.string(),metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('LAST_PAC_APPROVED', pa.timestamp('ns')),
        pa.field('LOB', pa.string()),
        pa.field('MATERIAL_COST', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('ORDERCATEGORY', pa.string()),
        pa.field('ORDER_ID', pa.string()),
        pa.field('OVERALL_ACTUAL', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('OVERALL_ACTUALINCAPPROVED', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('OVERALL_ACTUALLABOURAPPROVED', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('OVERALL_ACTUALMATAPPROVED', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('OVERALL_ACTUAL_BUDGET', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('OVERALL_ACTUAL_INCIDENTAL_COST', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('OVERALL_ACTUAL_LABOUR_COST', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('OVERALL_ACTUAL_MATERIAL_COST', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('OVERALL_ASSET_ASSETIZATION', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('OVERALL_BUDGET', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('OVERALL_BUDGET_APPROVED', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('OVERALL_COMMITMENT', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('OVERALL_COST', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('PAC_ID', pa.string()),
        pa.field('PAC_STATUS', pa.string()),
        pa.field('PROGRAM', pa.string()),
        pa.field('PROJECT_ID', pa.string()),
        pa.field('PROJECT_NAME', pa.string(), metadata={"req": "sensitive"}),
        pa.field('PROJECT_PERCENTAGE', pa.float64()),
        pa.field('PROJECT_STATUS', pa.string()),
        pa.field('PROJECT_VPRIME_PROGRESS', pa.float64()),
        pa.field('PSESSION', pa.string()),
        pa.field('RAP_INCIDENTAL', pa.float64()),
        pa.field('RAP_LABOUR', pa.float64()),
        pa.field('RAP_MATERIAL', pa.float64()),
        pa.field('RAP_TOTAL_REVISED_COST', pa.float64()),
        pa.field('REGION', pa.string()),
        pa.field('STATUS', pa.string()),
        pa.field('STOCK', pa.uint16()),
        pa.field('TMNODE', pa.string()),
        pa.field('TOTAL_COST_AR', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('TOTAL_Y1', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('TOTAL_Y2', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('Y1_INCIDENTAL', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('Y1_LABOUR', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('Y1_MATERIAL', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('Y2_INCIDENTAL', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('Y2_LABOUR', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('Y2_MATERIAL', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('YEAR_ACTUAL', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('YEAR_ACTUAL_BUDGET', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('YEAR_BUDGET', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('YEAR_COMMITMENT', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
        metadata={
            "Table_Name": "daa_clarity_pmt_financial_temp_p",
            "Classification": "Confidential"
        })
    
    return target_schema

# not process yet
def get_target_schema_daa_clarity_pmt_order_p(column_names):
    target_schema = pa.schema([
        pa.field('WAITERS', pa.string()),
        pa.field('PAYMENT_STATUS_ORDER', pa.string()),
        pa.field('ICHECK_REFNO', pa.string()),
        pa.field('HORIZONTAL_TRUNKING', pa.string()),
        pa.field('CREATOR_GROUP', pa.string()),
        pa.field('OPEXPROJNO', pa.string(), metadata={"req": "sensitive"}),
        pa.field('CUSTOMER_PIC_CONTACT', pa.string(), metadata={"req": "sensitive", "PII":"Phone Number"}),
        pa.field('LOCATION_SECTION', pa.string(), metadata={"req": "sensitive"}),
        pa.field('TOTALREVENUE', pa.string(),  metadata={"target_schema": "float64()"}),
        pa.field('CNFDACCESSTX', pa.string()),
        pa.field('TOTALRESIDENTIAL', pa.string(),  metadata={"target_schema": "uint16()"}),
        pa.field('CONFIRMED_BY', pa.string(), metadata={"req": "sensitive", "PII":"Yes"}),
        pa.field('CONFIRMED_DATE', pa.timestamp('ns')),
        pa.field('STATUS', pa.string()),
        pa.field('SFP_TYPE', pa.string()),
        pa.field('LOB', pa.string()),
        pa.field('PMNAME', pa.string()),
        pa.field('DESCRIPTION', pa.string(), metadata={"req": "sensitive"}),
        pa.field('STATE', pa.string()),
        pa.field('AREA_INVESTMENT', pa.string()),
        pa.field('CUSTOMER_NAME', pa.string()),
        pa.field('CUSTOMER_AGENCY', pa.string()),
        pa.field('DRY2', pa.uint16()),
        pa.field('DBY1', pa.uint16()),
        pa.field('RY3', pa.uint32()),
        pa.field('RY7', pa.uint32()),
        pa.field('CIRCULATION', pa.string()),
        pa.field('CNFDFACILITIES', pa.string()),
        pa.field('CTD', pa.string()),
        pa.field('INFRA_GROUP', pa.string()),
        pa.field('ORDER_OWNER', pa.string()),
        pa.field('STREAMYX_SUBS', pa.string()),
        pa.field('PRE_UNIFI_SUBS', pa.string()),
        pa.field('APPROVED_DATE', pa.timestamp('ns')),
        pa.field('WAITERS_ID', pa.decimal128(16, 0)),
        pa.field('TRO_NEW_FDP', pa.string(), metadata={"req": "sensitive"}),
        pa.field('SITE_READINESS', pa.string()),
        pa.field('TOTAL_BUILDING', pa.uint16()),
        pa.field('DBY5', pa.uint16()),
        pa.field('RY2', pa.uint32()),
        pa.field('SERVICETYPE', pa.string()),
        pa.field('SLG_INFO', pa.string()),
        pa.field('DATE_AGREEMENT', pa.timestamp('ns')),
        pa.field('CABINET_CATEGORY', pa.string()),
        pa.field('DATE_REVISED_REMARK', pa.string()),
        pa.field('COMPLETED_DATE', pa.timestamp('ns')),
        pa.field('AWACS_ID', pa.decimal128(20, 0)),
        pa.field('ORDERTYPE', pa.string()),
        pa.field('TMNODE2', pa.string(), metadata={"req": "sensitive"}),
        pa.field('LOCATION_UNIT', pa.string(), metadata={"req": "sensitive"}),
        pa.field('LOCATION_BUILDING', pa.string(), metadata={"req": "sensitive"}),
        pa.field('CITY', pa.string()),
        pa.field('DRY4', pa.uint16()),
        pa.field('DRY5', pa.uint16()),
        pa.field('DBY3', pa.uint16()),
        pa.field('RY4', pa.uint32()),
        pa.field('RY6', pa.uint32()),
        pa.field('SMARTPARTNERSHIP', pa.string()),
        pa.field('CREATE_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('CREATE_DATE', pa.timestamp('ns')),
        pa.field('UPDATE_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('BANDWIDTH_TYPE', pa.string()),
        pa.field('NRP_STATES', pa.string()),
        pa.field('BUILDING_AGREEMENT_STATUS', pa.string()),
        pa.field('CABINET_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('SFDC_OPPORTUNITY_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('ORDER_INST', pa.string(), metadata={"req": "sensitive"}),
        pa.field('BUILDING_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('PSESSION', pa.string()),
        pa.field('ORDERMSB', pa.string()),
        pa.field('PMCONTACT', pa.string(), metadata={"req": "sensitive"}),
        pa.field('REGION', pa.string()),
        pa.field('PROPERTYUNIT', pa.uint16()),
        pa.field('DRY3', pa.uint16()),
        pa.field('RY5', pa.uint32()),
        pa.field('PROGRAM', pa.string()),
        pa.field('APPROVED_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('CONTRACT_NUMBER', pa.string(), metadata={"req": "sensitive"}),
        pa.field('MIN_PF', pa.uint16()),
        pa.field('PF', pa.uint16()),
        pa.field('ORDER_ID', pa.string()),
        pa.field('ORDERGROUP', pa.string()),
        pa.field('REFID', pa.string()),
        pa.field('LOCATION', pa.string(), metadata={"req": "sensitive"}),
        pa.field('DATE_CUST_RFS', pa.timestamp('ns')),
        pa.field('DBY4', pa.uint16()),
        pa.field('RY8', pa.uint32()),
        pa.field('RY9', pa.uint32()),
        pa.field('PLANPHYSICAL', pa.string()),
        pa.field('DRAFT_FLAG', pa.string()),
        pa.field('INFRA_REQUIRED', pa.string()),
        pa.field('TOTALBUSINESS', pa.uint16()),
        pa.field('BANDWIDTH', pa.uint16()),
        pa.field('COMPLETED_BY', pa.string(), metadata={"req": "sensitive", "PII":"Yes"}),
        pa.field('TOTAL_SUBS', pa.uint16()),
        pa.field('SITE_ID_5G', pa.string(), metadata={"req": "sensitive"}),
        pa.field('ORDERCATEGORY', pa.string()),
        pa.field('CUSTOMER_PIC_NAME', pa.string(), metadata={"req": "sensitive", "PII":"Yes"}),
        pa.field('NOVA', pa.string(), metadata={"req": "sensitive"}),
        pa.field('TMNODE', pa.string(), metadata={"req": "sensitive"}),
        pa.field('ANDGROUP', pa.string()),
        pa.field('LOCATION_POSTCODE', pa.string()),
        pa.field('DATE_TM_RFS', pa.timestamp('ns')),
        pa.field('DRY1', pa.uint16()),
        pa.field('RY1', pa.uint32()),
        pa.field('RY10', pa.uint32()),
        pa.field('REMARK', pa.string(), metadata={"req": "sensitive"}),
        pa.field('DATE_DECOMM_ORDER', pa.timestamp('ns')),
        pa.field('MIGRATION_FLAG', pa.string()),
        pa.field('BAU_NEID_DP_NUMBER', pa.string(), metadata={"req": "sensitive"}),
        pa.field('AMOUNT_PAID', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('LOA_DATE', pa.timestamp('ns')),
        pa.field('LOCATION_STREET', pa.string(), metadata={"req": "sensitive"}),
        pa.field('PROPERTY_TYPE', pa.string()),
        pa.field('DATE_REVISED_RFS', pa.timestamp('ns')),
        pa.field('DBY2', pa.uint16()),
        pa.field('CONTRI_AMOUNT', pa.string()),
        pa.field('INFRATYPE', pa.string()),
        pa.field('NEID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('UPDATE_DATE', pa.timestamp('ns')),
        pa.field('ENDUSER_OID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
        metadata={
            "Table_Name": "daa_clarity_pmt_order_p",
            "Classification": "Confidential"
        })

    return target_schema

# not process yet
def get_target_schema_daa_clarity_pmt_orders_temp_p(column_names):
    target_schema = pa.schema([
        pa.field('ORDER_ID', pa.string()),
        pa.field('DESCRIPTION', pa.string(), metadata={"req": "sensitive"}),
        pa.field('REFID', pa.string()),
        pa.field('ENDUSER_OID', pa.string()),
        pa.field('ORDERTYPE', pa.string()),
        pa.field('ORDER_SUB_TYPE', pa.string()),
        pa.field('ORDERCATEGORY', pa.string()),
        pa.field('ORDER_STATUS', pa.string()),
        pa.field('ISSUES', pa.string()),
        pa.field('SESSIONS', pa.string()),
        pa.field('CUSTOMER_RFS', pa.string(), metadata={"target_schema": "date32()"}),
        pa.field('TM_RFS', pa.string(), metadata={"target_schema": "date32()"}),
        pa.field('REVISED_RFS', pa.string(), metadata={"target_schema": "date32()"}),
        pa.field('COMMISSIONED_DATE', pa.string(), metadata={"target_schema": "date32()"}),
        pa.field('COMM_INFRA_INFO', pa.string(), metadata={"req": "sensitive"}),
        pa.field('CUSTOMER_NAME', pa.string()),
        pa.field('CUSTOMER_AGENCY', pa.string()),
        pa.field('ADDESS', pa.string(), metadata={"req": "sensitive"}),
        pa.field('LOCATION_DESCRIPTION', pa.string(), metadata={"req": "sensitive"}),
        pa.field('REGION', pa.string()),
        pa.field('ANDGROUP', pa.string()),
        pa.field('TMNODE', pa.string(), metadata={"req": "sensitive"}),
        pa.field('INFRA_GROUP', pa.string()),
        pa.field('OWNERORDER', pa.string(), metadata={"req": "sensitive", "PII":"Yes"}),
        pa.field('PROJECTMANAGERNAME', pa.string(), metadata={"req": "sensitive", "PII":"Yes"}),
        pa.field('PROJECTMANAGERCONTACTNO', pa.string(), metadata={"req": "sensitive", "PII":"Phone Number"}),
        pa.field('CREATEDBY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('CREATEDDATE', pa.timestamp('ns')),
        pa.field('LOBS', pa.string()),
        pa.field('NOVAORDERID', pa.string()),
        pa.field('SERVICETYPE', pa.string()),
        pa.field('BANDWIDTH', pa.string()),
        pa.field('TYPE', pa.string()),
        pa.field('INFRA_REQUIRED', pa.string()),
        pa.field('SLG_INFO', pa.string()),
        pa.field('PROJECTREQUIRED', pa.string()),
        pa.field('PROJECTNO', pa.string()),
        pa.field('PROJECTSTATUS', pa.string()),
        pa.field('PEROJECTPROGRESS', pa.string()),
        pa.field('CURRENTACTIVITY', pa.string()),
        pa.field('NRP_STATES', pa.string()),
        pa.field('DRY1', pa.uint16()),
        pa.field('DRY2', pa.uint16()),
        pa.field('DRY3', pa.uint16()),
        pa.field('DRY4', pa.uint16()),
        pa.field('DRY5', pa.uint16()),
        pa.field('TOTALRESIDENTIAL', pa.uint16()),
        pa.field('DBY1', pa.uint16()),
        pa.field('DBY2', pa.uint16()),
        pa.field('DBY3', pa.uint16()),
        pa.field('DBY4', pa.uint16()),
        pa.field('DBY5', pa.uint16()),
        pa.field('TOTALBUSINESS', pa.uint32()),
        pa.field('PF', pa.string()),
        pa.field('WAITERS', pa.string()),
        pa.field('ICHECK_REFNO', pa.string()),
        pa.field('LOA_DATE', pa.string(), metadata={"target_schema":"date32()"}),
        pa.field('RY1', pa.uint32()),
        pa.field('RY2', pa.uint32()),
        pa.field('RY3', pa.uint32()),
        pa.field('TOTALREVENUE', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('BUILDING_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('MIGRATION_FLAG', pa.string()),
        pa.field('DATE_APPROVED', pa.timestamp('ns')),
        pa.field('DATE_CONFIRMED', pa.timestamp('ns')),
        pa.field('AREA_INVESTMENT', pa.string()),
        pa.field('STREAMYX_SUBS', pa.string()),
        pa.field('CABINET_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('CABINET_CATEGORY', pa.string()),
        pa.field('BAU_NEID_DP_NUMBER', pa.string(), metadata={"req": "sensitive"}),
        pa.field('PRE_UNIFI_SUBS', pa.string()),
        pa.field('PROPERTY_TYPE', pa.string()),
        pa.field('DATE_COMPLETED', pa.string(), metadata={"target_schema": "date32()"}),
        pa.field('PROJECT_ALL', pa.string()),
        pa.field('PROJECT_ISSUES_NAME', pa.string()),
        pa.field('CREATOR_GROUP', pa.string()),
        pa.field('NEW_UPDATE_BY', pa.string(), metadata={"req": "sensitive", "PII":"Yes"}),
        pa.field('JN_DATETIME', pa.timestamp('ns')),
        pa.field('CONTRACT_NUMBER', pa.string(), metadata={"req": "sensitive"}),
        pa.field('SFDC_OPPORTUNITY_ID', pa.decimal128(16, 0)),
        pa.field('TOTAL_SUBS', pa.string()),
        pa.field('OPEXPROJNO', pa.string()),
        pa.field('NEW_STATUS_UPDATE_DATE', pa.timestamp('ns')),
        pa.field('NO_PROPERTYUNIT', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
        metadata={
            "Table_Name": "daa_clarity_pmt_orders_temp_p",
            "Classification": "Confidential"
        })

    return target_schema

  
def get_target_schema_daa_clarity_pmt_pac_temp_p(column_names):
    target_schema = pa.schema([
        pa.field('PAC_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('PAC_STATUS', pa.string()),
        pa.field('PAC_CREATED_BY', pa.string(), metadata={"req": "sensitive", "PII":"Yes"}),
        pa.field('CREATEDDATE', pa.timestamp('ns')),
        pa.field('LAST_PAC_APPROVED', pa.timestamp('ns')),
        pa.field('PAC_NPV', pa.float64()),
        pa.field('PAC_IRR', pa.float64()),
        pa.field('PAC_PAYBACK', pa.float64()),
        pa.field('PAC_ARPU', pa.float64()),
        pa.field('PAC_TOTAL', pa.float64()),
        pa.field('ORDER_ID', pa.string()), #
        pa.field('ORDER_DESCRIPTION', pa.string(), metadata={"req": "sensitive"}),
        pa.field('ORDER_STATUS', pa.string()),
        pa.field('ORDERTYPE', pa.string()),
        pa.field('ORDERCATEGORY', pa.string()),
        pa.field('TMNODE', pa.string(), metadata={"req": "sensitive"}),
        pa.field('ANDGROUP', pa.string()),
        pa.field('REGION', pa.string()),
        pa.field('CREATOR_GROUP', pa.string()),
        pa.field('BUILDING_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('INFRA_GROUP', pa.string()),
        pa.field('LOBS', pa.string()),
        pa.field('MIGRATION_FLAG', pa.string()),
        pa.field('STREAMYX_SUBS', pa.string(), metadata={"Detail": "Need to process proper null"}), 
        pa.field('PROJECT_NO', pa.string()),
        pa.field('PROJECT_DESCRIPTION', pa.string(), metadata={"req": "sensitive"}),
        pa.field('TAG', pa.string()),
        pa.field('NE_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('PHYSICAL_TYPE', pa.string()),
        pa.field('PHYSICAL_OUTPUT', pa.string()),
        pa.field('PLAN_S_DATE', pa.timestamp('ns')),
        pa.field('PLAN_F_DATE', pa.timestamp('ns')),
        pa.field('RFS_DATE', pa.timestamp('ns')),
        pa.field('Y1_LABOUR', pa.float64()),
        pa.field('Y1_MATERIAL', pa.float64()),
        pa.field('Y1_INCIDENTAL', pa.float64()),
        pa.field('TOTAL_Y1', pa.float64()),
        pa.field('Y2_LABOUR', pa.float64()),
        pa.field('Y2_MATERIAL', pa.float64()),
        pa.field('Y2_INCIDENTAL', pa.float64()),
        pa.field('TOTAL_Y2', pa.float64()),
        pa.field('OVERALL_COST', pa.float64()),
        pa.field('PROPERTY_TYPE', pa.string()),
        pa.field('PREMISES', pa.decimal128(38, 10)),
        pa.field('PENETRATION_FACTOR', pa.decimal128(38, 10)),
        pa.field('JUSTIFICATION', pa.string()),
        pa.field('REMARK', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
        metadata={
            "Table_Name": "daa_clarity_pmt_pac_temp_p",
            "Classification": "Confidential"
        })

    return target_schema

# not process yet
def get_target_schema_daa_clarity_pmt_po_p(column_names):
    target_schema = pa.schema([
        pa.field('POITEMCATEGORY', pa.string()),
        pa.field('PUITEMNUMBER', pa.string()),
        pa.field('POVENDORID', pa.string()),
        pa.field('POITEMNUMBER', pa.string()),
        pa.field('POQUANTITY', pa.string(), metadata={"target_schema":"float64()", "Detail":"Some value have random character. Need to clean before change schema"}),
        pa.field('POUNIT', pa.string()),
        pa.field('PUGROSSPRICE', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('CONTRACT_ITEM_NO', pa.string()),
        pa.field('PROJECTNUMBER', pa.string()),
        pa.field('PONUMBER', pa.string()),
        pa.field('POMATERIALNUMBER', pa.string()),
        pa.field('LORTRACKINGNO', pa.string()),
        pa.field('NETWORKNO', pa.string()),
        pa.field('REQUIREMENTNO', pa.string()),
        pa.field('LOR_NO', pa.string()),
        pa.field('POVENDORNAME', pa.string()),
        pa.field('POCURRENCY', pa.string()),
        pa.field('CONTRACT_NO', pa.string(), metadata={"req": "sensitive"}),
        pa.field('REGION', pa.string()),
        pa.field('DELETIONINDICATOR', pa.string()),
        pa.field('PUITEMSTATUS', pa.string()),
        pa.field('PUQUANTITY', pa.string(), metadata={"target_schema":"float64()"}),
        pa.field('PUUNIT', pa.string()),
        pa.field('PODESCRIPTION', pa.string(), metadata={"req": "sensitive"}),
        pa.field('PUNUMBER', pa.string()),
        pa.field('PONETTPRICE', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('PUDESCRIPTION', pa.string()),
        pa.field('JOB_STATUS', pa.string()),
        pa.field('NETWORKHEADER', pa.string()),
        pa.field('BATCH_DATE', pa.timestamp('ns')),
        pa.field('PODATE', pa.timestamp('ns')),
        pa.field('PODELIVERYDATE', pa.timestamp('ns')),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
        metadata={
            "Table_Name": "daa_clarity_pmt_po_p",
            "Classification": "Confidential"
        })

    return target_schema

def get_target_schema_daa_clarity_pmt_project_ar_p(column_names):
    target_schema = pa.schema([
        pa.field('CREATE_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('CREATE_DATE', pa.timestamp('ns')),
        pa.field('ORDER_ID', pa.string()),
        pa.field('ORDER_INST', pa.string()),
        pa.field('PROJECT_AR_APPROVE_DATE', pa.timestamp('ns')),
        pa.field('PROJECT_AR_INST', pa.string()),
        pa.field('PROJECT_AR_NO', pa.string()),
        pa.field('PROJECT_AR_SUBMIT_DATE', pa.timestamp('ns')),
        pa.field('PROJECT_ID', pa.string()),
        pa.field('PROJECT_INCIDENTAL_COST', pa.float64()),
        pa.field('PROJECT_INST', pa.float64()),
        pa.field('PROJECT_LABOUR_COST', pa.float64()),
        pa.field('PROJECT_MATERIAL_COST', pa.float64()),
        pa.field('PROJECT_TOTALCOST', pa.float64()),
        pa.field('REVISE_NO', pa.decimal128(38, 10), metadata={"target_schema": "uint16()"}),
        pa.field('UPDATE_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('UPDATE_DATE', pa.timestamp('ns')),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
        metadata={
            "Table_Name": "daa_clarity_pmt_project_ar_p",
            "Classification": "Confidential"
        })

    return target_schema

def get_target_schema_daa_clarity_pmt_project_temp_p(column_names):
    target_schema = pa.schema([
        pa.field('PROJECTNO', pa.string()),
        pa.field('PROJECT_DESCRIPTION', pa.string(), metadata={"req": "sensitive"}),
        pa.field('ORDERID', pa.string()),
        pa.field('PROJECTDESIGNATION', pa.string()),
        pa.field('PROJECTSTATUS', pa.string()),
        pa.field('ORDERSTATUS', pa.string()),
        pa.field('ORDERCATEGORY', pa.string()),
        pa.field('ORDERSESSION', pa.string()),
        pa.field('TMRFSI', pa.string(), metadata={"target_schema": "date32()"}),
        pa.field('CUSTOMERRFSI', pa.string(), metadata={"target_schema": "date32()"}),
        pa.field('REVISEDRFSI', pa.string(), metadata={"target_schema": "date32()"}),
        pa.field('ORDERDESCRIPTION', pa.string(), metadata={"req": "sensitive"}),
        pa.field('CUSTOMERNAME', pa.string()),
        pa.field('NOVAID', pa.string()),
        pa.field('LOCATION', pa.string(), metadata={"req": "sensitive"}),
        pa.field('REGION', pa.string()),
        pa.field('PTT', pa.string()),
        pa.field('EXCHANGE', pa.string(), metadata={"req": "sensitive"}),
        pa.field('IPNAME', pa.string(), metadata={"req": "sensitive", "PII":"Yes"}),
        pa.field('PDTNAME', pa.string(), metadata={"req": "sensitive", "PII":"Yes"}),
        pa.field('BL_STARTPROJECTCREATION', pa.string(), metadata={"target_schema": "date32()"}),
        pa.field('BL_ENDRFSICOMM', pa.string(), metadata={"target_schema": "date32()"}),
        pa.field('BL_ENDCLOSED', pa.string(), metadata={"target_schema": "date32()"}),
        pa.field('PLANNED_START_PROJECTCREATION', pa.string(), metadata={"target_schema": "date32()"}),
        pa.field('PLANNED_END_RFSICOMM', pa.string(), metadata={"target_schema": "date32()"}),
        pa.field('PLANNED_END_CLOSED', pa.string(), metadata={"target_schema": "date32()"}),
        pa.field('REQUESTDATE', pa.string(), metadata={"target_schema": "date32()"}),
        pa.field('SERVICETYPE', pa.string()),
        pa.field('SLGINFO', pa.string()),
        pa.field('INFRAREQUIRED', pa.string()),
        pa.field('INSTALLTYPE', pa.string()),
        pa.field('COMMISSIONEDDATE', pa.string(), metadata={"target_schema": "date32()"}),
        pa.field('COMMISSIONEDINFRAINFO', pa.string(), metadata={"req": "sensitive"}),
        pa.field('PROGRESS', pa.string(), metadata={"target_schema": "float64()"}),
        pa.field('CURRENTACTIVITY', pa.string()),
        pa.field('PROJECTISSUES', pa.string()),
        pa.field('PROJECTREMARKS', pa.string()),
        pa.field('MPCP', pa.timestamp('ns')),
        pa.field('LABOURCOST', pa.string(), metadata={"req": "sensitive", "target_schema": "float64()"}),
        pa.field('MATERIALCOST', pa.string(), metadata={"req": "sensitive", "target_schema": "float64()"}),
        pa.field('INCIDENTALCOST', pa.string(), metadata={"req": "sensitive", "target_schema": "float64()"}),
        pa.field('TOTALCOST', pa.string(), metadata={"req": "sensitive", "target_schema": "float64()"}),
        pa.field('PHYSICALTYPE', pa.string()),
        pa.field('PHYSICALPLANNED', pa.string()),
        pa.field('PHYSICALACTUAL', pa.string()),
        pa.field('PROJECTDURATION_DAY', pa.decimal128(38, 10)),
        pa.field('DATEADDED', pa.string(), metadata={"target_schema": "date32()"}),
        pa.field('PROJECT_CREATION_DATE', pa.string(), metadata={"target_schema": "date32()"}),
        pa.field('PROJECT_APPROVAL_DATE', pa.string(), metadata={"target_schema": "date32()"}),
        pa.field('PROJECT_AR_DATE', pa.string(), metadata={"target_schema": "date32()"}),
        pa.field('LOI_MPCP', pa.string()),
        pa.field('LOI_REQUEST_DATE', pa.string(), metadata={"target_schema": "date32()"}),
        pa.field('LOI_RECEIVED_DATE', pa.string(), metadata={"target_schema": "date32()"}),
        pa.field('JKH_SURVEY_DATE', pa.string(), metadata={"target_schema": "date32()"}),
        pa.field('PRPO_PO_DATE', pa.string(), metadata={"target_schema": "date32()"}),
        pa.field('PRPO_DELIVERY_DATE', pa.string(), metadata={"target_schema": "date32()"}),
        pa.field('PRPO_RESERVE_DATE', pa.string(), metadata={"target_schema": "date32()"}),
        pa.field('PRPO_ISSUANCE_DATE', pa.string(), metadata={"target_schema": "date32()"}),
        pa.field('HANDOVER_DATE', pa.string(), metadata={"target_schema": "date32()"}),
        pa.field('HANDOVER_SUBMITTED_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('HANDOVER_RECEIVED_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('CREATEDDATE', pa.timestamp('ns')),
        pa.field('DATE_APPROVED', pa.timestamp('ns')),
        pa.field('WAYLEAVE_REQDATE', pa.timestamp('ns')),
        pa.field('WAYLEAVE_APPDATE', pa.timestamp('ns')),
        pa.field('WAYLEAVE_DEPOSIT', pa.string()),
        pa.field('WAYLEAVE_COLLECTED_DATE', pa.timestamp('ns')),
        pa.field('WAYLEAVE_COLLECTED', pa.string()),
        pa.field('WAYLEAVE_REMARK', pa.string()),
        pa.field('PIC_NAME', pa.string(), metadata={"req": "sensitive","PII":"Yes"}),
        pa.field('LAT', pa.string(), metadata={"req": "sensitive","target_schema": "float64()"}),
        pa.field('LNG', pa.string(), metadata={"req": "sensitive","target_schema": "float64()"}),
        pa.field('DMA', pa.string()),
        pa.field('AGREEMENT_DOC', pa.string()),
        pa.field('BOUNDARY_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('FIBER_LAST_MANHOLE_JOINT_DATE', pa.string(), metadata={"target_schema": "date32()"}),
        pa.field('FIBER_TERMINATED_DATE', pa.string(), metadata={"target_schema": "date32()"}),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_clarity_pmt_project_temp_p",
        "Classification": "Confidential"
    })

    return target_schema

def get_target_schema_daa_clarity_pmt_sphere_activity_update_p(column_names):
    target_schema = pa.schema([
        pa.field('STATUS', pa.string()),
        pa.field('GEMS_ACTIVITIES_TYPE', pa.string()),
        pa.field('GEMS_UPDATE_DATE', pa.string(), metadata={"target_schema": "date32()"}),
        pa.field('EXECUTE_DATE', pa.timestamp('ns')),
        pa.field('GEMS_UPDATE_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('INST_ID', pa.decimal128(16, 0)),
        pa.field('GEMS_PROJECT_NO', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_clarity_pmt_sphere_activity_update_p",
        "Classification": "Confidential"
    })

    return target_schema

def get_target_schema_daa_clarity_pmt_waiters_nerve_p(column_names):
    target_schema = pa.schema([
        pa.field('ALT_SOLUTION', pa.string()),
        pa.field('COUNTER_REVISE', pa.decimal128(38, 10), metadata={"target_schema": "uint16()"}),
        pa.field('FDP_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('ISSUES', pa.string()),
        pa.field('JUSTIFICATION', pa.string()),
        pa.field('LIST_STATUS', pa.string()),
        pa.field('NEW_FDP_NO', pa.string(), metadata={"req": "sensitive"}),
        pa.field('NO_OF_PROPERTY', pa.string()),
        pa.field('NUMBER_OF_PREMISES', pa.decimal128(38, 10)),
        pa.field('PAC_REMARK', pa.string(), metadata={"req": "sensitive"}),
        pa.field('PENETRATION_FACTOR', pa.decimal128(38, 10), metadata={"target_schema": "uint16()"}),
        pa.field('PROJECT_ID', pa.string()), 
        pa.field('PROJECT_STATUS_WORKLIST', pa.string()),
        pa.field('REMARKS', pa.string(), metadata={"req": "sensitive"}),
        pa.field('REVISE_RFSI_DATE', pa.timestamp('ns')),
        pa.field('RFSI_DATE', pa.timestamp('ns')),
        pa.field('SPHERE_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('TROIKA_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('TYPE_OF_PROPERTY', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_clarity_pmt_waiters_nerve_p",
        "Classification": "Confidential"
    })

    return target_schema

def get_target_schema_daa_clarity_pmt_waiters_vreport_p(column_names):
    target_schema = pa.schema([
        pa.field('ADDRESS', pa.string(), metadata={"req": "sensitive"}),
        pa.field('ALT_SOLUTION', pa.string()),
        pa.field('AND_GROUP', pa.string()),
        pa.field('CHILD_ORDER_ID', pa.string()),
        pa.field('DATE_CREATED', pa.timestamp('ns')),
        pa.field('ISSUES', pa.string()),
        pa.field('LIST_STATUS', pa.string()),
        pa.field('NBA', pa.string()),
        pa.field('NEW_FDP', pa.string(), metadata={"req": "sensitive"}),
        pa.field('NEW_FDP_NO', pa.string(), metadata={"req": "sensitive"}),
        pa.field('NO', pa.float64()),
        pa.field('OLD_FDP', pa.string(), metadata={"req": "sensitive"}),
        pa.field('ORDER_ID', pa.string()),
        pa.field('PROJECT_ID', pa.string()),
        pa.field('REGION', pa.string()),
        pa.field('REMARKS', pa.string(), metadata={"req": "sensitive"}),
        pa.field('REVISED_RFS', pa.timestamp('ns')),
        pa.field('RFS_AGING', pa.decimal128(38, 10), metadata={"target_schema": "uint16()"}),
        pa.field('TM_NODE', pa.string()),
        pa.field('TM_RFS', pa.timestamp('ns')),
        pa.field('VFDP', pa.string()),
        pa.field('WAITERS_AGING', pa.float64()),
        pa.field('WAITERS_ID', pa.decimal128(16, 0)),
        pa.field('WAITER_COMPLETED_DATE', pa.timestamp('ns')),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_clarity_pmt_waiters_vreport_p",
        "Classification": "Confidential"
    })

    return target_schema

  
def get_target_schema_daa_clarity_port_hierarchy_p(column_names):
    target_schema = pa.schema([
        pa.field('PORH_PARENTID', pa.string()),
        pa.field('PORH_CHILDID', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_clarity_port_hierarchy_p",
        "Classification": "Confidential"
    })

    return target_schema

def get_target_schema_daa_clarity_port_link_ports_p(column_names):
    target_schema = pa.schema([
        pa.field('POLP_PORT_ID', pa.decimal128(16, 0)),
        pa.field('POLP_PORL_ID', pa.decimal128(16, 0)),
        pa.field('POLP_COMMONPORT', pa.string()),
        pa.field('POLP_FRAA_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_clarity_port_link_ports_p",
        "Classification": "Confidential"
    })

    return target_schema
  
def get_target_schema_daa_clarity_port_links_p(column_names):
    target_schema = pa.schema([
        pa.field('PORL_ID', pa.decimal128(16, 0)),
        pa.field('PORL_CIRT_NAME', pa.string()),
        pa.field('PORL_SEQUENCE', pa.decimal128(38, 10), metadata={"target_schema": "uint16()"}),
        pa.field('PORL_LINT_ABBREVIATION', pa.string()),
        pa.field('PORL_DETAILS', pa.string()),
        pa.field('PORL_EXTERNAL', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_clarity_port_links_p",
        "Classification": "Confidential"
    })

    return target_schema

def get_target_schema_daa_clarity_port_servicetypes_template_p(column_names):
    target_schema = pa.schema([
        pa.field('PSTT_ID', pa.decimal128(16, 0)),
        pa.field('PSTT_PORT_ID', pa.decimal128(16, 0)),
        pa.field('PSTT_SETT_ID', pa.decimal128(16, 0)),
        pa.field('PSTT_PRIORITY', pa.decimal128(38, 10), metadata={"target_schema": "uint16()"}),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_clarity_port_servicetypes_template_p",
        "Classification": "Confidential"
    })

    return target_schema
  
import pyarrow as pa

def get_target_schema_daa_clarity_ports_p(column_names):
    target_schema = pa.schema([
        pa.field('PORT_ID', pa.decimal128(16, 0)),
        pa.field('PORT_EQUP_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('PORT_NAME', pa.string()),
        pa.field('PORT_CARD_SLOT', pa.string()),
        pa.field('PORT_ALARMNAME', pa.string()),
        pa.field('PORT_CIRT_NAME', pa.string()),
        pa.field('PORT_USAGE', pa.string()),
        pa.field('PORT_PORC_ABBREVIATION', pa.string()),
        pa.field('PORT_RELATION', pa.string()),
        pa.field('PORT_LOCN_TTNAME', pa.string()),
        pa.field('PORT_STATUS', pa.string(), metadata={"req": "sensitive"}),
        pa.field('PORT_DISPLAYED', pa.string()),
        pa.field('PORT_PHYSICAL', pa.string()),
        pa.field('PORT_SPED_ABBREVIATION', pa.string()),
        pa.field('PORT_DYNAMIC', pa.string()),
        pa.field('PORT_OLD_STATUS', pa.string()),
        pa.field('PORT_PHYC_ID', pa.decimal128(16, 0)),
        pa.field('PORT_CACE_ID', pa.decimal128(16, 0)),
        pa.field('PORT_NAMEGROUPID', pa.string()),
        pa.field('PORT_NUMB_ID', pa.decimal128(16, 0)),
        pa.field('PORT_ROOT', pa.string()),
        pa.field('PORT_CREATEDBYOBJECTTYPE', pa.string()),
        pa.field('PORT_CREATEDBYOBJECTID', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_clarity_ports_p",
        "Classification": "Confidential"
    })

    return target_schema

def get_target_schema_daa_clarity_service_implementation_tasks_p(column_names):
    target_schema = pa.schema([
        pa.field('SEIT_ID', pa.decimal128(16, 0)),
        pa.field('SEIT_SERO_ID', pa.decimal128(16, 0)),
        pa.field('SEIT_SERO_REVISION', pa.decimal128(38, 10)),
        pa.field('SEIT_TIMING', pa.decimal128(38, 10)),
        pa.field('SEIT_TASKNAME', pa.string()),
        pa.field('SEIT_STAS_ABBREVIATION', pa.string()),
        pa.field('SEIT_STATUSDATE', pa.timestamp('ns')),
        pa.field('SEIT_USERNAME', pa.string()),
        pa.field('SEIT_WORG_NAME', pa.string()),
        pa.field('SEIT_ASSIGNED', pa.timestamp('ns')),
        pa.field('SEIT_IMTL_WORKFLOW_FLAG', pa.string()),
        pa.field('SEIT_IMTL_TASKTYPE', pa.string()),
        pa.field('SEIT_PROPOSED_START_DATE', pa.timestamp('ns')),
        pa.field('SEIT_PROPOSED_END_DATE', pa.timestamp('ns')),
        pa.field('SEIT_ACTUAL_START_DATE', pa.timestamp('ns')),
        pa.field('SEIT_ACTUAL_END_DATE', pa.timestamp('ns')),
        pa.field('SEIT_IMTL_WORK_NAME', pa.string()),
        pa.field('SEIT_IMTL_FUNCTION', pa.string()),
        pa.field('SEIT_WF_ITEMTYPE', pa.string()),
        pa.field('SEIT_WF_ITEMKEY', pa.string()),
        pa.field('SEIT_WF_ACTID', pa.string()),
        pa.field('SEIT_IMTL_WOPR_NAME', pa.string()),
        pa.field('SEIT_DISPLAY_ORDER', pa.decimal128(38, 10), metadata={"target_schema": "uint16()"}),
        pa.field('SEIT_ESCALATION_DATE', pa.timestamp('ns')),
        pa.field('SEIT_EMPE_ID', pa.string()),
        pa.field('SEIT_CALLEDTYPE', pa.string()),
        pa.field('SEIT_CALLEDKEY', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_clarity_service_implementation_tasks_p",
        "Classification": "Confidential"
    })

    return target_schema

def get_target_schema_daa_clarity_service_order_attributes_p(column_names):
    target_schema = pa.schema([
        pa.field('SEOA_ID', pa.decimal128(16, 0)),
        pa.field('SEOA_NAME', pa.string()),
        pa.field('SEOA_SERO_ID', pa.decimal128(16, 0)),
        pa.field('SEOA_SERO_REVISION', pa.string()),
        pa.field('SEOA_DEFAULTVALUE', pa.string(), metadata={"req": "sensitive"}),
        pa.field('SEOA_DISPLAY_ORDER', pa.decimal128(38, 10), metadata={"target_schema": "uint16()"}),
        pa.field('SEOA_PREV_VALUE', pa.string(), metadata={"req": "sensitive"}),
        pa.field('SEOA_SOFE_ID', pa.decimal128(16, 0)), 
        pa.field('SEOA_HIDDEN', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_clarity_service_order_attributes_p",
        "Classification": "Confidential"
    })

    return target_schema

def get_target_schema_daa_clarity_service_orders_p(column_names):
    target_schema = pa.schema([
        pa.field('SERO_ID', pa.string()),
        pa.field('SERO_REVISION', pa.string()),
        pa.field('SERO_CUSR_ABBREVIATION', pa.string()),
        pa.field('SERO_ACCT_NUMBER', pa.string(), metadata={"req": "sensitive"}),
        pa.field('SERO_SEOP_PRIORITY', pa.string()),
        pa.field('SERO_WORG_NAME', pa.string()),
        pa.field('SERO_LOCN_ID_AEND', pa.string()),
        pa.field('SERO_LOCN_ID_BEND', pa.string()),
        pa.field('SERO_ORDT_TYPE', pa.string()),
        pa.field('SERO_STAS_ABBREVIATION', pa.string()),
        pa.field('SERO_STATUSDATE', pa.timestamp('ns')),
        pa.field('SERO_SERT_ABBREVIATION', pa.string()),
        pa.field('SERO_SPED_ABBREVIATION', pa.string()),
        pa.field('SERO_TRAT_APPLICATION', pa.string()),
        pa.field('SERO_CONTRACTNO', pa.string()),
        pa.field('SERO_CIRT_NAME', pa.string()),
        pa.field('SERO_DATECREATED', pa.timestamp('ns')),
        pa.field('SERO_USERCREATED', pa.string()),
        pa.field('SERO_OEID', pa.string()),
        pa.field('SERO_STAS_REASON', pa.string()),
        pa.field('SERO_PROJECTID', pa.string()),
        pa.field('SERO_CREQ_CSRFNO', pa.string()),
        pa.field('SERO_CREQ_REQUESTNO', pa.string()),
        pa.field('SERO_WF_ITEMTYPE', pa.string()),
        pa.field('SERO_WF_ITEMKEY', pa.string()),
        pa.field('SERO_WF_USERKEY', pa.string()),
        pa.field('SERO_CIRT_COUNT', pa.string()),
        pa.field('SERO_ADDE_ID_BEND', pa.string()),
        pa.field('SERO_ADDE_ID_AEND', pa.string()),
        pa.field('SERO_SERV_ID', pa.string()),
        pa.field('SERO_AREA_CODE', pa.string()),
        pa.field('SERO_COMPLETION_DATE', pa.timestamp('ns')),
        pa.field('SERO_TRUG_ID', pa.decimal128(16, 0)),
        pa.field('SERO_SLAT_NAME', pa.string()),
        pa.field('SERO_ESCALATION_DATE', pa.timestamp('ns')),
        pa.field('SERO_SERO_ID', pa.string()),
        pa.field('SERO_SERV_DISPLAYNAME', pa.string()),
        pa.field('SERO_SEIT_ID', pa.decimal128(16, 0)),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_clarity_service_orders_p",
        "Classification": "Confidential"
    })

    return target_schema


def get_target_schema_daa_clarity_service_types_definition_p(column_names):
    target_schema = pa.schema([
        pa.field('SETD_ID', pa.decimal128(16, 0)),
        pa.field('SETD_SETT_ID', pa.decimal128(16, 0)),
        pa.field('SETD_SERT_ABBREVIATION', pa.string()),
        pa.field('SETD_PRIORTY', pa.decimal128(38, 10), metadata={"target_schema": "uint16()"}),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_clarity_service_types_definition_p",
        "Classification": "Confidential"
    })

    return target_schema

def get_target_schema_daa_clarity_service_types_template_p(column_names):
    target_schema = pa.schema([
        pa.field('SETT_ID', pa.decimal128(16, 0)),
        pa.field('SETT_NAME', pa.string()),
        pa.field('SETT_DESCRIPTION', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_clarity_service_types_template_p",
        "Classification": "Confidential"
    })

    return target_schema


def get_target_schema_daa_clarity_services_address_p(column_names):
    target_schema = pa.schema([
        pa.field('SADD_SERV_ID', pa.string()),
        pa.field('SADD_ADDE_ID', pa.decimal128(16, 0)),
        pa.field('SADD_TYPE', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_clarity_services_address_p",
        "Classification": "Confidential"
    })

    return target_schema

def get_target_schema_daa_clarity_services_attributes_p(column_names):
    target_schema = pa.schema([
        pa.field('SATT_ID', pa.decimal128(24, 0)),
        pa.field('SATT_SERV_ID', pa.string()),
        pa.field('SATT_ATTRIBUTE_NAME', pa.string()),
        pa.field('SATT_DEFAULTVALUE', pa.string()),
        pa.field('SATT_SFEA_ID', pa.decimal128(24, 0)),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_clarity_services_attributes_p",
        "Classification": "Confidential"
    })

    return target_schema

def get_target_schema_daa_clarity_states_p(column_names):
    target_schema = pa.schema([
        pa.field('STAT_ABBREVIATION', pa.string()),
        pa.field('STAT_DESCRIPTION', pa.string()),
        pa.field('STAT_CODE', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_clarity_states_p",
        "Classification": "Confidential"
    })

    return target_schema


def get_target_schema_daa_clarity_texis_exch_range_p(column_names):
    target_schema = pa.schema([
        pa.field('ALLOW_INCOMING', pa.string()),
        pa.field('CHARGE_AREA', pa.string()),
        pa.field('CHARGE_DATA', pa.string()),
        pa.field('CHARGE_DISTRICT', pa.string()),
        pa.field('CHARGE_LOCATION', pa.string()),
        pa.field('D_L', pa.decimal128(38, 10), metadata={"target_schema": "uint16()"}),
        pa.field('D_L_N', pa.decimal128(38, 10), metadata={"target_schema": "uint16()"}),
        pa.field('D_L_X', pa.decimal128(38, 10), metadata={"target_schema": "uint16()"}),
        pa.field('EXCH_ABBR', pa.string(), metadata={"req": "sensitive"}),
        pa.field('EXCH_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('EXCH_RANGE_ID', pa.decimal128(16, 0)),
        pa.field('HOST_EXCHANGE', pa.string(), metadata={"req": "sensitive"}),
        pa.field('INSERT_DATE', pa.timestamp('ns')),
        pa.field('IS_DEL', pa.decimal128(38, 10), metadata={"target_schema": "uint16()"}),
        pa.field('KEMUDAHAN_LAMA', pa.string(), metadata={"req": "sensitive"}),
        pa.field('KODA_CATEGORY', pa.string()),
        pa.field('MOS_CODE', pa.string()),
        pa.field('OLD_NO_SIRI', pa.string()),
        pa.field('PREFIX', pa.string()),
        pa.field('PREFIX_OLNO', pa.string()),
        pa.field('PREFIX_SPECIAL_CODE', pa.string()),
        pa.field('PUSAT_CAMA', pa.string(), metadata={"req": "sensitive"}),
        pa.field('P_EXCH_RANGE_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('RANGE', pa.string()),
        pa.field('RANGE_ABBR', pa.string()),
        pa.field('RANGE_DESCR', pa.string()),
        pa.field('RANGE_END', pa.decimal128(38, 10)),
        pa.field('RANGE_START', pa.decimal128(38, 10)),
        pa.field('ROUTING', pa.string(), metadata={"req": "sensitive"}),
        pa.field('SEQ_PREV', pa.decimal128(38, 10)),
        pa.field('SERVICE', pa.string()),
        pa.field('SERVICE_ID', pa.decimal128(16, 0)),
        pa.field('SERVICE_NAME', pa.string()),
        pa.field('STATUS', pa.string()),
        pa.field('TS_CLOSE', pa.timestamp('ns')),
        pa.field('TS_LAUNCH', pa.timestamp('ns')),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_clarity_texis_exch_range_p",
        "Classification": "Confidential"
    })

    return target_schema


def get_target_schema_daa_clarity_texis_medicon_p(column_names):
    target_schema = pa.schema([
        pa.field('EXCH_RANGE_ID', pa.decimal128(16, 0)),
        pa.field('CA_CODE', pa.string(), metadata={"req": "sensitive"}),
        pa.field('NXX_TYPE', pa.string()), 
        pa.field('PLACE_NAME', pa.string()),
        pa.field('PROCESS_CTR', pa.string()), 
        pa.field('MTX_AREA', pa.string()),
        pa.field('MOB_CALL_SIGN', pa.string()),
        pa.field('NOP_ID', pa.string()), 
        pa.field('CD_CODE', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_clarity_texis_medicon_p",
        "Classification": "Confidential"
    })

    return target_schema

def get_target_schema_daa_clarity_texis_medicon_request_p(column_names):
    target_schema = pa.schema([
        pa.field('EXCH_RANGE_ID', pa.decimal128(16, 0)),
        pa.field('CA_CODE', pa.string(), metadata={"req": "sensitive"}),
        pa.field('NXX_TYPE', pa.string()), 
        pa.field('PLACE_NAME', pa.string()),
        pa.field('PROCESS_CTR', pa.string()),
        pa.field('MTX_AREA', pa.string()), 
        pa.field('MOB_CALL_SIGN', pa.string()),
        pa.field('NOP_ID', pa.string()),
        pa.field('CD_CODE', pa.string()),
        pa.field('SERV_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_clarity_texis_medicon_request_p",
        "Classification": "Confidential"
    })

    return target_schema


def get_target_schema_daa_clarity_texis_request_p(column_names):
    target_schema = pa.schema([
        pa.field('T_SERV_ID', pa.string()),
        pa.field('T_SERO_ID', pa.string()),
        pa.field('T_SERO_DATECREATED', pa.timestamp('ns')),
        pa.field('INSTRUCTION_TYPE', pa.string()),
        pa.field('INSTRUCTION_TITLE', pa.string()),
        pa.field('INTENDED_TO', pa.string(), metadata={"req": "sensitive"}),
        pa.field('OPERATOR_NAME', pa.string()),
        pa.field('SERVICE', pa.string()),
        pa.field('SERVICE_NAME', pa.string()),
        pa.field('WSID', pa.string()),
        pa.field('ABBR', pa.string(), metadata={"req": "sensitive"}),
        pa.field('ABBR_DESC', pa.string()),
        pa.field('LAUNCHING_DATE', pa.timestamp('ns')),
        pa.field('CLOSING_DATE', pa.timestamp('ns')),
        pa.field('REMARKS', pa.string(), metadata={"req": "sensitive"}),
        pa.field('INSERT_DATE', pa.timestamp('ns')),
        pa.field('OPERATION_TYPE', pa.string()),
        pa.field('EMPE_USERID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('RETURN_REMARK', pa.string(), metadata={"req": "sensitive"}),
        pa.field('EXCH_INVOLVED', pa.string(), metadata={"req": "sensitive"}),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_clarity_texis_request_p",
        "Classification": "Confidential"
    })

    return target_schema


def get_target_schema_daa_clarity_tm_attain_speed_rate_backup2_p(column_names):
    target_schema = pa.schema([
        pa.field('SERVNUMBER', pa.string()),
        pa.field('VPORTMO', pa.string(), metadata={"req": "sensitive"}),
        pa.field('MIN_ATTAINABLE_RATE', pa.decimal128(38, 10), metadata={"target_schema": "float64()"}),
        pa.field('INSERT_DATE', pa.timestamp('ns')),
        pa.field('DP_FRAC_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('BUILDING_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('NIS_BUILDING_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('NIS_DSLAM_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('SNR_DL', pa.decimal128(38, 10), metadata={"target_schema": "float64()"}),
        pa.field('SNR_UL', pa.decimal128(38, 10), metadata={"target_schema": "float64()"}),
        pa.field('ATTENUATION_DL', pa.decimal128(38, 10), metadata={"target_schema": "float64()"}),
        pa.field('ATTENUATION_UL', pa.decimal128(38, 10), metadata={"target_schema": "float64()"}),
        pa.field('DSLAM_EQUP_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('DSLAM_TYPE', pa.string()),
        pa.field('DIST_OK', pa.string()),
        pa.field('DSLAMDISTANCE', pa.decimal128(38, 10), metadata={"target_schema": "float64()"}),
        pa.field('JOHNSPEED', pa.decimal128(38, 10), metadata={"target_schema": "float64()"}),
        pa.field('TOFOLLOWJOHN', pa.string()),
        pa.field('SYNC_MODE', pa.string()),
        pa.field('TRANS_MODE', pa.string()),
        pa.field('UPLOAD_RATE', pa.decimal128(38, 10), metadata={"target_schema": "float64()"}),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_clarity_tm_attain_speed_rate_backup2_p",
        "Classification": "Confidential"
    })

    return target_schema


def get_target_schema_daa_clarity_tm_attain_speed_rate_backup_p(column_names):
    target_schema = pa.schema([
        pa.field('SERVNUMBER', pa.string()),
        pa.field('VPORTMO', pa.string(), metadata={"req": "sensitive"}),
        pa.field('MIN_ATTAINABLE_RATE', pa.decimal128(38, 10), metadata={"target_schema": "float64()"}),
        pa.field('INSERT_DATE', pa.timestamp('ns')),
        pa.field('DP_FRAC_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('BUILDING_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('NIS_BUILDING_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('NIS_DSLAM_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('SNR_DL', pa.decimal128(38, 10), metadata={"target_schema": "float64()"}),
        pa.field('SNR_UL', pa.decimal128(38, 10), metadata={"target_schema": "float64()"}),
        pa.field('ATTENUATION_DL', pa.decimal128(38, 10), metadata={"target_schema": "float64()"}),
        pa.field('ATTENUATION_UL', pa.decimal128(38, 10), metadata={"target_schema": "float64()"}),
        pa.field('DSLAM_EQUP_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('DSLAM_TYPE', pa.string()),
        pa.field('DIST_OK', pa.string()),
        pa.field('DSLAMDISTANCE', pa.decimal128(38, 10), metadata={"target_schema": "float64()"}),
        pa.field('JOHNSPEED', pa.decimal128(38, 10), metadata={"target_schema": "float64()"}),
        pa.field('TOFOLLOWJOHN', pa.string()),
        pa.field('SYNC_MODE', pa.string()),
        pa.field('TRANS_MODE', pa.string()),
        pa.field('UPLOAD_RATE', pa.decimal128(38, 10), metadata={"target_schema": "float64()"}),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_clarity_tm_attain_speed_rate_backup_p",
        "Classification": "Confidential"
    })

    return target_schema

def get_target_schema_daa_clarity_tm_attain_speed_rate_jn_p(column_names):
    target_schema = pa.schema([
        pa.field('SERVNUMBER', pa.string()),
        pa.field('VPORTMO', pa.string(), metadata={"req": "sensitive"}),
        pa.field('MIN_ATTAINABLE_RATE', pa.decimal128(38, 10), metadata={"target_schema": "float64()"}),
        pa.field('INSERT_DATE', pa.timestamp('ns')),
        pa.field('DP_FRAC_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('BUILDING_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('NIS_BUILDING_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('SNR_DL', pa.decimal128(38, 10), metadata={"target_schema": "float64()"}),
        pa.field('SNR_UL', pa.decimal128(38, 10), metadata={"target_schema": "float64()"}),
        pa.field('ATTENUATION_DL', pa.decimal128(38, 10), metadata={"target_schema": "float64()"}),
        pa.field('ATTENUATION_UL', pa.decimal128(38, 10), metadata={"target_schema": "float64()"}),
        pa.field('DSLAM_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('DSLAM_TYPE', pa.string()),
        pa.field('DSLAM_DIST_OK', pa.string()),
        pa.field('DSLAMDISTANCE', pa.decimal128(38, 10), metadata={"target_schema": "float64()"}),
        pa.field('JOHNSPEED', pa.decimal128(38, 10), metadata={"target_schema": "float64()"}),
        pa.field('TOFOLLOWJOHN', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_clarity_tm_attain_speed_rate_jn_p",
        "Classification": "Confidential"
    })

    return target_schema


def get_target_schema_daa_clarity_tm_dslam_search2_p(column_names):
    target_schema = pa.schema([
        pa.field('ATM_PORT', pa.string()),
        pa.field('EXCHANGE_NAME', pa.string()),
        pa.field('EXCHANGE_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('PTT', pa.string()),
        pa.field('COT_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('COT_IP', pa.string(), metadata={"req": "sensitive"}),
        pa.field('COT_EMS_IP', pa.string(), metadata={"req": "sensitive"}),
        pa.field('COT_EMS_VP_VC', pa.string()),
        pa.field('COT_ROUTER_VP_VC', pa.string()),
        pa.field('RT_LOCATION', pa.string(), metadata={"req": "sensitive"}),
        pa.field('RT_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('ADSL_CASS_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('RT_IP', pa.string(), metadata={"req": "sensitive"}),
        pa.field('RT_EMS_IP', pa.string(), metadata={"req": "sensitive"}),
        pa.field('RT_EMS_VP_VC', pa.string()),
        pa.field('RT_ROUTER_VP_VC', pa.string()),
        pa.field('ADSL_VP_VLAN', pa.string()),
        pa.field('MSAN_TYPE', pa.string()),
        pa.field('SUBTENDING_FROM', pa.string(), metadata={"req": "sensitive"}),
        pa.field('HAVE_CONTRACT', pa.string()),
        pa.field('DSLAM_COMM', pa.timestamp('ns')),
        pa.field('ATM_NODE', pa.string(), metadata={"req": "sensitive"}),
        pa.field('LOCATION', pa.string(), metadata={"req": "sensitive"}),
        pa.field('DSLAM_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('DSLAM_IP', pa.string(), metadata={"req": "sensitive"}),
        pa.field('NMS_IP', pa.string(), metadata={"req": "sensitive"}),
        pa.field('VP_DSLAM', pa.string()),
        pa.field('VP_ROUTER', pa.string()),
        pa.field('SUBNET_MASK', pa.string(), metadata={"req": "sensitive"}),
        pa.field('EQUP_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('EPE', pa.string(), metadata={"req": "sensitive"}),
        pa.field('HSI_VLAN', pa.string()),
        pa.field('EMS_VLAN', pa.string()),
        pa.field('EMS_GATEWAY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('EMS_SERVER', pa.string(), metadata={"req": "sensitive"}),
        pa.field('DSLAM_TYPE', pa.string()),
        pa.field('DSLAM_STATUS', pa.string()),
        pa.field('COT_GATEWAY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('COT_EMS_VLAN', pa.string()),
        pa.field('METROE_PORT', pa.string()),
        pa.field('NPE', pa.string(), metadata={"req": "sensitive"}),
        pa.field('RT_EQUP_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('IP_PVMX', pa.string(), metadata={"req": "sensitive"}),
        pa.field('SUPPLIER', pa.string()),
        pa.field('SITE_NAME', pa.string(), metadata={"req": "sensitive"}),
        pa.field('DESCRIPTION', pa.string()),
        pa.field('PORTNAME_VLAN', pa.string()),
        pa.field('PORTNAME', pa.string()),
        pa.field('VLAN', pa.string()),
        pa.field('NE_ID', pa.decimal128(16, 0)),
        pa.field('ME_BRAND', pa.string()),
        pa.field('PRIMARY', pa.string()),
        pa.field('SITE_NAME2', pa.string(), metadata={"req": "sensitive"}),
        pa.field('PORTNAME2', pa.string()),
        pa.field('EQPT_GROUP', pa.string()),
        pa.field('SOURCE', pa.string()),
        pa.field('GRANITE_ID', pa.decimal128(16, 0)),
        pa.field('PING_TEST', pa.string()),
        pa.field('LAST_SESSION', pa.timestamp('ns')),
        pa.field('NTT_2020', pa.decimal128(38, 10), metadata={"target_schema": "uint16()"}),
        pa.field('NTT_2019', pa.decimal128(38, 10), metadata={"target_schema": "uint16()"}),
        pa.field('SUB_COUNT', pa.decimal128(38, 10), metadata={"target_schema": "uint16()"}),
        pa.field('NTT_TOTAL', pa.decimal128(38, 10), metadata={"target_schema": "uint16()"}),
        pa.field('NTT_POWER1', pa.decimal128(38, 10), metadata={"target_schema": "uint16()"}),
        pa.field('NTT_POWER2', pa.decimal128(38, 10), metadata={"target_schema": "uint16()"}),
        pa.field('NTT_EQPT', pa.decimal128(38, 10), metadata={"target_schema": "uint16()"}),
        pa.field('NTT_FIBER', pa.decimal128(38, 10), metadata={"target_schema": "uint16()"}),
        pa.field('NTT_OTHERS', pa.decimal128(38, 10), metadata={"target_schema": "uint16()"}),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_clarity_tm_dslam_search2_p",
        "Classification": "Confidential"
    })

    return target_schema

def get_target_schema_daa_clarity_tmkoh_dslam_bras_report_p(column_names):
    target_schema = pa.schema([
        pa.field('BAS', pa.string(), metadata={"req": "sensitive"}),
        pa.field('IP', pa.string(), metadata={"req": "sensitive"}),
        pa.field('REG', pa.string()),
        pa.field('DSLAM', pa.string(), metadata={"req": "sensitive"}),
        pa.field('DSLAM_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('ATM', pa.string(), metadata={"req": "sensitive"}),
        pa.field('ATM_PO', pa.string()),
        pa.field('D_CAP', pa.string(), metadata={"target_schema": "uint16()"}),
        pa.field('B_CFG', pa.string(), metadata={"target_schema": "uint16()"}),
        pa.field('CFG_B', pa.string(), metadata={"target_schema": "uint16()"}),
        pa.field('CFG_H', pa.string(), metadata={"target_schema": "uint16()"}),
        pa.field('B_VR', pa.string(), metadata={"req": "sensitive"}),
        pa.field('B_BAS', pa.string()),
        pa.field('B_NODE', pa.string(), metadata={"req": "sensitive"}),
        pa.field('B_VP0', pa.string(), metadata={"target_schema": "uint16()"}),
        pa.field('H_VR', pa.string(), metadata={"req": "sensitive"}),
        pa.field('H_BAS', pa.string()),
        pa.field('H_NODE', pa.string(), metadata={"req": "sensitive"}),
        pa.field('H_VP0', pa.string(), metadata={"target_schema": "uint16()"}),
        pa.field('B_BAS_NODE', pa.string(), metadata={"req": "sensitive"}),
        pa.field('H_BAS_NODE', pa.string(), metadata={"req": "sensitive"}),
        pa.field('MIGRATED_FLAG', pa.string()),
        pa.field('DSLAM_TYPE', pa.string()),
        pa.field('DSLAM_MANUFACTURER', pa.string()),
        pa.field('DSLAM_EQUP_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('ACESS_HSI_VLAN', pa.string()),
        pa.field('DSLAM_HOST', pa.string()),
        pa.field('EQUP_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('EQUP_ID_HOST', pa.string(), metadata={"req": "sensitive"}),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_clarity_tmkoh_dslam_bras_report_p",
        "Classification": "Confidential"
    })

    return target_schema


def get_target_schema_daa_clarity_tmkoh_dslam_sub_install_p(column_names):
    target_schema = pa.schema([
        pa.field('BRAS', pa.string(), metadata={"req": "sensitive"}),
        pa.field('BRAS_PORT', pa.string()),
        pa.field('B_BAS_NODE', pa.string(), metadata={"req": "sensitive"}),
        pa.field('WORKING_SUB', pa.uint16()),
        pa.field('INSTALLED_PORTS', pa.uint16()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_clarity_tmkoh_dslam_sub_install_p",
        "Classification": "Confidential"
    })

    return target_schema

def get_target_schema_daa_clarity_tmkoh_dslam_work_sub_p(column_names):
    target_schema = pa.schema([
        pa.field('EQUP_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('EQUP_EQUT_ABBREVIATION', pa.string()),
        pa.field('EQUP_INDEX', pa.string()),
        pa.field('EQUP_LOCN_TTNAME', pa.string(), metadata={"req": "sensitive"}),
        pa.field('WORKING_SUB', pa.uint16()),
        pa.field('INSTALLED_PORTS', pa.uint16()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_clarity_tmkoh_dslam_work_sub_p",
        "Classification": "Confidential"
    })

    return target_schema


def get_target_schema_daa_clarity_tmkoh_ref_dslam_max_cap_p(column_names):
    target_schema = pa.schema([
        pa.field('TYPE', pa.string()),
        pa.field('BRAND', pa.string()),
        pa.field('MODEL', pa.string()),
        pa.field('MAXIMUM_CAPACITY', pa.string()),
        pa.field('X65', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_clarity_tmkoh_ref_dslam_max_cap_p",
        "Classification": "Public"
    })

    return target_schema

import pyarrow as pa

def get_target_schema_daa_clarity_ttn_contractmaster_p(column_names):
    target_schema = pa.schema([
        pa.field('ITEM_NO', pa.string()),
        pa.field('ITEM_VALUE', pa.string()),
        pa.field('MATERIALNO_SERVICENO', pa.string()),
        pa.field('CTM_INST', pa.string()),
        pa.field('TARGET_VALUE', pa.string()),
        pa.field('VENDOR_NO', pa.string()),
        pa.field('VALIDITY_END', pa.timestamp('ns')),
        pa.field('TTN_ACTION', pa.string()),
        pa.field('CONTRACT_NO', pa.string()),
        pa.field('PURCHASING_GROUP', pa.string()),
        pa.field('MATERIAL_DESCRIPTION', pa.string()),
        pa.field('RUN_DATE', pa.timestamp('ns')),
        pa.field('DELETION_INDICATOR', pa.string()),
        pa.field('VALIDITY_START', pa.timestamp('ns')),
        pa.field('CONTRACT_BALANCE', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_clarity_ttn_contractmaster_p",
        "Classification": "Public"
    })

    return target_schema


def get_target_schema_daa_clarity_ttn_daily_progress_p(column_names):
    target_schema = pa.schema([
        pa.field('PLATFORM', pa.string()),
        pa.field('TEAM_NAME', pa.string()),
        pa.field('LOR_INST', pa.string()),
        pa.field('DAILY_PROGRESS_INST', pa.string()),
        pa.field('WORK_STATUS', pa.string()),
        pa.field('DAILY_ACTIVITY_CATEGORY', pa.string()),
        pa.field('DAILY_ACTIVITY_REMARK', pa.string()),
        pa.field('CLAIM_STATUS', pa.string()),
        pa.field('ACTUAL_COMPLETION_DATE', pa.timestamp('ns')),
        pa.field('PO_NUMBER', pa.string()),
        pa.field('DAILY_CURRENT_ISSUE', pa.string()),
        pa.field('DAILY_PROGRESS_PERCENTAGE', pa.float64()),
        pa.field('DAILY_ACTIVITY_DATE', pa.timestamp('ns')),
        pa.field('POSITIONS', pa.string()),
        pa.field('DAILY_UPDATE_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_clarity_ttn_daily_progress_p",
        "Classification": "Public"
    })

    return target_schema

def get_target_schema_daa_clarity_ttn_eot_p(column_names):
    target_schema = pa.schema([
        pa.field('EOT_REQUEST_DATE', pa.timestamp('ns')),
        pa.field('EOT_REMARK', pa.string()),
        pa.field('LOR_INST', pa.string()),
        pa.field('EOT_STATUS', pa.string()),
        pa.field('EOT_REQUEST_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('EOT_APPROVE_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('EOT_APPROVE_DATE', pa.timestamp('ns')),
        pa.field('EOT_INST', pa.string()),
        pa.field('EOT_RFS_DATE', pa.timestamp('ns')),
        pa.field('EOT_REASON', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_clarity_ttn_eot_p",
        "Classification": "Public"
    })

    return target_schema


def get_target_schema_daa_clarity_ttn_location_p(column_names):
    target_schema = pa.schema([
        pa.field('LOR_INST', pa.string()),
        pa.field('LNG_OUT', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('LAT', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('TEAM_NAME', pa.string()),
        pa.field('TYPE', pa.string()),
        pa.field('LOC_INST', pa.string()),
        pa.field('CHECK_DATE', pa.timestamp('ns')),
        pa.field('PLANTUNIT', pa.string()),
        pa.field('CHECKOUT_DATE', pa.timestamp('ns')),
        pa.field('CHECK_OUT_REASON', pa.string()),
        pa.field('MATERIAL', pa.string()),
        pa.field('LAT_OUT', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('LNG', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('CHECKOUT_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('CHECK_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_clarity_ttn_location_p",
        "Classification": "Public"
    })

    return target_schema

def get_target_schema_daa_clarity_ttn_lor_request_p(column_names):
    target_schema = pa.schema([
        pa.field('TURNKEY', pa.string()),
        pa.field('PROJECT_NO', pa.string()),
        pa.field('LOR_AMOUNT', pa.decimal128(38, 10), metadata={"target_schema":"float64()"}),
        pa.field('TOTAL_PORTS', pa.decimal128(38, 10), metadata={"target_schema":"uint16()"}),
        pa.field('SCOPE_OF_WORK', pa.string()),
        pa.field('CANCEL_VERIFY_DATE', pa.timestamp('ns')),
        pa.field('CANCEL_APPROVE_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('CANCEL_REMARK', pa.string()),
        pa.field('PO', pa.string()),
        pa.field('TP_VERIFY_DATE', pa.timestamp('ns')),
        pa.field('PROPOSED_RFS', pa.timestamp('ns')),
        pa.field('LOR_INST', pa.string(), metadata={"req": "sensitive"}),
        pa.field('STATE', pa.string()),
        pa.field('RFS_DATE', pa.timestamp('ns')),
        pa.field('TYPE_OF_WORK', pa.string()),
        pa.field('REQUEST_DATE', pa.timestamp('ns')),
        pa.field('BASKET', pa.string()),
        pa.field('ACCEPT_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('MGR', pa.string(), metadata={"req": "sensitive"}),
        pa.field('PROJECT_DESCRIPTION', pa.string()),
        pa.field('QC_VERIFY_DATE', pa.timestamp('ns')),
        pa.field('CANCEL_REQUEST_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('PO_PROGRESS', pa.decimal128(38, 10), metadata={"target_schema":"float64()"}),
        pa.field('UPDATE_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('TOTAL_DP', pa.decimal128(38, 10), metadata={"target_schema":"uint16()"}),
        pa.field('REQUEST_BY', pa.string()),
        pa.field('VERIFY_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('APPROVE_DATE', pa.timestamp('ns')),
        pa.field('VENDOR_NO', pa.string()),
        pa.field('CANCEL_VERIFY_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('REGION', pa.string()),
        pa.field('AM', pa.string(), metadata={"req": "sensitive"}),
        pa.field('PDT', pa.string(), metadata={"req": "sensitive"}),
        pa.field('SPHERE_NO', pa.string(), metadata={"req": "sensitive"}),
        pa.field('PROGRAM', pa.string()),
        pa.field('CONTRACT_NO', pa.string()),
        pa.field('MATERIAL', pa.string()),
        pa.field('ATP_SUBMISSION_DATE', pa.timestamp('ns')),
        pa.field('TP_VERIFY_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('PTT', pa.string(), metadata={"req": "sensitive"}),
        pa.field('EXCH', pa.string(), metadata={"req": "sensitive"}),
        pa.field('ACCEPT_DATE', pa.timestamp('ns')),
        pa.field('LOR_REMARK', pa.string()),
        pa.field('CANCEL_APPROVE_DATE', pa.timestamp('ns')),
        pa.field('ACT_COM_DATE', pa.timestamp('ns')),
        pa.field('TITAN', pa.string(), metadata={"req": "sensitive"}),
        pa.field('LOR_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('QC_STATUS', pa.string()),
        pa.field('QC_APPROVE_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('CANCEL_REQUEST_DATE', pa.timestamp('ns')),
        pa.field('MIGRATE_FLAG', pa.string()),
        pa.field('UPDATE_DATE', pa.timestamp('ns')),
        pa.field('NEWLORVALUE', pa.decimal128(38, 10), metadata={"target_schema":"float64()"}),
        pa.field('TMSO', pa.string()),
        pa.field('S_DATE', pa.timestamp('ns')),
        pa.field('F_DATE', pa.timestamp('ns')),
        pa.field('CATEGORY_OF_WORK', pa.string()),
        pa.field('VERIFY_DATE', pa.timestamp('ns')),
        pa.field('APPROVE_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('ACCEPT_STATUS', pa.string()),
        pa.field('LOR_STATUS', pa.string()),
        pa.field('QC_VERIFY_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('QC_APPROVE_DATE', pa.timestamp('ns')),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_clarity_ttn_lor_request",
        "Classification": "Confidential"
    })

    return target_schema


def get_target_schema_daa_clarity_ttn_lor_team_p(column_names):
    target_schema = pa.schema([
        pa.field('DATE_FINISH', pa.timestamp('ns')),
        pa.field('ACCEPT_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('LOR_INST', pa.string()),
        pa.field('TEAM_NAME', pa.string()),
        pa.field('TEAM_LEADER', pa.string(), metadata={"req": "sensitive", "PII":"Yes"}),
        pa.field('TEAM_MEMBER5', pa.string(), metadata={"req": "sensitive", "PII":"Yes"}),
        pa.field('ACCEPT_DATE', pa.timestamp('ns')),
        pa.field('TEAM_MEMBER1', pa.string(), metadata={"req": "sensitive", "PII":"Yes"}),
        pa.field('TEAM_MEMBER2', pa.string(), metadata={"req": "sensitive", "PII":"Yes"}),
        pa.field('TEAM_MEMBER3', pa.string(), metadata={"req": "sensitive", "PII":"Yes"}),
        pa.field('TEAM_INST', pa.string()),
        pa.field('TEAM_MEMBER4', pa.string(), metadata={"req": "sensitive", "PII":"Yes"}),
        pa.field('TEAM_MEMBER6', pa.string(), metadata={"req": "sensitive", "PII":"Yes"}),
        pa.field('DATE_START', pa.timestamp('ns')),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_clarity_ttn_lor_team_p",
        "Classification": "Public"
    })

    return target_schema


def get_target_schema_daa_clarity_ttn_pu_material_p(column_names):
    target_schema = pa.schema([
        pa.field('PLATFORM', pa.string()),
        pa.field('MATERIAL_QUANTITY', pa.string(), metadata={"target_schema": "uint16()"}),
        pa.field('MATERIAL_UPDATE_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('UNIT_OF_MEASURE', pa.string()),
        pa.field('PU_MAT_INST', pa.string()),
        pa.field('BATCH', pa.string()),
        pa.field('VALUATION_TYPE', pa.string()),
        pa.field('MOVING_AVERAGE_PLANT', pa.string(), metadata={"target_schema": "float64()"}),
        pa.field('MATERIAL_NUMBER', pa.string()),
        pa.field('MATERIAL_USED', pa.decimal128(38, 10), metadata={"target_schema": "uint64()"}),
        pa.field('PLANT', pa.string()),
        pa.field('SEND_GI', pa.decimal128(38, 10), metadata={"target_schema": "float64()"}),
        pa.field('VENDOR_NO', pa.string()),
        pa.field('UNRESTRICTED_STOCK', pa.decimal128(38, 10), metadata={"target_schema": "uint64()"}),
        pa.field('LOR_NO', pa.string()),
        pa.field('MATERIAL_DESCRIPTION', pa.string()),
        pa.field('RUN_DATE', pa.timestamp('ns')),
        pa.field('FLAG', pa.string()),
        pa.field('MATERIAL_UPDATE_DATE', pa.timestamp('ns')),
        pa.field('SITE_ID_PROJECT_DEF', pa.string()),
        pa.field('STORAGE_LOCATION', pa.string()),
        pa.field('REGION_CODE', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_clarity_ttn_pu_material_p",
        "Classification": "Public"
    })

    return target_schema


def get_target_schema_daa_clarity_ttn_pu_p(column_names):
    target_schema = pa.schema([
        pa.field('PUITEMNUMBER', pa.string()),
        pa.field('PU_UPDATE_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('PU_QUANTITY', pa.decimal128(8, 3), metadata={"target_schema": "uint64()"}),
        pa.field('PLATFORM', pa.string()),
        pa.field('POITEMNUMBER', pa.string()),
        pa.field('PU_INST', pa.string()),
        pa.field('PU_REMARK', pa.string()),
        pa.field('LOR_INST', pa.string()),
        pa.field('PU_NUMBER', pa.string()),
        pa.field('PU_DESCRIPTION', pa.string()),
        pa.field('PU_UPDATE_DATE', pa.timestamp('ns')),
        pa.field('SEND_GR', pa.decimal128(38, 10), metadata={"target_schema": "float64()"}),
        pa.field('PU_ACTUAL', pa.decimal128(8, 3), metadata={"target_schema": "float64()"}),
        pa.field('GEMSPUQTY', pa.decimal128(8, 3), metadata={"target_schema": "float64()"}),
        pa.field('PUUNIT', pa.string()),
        pa.field('PO_NUMBER', pa.string()),
        pa.field('PU_ITEMNUMBER', pa.decimal128(38, 10), metadata={"target_schema": "uint64()"}),
        pa.field('PUGROSSPRICE', pa.decimal128(38, 10), metadata={"target_schema": "float64()"}),
        pa.field('PU_PROGRESSPERCENTAGE', pa.decimal128(38, 10), metadata={"target_schema": "float64()"}),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_clarity_ttn_pu_p",
        "Classification": "Public"
    })

    return target_schema


def get_target_schema_daa_clarity_ttn_remark_p(column_names):
    target_schema = pa.schema([
        pa.field('LOR_INST', pa.string()),
        pa.field('REMARK_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('VENDOR_NO', pa.string()),
        pa.field('UPDATE_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('REJECT_CATEGORY', pa.string()),
        pa.field('REMARK_VALUE', pa.string()),
        pa.field('REMARK_DATE', pa.timestamp('ns')),
        pa.field('UPDATE_DATE', pa.timestamp('ns')),
        pa.field('RMK_INST', pa.string()),
        pa.field('REMARK_TYPE', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_clarity_ttn_remark_p",
        "Classification": "Public"
    })

    return target_schema


def get_target_schema_daa_clarity_ttn_slims_header_p(column_names):
    target_schema = pa.schema([
        pa.field('SAP_DOC_NO', pa.string()),
        pa.field('SAP_ERROR_MESSAGE', pa.string()),
        pa.field('REG_CODE', pa.string()),
        pa.field('PONUMBER', pa.string()),
        pa.field('TRANS_DATE_TIME', pa.timestamp('ns')),
        pa.field('TMSOA_ERROR_MESSAGE', pa.string()),
        pa.field('LOR_INST', pa.string()),
        pa.field('SAP_DOC_DATE', pa.string(), metadata={"target_schema": "date32()"}),
        pa.field('TMSOA_ERROR_CODE', pa.string()),
        pa.field('INDICATOR', pa.string()),
        pa.field('LOR_NO', pa.string()),
        pa.field('PERCENTAGE', pa.float64()),
        pa.field('TRANS_NO', pa.string()),
        pa.field('RESUBMIT_DATE', pa.timestamp('ns')),
        pa.field('SAP_TRANS_DATE', pa.timestamp('ns')),
        pa.field('PARTIAL_GI_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('TEAM_ID', pa.decimal128(16, 0)),
        pa.field('WO_TYPE', pa.string()),
        pa.field('PROJ_NO', pa.string()),
        pa.field('INDICATORDATE', pa.timestamp('ns')),
        pa.field('PARTIAL_GI_DATE', pa.timestamp('ns')),
        pa.field('VENDOR_ID', pa.decimal128(16, 0)),
        pa.field('TRANS_DATE', pa.string(), metadata={"target_schema": "date32()"}),
        pa.field('TMSOA_STATUS', pa.string()),
        pa.field('RESUBMIT_BY', pa.string()),
        pa.field('TRANS_NO_INST', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_clarity_ttn_slims_header_p",
        "Classification": "Public"
    })

    return target_schema


def get_target_schema_daa_clarity_ttn_slims_item_p(column_names):
    target_schema = pa.schema([
        pa.field('MATERIAL_UPDATE_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('NETWORK_HEAD', pa.string()),
        pa.field('NETWORK_ACT', pa.string()),
        pa.field('SERIAL_NO', pa.string()),
        pa.field('UNIT_OF_MEASURE', pa.string()),
        pa.field('TRANS_DATE_TIME', pa.timestamp('ns')),
        pa.field('PU_MAT_INST', pa.string()),
        pa.field('MO_NO', pa.string()),
        pa.field('BATCH', pa.string()),
        pa.field('PONUMBER', pa.string()),
        pa.field('TRANS_ITEM_INST', pa.string()),
        pa.field('PLANT', pa.string()),
        pa.field('UNRESTRICTED_STOCK', pa.decimal128(38, 10), metadata={"target_schema": "uint64()"}),
        pa.field('TRANS_NO', pa.string()),
        pa.field('MATERIAL_DESCRIPTION', pa.string()),
        pa.field('PUNUMBER', pa.string()),
        pa.field('MAT_NO', pa.string()),
        pa.field('MATERIAL_UPDATE_DATE', pa.timestamp('ns')),
        pa.field('QUANTITY', pa.string(), metadata={"target_schema": "uint64()"}),
        pa.field('VAL_TYPE', pa.string()),
        pa.field('STORAGE_LOCATION', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_clarity_ttn_slims_item_p",
        "Classification": "Public"
    })

    return target_schema


def get_target_schema_daa_clarity_ttn_user_p(column_names):
    target_schema = pa.schema([
        pa.field('ORG_UNIT_DEPT', pa.string()),
        pa.field('STATE', pa.string()),
        pa.field('TEAM_NAME', pa.string()),
        pa.field('STATUS', pa.string()),
        pa.field('TOKEN_DATE', pa.timestamp('ns')),
        pa.field('USER_INST', pa.string()),
        pa.field('ROLE', pa.string()),
        pa.field('PLANT', pa.string()),
        pa.field('TM_SUPERVISOR_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('TTN_ACTION', pa.string()),
        pa.field('LAST_LOGIN', pa.timestamp('ns')),
        pa.field('UPDATE_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('CREATE_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('CREATE_DATE', pa.timestamp('ns')),
        pa.field('TOKEN', pa.string()),
        pa.field('VENDOR_NO', pa.string()),
        pa.field('STAFF_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('TEAM_TYPE', pa.string()),
        pa.field('RUN_DATE', pa.timestamp('ns')),
        pa.field('ORG_UNIT', pa.string()),
        pa.field('STAFF_NAME', pa.string(), metadata={"req": "sensitive", "PII":"Yes"}),
        pa.field('REGION', pa.string()),
        pa.field('TELEPHONE_NUMBER', pa.string(), metadata={"req": "sensitive", "PII":"Phone Number"}),
        pa.field('SUBGROUP', pa.string()),
        pa.field('PTT', pa.string()),
        pa.field('EMAIL', pa.string(), metadata={"req": "sensitive"}),
        pa.field('TULIP_ID', pa.decimal128(16, 0)),
        pa.field('ACTION', pa.string()),
        pa.field('TITLE', pa.string()),
        pa.field('PASSCARD_NO', pa.string()),
        pa.field('PASSCARD_VALIDITY_PERIOD', pa.timestamp('ns')),
        pa.field('UPDATE_DATE', pa.timestamp('ns')),
        pa.field('POSITIONS', pa.string()),
        pa.field('COMPANY_NAME', pa.string()),
        pa.field('IC_NUMBER', pa.string(), metadata={"req": "sensitive", "PII":"IC Number"}),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_clarity_ttn_user_p",
        "Classification": "Public"
    })

    return target_schema


def get_target_schema_daa_clarity_ttn_vendor_master_p(column_names):
    target_schema = pa.schema([
        pa.field('CTT_INST', pa.string()),
        pa.field('ROC_NO', pa.string()),
        pa.field('COMPANY_CODE', pa.string()),
        pa.field('VENDOR_NUMBER', pa.string()),
        pa.field('VENDOR_NAME2', pa.string()),
        pa.field('STATE', pa.string()),
        pa.field('ADDRESS2', pa.string(), metadata={"req": "sensitive"}),
        pa.field('CITY', pa.string()),
        pa.field('CONTACT_NO', pa.string(), metadata={"req": "sensitive", "PII":"Phone Number"}),
        pa.field('TTN_ACTION', pa.string()),
        pa.field('POSTING_BLOCK', pa.string()),
        pa.field('POSTCODE', pa.string()),
        pa.field('RUN_DATE', pa.timestamp('ns')),
        pa.field('VENDOR_NAME1', pa.string()),
        pa.field('ADDRESS3', pa.string(), metadata={"req": "sensitive"}),
        pa.field('EMAIL', pa.string(), metadata={"req": "sensitive"}),
        pa.field('ADDRESS1', pa.string(), metadata={"req": "sensitive"}),
        pa.field('ABBREVIATION', pa.string()),
        pa.field('COUNTRY', pa.string()),
        pa.field('FAX_NO', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_clarity_ttn_vendor_master_p",
        "Classification": "Public"
    })

    return target_schema


def get_target_schema_daa_clarity_work_order_activities_p(column_names):
    target_schema = pa.schema([
        pa.field('WOOA_ID', pa.decimal128(20, 0)),
        pa.field('WOOA_WORO_ID', pa.string()),
        pa.field('WOOA_WORO_REVISION', pa.decimal128(20, 0)),
        pa.field('WOOA_WORG_NAME', pa.string()),
        pa.field('WOOA_ASSIGNED', pa.string()),
        pa.field('WOOA_SEQUENCE', pa.string()),
        pa.field('WOOA_TIMING', pa.string()),
        pa.field('WOOA_ACTIVITYNAME', pa.string()),
        pa.field('WOOA_STAS_ABBREVIATION', pa.string()),
        pa.field('WOOA_STATUSDATE', pa.timestamp('ns')),
        pa.field('WOOA_USERNAME', pa.string()),
        pa.field('WOOA_PROPOSED_START_DATE', pa.timestamp('ns')),
        pa.field('WOOA_PROPOSED_END_DATE', pa.timestamp('ns')),
        pa.field('WOOA_ACTUAL_START_DATE', pa.timestamp('ns')),
        pa.field('WOOA_ACTUAL_END_DATE', pa.timestamp('ns')),
        pa.field('WOOA_EMPE_ID', pa.string()),
        pa.field('WOOA_ACLN_NAME', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_clarity_work_order_activities_p",
        "Classification": "Public"
    })

    return target_schema

def get_target_schema_daa_clarity_work_order_p(column_names):
    target_schema = pa.schema([
        pa.field('WORO_ID', pa.string()), #PE2010102058089
        pa.field('WORO_REVISION', pa.string()),
        pa.field('WORO_SERO_ID', pa.string()),
        pa.field('WORO_SERO_REVISION', pa.string()),
        pa.field('WORO_WORG_NAME', pa.string()),
        pa.field('WORO_ORDT_TYPE', pa.string()),
        pa.field('WORO_CREATEDBY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('WORO_DATECREATED', pa.timestamp('ns')),
        pa.field('WORO_REVIEWEDBY', pa.string(), metadata={"req": "sensitive", "PII":"Yes"}),
        pa.field('WORO_REVIEWEDDATE', pa.timestamp('ns')),
        pa.field('WORO_APPROVEDBY', pa.string(), metadata={"req": "sensitive", "PII":"Yes"}),
        pa.field('WORO_APPROVEDDATE', pa.timestamp('ns')),
        pa.field('WORO_STAS_ABBREVIATION', pa.string()),
        pa.field('WORO_STATUSDATE', pa.timestamp('ns')),
        pa.field('WORO_USERUPDATED', pa.string(), metadata={"req": "sensitive"}),
        pa.field('WORO_CIRT_NAME', pa.string()),
        pa.field('WORO_PROM_NUMBER', pa.string()),
        pa.field('WORO_TASKNAME', pa.string()),
        pa.field('WORO_SEIT_ID', pa.decimal128(16, 0)),
        pa.field('WORO_TRUG_ID', pa.decimal128(16, 0)),
        pa.field('WORO_TROT_NUMBER', pa.string()),
        pa.field('WORO_ASSIGNED_DATE', pa.timestamp('ns')),
        pa.field('WORO_PROPOSED_START_DATE', pa.timestamp('ns')),
        pa.field('WORO_PROPOSED_END_DATE', pa.timestamp('ns')),
        pa.field('WORO_ACTUAL_START_DATE', pa.timestamp('ns')),
        pa.field('WORO_ACTUAL_END_DATE', pa.timestamp('ns')),
        pa.field('WORO_DESCRIPTION', pa.string()),
        pa.field('WORO_PLET_ID', pa.decimal128(16, 0)),
        pa.field('WORO_PETW_ID', pa.decimal128(16, 0)),
        pa.field('WORO_PETF_ID', pa.decimal128(16, 0)),
        pa.field('WORO_AREA_CODE', pa.string()),
        pa.field('WORO_EMPE_ID', pa.string()),
        pa.field('WORO_SERV_ID', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_clarity_work_order_p",
        "Classification": "Public"
    })

    return target_schema

def get_target_schema_daa_vprime_clarity_pmt_order_p(column_names):
    target_schema = pa.schema([
        pa.field('ORDER_INST', pa.string()),
        pa.field('ORDER_ID', pa.string()), #decimal128
        pa.field('STATUS', pa.string()),
        pa.field('ORDERTYPE', pa.string()),
        pa.field('ORDERGROUP', pa.string()),
        pa.field('ORDERCATEGORY', pa.string()),
        pa.field('PSESSION', pa.string()),
        pa.field('ORDERMSB', pa.string()),
        pa.field('REFID', pa.string()),
        pa.field('NOVA', pa.string()),
        pa.field('LOB', pa.string()),
        pa.field('PMNAME', pa.string()),
        pa.field('PMCONTACT', pa.string(), metadata={"req": "sensitive", "PII":"Yes"}),
        pa.field('DESCRIPTION', pa.string()),
        pa.field('TMNODE', pa.string(), metadata={"req": "sensitive"}),
        pa.field('ANDGROUP', pa.string()),
        pa.field('REGION', pa.string()),
        pa.field('TMNODE2', pa.string(), metadata={"req": "sensitive"}),
        pa.field('LOCATION_UNIT', pa.string(), metadata={"req": "sensitive"}),
        pa.field('LOCATION_BUILDING', pa.string(), metadata={"req": "sensitive"}),
        pa.field('LOCATION_STREET', pa.string(), metadata={"req": "sensitive"}),
        pa.field('LOCATION_SECTION', pa.string(), metadata={"req": "sensitive"}),
        pa.field('STATE', pa.string()),
        pa.field('LOCATION_POSTCODE', pa.string()),
        pa.field('CITY', pa.string()),
        pa.field('PROPERTYUNIT', pa.string()), #
        pa.field('PROPERTY_TYPE', pa.string()),
        pa.field('AREA_INVESTMENT', pa.string()),
        pa.field('LOCATION', pa.string(), metadata={"req": "sensitive"}),
        pa.field('DATE_CUST_RFS', pa.timestamp('ns')),
        pa.field('DATE_TM_RFS', pa.timestamp('ns')),
        pa.field('DATE_REVISED_RFS', pa.timestamp('ns')),
        pa.field('CUSTOMER_NAME', pa.string()),
        pa.field('CUSTOMER_AGENCY', pa.string()),
        pa.field('DRY1', pa.string(), metadata={"target_schema": "uint16()"}), 
        pa.field('DRY2', pa.string(), metadata={"target_schema": "uint16()"}), 
        pa.field('DRY3', pa.string(), metadata={"target_schema": "uint16()"}), 
        pa.field('DRY4', pa.string(), metadata={"target_schema": "uint16()"}), 
        pa.field('DRY5', pa.string(), metadata={"target_schema": "uint16()"}), 
        pa.field('DBY1', pa.string(), metadata={"target_schema": "uint16()"}), 
        pa.field('DBY2', pa.string(), metadata={"target_schema": "uint16()"}), 
        pa.field('DBY3', pa.string(), metadata={"target_schema": "uint16()"}), 
        pa.field('DBY4', pa.string(), metadata={"target_schema": "uint16()"}), 
        pa.field('DBY5', pa.string(), metadata={"target_schema": "uint16()"}), 
        pa.field('RY1', pa.string(), metadata={"target_schema": "float64()"}), 
        pa.field('RY2', pa.string(), metadata={"target_schema": "float64()"}), 
        pa.field('RY3', pa.string(), metadata={"target_schema": "float64()"}), 
        pa.field('RY4', pa.string(), metadata={"target_schema": "float64()"}), 
        pa.field('RY5', pa.string(), metadata={"target_schema": "float64()"}), 
        pa.field('RY6', pa.string(), metadata={"target_schema": "float64()"}), 
        pa.field('RY7', pa.string(), metadata={"target_schema": "float64()"}), 
        pa.field('RY8', pa.string(), metadata={"target_schema": "float64()"}), 
        pa.field('RY9', pa.string(), metadata={"target_schema": "float64()"}), 
        pa.field('RY10', pa.string(), metadata={"target_schema": "float64()"}), 
        pa.field('TOTALREVENUE', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('SERVICETYPE', pa.string()),
        pa.field('SMARTPARTNERSHIP', pa.string()),
        pa.field('CONTRI_AMOUNT', pa.string()),
        pa.field('CIRCULATION', pa.string()),
        pa.field('INFRATYPE', pa.string()),
        pa.field('NEID', pa.string()),
        pa.field('PLANPHYSICAL', pa.string()),
        pa.field('CNFDFACILITIES', pa.string()),
        pa.field('CNFDACCESSTX', pa.string()),
        pa.field('CTD', pa.string()),
        pa.field('PROGRAM', pa.string()),
        pa.field('REMARK', pa.string()),
        pa.field('DATE_DECOMM_ORDER', pa.timestamp('ns')),
        pa.field('DRAFT_FLAG', pa.string()),
        pa.field('CREATE_BY', pa.string()),
        pa.field('CREATE_DATE', pa.timestamp('ns')),
        pa.field('UPDATE_BY', pa.string()),
        pa.field('UPDATE_DATE', pa.timestamp('ns')),
        pa.field('ENDUSER_OID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('INFRA_GROUP', pa.string()),
        pa.field('SLG_INFO', pa.string()),
        pa.field('INFRA_REQUIRED', pa.string()),
        pa.field('ORDER_OWNER', pa.string()),
        pa.field('TOTALRESIDENTIAL', pa.string(), metadata={"target_schema": "uint16()"}), 
        pa.field('TOTALBUSINESS', pa.string(), metadata={"target_schema": "uint16()"}), 
        pa.field('BANDWIDTH', pa.string()),
        pa.field('BANDWIDTH_TYPE', pa.string()),
        pa.field('NRP_STATES', pa.string()),
        pa.field('MIGRATION_FLAG', pa.string()),
        pa.field('HORIZONTAL_TRUNKING', pa.string()),
        pa.field('BUILDING_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('TOTAL_BUILDING', pa.string(), metadata={"target_schema": "uint16()"}), 
        pa.field('CREATOR_GROUP', pa.string()),
        pa.field('OPEXPROJNO', pa.string()),
        pa.field('LOA_DATE', pa.timestamp('ns')),
        pa.field('SFP_TYPE', pa.string()),
        pa.field('CUSTOMER_PIC_NAME', pa.string(), metadata={"req": "sensitive", "PII":"Yes"}),
        pa.field('CUSTOMER_PIC_CONTACT', pa.string(), metadata={"req": "sensitive", "PII":"Yes"}),
        pa.field('SITE_READINESS', pa.string()),
        pa.field('PF', pa.string()),
        pa.field('WAITERS', pa.string()),
        pa.field('PAYMENT_STATUS_ORDER', pa.string()),
        pa.field('AMOUNT_PAID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('ICHECK_REFNO', pa.string()),
        pa.field('BUILDING_AGREEMENT_STATUS', pa.string()),
        pa.field('DATE_AGREEMENT', pa.timestamp('ns')),
        pa.field('STREAMYX_SUBS', pa.string()),
        pa.field('CABINET_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('CABINET_CATEGORY', pa.string()),
        pa.field('BAU_NEID_DP_NUMBER', pa.string(), metadata={"req": "sensitive"}),
        pa.field('PRE_UNIFI_SUBS', pa.string()),
        pa.field('APPROVED_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('APPROVED_DATE', pa.timestamp('ns')),
        pa.field('CONFIRMED_BY', pa.string(), metadata={"req": "sensitive", "PII":"Yes"}),
        pa.field('CONFIRMED_DATE', pa.timestamp('ns')),
        pa.field('COMPLETED_BY', pa.string(), metadata={"req": "sensitive", "PII":"Yes"}),
        pa.field('COMPLETED_DATE', pa.timestamp('ns')),
        pa.field('DATE_REVISED_REMARK', pa.string()),
        pa.field('WAITERS_ID', pa.string()), #TRO_WAITERS_ID #decimal128
        pa.field('TRO_NEW_FDP', pa.string(), metadata={"req": "sensitive"}),
        pa.field('CONTRACT_NUMBER', pa.string(), metadata={"req": "sensitive"}),
        pa.field('SFDC_OPPORTUNITY_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('TOTAL_SUBS', pa.string(), metadata={"target_schema": "uint16()"}),
        pa.field('AWACS_ID', pa.string()), #decimal128
        pa.field('SITE_ID_5G', pa.string()),
        pa.field('MIN_PF', pa.decimal128(38, 0)), #new
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns')),
        pa.field('BULK_UPDATE_REF', pa.string()) #new
    ],
    metadata={
        "Table_Name": "daa_vprime_clarity_pmt_order_p",
        "Classification": "Sensitive"
    })

    return target_schema

def get_target_schema_daa_vprime_clarity_pmt_po_p(column_names):
    target_schema = pa.schema([
        pa.field('POITEMCATEGORY', pa.string()),
        pa.field('PUITEMNUMBER', pa.string()),
        pa.field('POVENDORID', pa.string()),
        pa.field('POITEMNUMBER', pa.string()),
        pa.field('POQUANTITY', pa.string(), metadata={"target_schema": "uint16()"}),
        pa.field('POUNIT', pa.string()),
        pa.field('PUGROSSPRICE', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('CONTRACT_ITEM_NO', pa.string()),
        pa.field('PROJECTNUMBER', pa.string()),
        pa.field('PONUMBER', pa.string()),
        pa.field('POMATERIALNUMBER', pa.string()),
        pa.field('LORTRACKINGNO', pa.string()),
        pa.field('NETWORKNO', pa.string()),
        pa.field('REQUIREMENTNO', pa.string()),
        pa.field('LOR_NO', pa.string()),
        pa.field('POVENDORNAME', pa.string()),
        pa.field('POCURRENCY', pa.string()),
        pa.field('CONTRACT_NO', pa.string()),
        pa.field('REGION', pa.string()),
        pa.field('DELETIONINDICATOR', pa.string()),
        pa.field('PUITEMSTATUS', pa.string()),
        pa.field('PUQUANTITY', pa.string(), metadata={"target_schema": "uint16()"}),
        pa.field('PUUNIT', pa.string()),
        pa.field('PODESCRIPTION', pa.string(), metadata={"req": "sensitive"}),
        pa.field('PUNUMBER', pa.string()),
        pa.field('PONETTPRICE', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('PUDESCRIPTION', pa.string()),
        pa.field('JOB_STATUS', pa.string()),
        pa.field('NETWORKHEADER', pa.string()),
        pa.field('BATCH_DATE', pa.timestamp('ns')),
        pa.field('PODATE', pa.timestamp('ns')),
        pa.field('PODELIVERYDATE', pa.timestamp('ns')),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_vprime_clarity_pmt_po_p",
        "Classification": "Sensitive"
    })

    return target_schema

def get_target_schema_daa_vprime_clarity_pmt_sphere_activity_update_p(column_names):
    target_schema = pa.schema([
        pa.field('INST_ID', pa.decimal128(16, 0)),
        pa.field('GEMS_ACTIVITIES_TYPE', pa.string()),
        pa.field('GEMS_PROJECT_NO', pa.string()),
        pa.field('GEMS_UPDATE_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('GEMS_UPDATE_DATE', pa.string(), metadata={"target_schema": "date32()"}),
        pa.field('STATUS', pa.string()),
        pa.field('EXECUTE_DATE', pa.timestamp('ns')),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_vprime_clarity_pmt_sphere_activity_update_p",
        "Classification": "Sensitive"
    })

    return target_schema

def get_target_schema_daa_vprime_clarity_ttn_attachment_p(column_names):
    target_schema = pa.schema([
        pa.field('FILE_NAME', pa.string()),
        pa.field('PLATFORM', pa.string()),
        pa.field('LOR_INST', pa.string()),
        pa.field('STATUS_DOC', pa.string()),
        pa.field('ATT_INST', pa.string()),
        pa.field('UPDATE_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('FILE_TYPE', pa.string()),
        pa.field('UPLOAD_DATE', pa.timestamp('ns')),
        pa.field('UPLOAD_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('REMARK', pa.string()),
        pa.field('UPDATE_DATE', pa.timestamp('ns')),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns')),
        pa.field('QACI_INST', pa.string())
    ],
    metadata={
        "Table_Name": "daa_vprime_clarity_ttn_attachment_p",
        "Classification": "Sensitive"
    })

    return target_schema

def get_target_schema_daa_vprime_clarity_ttn_contractmaster_p(column_names):
    target_schema = pa.schema([
        pa.field('CONTRACT_NO', pa.string()),
        pa.field('VENDOR_NO', pa.string()),
        pa.field('TARGET_VALUE', pa.string(), metadata={"target_schema": "float64()"}),
        pa.field('VALIDITY_START', pa.timestamp('ns')),
        pa.field('VALIDITY_END', pa.timestamp('ns')),
        pa.field('PURCHASING_GROUP', pa.string()),
        pa.field('ITEM_NO', pa.string()),
        pa.field('MATERIALNO_SERVICENO', pa.string()),
        pa.field('MATERIAL_DESCRIPTION', pa.string()),
        pa.field('ITEM_VALUE', pa.string(), metadata={"target_schema": "float64()"}),
        pa.field('DELETION_INDICATOR', pa.string()),
        pa.field('CONTRACT_BALANCE', pa.string(), metadata={"target_schema": "float64()"}),
        pa.field('CTM_INST', pa.string()),
        pa.field('RUN_DATE', pa.timestamp('ns')),
        pa.field('TTN_ACTION', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_vprime_clarity_ttn_contractmaster_p",
        "Classification": "Sensitive"
    })

    return target_schema

def get_target_schema_daa_vprime_clarity_ttn_daily_progress_p(column_names):
    target_schema = pa.schema([
        pa.field('LOR_INST', pa.string()),
        pa.field('WORK_STATUS', pa.string()),
        pa.field('DAILY_ACTIVITY_CATEGORY', pa.string()),
        pa.field('DAILY_ACTIVITY_REMARK', pa.string()),
        pa.field('DAILY_ACTIVITY_DATE', pa.timestamp('ns')),
        pa.field('DAILY_PROGRESS_PERCENTAGE', pa.float64()),
        pa.field('DAILY_PROGRESS_INST', pa.string()),
        pa.field('DAILY_UPDATE_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('CLAIM_STATUS', pa.string()),
        pa.field('ACTUAL_COMPLETION_DATE', pa.timestamp('ns')),
        pa.field('PO_NUMBER', pa.string()),
        pa.field('DAILY_CURRENT_ISSUE', pa.string()),
        pa.field('PLATFORM', pa.string()),
        pa.field('TEAM_NAME', pa.string()),
        pa.field('POSITIONS', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_vprime_clarity_ttn_daily_progress_p",
        "Classification": "Sensitive"
    })

    return target_schema

def get_target_schema_daa_vprime_clarity_ttn_eot_p(column_names):
    target_schema = pa.schema([
        pa.field('EOT_INST', pa.string()),
        pa.field('EOT_RFS_DATE', pa.timestamp('ns')),
        pa.field('EOT_REASON', pa.string()),
        pa.field('EOT_REMARK', pa.string()),
        pa.field('EOT_REQUEST_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('EOT_REQUEST_DATE', pa.timestamp('ns')),
        pa.field('EOT_APPROVE_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('EOT_APPROVE_DATE', pa.timestamp('ns')),
        pa.field('EOT_STATUS', pa.string()),
        pa.field('LOR_INST', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_vprime_clarity_ttn_eot_p",
        "Classification": "Sensitive"
    })

    return target_schema

def get_target_schema_daa_vprime_clarity_ttn_location_p(column_names):
    target_schema = pa.schema([
        pa.field('LOC_INST', pa.string()),
        pa.field('LAT', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('LNG', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('CHECK_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('CHECK_DATE', pa.timestamp('ns')),
        pa.field('TYPE', pa.string()),
        pa.field('LOR_INST', pa.string()),
        pa.field('LAT_OUT', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('LNG_OUT', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('CHECKOUT_DATE', pa.timestamp('ns')),
        pa.field('CHECKOUT_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('TEAM_NAME', pa.string()),
        pa.field('CHECK_OUT_REASON', pa.string()),
        pa.field('PLANTUNIT', pa.string()),
        pa.field('MATERIAL', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns')),
        pa.field('RFC_ID', pa.string()), # new
        pa.field('RFC_DATE', pa.string()) # new
    ],
    metadata={
        "Table_Name": "daa_vprime_clarity_ttn_location_p",
        "Classification": "Sensitive"
    })

    return target_schema

def get_target_schema_daa_vprime_clarity_ttn_lor_log_p(column_names):
    target_schema = pa.schema([
        pa.field('LOG_USER', pa.string(), metadata={"req": "sensitive"}),
        pa.field('LOR_INST', pa.decimal128(38, 10)),
        pa.field('DESCRIPTION', pa.string()),
        pa.field('OLD_VALUE', pa.string()),
        pa.field('CATEGORY', pa.string()),
        pa.field('NEW_VALUE', pa.string()),
        pa.field('LOG_TYPE', pa.string()),
        pa.field('LOG_DATE', pa.timestamp('ns')),
        pa.field('LOG_INST', pa.decimal128(38, 10)),
        pa.field('TEAM_INST', pa.decimal128(38, 10)),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_vprime_clarity_ttn_lor_log_p",
        "Classification": "Sensitive"
    })

    return target_schema

def get_target_schema_daa_vprime_clarity_ttn_lor_request_p(column_names):
    target_schema = pa.schema([
        pa.field('LOR_INST', pa.string()),
        pa.field('LOR_ID', pa.string()), #pa.decimal128(16, 0)
        pa.field('PTT', pa.string()),
        pa.field('EXCH', pa.string(), metadata={"req": "sensitive"}),
        pa.field('STATE', pa.string()),
        pa.field('REGION', pa.string(), metadata={"req": "sensitive"}),
        pa.field('MGR', pa.string(), metadata={"req": "sensitive"}),
        pa.field('AM', pa.string(), metadata={"req": "sensitive"}),
        pa.field('TMSO', pa.string()),
        pa.field('PDT', pa.string()),
        pa.field('SPHERE_NO', pa.string()),
        pa.field('PROJECT_NO', pa.string()),
        pa.field('PROJECT_DESCRIPTION', pa.string(), metadata={"req": "sensitive"}),
        pa.field('S_DATE', pa.timestamp('ns')),
        pa.field('F_DATE', pa.timestamp('ns')),
        pa.field('RFS_DATE', pa.timestamp('ns')),
        pa.field('LOR_AMOUNT', pa.float64()),
        pa.field('TYPE_OF_WORK', pa.string()),
        pa.field('PROGRAM', pa.string()),
        pa.field('CATEGORY_OF_WORK', pa.string()),
        pa.field('TOTAL_PORTS', pa.uint64()),
        pa.field('TOTAL_DP', pa.uint64()),
        pa.field('SCOPE_OF_WORK', pa.string()),
        pa.field('REQUEST_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('REQUEST_DATE', pa.timestamp('ns')),
        pa.field('VERIFY_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('VERIFY_DATE', pa.timestamp('ns')),
        pa.field('APPROVE_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('APPROVE_DATE', pa.timestamp('ns')),
        pa.field('ACCEPT_STATUS', pa.string()),
        pa.field('ACCEPT_DATE', pa.timestamp('ns')),
        pa.field('LOR_STATUS', pa.string()),
        pa.field('VENDOR_NO', pa.string()),
        pa.field('CONTRACT_NO', pa.string()),
        pa.field('LOR_REMARK', pa.string()),
        pa.field('QC_STATUS', pa.string()),
        pa.field('BASKET', pa.string()),
        pa.field('QC_VERIFY_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('QC_VERIFY_DATE', pa.timestamp('ns')),
        pa.field('QC_APPROVE_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('QC_APPROVE_DATE', pa.timestamp('ns')),
        pa.field('CANCEL_REQUEST_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('CANCEL_REQUEST_DATE', pa.timestamp('ns')),
        pa.field('CANCEL_VERIFY_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('CANCEL_VERIFY_DATE', pa.timestamp('ns')),
        pa.field('CANCEL_APPROVE_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('CANCEL_APPROVE_DATE', pa.timestamp('ns')),
        pa.field('CANCEL_REMARK', pa.string()),
        pa.field('MIGRATE_FLAG', pa.string()),
        pa.field('ACCEPT_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('PO', pa.string()),
        pa.field('PO_PROGRESS', pa.float64()),
        pa.field('ACT_COM_DATE', pa.timestamp('ns')),
        pa.field('TITAN', pa.string()),
        pa.field('MATERIAL', pa.string()),
        pa.field('ATP_SUBMISSION_DATE', pa.timestamp('ns')),
        pa.field('UPDATE_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('UPDATE_DATE', pa.timestamp('ns')),
        pa.field('TURNKEY', pa.string()),
        pa.field('TP_VERIFY_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('TP_VERIFY_DATE', pa.timestamp('ns')),
        pa.field('PROPOSED_RFS', pa.string()), # new
        pa.field('NEWLORVALUE', pa.float64()), # new
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_vprime_clarity_ttn_lor_request_p",
        "Classification": "Sensitive"
    })

    return target_schema

def get_target_schema_daa_vprime_clarity_ttn_lor_team_p(column_names):
    target_schema = pa.schema([
        pa.field('TEAM_INST', pa.string()),
        pa.field('LOR_INST', pa.string()),
        pa.field('TEAM_NAME', pa.string()),
        pa.field('TEAM_LEADER', pa.string(), metadata={"req": "sensitive", "PII":"Yes"}),
        pa.field('TEAM_MEMBER1', pa.string(), metadata={"req": "sensitive", "PII":"Yes"}),
        pa.field('TEAM_MEMBER2', pa.string(), metadata={"req": "sensitive", "PII":"Yes"}),
        pa.field('TEAM_MEMBER3', pa.string(), metadata={"req": "sensitive", "PII":"Yes"}),
        pa.field('TEAM_MEMBER4', pa.string(), metadata={"req": "sensitive", "PII":"Yes"}),
        pa.field('TEAM_MEMBER5', pa.string(), metadata={"req": "sensitive", "PII":"Yes"}),
        pa.field('TEAM_MEMBER6', pa.string(), metadata={"req": "sensitive", "PII":"Yes"}),
        pa.field('DATE_START', pa.timestamp('ns')),
        pa.field('DATE_FINISH', pa.timestamp('ns')),
        pa.field('ACCEPT_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('ACCEPT_DATE', pa.timestamp('ns')),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns')),
        pa.field('TL_CONTACT', pa.string()), #new
        pa.field('UPDATE_DATE', pa.timestamp('ns')), #new
        pa.field('TL_SID', pa.string()), #new
        pa.field('TEAM_STATUS', pa.string()), #new
        pa.field('UPDATE_BY', pa.string()), #new
        pa.field('TEAM_TIME', pa.string()), #new
        pa.field('VENDOR_NO', pa.string()), #new
        pa.field('TL_NTMSP_EXPIRY_DATE', pa.timestamp('ns')), #new
        pa.field('TL_NTMSP', pa.string()) #new
    ],
    metadata={
        "Table_Name": "daa_vprime_clarity_ttn_lor_team_p",
        "Classification": "Sensitive"
    })

    return target_schema

def get_target_schema_daa_vprime_clarity_ttn_pu_material_p(column_names):
    target_schema = pa.schema([
        pa.field('PU_MAT_INST', pa.string()),
        pa.field('MATERIAL_NUMBER', pa.string()),
        pa.field('MATERIAL_DESCRIPTION', pa.string()),
        pa.field('MATERIAL_QUANTITY', pa.string(), metadata={"target_schema": "uint16()"}),
        pa.field('MATERIAL_USED', pa.decimal128(38, 10), metadata={"target_schema": "uint16()"}),
        pa.field('MATERIAL_UPDATE_DATE', pa.timestamp('ns')),
        pa.field('MATERIAL_UPDATE_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('VENDOR_NO', pa.string()),
        pa.field('PLANT', pa.string()),
        pa.field('STORAGE_LOCATION', pa.string()),
        pa.field('BATCH', pa.string()),
        pa.field('SITE_ID_PROJECT_DEF', pa.string()),
        pa.field('UNRESTRICTED_STOCK', pa.decimal128(38, 10), metadata={"target_schema": "uint16()"}),
        pa.field('VALUATION_TYPE', pa.string()),
        pa.field('LOR_NO', pa.string()),
        pa.field('REGION_CODE', pa.string()),
        pa.field('UNIT_OF_MEASURE', pa.string()),
        pa.field('RUN_DATE', pa.timestamp('ns')),
        pa.field('FLAG', pa.string()),
        pa.field('PLATFORM', pa.string()),
        pa.field('SEND_GI', pa.decimal128(38, 10), metadata={"target_schema": "uint16()"}),
        pa.field('MOVING_AVERAGE_PLANT', pa.string(), metadata={"target_schema": "float64()"}),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_vprime_clarity_ttn_pu_material_p",
        "Classification": "Sensitive"
    })

    return target_schema


def get_target_schema_daa_vprime_clarity_ttn_pu_p(column_names):
    target_schema = pa.schema([
        pa.field('PUITEMNUMBER', pa.string()),
        pa.field('PU_UPDATE_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('PU_QUANTITY', pa.decimal128(13, 3), metadata={"target_schema": "uint16()"}),
        pa.field('PLATFORM', pa.string()),
        pa.field('POITEMNUMBER', pa.string()),
        pa.field('PU_INST', pa.string()),
        pa.field('PU_REMARK', pa.string()),
        pa.field('LOR_INST', pa.string()),
        pa.field('PU_NUMBER', pa.string()),
        pa.field('PU_DESCRIPTION', pa.string()),
        pa.field('PU_UPDATE_DATE', pa.timestamp('ns')),
        pa.field('SEND_GR', pa.decimal128(38, 10), metadata={"target_schema": "float64()"}),
        pa.field('PU_ACTUAL', pa.decimal128(13, 3), metadata={"target_schema": "float64()"}),
        pa.field('GEMSPUQTY', pa.decimal128(13, 3), metadata={"target_schema": "uint16()"}),
        pa.field('PUUNIT', pa.string()),
        pa.field('PO_NUMBER', pa.string()),
        pa.field('PU_ITEMNUMBER', pa.decimal128(38, 10), metadata={"target_schema": "uint16()"}),
        pa.field('PUGROSSPRICE', pa.string(), metadata={"req": "sensitive", "target_schema":"float64()"}),
        pa.field('PU_PROGRESSPERCENTAGE', pa.decimal128(38, 10), metadata={"target_schema": "float64()"}),
        pa.field('EXTRACTION_TIMESTAMP', pa.string())
    ],
    metadata={
        "Table_Name": "daa_vprime_clarity_ttn_pu_p",
        "Classification": "Confidential"
    })

    return target_schema
  
def get_target_schema_daa_vprime_clarity_ttn_remark_p(column_names):
    target_schema = pa.schema([
        pa.field('RMK_INST', pa.string()),
        pa.field('LOR_INST', pa.string()),
        pa.field('REMARK_TYPE', pa.string()),
        pa.field('REMARK_VALUE', pa.string()),
        pa.field('REMARK_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('REMARK_DATE', pa.timestamp('ns')),
        pa.field('REJECT_CATEGORY', pa.string()),
        pa.field('VENDOR_NO', pa.string()),
        pa.field('UPDATE_BY', pa.string()),
        pa.field('UPDATE_DATE', pa.timestamp('ns')),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_vprime_clarity_ttn_remark_p",
        "Classification": "Confidential"
    })

    return target_schema
  
def get_target_schema_daa_vprime_clarity_ttn_slims_header_gr_p(column_names):
    target_schema = pa.schema([
        pa.field('PO_ITEM_NO', pa.string()),
        pa.field('VERIFYDIVISION', pa.string()),
        pa.field('TRANS_NO_GR_INST', pa.string()),
        pa.field('LOR_INST', pa.string()),
        pa.field('TMSOA_ERROR_MESSAGE', pa.string()),
        pa.field('TMSOA_TRANS_DATE_TIME', pa.timestamp('ns')),
        pa.field('APPROVEPOSITION', pa.string()),
        pa.field('VERIFY_POST', pa.string()),
        pa.field('DOC_DATE', pa.string(), metadata={"target_schema": "date32()"}),
        pa.field('UPDATE_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('VERIFY_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('APPROVE_DATE', pa.timestamp('ns')),
        pa.field('SAP_SERVICE_ENTRY_NUMBER', pa.string()),
        pa.field('GR_DOC_NUMBER', pa.string()),
        pa.field('TRANS_NO', pa.string()),
        pa.field('VERIFYPOSITION', pa.string()),
        pa.field('PROJ_NO', pa.string()),
        pa.field('PO_NO', pa.string()),
        pa.field('SAP_POSTING_DATE', pa.string()),
        pa.field('SAP_STATUS_MSG', pa.string()),
        pa.field('SAP_TRANS_DATE', pa.timestamp('ns')),
        pa.field('APPROVEDIVISION', pa.string()),
        pa.field('TRANS_DATE', pa.string()),
        pa.field('TMSOA_STATUS', pa.string()),
        pa.field('TMSOA_ERRORCODE', pa.string()),
        pa.field('TRANS_TYPE', pa.string()),
        pa.field('UPDATE_DATE', pa.timestamp('ns')),
        pa.field('VERIFY_DATE', pa.timestamp('ns')),
        pa.field('APPROVE_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('GR_DOC_YEAR', pa.string()),
        pa.field('SAP_STATUS_CODE', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_vprime_clarity_ttn_slims_header_gr_p",
        "Classification": "Confidential"
    })

    return target_schema

def get_target_schema_daa_vprime_clarity_ttn_slims_header_p(column_names):
    target_schema = pa.schema([
        pa.field('TRANS_NO_INST', pa.string()),
        pa.field('VENDOR_ID', pa.decimal128(16, 0)),
        pa.field('TEAM_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('TRANS_DATE', pa.string()),
        pa.field('WO_TYPE', pa.string()),
        pa.field('LOR_NO', pa.string()),
        pa.field('PROJ_NO', pa.string()),
        pa.field('REG_CODE', pa.string()),
        pa.field('PONUMBER', pa.string()),
        pa.field('TMSOA_STATUS', pa.string()),
        pa.field('TMSOA_ERROR_CODE', pa.string()),
        pa.field('TMSOA_ERROR_MESSAGE', pa.string()),
        pa.field('PERCENTAGE', pa.float64()),
        pa.field('LOR_INST', pa.string()),
        pa.field('TRANS_NO', pa.string()),
        pa.field('TRANS_DATE_TIME', pa.timestamp('ns')),
        pa.field('RESUBMIT_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('RESUBMIT_DATE', pa.timestamp('ns')),
        pa.field('SAP_DOC_NO', pa.string()),
        pa.field('SAP_DOC_DATE', pa.string()),
        pa.field('SAP_TRANS_DATE', pa.timestamp('ns')),
        pa.field('SAP_ERROR_MESSAGE', pa.string()),
        pa.field('PARTIAL_GI_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('PARTIAL_GI_DATE', pa.timestamp('ns')),
        pa.field('INDICATOR', pa.string()),
        pa.field('INDICATORDATE', pa.timestamp('ns')),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_vprime_clarity_ttn_slims_header_p",
        "Classification": "Confidential"
    })

    return target_schema
  
  
def get_target_schema_daa_vprime_clarity_ttn_slims_item_gr_p(column_names):
    target_schema = pa.schema([
        pa.field('TRANS_ITEM_GR_INST', pa.string()),
        pa.field('PU_ITEM_NUMBER', pa.string()),
        pa.field('PU_ACTUAL_QTY', pa.decimal128(13, 3), metadata={"target_data": "uint16()"}),
        pa.field('POITEMNUMBER', pa.string()),
        pa.field('SAP_SERVICE_ENTRY_ITEM_NUMBER', pa.string()),
        pa.field('TRANS_NO', pa.string()),
        pa.field('SAP_GR_DOC_ITEM_NO', pa.string()),
        pa.field('SAP_FINAL_ENTRY', pa.string()),
        pa.field('SAP_BLOCKING_INDICATOR', pa.string()),
        pa.field('SAP_DELETION_INDICATOR', pa.string()),
        pa.field('SAP_ACCEPTANCE', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_vprime_clarity_ttn_slims_item_gr_p",
        "Classification": "Confidential"
    })

    return target_schema

def get_target_schema_daa_vprime_clarity_ttn_slims_item_p(column_names):
    target_schema = pa.schema([
        pa.field('TRANS_ITEM_INST', pa.string()),
        pa.field('NETWORK_HEAD', pa.string()),
        pa.field('NETWORK_ACT', pa.string()),
        pa.field('MO_NO', pa.string()),
        pa.field('SERIAL_NO', pa.string()),
        pa.field('MAT_NO', pa.string()),
        pa.field('QUANTITY', pa.string(), metadata={"target_schema": "uint64()"}),
        pa.field('VAL_TYPE', pa.string()),
        pa.field('TRANS_NO', pa.string()),
        pa.field('TRANS_DATE_TIME', pa.timestamp('ns')),
        pa.field('UNRESTRICTED_STOCK', pa.string(), metadata={"target_schema": "uint64()"}),
        pa.field('MATERIAL_UPDATE_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('MATERIAL_UPDATE_DATE', pa.timestamp('ns')),
        pa.field('PU_MAT_INST', pa.string()),
        pa.field('PONUMBER', pa.string()),
        pa.field('PUNUMBER', pa.string()),
        pa.field('PLANT', pa.string()),
        pa.field('STORAGE_LOCATION', pa.string()),
        pa.field('BATCH', pa.string()),
        pa.field('UNIT_OF_MEASURE', pa.string()),
        pa.field('MATERIAL_DESCRIPTION', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_vprime_clarity_ttn_slims_item_p",
        "Classification": "Sensitive"
    })

    return target_schema

def get_target_schema_daa_vprime_clarity_ttn_user_p(column_names):
    target_schema = pa.schema([
        pa.field('USER_INST', pa.string()),
        pa.field('VENDOR_NO', pa.string()),
        pa.field('ORG_UNIT', pa.string()),
        pa.field('ORG_UNIT_DEPT', pa.string()),
        pa.field('POSITIONS', pa.string()),
        pa.field('SUBGROUP', pa.string()),
        pa.field('STAFF_NAME', pa.string(), metadata={"req": "sensitive", "PII":"Yes"}),
        pa.field('STAFF_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('REGION', pa.string()),
        pa.field('STATE', pa.string()),
        pa.field('PTT', pa.string()),
        pa.field('EMAIL', pa.string(), metadata={"req": "sensitive"}),
        pa.field('ROLE', pa.string()),
        pa.field('COMPANY_NAME', pa.string()),
        pa.field('PLANT', pa.string()),
        pa.field('TULIP_ID', pa.string()), #T000000038551 ?
        pa.field('IC_NUMBER', pa.string(), metadata={"req": "sensitive", "PII":"IC Number"}),
        pa.field('TELEPHONE_NUMBER', pa.string(), metadata={"req": "sensitive", "PII":"Phone Number"}),
        pa.field('PASSCARD_NO', pa.string()),
        pa.field('PASSCARD_VALIDITY_PERIOD', pa.timestamp('ns')),
        pa.field('TEAM_TYPE', pa.string()),
        pa.field('TEAM_NAME', pa.string()),
        pa.field('TM_SUPERVISOR_ID', pa.string(), metadata={"req": "sensitive"}),
        pa.field('STATUS', pa.string()),
        pa.field('ACTION', pa.string()),
        pa.field('RUN_DATE', pa.timestamp('ns')),
        pa.field('TTN_ACTION', pa.string()),
        pa.field('LAST_LOGIN', pa.timestamp('ns')),
        pa.field('TITLE', pa.string()),
        pa.field('UPDATE_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('UPDATE_DATE', pa.timestamp('ns')),
        pa.field('CREATE_BY', pa.string(), metadata={"req": "sensitive"}),
        pa.field('CREATE_DATE', pa.timestamp('ns')),
        pa.field('TOKEN', pa.string()),
        pa.field('TOKEN_DATE', pa.timestamp('ns')),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns')),
        pa.field('SUBPTT', pa.string()) # new
    ],
    metadata={
        "Table_Name": "daa_vprime_clarity_ttn_user_p",
        "Classification": "Confidential"
    })

    return target_schema
  

def get_target_schema_daa_vprime_clarity_ttn_vendor_master_p(column_names):
    target_schema = pa.schema([
        pa.field('CTT_INST', pa.string()),
        pa.field('COMPANY_CODE', pa.string()),
        pa.field('VENDOR_NUMBER', pa.string()),
        pa.field('VENDOR_NAME1', pa.string()),
        pa.field('VENDOR_NAME2', pa.string()),
        pa.field('ROC_NO', pa.string()),
        pa.field('POSTING_BLOCK', pa.string()),
        pa.field('ADDRESS1', pa.string(), metadata={"req": "sensitive"}),
        pa.field('ADDRESS2', pa.string(), metadata={"req": "sensitive"}),
        pa.field('ADDRESS3', pa.string(), metadata={"req": "sensitive"}),
        pa.field('POSTCODE', pa.string()),
        pa.field('CITY', pa.string()),
        pa.field('STATE', pa.string()),
        pa.field('COUNTRY', pa.string()),
        pa.field('CONTACT_NO', pa.string(), metadata={"req": "sensitive"}),
        pa.field('EMAIL', pa.string(), metadata={"req": "sensitive"}),
        pa.field('FAX_NO', pa.string()),
        pa.field('RUN_DATE', pa.timestamp('ns')),
        pa.field('TTN_ACTION', pa.string()),
        pa.field('ABBREVIATION', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns'))
    ],
    metadata={
        "Table_Name": "daa_vprime_clarity_ttn_vendor_master_p",
        "Classification": "Sensitive"
    })

    return target_schema
  
###
  
def get_target_schema_daa_clarity_equipment_features_p(column_names):
    target_schema = pa.schema([
        pa.field('extraction_date', pa.timestamp('ns')),
        pa.field('equf_equp_ID', pa.decimal128(16, 0)),
        pa.field('equf_sefl_name', pa.string()),
        pa.field('equf_total', pa.uint64()),
        pa.field('equf_percentage', pa.float64()),
        pa.field('equf_used', pa.uint64()),
        pa.field('equf_category', pa.string()),
        pa.field('equf_available', pa.string())
    ],
    metadata={
        "Table_Name": "daa_clarity_equipment_features_p",
        "Classification": "Sensitive"
    })

    return target_schema


def get_target_schema_daa_clarity_texis_view_koda_p(column_names):
    target_schema = pa.schema([
        pa.field('extraction_date', pa.timestamp('ns')),
        pa.field('exch_range_ID', pa.decimal128(16, 0)),
        pa.field('koda_category', pa.string()),
        pa.field('range_abbr', pa.string()),
        pa.field('range_descr', pa.string()),
        pa.field('d_l', pa.uint64()),
        pa.field('prefix', pa.string()),
        pa.field('range', pa.string()),
        pa.field('range_start', pa.string()),
        pa.field('range_end', pa.string()),
        pa.field('charge_data', pa.string()),
        pa.field('charge_location', pa.string()),
        pa.field('ts_launch', pa.timestamp('ns')),
        pa.field('ts_close', pa.timestamp('ns')),
        pa.field('charge_area', pa.string()),
        pa.field('routing', pa.string()),
        pa.field('d_l_n', pa.uint64()),
        pa.field('d_l_x', pa.uint64()),
        pa.field('old_no_siri', pa.string()),
        pa.field('service_name', pa.string()),
        pa.field('status', pa.string()),
        pa.field('exch_abbr', pa.string()),
        pa.field('service', pa.string()),
        pa.field('service_ID', pa.decimal128(16, 0)),
        pa.field('exch_ID', pa.decimal128(16, 0)),
        pa.field('allow_incoming', pa.string()),
        pa.field('charge_district', pa.string()),
        pa.field('host_exchange', pa.string()),
        pa.field('pusat_cama', pa.string()),
        pa.field('kemudahan_lama', pa.string()),
        pa.field('region', pa.string()),
        pa.field('state_code', pa.string()),
        pa.field('state', pa.string()),
        pa.field('ibst_induk', pa.string()),
        pa.field('place_name', pa.string()),
        pa.field('ca_code', pa.string()),
        pa.field('cd_code', pa.string()),
        pa.field('tm_poi', pa.string()),
        pa.field('olno_poi', pa.string()),
        pa.field('route_name', pa.string()),
        pa.field('no_ujian', pa.string()),
        pa.field('pilot_no', pa.string()),
        pa.field('nama_syarikat', pa.string()),
        pa.field('nama_perkhidmatan', pa.string()),
        pa.field('nama_pelanggan', pa.string()),
        pa.field('nop_ID', pa.string()),
        pa.field('nxx_type', pa.string()),
        pa.field('mob_call_sign', pa.string()),
        pa.field('processing_center', pa.uint64()),
        pa.field('mtx_area', pa.uint64()),
        pa.field('jenis_arahan', pa.string()),
        pa.field('perkara', pa.string()),
        pa.field('routing_attachment', pa.string())
    ],
    metadata={
        "Table_Name": "daa_clarity_texis_view_koda_p",
        "Classification": "Sensitive"
    })

    return target_schema
