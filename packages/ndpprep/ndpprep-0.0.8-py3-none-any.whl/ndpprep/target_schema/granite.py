##daa_granite
import pyarrow as pa

def get_target_schema_daa_git_mobile_flash_cable_e2e_view_p(column_names):        
    target_schema = pa.schema([
        pa.field('CORE_STATUS', pa.string()),
        pa.field('FRAME_LOCATION', pa.string()),
        pa.field('PAIR_ID', pa.decimal128(12, 0)),
        pa.field('ASSIGN_NE_ID', pa.string()),
        pa.field('FRAME_UNIT_ID2', pa.decimal128(12, 0)),
        pa.field('SHELF_BLOCK2', pa.string(), metadata={"req":"sensitive"}),
        pa.field('ROW_NO2', pa.string()),
        pa.field('PAIR_NO2', pa.decimal128(16, 0)),
        pa.field('FFP2_NE_PORT', pa.string()),
        pa.field('CCT_NAME2', pa.string()),
        pa.field('CABLE_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('STATUS', pa.string()),
        pa.field('ROW_NO', pa.string()),
        pa.field('FFP_QR_CODE_ID', pa.string()),
        pa.field('FFU2_QR_CODE_ID', pa.string()),
        pa.field('PAIR_ID2', pa.decimal128(12, 0)),
        pa.field('TYPE', pa.string()),
        pa.field('FRAME_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('QR_CODE_ID', pa.string()),
        pa.field('FRAME_LOCATION2', pa.string()),
        pa.field('UPDATE_BY2', pa.string(), metadata={"req":"sensitive"}),
        pa.field('CORE_ID', pa.decimal128(12, 0)),
        pa.field('UPDATE_BY', pa.string(), metadata={"req":"sensitive"}),
        pa.field('FRAME_TYPE2', pa.string()),
        pa.field('CABLE_ID', pa.decimal128(12, 0)),
        pa.field('FRAME_TYPE', pa.string()),
        pa.field('A_Z_SITE', pa.string()),
        pa.field('NE_ID', pa.string()),
        pa.field('NE_SHELF', pa.string()),
        pa.field('FRAME_ID2', pa.decimal128(12, 0)),
        pa.field('FFP2_NE_SLOT', pa.string()),
        pa.field('TM_NODE', pa.string(), metadata={"req":"sensitive"}),
        pa.field('FRAME_ID', pa.decimal128(12, 0)),
        pa.field('PAIR_STATUS', pa.string()),
        pa.field('FRAME_NAME2', pa.string(), metadata={"req":"sensitive"}),
        pa.field('P_CORE_ID', pa.decimal128(12, 0)),
        pa.field('CABLE_NO', pa.string(), metadata={"req":"sensitive"}),
        pa.field('TM_NODE_B', pa.string()),
        pa.field('FRAME_UNIT_ID', pa.decimal128(12, 0)),
        pa.field('PAIR_NO', pa.decimal128(16, 0)),
        pa.field('CCT_NAME', pa.string()),
        pa.field('NE_ID2', pa.string()),
        pa.field('ASSIGN_NE_ID2', pa.string()),
        pa.field('TOTAL_CORE', pa.decimal128(38, 10), metadata={"target_schema":"uint16()"}),
        pa.field('CORE_NO', pa.decimal128(38, 10), metadata={"target_schema":"uint16()"}),
        pa.field('SHELF_BLOCK', pa.string()),
        pa.field('VERTICAL', pa.string()),
        pa.field('FU_QR_CODE_ID', pa.string()),
        pa.field('NE_SLOT', pa.string()),
        pa.field('NE_PORT', pa.string()),
        pa.field('QR_CODE_ID2', pa.string()),
        pa.field('VERTICAL2', pa.string()),
        pa.field('A_Z_SITE2', pa.string()),
        pa.field('STATUS2', pa.string()),
        pa.field('NE_SHELF2', pa.string()),
        pa.field('FFP2_QR_CODE_ID2', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })
    
    return target_schema

def get_target_schema_daa_grnprd_card_attr_settings_p(column_names):        
    target_schema = pa.schema([
        pa.field('CARD_INST_ID', pa.decimal128(16, 0)),
        pa.field('VAL_ATTR_INST_ID', pa.decimal128(16, 0)),
        pa.field('ATTR_VALUE', pa.string(), metadata={"req":"sensitive"}),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })

    return target_schema


def get_target_schema_daa_grnprd_card_inst_p(column_names):
    target_schema = pa.schema([
        pa.field('CARD_INST_ID', pa.decimal128(16, 0)),
        pa.field('EQUIP_INST_ID', pa.decimal128(16, 0)),
        pa.field('SLOT', pa.string()),
        pa.field('TYPE', pa.string()),
        pa.field('STATUS', pa.string()), #dict
        pa.field('ORDERED', pa.timestamp('ns')),
        pa.field('DUE', pa.timestamp('ns')),
        pa.field('INSTALLED', pa.timestamp('ns')),
        pa.field('IN_SERVICE', pa.timestamp('ns')),
        pa.field('SCHED_DATE', pa.timestamp('ns')),
        pa.field('DECOMMISSION', pa.timestamp('ns')),
        pa.field('SERIAL_NO', pa.string()),
        pa.field('BATCH_NO', pa.string()),
        pa.field('BAR_CODE', pa.string()),
        pa.field('PURCHASE_PRICE', pa.decimal128(10, 2)),
        pa.field('PURCHASE_DATE', pa.timestamp('ns')),
        pa.field('ASSET_LIFE', pa.decimal128(12, 2)),
        pa.field('MAXPORTS', pa.decimal128(9, 0), metadata={"target_schema":"uint32()"}),
        pa.field('DESCRIPTION', pa.string()),
        pa.field('UNEQUIPPED', pa.string()),
        pa.field('CARD_TPLT_INST_ID', pa.decimal128(16, 0)),
        pa.field('LAST_MOD_BY', pa.string(), metadata={"req":"sensitive"}),
        pa.field('LAST_MOD_TS', pa.timestamp('ns')),
        pa.field('PARENT_CARD_INST_ID', pa.decimal128(16, 0)),
        pa.field('GRAND_PARENT_INST_ID', pa.decimal128(16, 0)),
        pa.field('NBR_SUB_CARDS', pa.decimal128(3, 0), metadata={"target_schema":"uint16()"}),
        pa.field('SLOT_OCCUPANCY', pa.decimal128(2, 0), metadata={"target_schema":"uint16()"}),
        pa.field('SLOT_INST_ID', pa.decimal128(16, 0)),
        pa.field('DYN_PORT_NAME_GEN_ID', pa.decimal128(16, 0)),
        pa.field('ROLE', pa.string()), #dict
        pa.field('NAME', pa.string()),
        pa.field('AID', pa.string()),
        pa.field('HECIG', pa.string()),
        pa.field('UNIT_OF_MEASURE', pa.string()),
        pa.field('DIRECTION', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })

    return target_schema


def get_target_schema_daa_grnprd_circ_attr_settings_p(column_names):
    target_schema = pa.schema([
      pa.field('CIRC_INST_ID', pa.decimal128(16, 0), nullable=False), #unique
      pa.field('VAL_ATTR_INST_ID', pa.decimal128(16, 0)),
      pa.field('ATTR_VALUE', pa.string(), metadata={"req":"sensitive"}),
      pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })
    
    return target_schema

def get_target_schema_daa_grnprd_circ_bw_p(column_names):        
    target_schema = pa.schema([
        pa.field('BW_NAME', pa.string()),
        pa.field('NBR_CHANNELS', pa.decimal128(6, 0), metadata={"target_schema":"uint16()"}),
        pa.field('CHANNEL_BW', pa.string()),
        pa.field('PARENT_BW', pa.string()),
        pa.field('PARENT_SUBRATE_CHANNELS', pa.decimal128(6, 0), metadata={"target_schema":"uint16()"}),
        pa.field('PARENT_SUBRATE_BW', pa.string()),
        pa.field('ARE_CONTIGUOUS', pa.string()),
        pa.field('ARE_MULTIPLES', pa.string()),
        pa.field('IS_AGGREGATE', pa.string()),
        pa.field('OPTION_FLAGS', pa.string()),
        pa.field('REL_ORDER', pa.decimal128(6, 0), metadata={"target_schema":"uint16()"}),
        pa.field('REL_BW_UNITS', pa.decimal128(12, 0), metadata={"target_schema":"uint16()"}),
        pa.field('MAX_PCT_OVERSUBSCRIPTION', pa.decimal128(12, 2), metadata={"target_schema":"float64()"}),
        pa.field('CHAN_TPLT_INST_ID', pa.decimal128(16, 0)), 
        pa.field('IS_VIRTUAL', pa.string()), #dict
        pa.field('ALLOW_OVERSUBSCRIPTION', pa.string()), #dict
        pa.field('RED_VAL', pa.decimal128(3, 0), metadata={"target_schema":"uint16()"}),
        pa.field('GREEN_VAL', pa.decimal128(3, 0), metadata={"target_schema":"uint16()"}),
        pa.field('BLUE_VAL', pa.decimal128(3, 0), metadata={"target_schema":"uint16()"}),
        pa.field('CIRC_BW_INST_ID', pa.decimal128(16, 0)),
        pa.field('BPS_USED', pa.decimal128(18, 0), metadata={"target_schema":"uint32()"}),
        pa.field('BPS_PRESENTED', pa.decimal128(18, 0), metadata={"target_schema":"uint32()"}),
        pa.field('USE_IN_PATHS', pa.string()), #dict
        pa.field('USE_IN_NETWORK', pa.string()), #dict
        pa.field('USE_IN_QOS', pa.string()), #dict
        pa.field('IS_PACKET', pa.string()), #dict
        pa.field('TYPE_ID', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })
    
    return target_schema

def get_target_schema_daa_grnprd_circ_path_attr_settings_p(column_names):        
    target_schema = pa.schema([
        pa.field('CIRC_PATH_INST_ID', pa.decimal128(16, 0)),
        pa.field('VAL_ATTR_INST_ID', pa.decimal128(16, 0)),
        pa.field('ATTR_VALUE', pa.string(), metadata={"req":"sensitive"}),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })
    
    return target_schema

#daa_grnprd_circ_path_element_p
def get_target_schema_daa_grnprd_circ_path_element_p(column_names):        
    target_schema = pa.schema([
        pa.field('CIRC_PATH_INST_ID', pa.decimal128(16, 0)),
        pa.field('SEQUENCE', pa.decimal128(6, 0)),
        pa.field('MEMBER_NBR', pa.decimal128(6, 0)),
        pa.field('CONNECT_TYPE', pa.string()),
        pa.field('ELEMENT_TYPE', pa.string()),
        pa.field('PORT_INST_ID', pa.decimal128(16, 0), metadata={"target_schema":"string()"}),
        pa.field('SEGMENT_INST_ID', pa.decimal128(16, 0), metadata={"target_schema":"string()"}),
        pa.field('PATH_INST_ID', pa.decimal128(16, 0), metadata={"target_schema":"string()"}),
        pa.field('CHANNEL_USED', pa.decimal128(6, 0), metadata={"target_schema":"uint16()"}),
        pa.field('LINK_DB_NAME', pa.string()),
        pa.field('CABLE_INST_ID', pa.decimal128(16, 0), metadata={"target_schema":"string()"}),
        pa.field('CABLE_MEM_NBR', pa.decimal128(6, 0)),
        pa.field('FRAMING', pa.string()),
        pa.field('SIGNALING', pa.string()),
        pa.field('CATEGORY', pa.string()),
        pa.field('VENDOR', pa.string()),
        pa.field('BANDWIDTH', pa.string()),
        pa.field('MODEL', pa.string()),
        pa.field('CARD_TYPE', pa.string()),
        pa.field('CONNECTOR_TYPE', pa.string()),
        pa.field('DESCRIPTION', pa.string()),
        pa.field('CHAN_INST_ID', pa.decimal128(16, 0), metadata={"target_schema":"string()"}),
        pa.field('CABLE_PAIR_INST_ID', pa.decimal128(16, 0), metadata={"target_schema":"string()"}),
        pa.field('ELEMENT_INST_ID', pa.decimal128(16, 0), metadata={"target_schema":"string()"}),
        pa.field('BANDWIDTH_INST_ID', pa.decimal128(16, 0), metadata={"target_schema":"string()"}),
        pa.field('UDC_INST_ID', pa.decimal128(16, 0), metadata={"target_schema":"string()"}),
        pa.field('RESOURCE_INST_ID', pa.decimal128(16, 0), metadata={"target_schema":"string()"}),
        pa.field('PARENT_INST_ID', pa.decimal128(16, 0), metadata={"target_schema":"string()"}),
        pa.field('DEFINITION_ID', pa.decimal128(16, 0), metadata={"target_schema":"string()"}),
        pa.field('CLOUD_INST_ID', pa.decimal128(16, 0), metadata={"target_schema":"string()"}),
        pa.field('ASSIGNMENT_GROUP', pa.decimal128(9, 0), metadata={"target_schema":"string()"}),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })

    return target_schema

#daa_grnprd_circ_path_inst_p
def get_target_schema_daa_grnprd_circ_path_inst_p(column_names):        
    target_schema = pa.schema([
        pa.field('CIRC_PATH_INST_ID', pa.decimal128(16, 0)),
        pa.field('CIRC_PATH_HUM_ID', pa.string(), metadata={"req":"sensitive"}),
        pa.field('CIRC_PATH_REV_NBR', pa.decimal128(6, 0), metadata={"target_schema":"uint16()"}),
        pa.field('STATUS', pa.string()),
        pa.field('BANDWIDTH', pa.string()),
        pa.field('TYPE', pa.string()),
        pa.field('TOPOLOGY', pa.string()),
        pa.field('TRUNK_GROUP', pa.string()),
        pa.field('NBR_MEMBERS', pa.decimal128(6, 0), metadata={"target_schema":"uint16()"}),
        pa.field('MEMBER_BW', pa.string()),
        pa.field('NBR_CHANNELS', pa.decimal128(6, 0), metadata={"target_schema":"uint16()"}),
        pa.field('VIRTUAL_CHANS', pa.string()),
        pa.field('CHAN_WARN_THRESHOLD', pa.decimal128(6, 0), metadata={"target_schema":"uint16()"}),
        pa.field('NBR_CHAN_ASSIGNED', pa.decimal128(6, 0), metadata={"target_schema":"uint16()"}),
        pa.field('NBR_ELEMENTS', pa.decimal128(6, 0), metadata={"target_schema":"uint16()"}),
        pa.field('CUSTOMER_ID', pa.string()),
        pa.field('A_SIDE_CUSTOMER', pa.string()),
        pa.field('Z_SIDE_CUSTOMER', pa.string()),
        pa.field('FRAMING', pa.string()),
        pa.field('SIGNALING', pa.string()),
        pa.field('ORDER_NUM', pa.string()),
        pa.field('ORDERED', pa.timestamp('ns')),
        pa.field('DUE', pa.timestamp('ns')),
        pa.field('INSTALLED', pa.timestamp('ns')),
        pa.field('IN_SERVICE', pa.timestamp('ns')),
        pa.field('SCHED_DATE', pa.timestamp('ns')),
        pa.field('DECOMMISSION', pa.timestamp('ns')),
        pa.field('PREV_PATH_INST_ID', pa.decimal128(16, 0)),
        pa.field('NEXT_PATH_INST_ID', pa.decimal128(16, 0)),
        pa.field('LAST_MOD_BY', pa.string()),
        pa.field('LAST_MOD_TS', pa.timestamp('ns')),
        pa.field('INST_VER', pa.decimal128(6, 0), metadata={"target_schema":"uint16()"}),
        pa.field('A_SIDE_SITE_ID', pa.decimal128(16, 0)),
        pa.field('Z_SIDE_SITE_ID', pa.decimal128(16, 0)),
        pa.field('LOCK_TS', pa.string()),
        pa.field('LOCK_BY', pa.string()),
        pa.field('DESCRIPTION', pa.string()),
        pa.field('ELEM_COST', pa.decimal128(12, 2)),
        pa.field('DISTANCE', pa.decimal128(13, 3)),
        pa.field('MAX_PCT_OVERSUBSCRIPTION', pa.decimal128(12, 2)),
        pa.field('SVC_PRIORITY', pa.string()),
        pa.field('TCIC_TFN_AUTOGEN', pa.string()),
        pa.field('BTCIC_BTFN_NBR', pa.decimal128(9, 0), metadata={"target_schema":"uint16()"}),
        pa.field('TCIC_NBR_PLAN', pa.string()),
        pa.field('TOTAL_BPS_AVAIL', pa.decimal128(18, 0), metadata={"target_schema":"uint16()"}),
        pa.field('BPS_ASSIGNED', pa.decimal128(18, 0), metadata={"target_schema":"uint16()"}),
        pa.field('WARN_THRESHOLD_PCT', pa.decimal128(9, 2)),
        pa.field('START_CHAN_NBR', pa.decimal128(6, 0), metadata={"target_schema":"uint16()"}),
        pa.field('END_CHAN_NBR', pa.decimal128(6, 0), metadata={"target_schema":"uint16()"}),
        pa.field('CHAN_NAME_GEN_ID', pa.decimal128(16, 0)),
        pa.field('BW_ADJUST_GEN_ID', pa.decimal128(16, 0)),
        pa.field('BANDWIDTH_INST_ID', pa.decimal128(16, 0)),
        pa.field('PATH_CLASS', pa.string()),
        pa.field('DRAFT', pa.string()),
        pa.field('DIRECTION', pa.string()),
        pa.field('ROLE', pa.string()),
        pa.field('QOS_POLICY_INST_ID', pa.decimal128(16, 0)),
        pa.field('IS_IP', pa.string()),
        pa.field('OWNER', pa.string()),
        pa.field('IS_STALE', pa.string()),
        pa.field('PATH_SPEC_BITRATE_TYPE', pa.string()),
        pa.field('PATH_SPEC_BITRATE_LONG', pa.decimal128(18, 0)),
        pa.field('PATH_SPEC_BITRATE_STR', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })

    return target_schema
  

def get_target_schema_daa_grnprd_del_resource_inst_p(column_names):        
    target_schema = pa.schema([
        pa.field('RESOURCE_INST_ID', pa.decimal128(16, 0)),
        pa.field('PARENT_INST_ID', pa.decimal128(16, 0)),
        pa.field('TEMPLATE_INST_ID', pa.decimal128(16, 0)),
        pa.field('DEFINITION_INST_ID', pa.decimal128(16, 0)),
        pa.field('NAME', pa.string(), metadata={"req": "sensitive"}),
        pa.field('CATEGORY', pa.string()),
        pa.field('FLAGS', pa.string()),
        pa.field('LAST_MOD_TS', pa.timestamp('ns')),
        pa.field('LAST_MOD_BY', pa.string()),
        pa.field('INST_VER', pa.decimal128(6, 0), metadata={"target_schema": "uint16()"}),
        pa.field('REVISION', pa.decimal128(6, 0), metadata={"target_schema": "uint16()"}),
        pa.field('START_DATE', pa.timestamp('ns')),
        pa.field('END_DATE', pa.timestamp('ns')),
        pa.field('LOCK_TS', pa.timestamp('ns')),
        pa.field('LOCK_BY', pa.string()),
        pa.field('STATUS', pa.string()),
        pa.field('ORDERED', pa.timestamp('ns')),
        pa.field('SCHED_DATE', pa.timestamp('ns')),
        pa.field('DUE', pa.timestamp('ns')),
        pa.field('INSTALLED', pa.timestamp('ns')),
        pa.field('IN_SERVICE', pa.timestamp('ns')),
        pa.field('DECOMMISSION', pa.timestamp('ns')),
        pa.field('CIRC_PATH_INST_ID', pa.decimal128(16, 0)),
        pa.field('NEXT_PATH_INST_ID', pa.decimal128(16, 0)),
        pa.field('PATH_CHG_DATE', pa.timestamp('ns')),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })
    
    return target_schema

#  daa_grnprd_epa_p
def get_target_schema_daa_grnprd_epa_p(column_names):
    target_schema = pa.schema([
        pa.field('PORT_INST_ID', pa.decimal128(16, 0)),
        pa.field('CARD_INST_ID', pa.decimal128(16, 0)),
        pa.field('PORT_HUM_ID', pa.string()),
        pa.field('BANDWIDTH', pa.string()),
        pa.field('DESCRIPTION', pa.string()),
        pa.field('STATUS', pa.string()),
        pa.field('CONNECTOR_TYPE', pa.string()),
        pa.field('EQUIP_INST_ID', pa.decimal128(16, 0)),
        pa.field('SITE_INST_ID', pa.decimal128(16, 0)),
        pa.field('CIRC_INST_ID', pa.decimal128(16, 0)),
        pa.field('CIRC_PATH_INST_ID', pa.decimal128(16, 0)),
        pa.field('CABLE_INST_ID', pa.decimal128(16, 0)),
        pa.field('SWITCH_TG_MEM', pa.string()),
        pa.field('USER_TG_MEM', pa.string()),
        pa.field('EFFECT_TG_MEM', pa.timestamp('ns')),
        pa.field('PATH_CHG_DATE', pa.timestamp('ns')),
        pa.field('NEXT_PATH_INST_ID', pa.string()),#10
        pa.field('A_WIRED_PORT_INST_ID', pa.string()),#10
        pa.field('Z_WIRED_PORT_INST_ID', pa.string()),#10
        pa.field('PARENT_PORT_INST_ID', pa.string()),#10
        pa.field('PARENT_PORT_CHAN', pa.string()),#6
        pa.field('VIRTUAL_PORT', pa.string()),
        pa.field('PORT_ACCESS_ID', pa.string()),
        pa.field('PARENT_PORT_CHAN_NAME', pa.string()),
        pa.field('COST', pa.string()),
        pa.field('LAST_MOD_BY', pa.string()),
        pa.field('LAST_MOD_TS', pa.timestamp('ns')),
        pa.field('BANDWIDTH_INST_ID', pa.string()),#10
        pa.field('PATH_CHAN_INST_ID', pa.string()),#10
        pa.field('NEXT_CHAN_INST_ID', pa.string()),#10
        pa.field('DIRECTION', pa.string()),
        pa.field('ROLE', pa.string()),
        pa.field('RESERVATION_INST_ID', pa.string()),#10
        pa.field('AID', pa.string()),
        pa.field('HECIG', pa.string()),
        pa.field('NETWORK_DIRECTION', pa.string()),
        pa.field('PHYSICAL_PORT_NAME', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })

    return target_schema

  
def get_target_schema_daa_grnprd_equip_attr_settings_p(column_names):        
    target_schema = pa.schema([
        pa.field('EQUIP_INST_ID', pa.decimal128(16, 0)),
        pa.field('VAL_ATTR_INST_ID', pa.decimal128(16, 0)),
        pa.field('ATTR_VALUE', pa.string(), metadata={"req":"sensitive"}),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ])

    return target_schema


#done but cant cast to timestamp('s')
def get_target_schema_daa_grnprd_equip_inst_p(column_names):        
    target_schema = pa.schema([
        pa.field('EQUIP_INST_ID', pa.decimal128(16, 0)),
        pa.field('TYPE', pa.string()),
        pa.field('VENDOR', pa.string()),
        pa.field('MODEL', pa.string()),
        pa.field('REV', pa.string()),
        pa.field('SW_REV', pa.string()),
        pa.field('DESCR', pa.string()),
        pa.field('SITE_INST_ID', pa.decimal128(16, 0)),
        pa.field('PARENT_EQ_INST_ID', pa.decimal128(16, 0)),
        pa.field('STATUS', pa.string()),
        pa.field('EQ_CLASS', pa.string()),
        pa.field('DIM_HEIGHT', pa.decimal128(10, 3)),
        pa.field('DIM_WIDTH', pa.decimal128(10, 3)),
        pa.field('DIM_DEPTH', pa.decimal128(10, 3)),
        pa.field('DIM_DIST_TO_BASE', pa.decimal128(10, 3)),
        pa.field('DIM_DIST_TO_LEFT', pa.decimal128(10, 3)),
        pa.field('DIM_DIST_TO_FRONT', pa.decimal128(10, 3)),
        pa.field('LINEUP', pa.string()),
        pa.field('FRAME', pa.string()),
        pa.field('SHELF', pa.string()),
        pa.field('TARGET_ID', pa.string()),
        pa.field('NMS_EMS', pa.string()),
        pa.field('ORDER_NUM', pa.string()),
        pa.field('ORDERED', pa.timestamp('ns')),
        pa.field('DUE', pa.timestamp('ns')),
        pa.field('INSTALLED', pa.timestamp('ns')),
        pa.field('IN_SERVICE', pa.timestamp('ns')),
        pa.field('SCHED_DATE', pa.timestamp('ns')),
        pa.field('DECOMMISSION', pa.timestamp('ns')),
        pa.field('SERIAL_NO', pa.string()),
        pa.field('BATCH_NO', pa.string()),
        pa.field('BAR_CODE', pa.string()),
        pa.field('PURCHASE_PRICE', pa.decimal128(10, 2)),
        pa.field('PURCHASE_DATE', pa.timestamp('ns')),
        pa.field('ASSET_LIFE', pa.decimal128(12, 2)),
        pa.field('TG_MEM_ACTIVE', pa.string()),
        pa.field('LAST_TG_MEM_UPD', pa.timestamp('ns')),
        pa.field('LAST_TG_MEM_REVIEWED', pa.timestamp('ns')),
        pa.field('COMMENTS', pa.string()),
        pa.field('LAST_MOD_TS', pa.timestamp('ns')),
        pa.field('LAST_MOD_BY', pa.string()),
        pa.field('INST_VER', pa.decimal128(6, 0)),
        pa.field('LOCK_TS', pa.timestamp('ns')),
        pa.field('LOCK_BY', pa.string()),
        pa.field('AUTOMATION', pa.string()),
        pa.field('PLANNING_ENABLED', pa.string()),
        pa.field('WARN_USER_MOD', pa.string()),
        pa.field('CLLI', pa.string()),
        pa.field('CLEI', pa.string()),
        pa.field('POINT_CODE', pa.string()),
        pa.field('EQ_TPLT_INST_ID', pa.decimal128(16, 0)),
        pa.field('CUST_INST_ID', pa.decimal128(16, 0)),
        pa.field('NPA', pa.string()),
        pa.field('ADM_CO_INST_ID', pa.decimal128(16, 0)),
        pa.field('OFFSET_X', pa.decimal128(10, 3)),
        pa.field('OFFSET_Y', pa.decimal128(10, 3)),
        pa.field('OFFSET_Z', pa.decimal128(10, 3)),
        pa.field('ROTATION', pa.decimal128(10, 3)),
        pa.field('AID', pa.string()),
        pa.field('HECIG', pa.string()),
        pa.field('UNIT_OF_MEASURE', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })

    return target_schema

def get_target_schema_daa_grnprd_inst_audit_p(column_names):        
    target_schema = pa.schema([
        pa.field('ELEMENT_TYPE', pa.string()),
        pa.field('INST_ID', pa.decimal128(16, 0)),
        pa.field('VERSION_CHGD', pa.decimal128(6, 0)),
        pa.field('EDIT_OPERATION', pa.string()),
        pa.field('CHG_TS', pa.timestamp('ns')),
        pa.field('CHG_BY', pa.string()),
        pa.field('CHG_DESC', pa.string(), metadata={"req":"sensitive"}),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })

    return target_schema


def get_target_schema_daa_grnprd_plan_table_p(column_names):        
    target_schema = pa.schema([
        pa.field('STATEMENT_ID', pa.string()),
        pa.field('PLAN_ID', pa.decimal128(16, 0)),
        pa.field('TIMESTAMP', pa.timestamp('ns')),
        pa.field('REMARKS', pa.string()),
        pa.field('OPERATION', pa.string()),
        pa.field('OPTIONS', pa.string()),
        pa.field('OBJECT_NODE', pa.string()),
        pa.field('OBJECT_OWNER', pa.string()),
        pa.field('OBJECT_NAME', pa.string()),
        pa.field('OBJECT_ALIAS', pa.string()),
        pa.field('OBJECT_INSTANCE', pa.decimal128(38, 0), metadata={"target_schema":"uint16()"}),
        pa.field('OBJECT_TYPE', pa.string()),
        pa.field('OPTIMIZER', pa.string()),
        pa.field('SEARCH_COLUMNS', pa.decimal128(38, 10), metadata={"target_schema":"decimal128(10, 0)"}),
        pa.field('ID', pa.decimal128(38, 0), metadata={"target_schema":"decimal128(10, 0)"}),
        pa.field('PARENT_ID', pa.decimal128(38, 0), metadata={"target_schema":"decimal128(10, 0)"}),
        pa.field('DEPTH', pa.decimal128(16, 0)),
        pa.field('POSITION', pa.decimal128(16, 0)),
        pa.field('COST', pa.decimal128(38, 0), metadata={"target_schema":"float64()"}),
        pa.field('CARDINALITY', pa.decimal128(16, 0)),
        pa.field('BYTES', pa.decimal128(16, 0)),
        pa.field('OTHER_TAG', pa.string()),
        pa.field('PARTITION_START', pa.string()),
        pa.field('PARTITION_STOP', pa.string()),
        pa.field('PARTITION_ID', pa.decimal128(12, 0)),
        pa.field('OTHER', pa.string()),
        pa.field('DISTRIBUTION', pa.string()),
        pa.field('CPU_COST', pa.decimal128(38, 0), metadata={"target_schema":"float64()"}),
        pa.field('IO_COST', pa.decimal128(38, 0), metadata={"target_schema":"float64()"}),
        pa.field('TEMP_SPACE', pa.decimal128(38, 0), metadata={"target_schema":"uint32()"}),
        pa.field('ACCESS_PREDICATES', pa.string()),
        pa.field('FILTER_PREDICATES', pa.string()),
        pa.field('PROJECTION', pa.string()),
        pa.field('TIME',  pa.decimal128(38, 0), metadata={"target_schema":"uint16()"}),
        pa.field('QBLOCK_NAME', pa.string()),
        pa.field('OTHER_XML', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })
    
    return target_schema

def get_target_schema_daa_grnprd_port_attr_settings_p(column_names):        
    target_schema = pa.schema([
        pa.field('PORT_INST_ID', pa.decimal128(16, 0)),
        pa.field('VAL_ATTR_INST_ID', pa.decimal128(16, 0)),
        pa.field('ATTR_VALUE', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })
    return target_schema


def get_target_schema_daa_grnprd_resource_associations_p(column_names):        
    target_schema = pa.schema([
        pa.field('RESOURCE_ASSOC_ID', pa.decimal128(16, 0)),
        pa.field('RESOURCE_INST_ID', pa.decimal128(16, 0)),
        pa.field('TARGET_TYPE_ID', pa.decimal128(16, 0)),
        pa.field('TARGET_SUBTYPE', pa.string()),
        pa.field('TARGET_INST_ID', pa.decimal128(16, 0)),
        pa.field('ALLOCATED_CAPACITY', pa.decimal128(16, 0), metadata={"target_schema":"uint16()"}),
        pa.field('CAPACITY_ACTIVE', pa.string(), metadata={"target_schema":"uint16()"}),
        pa.field('FLAGS', pa.string()),
        pa.field('INST_VER', pa.decimal128(6, 0)),
        pa.field('START_DATE', pa.timestamp('ns')),
        pa.field('END_DATE', pa.timestamp('ns')),
        pa.field('RESOURCE_ASSOC_TYPE_ID', pa.decimal128(16, 0)),
        pa.field('NAME', pa.string()),
        pa.field('DESCRIPTION', pa.string()),
        pa.field('OWNER', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })
    
    return target_schema

def get_target_schema_daa_grnprd_resource_attr_settings_p(column_names):        
    target_schema = pa.schema([
        pa.field('RESOURCE_INST_ID', pa.decimal128(16, 0)),
        pa.field('VAL_ATTR_INST_ID', pa.decimal128(16, 0)),
        pa.field('RESOURCE_DEF_ID', pa.decimal128(16, 0)),
        pa.field('GROUP_INST_ID', pa.decimal128(16, 0)),
        pa.field('ATTR_VALUE', pa.string(), metadata={"req":"sensitive"}),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })
    
    return target_schema


def get_target_schema_daa_grnprd_resource_inst_p(column_names):        
    target_schema = pa.schema([
        pa.field('RESOURCE_INST_ID', pa.decimal128(16, 0)),
        pa.field('PARENT_INST_ID', pa.decimal128(16, 0)),
        pa.field('TEMPLATE_INST_ID', pa.decimal128(16, 0)),
        pa.field('DEFINITION_INST_ID', pa.decimal128(16, 0)),
        pa.field('NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('CATEGORY', pa.string()),
        pa.field('FLAGS', pa.string()),
        pa.field('LAST_MOD_TS', pa.timestamp('ns')),
        pa.field('LAST_MOD_BY', pa.string(), metadata={"req":"sensitive"}),
        pa.field('INST_VER', pa.decimal128(6, 0)),
        pa.field('REVISION', pa.decimal128(6, 0)),
        pa.field('START_DATE', pa.timestamp('ns')),
        pa.field('END_DATE', pa.timestamp('ns')),
        pa.field('LOCK_TS', pa.timestamp('ns')),
        pa.field('LOCK_BY', pa.string()),
        pa.field('STATUS', pa.string()),
        pa.field('ORDERED', pa.timestamp('ns')),
        pa.field('SCHED_DATE', pa.timestamp('ns')),
        pa.field('DUE', pa.timestamp('ns')),
        pa.field('INSTALLED', pa.timestamp('ns')),
        pa.field('IN_SERVICE', pa.timestamp('ns')),
        pa.field('DECOMMISSION', pa.timestamp('ns')),
        pa.field('CIRC_PATH_INST_ID', pa.decimal128(16, 0)),
        pa.field('NEXT_PATH_INST_ID', pa.decimal128(16, 0)),
        pa.field('PATH_CHG_DATE', pa.timestamp('ns')),
        pa.field('RESERVATION_INST_ID', pa.decimal128(16, 0)),
        pa.field('PREV_REVISION', pa.decimal128(16, 0)),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
        metadata={
            "Classification": "Confidential"
        })

    return target_schema


def get_target_schema_daa_grnprd_rm_allocated_numbers_p(column_names):        
    target_schema = pa.schema([
        pa.field('ALLOCATED_NUMBER_INST_ID', pa.decimal128(16, 0)),
        pa.field('NUMBER_RANGE_INST_ID', pa.decimal128(16, 0)),
        pa.field('THE_NUMBER', pa.decimal128(16, 0)),
        pa.field('STATUS', pa.string()),
        pa.field('CATEGORY', pa.string()),
        pa.field('RESERVED', pa.timestamp('ns')),
        pa.field('ORDERED', pa.timestamp('ns')),
        pa.field('ACTIVE', pa.timestamp('ns')),
        pa.field('DECOMMISSIONED', pa.timestamp('ns')),
        pa.field('COMMENTS', pa.string(), metadata={"req":"sensitive"}),
        pa.field('DESCRIPTION', pa.string(), metadata={"req":"sensitive"}),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })

    return target_schema


def get_target_schema_daa_grnprd_rm_number_ranges_p(column_names):        
    target_schema = pa.schema([
        pa.field('NUMBER_RANGE_INST_ID', pa.decimal128(16, 0)),
        pa.field('INST_VER', pa.decimal128(6, 0)),
        pa.field('DEFAULT_NUMBER_CATEGORY', pa.string()),
        pa.field('PARENT_NUMBER_RANGE_INST_ID', pa.decimal128(16, 0)),
        pa.field('RANGE_NAME', pa.string()),
        pa.field('CATEGORY', pa.string()),
        pa.field('STATUS', pa.string()),
        pa.field('RANGE_PREFIX', pa.string()),
        pa.field('RANGE_SUFFIX', pa.string()),
        pa.field('RANGE_LENGTH', pa.decimal128(1, 0)),
        pa.field('RANGE_START', pa.decimal128(9, 0)),
        pa.field('RANGE_END', pa.decimal128(9, 0)),
        pa.field('WARNING_THRESHOLD', pa.decimal128(3, 0)),
        pa.field('COMMENTS', pa.string()),
        pa.field('LAST_MOD_BY', pa.string(), metadata={"req":"sensitive"}),
        pa.field('LAST_MOD_TS', pa.timestamp('ns')),
        pa.field('LOCK_BY', pa.string()),
        pa.field('LOCK_TS', pa.timestamp('ns')),
        pa.field('DESCRIPTION', pa.string()),
        pa.field('NBR_ALLOCATED_NUMBERS', pa.decimal128(16, 0)),
        pa.field('NBR_UNALLOCATED_NUMBERS', pa.decimal128(16, 0)),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })
    
    return target_schema


def get_target_schema_daa_grnprd_site_attr_settings_p(column_names):        
    target_schema = pa.schema([
        pa.field('SITE_INST_ID', pa.decimal128(16, 0)),
        pa.field('VAL_ATTR_INST_ID', pa.decimal128(16, 0)),
        pa.field('ATTR_VALUE', pa.string(), metadata={"req":"sensitive"}),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })
    
    return target_schema

def get_target_schema_daa_grnprd_site_inst_p(column_names):        
    target_schema = pa.schema([
        pa.field('SITE_INST_ID', pa.decimal128(16, 0)),
        pa.field('SITE_HUM_ID', pa.string(), metadata={"req":"sensitive"}),
        pa.field('CLLI', pa.string(), metadata={"req":"sensitive"}),
        pa.field('NUM', pa.string()),
        pa.field('BASE_NUM', pa.string()),
        pa.field('LATITUDE', pa.string()),
        pa.field('LONGITUDE', pa.string()),
        pa.field('RESTRICTIONS', pa.string()),
        pa.field('CONTACTS', pa.string()),
        pa.field('ADDRESS', pa.string()),
        pa.field('POST_CODE_1', pa.string()),
        pa.field('POST_CODE_2', pa.string()),
        pa.field('CITY', pa.string()),
        pa.field('STATE_PROV', pa.string()),
        pa.field('COUNTY', pa.string()),
        pa.field('COUNTRY', pa.string()),
        pa.field('ROOM', pa.string(), metadata={"req":"sensitive"}),
        pa.field('FLOOR', pa.string(), metadata={"req":"sensitive"}),
        pa.field('NPA_NXX', pa.string(), metadata={"req":"sensitive"}),
        pa.field('COMMENTS', pa.string()),
        pa.field('LAST_MOD_TS', pa.timestamp('ns')),
        pa.field('LAST_MOD_BY', pa.string(), metadata={"req":"sensitive"}),
        pa.field('INST_VER', pa.decimal128(6, 0)),
        pa.field('LOCK_TS', pa.timestamp('ns')),
        pa.field('LOCK_BY', pa.string()),
        pa.field('PARENT_SITE_INST_ID', pa.decimal128(16, 0)),
        pa.field('STATUS', pa.string()),
        pa.field('FPLAN_DEPTH', pa.decimal128(10, 3)),
        pa.field('FPLAN_WIDTH', pa.decimal128(10, 3)),
        pa.field('FPLAN_HEIGHT', pa.decimal128(10, 3)),
        pa.field('FPLAN_NAME', pa.string()),
        pa.field('FPLAN_ORIGIN_X', pa.decimal128(10, 3)),
        pa.field('FPLAN_ORIGIN_Y', pa.decimal128(10, 3)),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })

    return target_schema

#daa_grnprd_slot_inst_p
def get_target_schema_daa_grnprd_slot_inst_p(column_names):
    target_schema = pa.schema([
        pa.field('SLOT_INST_ID', pa.decimal128(16, 0)),
        pa.field('EQUIP_INST_ID', pa.decimal128(16, 0)),
        pa.field('PARENT_CARD_INST_ID', pa.decimal128(16, 0)),
        pa.field('SLOT', pa.string()),
        pa.field('CARD_INST_ID', pa.decimal128(16, 0)),
        pa.field('REL_ORDER', pa.decimal128(6, 0)),
        pa.field('DIM_HEIGHT', pa.decimal128(10, 3)),
        pa.field('DIM_WIDTH', pa.decimal128(10, 3)),
        pa.field('DIM_DEPTH', pa.decimal128(10, 3)),
        pa.field('DIM_DIST_TO_BASE', pa.decimal128(10, 3)),
        pa.field('DIM_DIST_TO_LEFT', pa.decimal128(10, 3)),
        pa.field('DIM_DIST_TO_FRONT', pa.decimal128(10, 3)),
        pa.field('DESCRIPTION', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })

    return target_schema


def get_target_schema_daa_grnprd_tm_ont_id_p(column_names):        
    target_schema = pa.schema([
        pa.field('OLT_PORT_INST_ID', pa.decimal128(16, 0)),
        pa.field('ONU_EQUIP_INST_ID', pa.decimal128(16, 0)),
        pa.field('ONT_ID', pa.decimal128(16, 0)),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })
    return target_schema


#latest date 2023-06-17   
def get_target_schema_daa_grnprd_tm_service_availability_p(column_names):        
    target_schema = pa.schema([
        pa.field('INSERT_DATE', pa.timestamp('ns')),
        pa.field('COPPER_OWN_TM', pa.string()),
        pa.field('PREMISE_TYPE', pa.string()),
        pa.field('OPERATION_DATE', pa.timestamp('ns')),
        pa.field('STATE', pa.string()),
        pa.field('MAIN_DP', pa.string(), metadata={"req":"sensitive"}),
        pa.field('RESOURCE_INST_ID', pa.decimal128(16, 0)),
        pa.field('DDP', pa.string()),
        pa.field('CITY', pa.string()),
        pa.field('STREET_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('ADDRESS_FULL', pa.string(), metadata={"req":"sensitive"}),
        pa.field('POSTCODE', pa.string()),
        pa.field('BUILDING_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('SMART_DEVELOPER', pa.string()),
        pa.field('SMART_PROJECT_ID', pa.string()),
        pa.field('OPERATION_TYPE', pa.string()),
        pa.field('STREET_TYPE', pa.string()),
        pa.field('LATITUDE', pa.string(), metadata={"req":"sensitive", "target_schema":"float64()"}),
        pa.field('ADDR_SERVICE_CATEGORY', pa.string()),
        pa.field('SECTION', pa.string()),
        pa.field('HYBRID', pa.string()),
        pa.field('LONGITUDE', pa.string(), metadata={"req":"sensitive", "target_schema":"float64()"}),
        pa.field('HOUSE_UNIT_LOT', pa.string(), metadata={"req":"sensitive"}),
        pa.field('FLOOR_NUMBER', pa.string(), metadata={"req":"sensitive"}),
        pa.field('COUNTRY', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })

    return target_schema

def get_target_schema_daa_grnprd_toad_plan_table_p(column_names):        
    target_schema = pa.schema([
        pa.field('STATEMENT_ID', pa.string()),
        pa.field('PLAN_ID', pa.decimal128(12, 0)),
        pa.field('TIMESTAMP', pa.timestamp('ns')),
        pa.field('REMARKS', pa.string()),
        pa.field('OPERATION', pa.string()),
        pa.field('OPTIONS', pa.string()),
        pa.field('OBJECT_NODE', pa.string()),
        pa.field('OBJECT_OWNER', pa.string()),
        pa.field('OBJECT_NAME', pa.string()),
        pa.field('OBJECT_ALIAS', pa.string()),
        pa.field('OBJECT_INSTANCE', pa.decimal128(16, 0)),
        pa.field('OBJECT_TYPE', pa.string()),
        pa.field('OPTIMIZER', pa.string()),
        pa.field('SEARCH_COLUMNS', pa.decimal128(38, 10), metadata={"target_schema":"decimal128(16, 0)"}),
        pa.field('ID', pa.decimal128(16, 0)),
        pa.field('PARENT_ID', pa.decimal128(16, 0)),
        pa.field('DEPTH', pa.decimal128(16, 0)),
        pa.field('POSITION', pa.decimal128(16, 0)),
        pa.field('COST', pa.decimal128(16, 0)),
        pa.field('CARDINALITY', pa.decimal128(16, 0)),
        pa.field('BYTES', pa.decimal128(16, 0)),
        pa.field('OTHER_TAG', pa.string()),
        pa.field('PARTITION_START', pa.string()),
        pa.field('PARTITION_STOP', pa.string()),
        pa.field('PARTITION_ID', pa.decimal128(16, 0)),
        pa.field('OTHER', pa.string()),
        pa.field('DISTRIBUTION', pa.string()),
        pa.field('CPU_COST', pa.decimal128(16, 0), metadata={"target_schema":"decimal128(16, 2)"}),
        pa.field('IO_COST', pa.decimal128(16, 0), metadata={"target_schema":"decimal128(16, 2)"}),
        pa.field('TEMP_SPACE', pa.decimal128(38, 0)),
        pa.field('ACCESS_PREDICATES', pa.string(), metadata={"req":"sensitive"}),
        pa.field('FILTER_PREDICATES', pa.string()),
        pa.field('PROJECTION', pa.string()),
        pa.field('TIME', pa.decimal128(38, 0)),
        pa.field('QBLOCK_NAME', pa.string()),
        pa.field('OTHER_XML', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })
    
    return target_schema

#udc
def get_target_schema_daa_grnprd_udc_attribute_p(column_names):        
    target_schema = pa.schema([
        pa.field('ATTR_DEF_ID', pa.decimal128(9, 0)),
        pa.field('UDC_INST_ID', pa.decimal128(9, 0)),
        pa.field('UDC_ATTR_VALUE', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })

    return target_schema


def get_target_schema_daa_grnprd_udc_role_inst_p(column_names):        
    target_schema = pa.schema([
        pa.field('UDC_ROLE_INST_ID', pa.decimal128(16, 0)),
        pa.field('ROLE_DEF_ID', pa.decimal128(16, 0)),
        pa.field('OPERATOR_INST_ID', pa.decimal128(16, 0)),
        pa.field('OPERAND_INST_ID', pa.decimal128(16, 0)),
        pa.field('IS_PREFERRED_DIRECTION', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })

    return target_schema

#val
def get_target_schema_daa_grnprd_val_attr_name_p(column_names):        
    target_schema = pa.schema([
        pa.field('VAL_ATTR_INST_ID', pa.decimal128(16, 0)),
        pa.field('ATTR_NAME', pa.string()),
        pa.field('GROUP_NAME', pa.string()),
        pa.field('ATTR_DATA_TYPE', pa.string()),
        pa.field('SEQ_NBR', pa.decimal128(6, 0)),
        pa.field('MIN_VALUE', pa.decimal128(12, 3)),
        pa.field('MAX_VALUE', pa.decimal128(12, 3)),
        pa.field('MAX_LENGTH', pa.decimal128(9, 0)),
        pa.field('DEFAULT_VALUE', pa.string()),
        pa.field('OPTION_FLAGS', pa.string()),
        pa.field('DATA_TYPE_INST_ID', pa.decimal128(16, 0)),
        pa.field('LOCK_BY', pa.string()),
        pa.field('LOCK_TS', pa.timestamp('ns')),
        pa.field('RETURN_IN_RESULTS', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })

    return target_schema
  
#['NTW_LEVEL_TYPE', 'PORT_OTHER_STATUS', 'EXCHANGE', 'SNO', 'EQUIPMENT_COMMENTS', 'VENDOR', 'MODEL', 'NTW_LOC_LONG', 'NEPS_KEY_ID', 'NTW_KEY_ID', 'SOURCE_SYSTEM', 'CREATE_DATE', 'NTW_ELEMENT_ID', 'NTW_CD', 'PORT_RESERVED', 'EQUP_LOCATION', 'LOCAL_DN', 'NTW_DESC', 'PORT_IN_SERVICE', 'BUILDING_NAME', 'EQUP_INDEX', 'NEPS_UTIL_ID', 'REGION_NAME', 'PORT_TOTAL', 'PORT_PENDING_ACTIVATION', 'UTIL_KEY_ID', 'NTW_LOC_LAT', 'PORT_AVAILABLE', 'PORT_FAULTY', 'RFSI_DATE', 'DETAILS_ADDRESS', 'PORT_PLANNED', 'NTW_ELEM_TYPE', 'RFSI_STATUS', 'EQUP_ADDRESS', 'IP_ADDRESS', 'EXTRACTION_TIMESTAMP'], 

'''
#prob with parquet
def get_target_schema_daa_oraforms_d_network_all_grn_p(column_names):        
    target_schema = pa.schema([
        pa.field('NTW_ELEMENT_ID', pa.decimal128(38, 0), metadata={"target_schema":"decimal128(16, 0)"}),
        pa.field('NTW_LEVEL_TYPE', pa.string()),
        pa.field('NTW_CD', pa.string(), metadata={"req": "sensitive"}),
        pa.field('NTW_DESC', pa.string(), metadata={"req": "sensitive"}),
        pa.field('NTW_LOC_LAT', pa.string(), metadata={"req":"sensitive", "target_schema":"float64()"}),
        pa.field('NTW_LOC_LONG', pa.string(), metadata={"req":"sensitive", "target_schema":"float64()"}),
        pa.field('NTW_KEY_ID', pa.decimal128(38, 0), metadata={"target_schema":"decimal128(16, 0)"}),
        pa.field('PORT_TOTAL', pa.decimal128(38, 0), metadata={"target_schema":"decimal128(6, 0)"}),
        pa.field('PORT_IN_SERVICE', pa.decimal128(38, 0), metadata={"target_schema":"decimal128(6, 0)"}),
        pa.field('PORT_AVAILABLE', pa.decimal128(38, 0), metadata={"target_schema":"decimal128(6, 0)"}),
        pa.field('PORT_RESERVED', pa.decimal128(38, 0), metadata={"target_schema":"decimal128(6, 0)"}),
        pa.field('PORT_PENDING_ACTIVATION', pa.decimal128(38, 0), metadata={"target_schema":"decimal128(6, 0)"}),
        pa.field('PORT_FAULTY', pa.decimal128(38, 0), metadata={"target_schema":"decimal128(6, 0)"}),
        pa.field('PORT_PLANNED', pa.decimal128(38, 0), metadata={"target_schema":"decimal128(6, 0)"}),
        pa.field('PORT_OTHER_STATUS', pa.decimal128(38, 0), metadata={"target_schema":"decimal128(6, 0)"}),
        pa.field('NTW_ELEM_TYPE', pa.string()),
        pa.field('EXCHANGE', pa.string(), metadata={"req": "sensitive"}),
        pa.field('SNO', pa.decimal128(38, 0), metadata={"target_schema":"decimal128(16, 0)"}),
        pa.field('RFSI_STATUS', pa.string()),
        pa.field('RFSI_DATE', pa.string(), metadata={"target_schema":"date32()"}),
        pa.field('EQUP_ADDRESS', pa.string(), metadata={"req": "sensitive"}),
        pa.field('BUILDING_NAME', pa.string(), metadata={"req": "sensitive"}),
        pa.field('DETAILS_ADDRESS', pa.string(), metadata={"req": "sensitive"}),
        pa.field('EQUIPMENT_COMMENTS', pa.string()),
        pa.field('EQUP_LOCATION', pa.string()),
        pa.field('EQUP_INDEX', pa.string()),
        pa.field('VENDOR', pa.string()),
        pa.field('MODEL', pa.string()),
        pa.field('IP_ADDRESS', pa.string(), metadata={"req": "sensitive"}),
        pa.field('SOURCE_SYSTEM', pa.string()),
        pa.field('NEPS_UTIL_ID', pa.decimal128(38, 0), metadata={"target_schema":"decimal128(16, 0)"}),
        pa.field('UTIL_KEY_ID', pa.decimal128(38, 0), metadata={"target_schema":"decimal128(16, 0)"}),
        pa.field('NEPS_KEY_ID', pa.decimal128(38, 0), metadata={"target_schema":"decimal128(16, 0)"}),
        pa.field('REGION_NAME', pa.string()),
        pa.field('LOCAL_DN', pa.decimal128(16, 0)),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })
    
    return target_schema
'''

def get_target_schema_daa_oraforms_d_network_all_nis_p(column_names):
    target_schema = pa.schema([
        pa.field('NTW_LEVEL_TYPE', pa.string()),
        pa.field('PORT_OTHER_STATUS', pa.decimal128(38, 0), metadata={"target_schema":"decimal128(6, 0)"}),
        pa.field('EXCHANGE', pa.string()),
        pa.field('SNO', pa.decimal128(16, 0)),
        pa.field('EQUIPMENT_COMMENTS', pa.string()),
        pa.field('VENDOR', pa.string()),
        pa.field('MODEL', pa.string()),
        pa.field('NTW_LOC_LONG', pa.string(), metadata={"req":"sensitive", "target_schema":"float64()"}),
        pa.field('NEPS_KEY_ID', pa.decimal128(16, 0)),
        pa.field('NTW_KEY_ID', pa.decimal128(16, 0)),
        pa.field('SOURCE_SYSTEM', pa.string()),
        pa.field('NTW_ELEMENT_ID', pa.decimal128(16, 0)),
        pa.field('NTW_CD', pa.string()),
        pa.field('PORT_RESERVED', pa.decimal128(38, 0), metadata={"target_schema":"decimal128(6, 0)"}),
        pa.field('EQUP_LOCATION', pa.string()),
        pa.field('LOCAL_DN', pa.decimal128(16, 0)),
        pa.field('CREATE_DATE', pa.timestamp('ns')),
        pa.field('NTW_DESC', pa.string(), metadata={"req":"sensitive"}),
        pa.field('PORT_IN_SERVICE', pa.decimal128(38, 0), metadata={"target_schema":"decimal128(6, 0)"}),
        pa.field('BUILDING_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('EQUP_INDEX', pa.string()),
        pa.field('NEPS_UTIL_ID', pa.decimal128(16, 0)),
        pa.field('REGION_NAME', pa.string()),
        pa.field('PORT_TOTAL', pa.decimal128(38, 0), metadata={"target_schema":"decimal128(6, 0)"}),
        pa.field('PORT_PENDING_ACTIVATION', pa.decimal128(38, 0), metadata={"target_schema":"decimal128(6, 0)"}),
        pa.field('UTIL_KEY_ID', pa.string()),
        pa.field('NTW_LOC_LAT', pa.string(), metadata={"req":"sensitive", "target_schema":"float64()"}),
        pa.field('PORT_AVAILABLE', pa.decimal128(38, 0), metadata={"target_schema":"decimal128(6, 0)"}),
        pa.field('PORT_FAULTY', pa.decimal128(38, 0), metadata={"target_schema":"decimal128(6, 0)"}),
        pa.field('RFSI_DATE', pa.string(), metadata={"target_schema":"date32()"}),
        pa.field('DETAILS_ADDRESS', pa.string(), metadata={"req":"sensitive"}),
        pa.field('PORT_PLANNED', pa.decimal128(38, 0), metadata={"target_schema":"decimal128(6, 0)"}),
        pa.field('NTW_ELEM_TYPE', pa.string()),
        pa.field('RFSI_STATUS', pa.string()), #dict
        pa.field('EQUP_ADDRESS', pa.string(), metadata={"req":"sensitive"}),
        pa.field('IP_ADDRESS', pa.string(), metadata={"req":"sensitive"}),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('ns')),
    ],
    metadata={
        "Classification": "Confidential"
    })

    return target_schema

def get_target_schema_daa_oraforms_d_network_view_p(column_names):        
    target_schema = pa.schema([
        pa.field('NTW_ELEMENT_ID', pa.decimal128(16, 0)),
        pa.field('NTW_LEVEL_TYPE', pa.string()),
        pa.field('NTW_CD', pa.string(), metadata={"req":"sensitive"}),
        pa.field('NTW_DESC', pa.string(), metadata={"req":"sensitive"}),
        pa.field('NTW_PARENT_LVL_ID', pa.decimal128(16, 0)),
        pa.field('NTW_OPCO_ID', pa.decimal128(16, 0)),
        pa.field('NTW_SITE_TYPE_ID', pa.decimal128(16, 0)),
        pa.field('NTW_LOC_LAT', pa.string(), metadata={"req":"sensitive", "target_schema":"float64()"}),
        pa.field('NTW_LOC_LONG', pa.string(), metadata={"req":"sensitive", "target_schema":"float64()"}),
        pa.field('NTW_TIER_ID', pa.decimal128(16, 0)),
        pa.field('NTW_KEY_ID', pa.decimal128(16, 0)),
        pa.field('PORT_TOTAL', pa.decimal128(16, 0)),
        pa.field('PORT_IN_SERVICE', pa.decimal128(16, 0)),
        pa.field('PORT_AVAILABLE', pa.decimal128(16, 0)),
        pa.field('PORT_RESERVED', pa.decimal128(16, 0)),
        pa.field('PORT_PENDING_ACTIVATION', pa.decimal128(16, 0)),
        pa.field('PORT_FAULTY', pa.decimal128(16, 0)),
        pa.field('PORT_PLANNED', pa.decimal128(16, 0)),
        pa.field('PORT_OTHER_STATUS', pa.decimal128(16, 0)),
        pa.field('PORT_TOTAL_B', pa.decimal128(16, 0)),
        pa.field('PORT_IN_SERVICE_B', pa.decimal128(16, 0)),
        pa.field('PORT_AVAILABLE_B', pa.decimal128(16, 0)),
        pa.field('PORT_RESERVED_B', pa.decimal128(16, 0)),
        pa.field('PORT_FAULTY_B', pa.decimal128(16, 0)),
        pa.field('PORT_PLANNED_B', pa.decimal128(16, 0)),
        pa.field('PORT_OTHER_STATUS_B', pa.decimal128(16, 0)),
        pa.field('NTW_ELEM_TYPE', pa.string()),
        pa.field('EXCHANGE_ID', pa.decimal128(16, 0)),
        pa.field('EXCHANGE', pa.string()),
        pa.field('SNO', pa.decimal128(16, 0)),
        pa.field('RFSI_STATUS', pa.string()),
        pa.field('RFSI_DATE', pa.string()),
        pa.field('EQUP_ADDRESS', pa.string(), metadata={"req":"sensitive"}),
        pa.field('BUILDING_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('DETAILS_ADDRESS', pa.string(), metadata={"req":"sensitive"}),
        pa.field('EQUIPMENT_COMMENTS', pa.string(), metadata={"req":"sensitive"}),
        pa.field('EQUP_LOCATION', pa.string(), metadata={"req":"sensitive"}),
        pa.field('EQUP_INDEX', pa.string()),
        pa.field('VENDOR', pa.string()),
        pa.field('MODEL', pa.string()),
        pa.field('IP_ADDRESS', pa.string(), metadata={"req":"sensitive"}),
        pa.field('SOURCE_TABLE', pa.string()),
        pa.field('SOURCE_SYSTEM', pa.string()),
        pa.field('CREATE_DATE', pa.timestamp('ns')),
        pa.field('UPDATE_DATE', pa.timestamp('ns')),
        pa.field('NEPS_UTIL_ID', pa.decimal128(16, 0)),
        pa.field('CO_LOCATION_IND', pa.decimal128(16, 0)),
        pa.field('CO_LOC_PARENT_ID', pa.decimal128(16, 0)),
        pa.field('UPDATED_BY', pa.string()),
        pa.field('LOAD_DATE', pa.timestamp('ns')),
        pa.field('LOAD_SRC', pa.string()),
        pa.field('LOAD_RUN_ID', pa.decimal128(16, 0)),
        pa.field('DELETE_IND', pa.decimal128(16, 0)),
        pa.field('UTIL_KEY_ID', pa.decimal128(16, 0)),
        pa.field('NEPS_KEY_ID', pa.decimal128(16, 0)),
        pa.field('STATE', pa.string()),
        pa.field('REGION_NAME', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
        metadata={
        "Classification": "Confidential"
    })

    return target_schema

#edwh
def get_target_schema_daa_oraforms_edwh_frame_route_p(column_names):        
    target_schema = pa.schema([
        pa.field('LEGID', pa.string()),
        pa.field('USERNAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('PASSWORD_FR', pa.string(), metadata={"req":"sensitive"}),
        pa.field('DOMAINNAME_FR', pa.string(), metadata={"req":"sensitive"}),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })
    
    return target_schema


def get_target_schema_daa_oraforms_edwh_ipvpn_full_p(column_names):        
    target_schema = pa.schema([
        pa.field('L3_CATEGORY', pa.string()),
        pa.field('RG', pa.string()),
        pa.field('RG_STATUS', pa.string()),
        pa.field('L3VPN', pa.string()),
        pa.field('SERVICE_STATUS', pa.string()),
        pa.field('BANDWIDTH', pa.string()),
        pa.field('CIRC_PATH_REV_NBR', pa.decimal128(6, 0)),
        pa.field('TECHNICAL_SLA_SLG', pa.string()),
        pa.field('CUSTOMER_SITE_ABBREVIATION', pa.string()),
        pa.field('LAYER2', pa.string()),
        pa.field('CONNECTION', pa.string(), metadata={"req":"sensitive"}),
        pa.field('CPE_SERVICE_INSTANCE_ID', pa.string()),
        pa.field('VENDOR', pa.string()),
        pa.field('MODELS', pa.string()),
        pa.field('PORT_ACCESS_ID', pa.string()),
        pa.field('ACCESS_NAME', pa.string()),
        pa.field('ACCESS_TYPE', pa.string()),
        pa.field('TYPE_ACC', pa.string()),
        pa.field('PE_INFO', pa.string()),
        pa.field('LAST_MOD_TS', pa.timestamp('ns')),
        pa.field('L3VPN_CCT_ID', pa.decimal128(16, 0)),
        pa.field('FRIENDLY_SITE_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })
    
    return target_schema


def get_target_schema_daa_oraforms_edwh_ipvpn_ip_full_p(column_names):        
    target_schema = pa.schema([
        pa.field('L3VPN_CCT_ID', pa.decimal128(16, 0)),
        pa.field('L3VPN_CCT_NAME', pa.string()),
        pa.field('IP_ID', pa.decimal128(16, 0)),
        pa.field('IP_ADDRESS', pa.string(), metadata={"req":"sensitive"}),
        pa.field('CIDR', pa.decimal128(16, 0)),
        pa.field('IP_NETWORK', pa.string()),
        pa.field('REGION', pa.string()),
        pa.field('USAGE', pa.string()),
        pa.field('IP_TYPE', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })

    return target_schema


def get_target_schema_daa_oraforms_edwh_ipvpn_p(column_names):        
    target_schema = pa.schema([
        pa.field('L3_CATEGORY', pa.string()),
        pa.field('RG', pa.string()),
        pa.field('L3VPN', pa.string()),
        pa.field('BANDWIDTH', pa.string()),
        pa.field('CIRC_PATH_REV_NBR', pa.decimal128(16, 0)),
        pa.field('TECHNICAL_SLA_SLG', pa.string()),
        pa.field('CUSTOMER_SITE_ABBREVIATION', pa.string()),
        pa.field('LAYER2', pa.string()),
        pa.field('CONNECTION', pa.string(), metadata={"req":"sensitive"}),
        pa.field('CPE_SERVICE_INSTANCE_ID', pa.string()),
        pa.field('VENDOR', pa.string()),
        pa.field('MODELS', pa.string()),
        pa.field('PORT_ACCESS_ID', pa.string()),
        pa.field('ACCESS_NAME', pa.string()),
        pa.field('ACCESS_TYPE', pa.string()),
        pa.field('TYPE_ACC', pa.string()),
        pa.field('PE_INFO', pa.string(), metadata={"req":"sensitive"}),
        pa.field('LAST_MOD_TS', pa.timestamp('ns')),
        pa.field('RG_STATUS', pa.string()),
        pa.field('SERVICE_STATUS', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
        metadata={
            "Classification": "Confidential"
    })
    return target_schema


def get_target_schema_daa_oraforms_edwh_me_customer_service_p(column_names):        
    target_schema = pa.schema([
        pa.field('PATH_ID', pa.string(), metadata={"req":"sensitive"}),
        pa.field('PRIMARY_NO', pa.string()),
        pa.field('SERVICE_STATUS', pa.string()),
        pa.field('PRIMARY_REVISION_NO', pa.string()),
        pa.field('EMS_SERVICE_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('BANDWIDTH', pa.string()),
        pa.field('REDUNDANCY_GROUP_ID', pa.string()),
        pa.field('PRIMARY_LEG_LEGACY_ID', pa.string()),
        pa.field('UPE_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('UPE_VENDOR', pa.string()),
        pa.field('UPE_MODEL', pa.string()),
        pa.field('UPE_IP_ADDRESS', pa.string(), metadata={"req":"sensitive"}),
        pa.field('UPE_CARD', pa.string()),
        pa.field('UPE_SLOT', pa.string()),
        pa.field('UPE_PORT', pa.string()),
        pa.field('UPE_PORT_STATUS', pa.string()),
        pa.field('SERVING_EXCHANGE', pa.string(), metadata={"req":"sensitive"}),
        pa.field('EPE_NPE_NAME', pa.string()),
        pa.field('EPE_NPE_VENDOR', pa.string()),
        pa.field('EPE_NPE_MODEL', pa.string()),
        pa.field('EPE_NPE_CARD', pa.string()),
        pa.field('EPE_NPE_SLOT', pa.string()),
        pa.field('EPE_NPE_PORT', pa.string()),
        pa.field('EPE_NPE_PORT_STATUS', pa.string()),
        pa.field('ROLE', pa.string()),
        pa.field('EPE_NPE_LAG_ID', pa.string()),
        pa.field('PRIMARY_LEG_ID', pa.string()),
        pa.field('SECONDARY_LEG_ID', pa.string()),
        pa.field('CUSTOMER_ABBREVIATION', pa.string()),
        pa.field('CUSTOMER_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('SERVICE_ID', pa.string()),
        pa.field('PRODUCT', pa.string()),
        pa.field('TECHNICAL_SLA_SLG', pa.string()),
        pa.field('UPE_PORT_ACCESS_ID', pa.string()),
        pa.field('EPE_NPE_PORT_ACCESS_ID', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })

    return target_schema


def get_target_schema_daa_oraforms_edwh_service_link_ftth_p(column_names):        
    target_schema = pa.schema([
        pa.field('ROW_NUM', pa.decimal128(16, 0)),
        pa.field('LOGIN_ID', pa.string(), metadata={"req":"sensitive"}),
        pa.field('SERVICE_NAME', pa.string()),
        pa.field('STATUS', pa.string()),
        pa.field('TYPE', pa.string()),
        pa.field('CUSTOMER_ID', pa.string()),
        pa.field('TOPOLOGY', pa.string()),
        pa.field('CIRC_PATH_INST_ID', pa.decimal128(16, 0)),
        pa.field('CIRC_PATH_HUM_ID', pa.string()),
        pa.field('A_SIDE_SITE_ID', pa.string()),
        pa.field('Z_SIDE_SITE_ID', pa.string()),
        pa.field('BANDWIDTH', pa.string()),
        pa.field('LAST_MOD_TS', pa.timestamp('ns')),
        pa.field('LAST_MOD_BY', pa.string(), metadata={"req":"sensitive"}),
        pa.field('ORDER_NUM', pa.string()),
        pa.field('EQOLT_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('SITEOLTID', pa.decimal128(16, 0)),
        pa.field('EQOLTID', pa.decimal128(16, 0)),
        pa.field('SITEFDC_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('SITEFDCID', pa.decimal128(16, 0)),
        pa.field('EQFDCID', pa.decimal128(16, 0)),
        pa.field('SITEDP_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('SITEDPID', pa.decimal128(16, 0)),
        pa.field('EQDPID', pa.decimal128(16, 0)),
        pa.field('SHELF', pa.string()),
        pa.field('SLOT', pa.string()),
        pa.field('SLOT_INST_ID', pa.decimal128(16, 0)),
        pa.field('PORT_OLT_NAME', pa.string()),
        pa.field('PORT_OLT_ID', pa.decimal128(16, 0)),
        pa.field('EQTYPE', pa.string()),
        pa.field('EQVENDOR', pa.string()),
        pa.field('HOUSENO', pa.string(), metadata={"req":"sensitive"}),
        pa.field('FLOOR', pa.string(), metadata={"req":"sensitive"}),
        pa.field('STREETTYPE', pa.string()),
        pa.field('STREETNAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('SECTION', pa.string()),
        pa.field('POSTCODE', pa.string()),
        pa.field('CITY', pa.string()),
        pa.field('STATE', pa.string()),
        pa.field('COUNTRY', pa.string()),
        pa.field('ONUPASS', pa.decimal128(16, 0)),
        pa.field('ONTID', pa.decimal128(16, 0)),
        pa.field('EQONUID', pa.decimal128(16, 0)),
        pa.field('PROVIDER_ATTR', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })

    return target_schema



def get_target_schema_daa_oraforms_edwh_service_link_vdsl_p(column_names):        
    target_schema = pa.schema([
        pa.field('ROW_NUM', pa.decimal128(16, 0)),
        pa.field('LOGIN_ID', pa.string()),
        pa.field('ORDER_NUM', pa.string()),
        pa.field('SERVICE_NAME', pa.string()),
        pa.field('STATUS', pa.string()),
        pa.field('TYPE', pa.string()),
        pa.field('SITEEQID', pa.decimal128(16, 0)),
        pa.field('SITEEQNAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('A_SIDE_SITE_ID', pa.string()),
        pa.field('Z_SIDE_SITE_ID', pa.string()),
        pa.field('BANDWIDTH', pa.string()),
        pa.field('CUSTOMER_ID', pa.string()),
        pa.field('TOPOLOGY', pa.string()),
        pa.field('CIRC_PATH_INST_ID', pa.decimal128(16, 0)),
        pa.field('CIRC_PATH_HUM_ID', pa.string()),
        pa.field('LAST_MOD_TS', pa.timestamp('ns')),
        pa.field('LAST_MOD_BY', pa.string()),
        pa.field('PARENT_EQ_INST_ID', pa.decimal128(16, 0)),
        pa.field('EQAMSANID', pa.decimal128(16, 0)),
        pa.field('EQAMSANNAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('EQSDFNAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('EQAMSANSHELF', pa.string()),
        pa.field('SLOT', pa.string()),
        pa.field('SLOT_INST_ID', pa.decimal128(16, 0)),
        pa.field('EPAMSANNAME', pa.string()),
        pa.field('EQTYPE', pa.string()),
        pa.field('EQVENDOR', pa.string()),
        pa.field('EPAAID', pa.decimal128(16, 0)),
        pa.field('HOUSENO', pa.string(), metadata={"req":"sensitive"}),
        pa.field('FLOOR', pa.string(), metadata={"req":"sensitive"}),
        pa.field('BUILDNO', pa.string(), metadata={"req":"sensitive"}),
        pa.field('STREETTYPE', pa.string()),
        pa.field('STREETNAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('SECTION', pa.string(), metadata={"req":"sensitive"}),
        pa.field('POSTCODE', pa.string()),
        pa.field('CITY', pa.string()),
        pa.field('STATE', pa.string()),
        pa.field('COUNTRY', pa.string()),
        pa.field('EQONUID', pa.decimal128(16, 0)),
        pa.field('PROVIDER_ATTR', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })
    
    return target_schema


def get_target_schema_daa_oraforms_edwh_utilize_ftth_p(column_names):        
    target_schema = pa.schema([
        pa.field('DP_SITE_INST_ID', pa.decimal128(16, 0)),
        pa.field('FDC_SITE_ADDRESS', pa.string(), metadata={"req":"sensitive"}),
        pa.field('DP_ID', pa.string(), metadata={"req":"sensitive"}),
        pa.field('RFSI_STATUS', pa.string()), #dict
        pa.field('RFSI_DATE', pa.string(), metadata={"target_schema":"date32()"}),
        pa.field('FDC_ID', pa.string(), metadata={"req":"sensitive"}),
        pa.field('EXCHANGE', pa.string(), metadata={"req":"sensitive"}),
        pa.field('PTT', pa.string()),
        pa.field('TYPE', pa.string()), #dict
        pa.field('PORT_WORKING_TOTAL_PORT', pa.decimal128(16, 0)),
        pa.field('PORT_IN_SERVICE', pa.decimal128(16, 0)),
        pa.field('PORT_AVAILABLE', pa.decimal128(16, 0)),
        pa.field('PORT_RESERVED', pa.decimal128(16, 0)),
        pa.field('PENDING_ACTIVATION', pa.decimal128(16, 0)),
        pa.field('OTHER_PORT_STATUS', pa.decimal128(16, 0)),
        pa.field('DP_ADDRESS', pa.string(), metadata={"req":"sensitive"}),
        pa.field('EQUIPMENT_LOCATION', pa.string()),
        pa.field('BUILDING_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('PORT_PLANNED', pa.decimal128(16, 0)),
        pa.field('DESIGN_TAGGING', pa.string()),
        pa.field('PROJECT_TAGGING', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })

    return target_schema


def get_target_schema_daa_oraforms_edwh_utilize_vdsl_p(column_names):        
    target_schema = pa.schema([
        pa.field('SITE_ADDRESS', pa.string(), metadata={"req":"sensitive"}),
        pa.field('BUILDING_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('MSAN_SITE_INST_ID', pa.decimal128(16, 0)),
        pa.field('MSAN_ID', pa.string(), metadata={"req":"sensitive"}),
        pa.field('VENDOR', pa.string()),
        pa.field('MODEL', pa.string()),
        pa.field('RFSI_STATUS', pa.string()),
        pa.field('RFSI_DATE', pa.string()),
        pa.field('EXCHANGE', pa.string(), metadata={"req":"sensitive"}),
        pa.field('PTT', pa.string()),
        pa.field('TYPE', pa.string()),
        pa.field('PORT_WORKING_TOTAL_PORT', pa.decimal128(16, 0)),
        pa.field('PORT_IN_SERVICE', pa.decimal128(16, 0)),
        pa.field('PORT_AVAILABLE', pa.decimal128(16, 0)),
        pa.field('PORT_RESERVED', pa.decimal128(16, 0)),
        pa.field('PENDING_ACTIVATION', pa.decimal128(16, 0)),
        pa.field('OTHER_PORT_STATUS', pa.decimal128(16, 0)),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })
    
    return target_schema

#full_service

def get_target_schema_daa_oraforms_full_service_link_ftth_daily_p(column_names):        
    target_schema = pa.schema([
        pa.field('ROW_NUM', pa.decimal128(16, 0)),
        pa.field('LOGIN_ID', pa.string(), metadata={"req":"sensitive"}),
        pa.field('SERVICE_NAME', pa.string()),
        pa.field('SERVICE_TYPE', pa.string()),
        pa.field('STATUS', pa.string()),
        pa.field('TYPE_CP', pa.string()),
        pa.field('CUSTOMER_ID', pa.string()),
        pa.field('TOPOLOGY', pa.string()),
        pa.field('CIRC_PATH_INST_ID', pa.decimal128(16, 0)),
        pa.field('CIRC_PATH_HUM_ID', pa.string()),
        pa.field('A_SIDE_SITE_ID', pa.decimal128(16, 0)),
        pa.field('Z_SIDE_SITE_ID', pa.decimal128(16, 0)),
        pa.field('BANDWIDTH', pa.string()),
        pa.field('LAST_MOD_TS', pa.timestamp('ns')),
        pa.field('LAST_MOD_BY', pa.string(), metadata={"req":"sensitive"}),
        pa.field('ORDER_NUM', pa.string()),
        pa.field('EQOLT_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('SITEOLTID', pa.decimal128(16, 0)),
        pa.field('EQOLTID', pa.decimal128(16, 0)),
        pa.field('SITEFDC_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('SITEFDCID', pa.decimal128(16, 0)),
        pa.field('EQFDCID', pa.decimal128(16, 0)),
        pa.field('SITEDP_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('SITEDPID', pa.decimal128(16, 0)),
        pa.field('EQDPID', pa.decimal128(16, 0)),
        pa.field('SHELF', pa.string()),
        pa.field('SLOT', pa.string()),
        pa.field('SLOT_INST_ID', pa.decimal128(16, 0)),
        pa.field('PORT_OLT_NAME', pa.string()),
        pa.field('PORT_OLT_ID', pa.decimal128(16, 0)),
        pa.field('EQTYPE', pa.string()),
        pa.field('EQVENDOR', pa.string()),
        pa.field('HOUSENO', pa.string(), metadata={"req":"sensitive"}),
        pa.field('FLOOR', pa.string(), metadata={"req":"sensitive"}),
        pa.field('STREETTYPE', pa.string()),
        pa.field('STREETNAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('SECTION', pa.string()),
        pa.field('POSTCODE', pa.string()),
        pa.field('CITY', pa.string()),
        pa.field('STATE', pa.string()),
        pa.field('COUNTRY', pa.string()),
        pa.field('ONUPASS', pa.string()),
        pa.field('ONTID', pa.decimal128(16, 0)),
        pa.field('PORTDPID', pa.decimal128(16, 0)),
        pa.field('IP_DEVICE', pa.string(), metadata={"req":"sensitive"}),
        pa.field('PORT_BTU', pa.string()),
        pa.field('VLAN', pa.string()),
        pa.field('BTU_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('BUILDNAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('EQONUID', pa.decimal128(16, 0)),
        pa.field('PROVIDER_ATTR', pa.string()),
        pa.field('ACTUAL_DP_PORT', pa.string()),
        pa.field('PORT_STATUS', pa.string()),
        pa.field('EXTRA_PORT_FLAG', pa.string()),
        pa.field('ADD_POLE_FLAG', pa.string()),
        pa.field('SPLITTER_FLAG', pa.string()),
        pa.field('PTT', pa.string()),
        pa.field('EXCHANGE', pa.string(), metadata={"req":"sensitive"}),
        pa.field('SOURCE_SYSTEM', pa.string()),
        pa.field('GEN_DATE', pa.timestamp('ns')),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })
    
    return target_schema


def get_target_schema_daa_oraforms_full_service_link_ftth_new_p(column_names):        
    target_schema = pa.schema([
        pa.field('ROW_NUM', pa.decimal128(16, 0)),
        pa.field('LOGIN_ID', pa.string(), metadata={"req":"sensitive"}),
        pa.field('SERVICE_NAME', pa.string()),
        pa.field('SERVICE_TYPE', pa.string()),
        pa.field('STATUS', pa.string()),
        pa.field('TYPE_CP', pa.string()),
        pa.field('CUSTOMER_ID', pa.string()),
        pa.field('TOPOLOGY', pa.string()),
        pa.field('CIRC_PATH_INST_ID', pa.decimal128(16, 0)),
        pa.field('CIRC_PATH_HUM_ID', pa.string()),
        pa.field('A_SIDE_SITE_ID', pa.decimal128(16, 0)),
        pa.field('Z_SIDE_SITE_ID', pa.decimal128(16, 0)),
        pa.field('BANDWIDTH', pa.string()),
        pa.field('LAST_MOD_TS', pa.timestamp('ns')),
        pa.field('LAST_MOD_BY', pa.string(), metadata={"req":"sensitive"}),
        pa.field('ORDER_NUM', pa.string()),
        pa.field('EQOLT_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('SITEOLTID', pa.decimal128(16, 0)),
        pa.field('EQOLTID', pa.decimal128(16, 0)),
        pa.field('SITEFDC_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('SITEFDCID', pa.decimal128(16, 0)),
        pa.field('EQFDCID', pa.decimal128(16, 0)),
        pa.field('SITEDP_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('SITEDPID', pa.decimal128(16, 0)),
        pa.field('EQDPID', pa.decimal128(16, 0)),
        pa.field('SHELF', pa.string()),
        pa.field('SLOT', pa.string()),
        pa.field('SLOT_INST_ID', pa.decimal128(16, 0)),
        pa.field('PORT_OLT_NAME', pa.string()),
        pa.field('PORT_OLT_ID', pa.decimal128(16, 0)),
        pa.field('EQTYPE', pa.string()),
        pa.field('EQVENDOR', pa.string()),
        pa.field('HOUSENO', pa.string(), metadata={"req":"sensitive"}),
        pa.field('FLOOR', pa.string(), metadata={"req":"sensitive"}),
        pa.field('STREETTYPE', pa.string()),
        pa.field('STREETNAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('SECTION', pa.string(), metadata={"req":"sensitive"}),
        pa.field('POSTCODE', pa.string()),
        pa.field('CITY', pa.string()),
        pa.field('STATE', pa.string()),
        pa.field('COUNTRY', pa.string()),
        pa.field('ONUPASS', pa.string()),
        pa.field('ONTID', pa.string()),
        pa.field('PORTDPID', pa.decimal128(16, 0)),
        pa.field('IP_DEVICE', pa.string(), metadata={"req":"sensitive"}),
        pa.field('PORT_BTU', pa.string()),
        pa.field('VLAN', pa.string()),
        pa.field('BTU_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('BUILDNAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })
    
    return target_schema



def get_target_schema_daa_oraforms_full_service_link_ftth_p(column_names):
    target_schema = pa.schema([
        pa.field('ROW_NUM', pa.decimal128(16, 0)),
        pa.field('LOGIN_ID', pa.string(), metadata={"req":"sensitive"}),
        pa.field('SERVICE_NAME', pa.string()),
        pa.field('SERVICE_TYPE', pa.string()),
        pa.field('STATUS', pa.string()),
        pa.field('TYPE_CP', pa.string()),
        pa.field('CUSTOMER_ID', pa.string()),
        pa.field('TOPOLOGY', pa.string()),
        pa.field('CIRC_PATH_INST_ID', pa.decimal128(16, 0)),
        pa.field('CIRC_PATH_HUM_ID', pa.string()),
        pa.field('A_SIDE_SITE_ID', pa.decimal128(16, 0)),
        pa.field('Z_SIDE_SITE_ID', pa.decimal128(16, 0)),
        pa.field('BANDWIDTH', pa.string()),
        pa.field('LAST_MOD_TS', pa.timestamp('ns')),
        pa.field('LAST_MOD_BY', pa.string(), metadata={"req":"sensitive"}),
        pa.field('ORDER_NUM', pa.string()),
        pa.field('EQOLT_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('SITEOLTID', pa.decimal128(16, 0)),
        pa.field('EQOLTID', pa.decimal128(16, 0)),
        pa.field('SITEFDC_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('SITEFDCID', pa.decimal128(16, 0)),
        pa.field('EQFDCID', pa.decimal128(16, 0)),
        pa.field('SITEDP_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('SITEDPID', pa.decimal128(16, 0)),
        pa.field('EQDPID', pa.decimal128(16, 0)),
        pa.field('SHELF', pa.string()),
        pa.field('SLOT', pa.string()),
        pa.field('SLOT_INST_ID', pa.decimal128(16, 0)),
        pa.field('PORT_OLT_NAME', pa.string()),
        pa.field('PORT_OLT_ID', pa.decimal128(16, 0)),
        pa.field('EQTYPE', pa.string()),
        pa.field('EQVENDOR', pa.string()),
        pa.field('HOUSENO', pa.string(), metadata={"req":"sensitive"}),
        pa.field('FLOOR', pa.string(), metadata={"req":"sensitive"}),
        pa.field('STREETTYPE', pa.string()),
        pa.field('STREETNAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('SECTION', pa.string(), metadata={"req":"sensitive"}),
        pa.field('POSTCODE', pa.string()),
        pa.field('CITY', pa.string()),
        pa.field('STATE', pa.string()),
        pa.field('COUNTRY', pa.string()),
        pa.field('ONUPASS', pa.string()),
        pa.field('ONTID', pa.decimal128(16, 0)),
        pa.field('PORTDPID', pa.decimal128(16, 0)),
        pa.field('IP_DEVICE', pa.string(), metadata={"req":"sensitive"}),
        pa.field('PORT_BTU', pa.string()),
        pa.field('VLAN', pa.string()),
        pa.field('BTU_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('BUILDNAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('EQONUID', pa.decimal128(16, 0)),
        pa.field('PROVIDER_ATTR', pa.string()),
        pa.field('ACTUAL_DP_PORT', pa.string()),
        pa.field('PORT_STATUS', pa.string()),
        pa.field('EXTRA_PORT_FLAG', pa.string()),
        pa.field('ADD_POLE_FLAG', pa.string()),
        pa.field('SPLITTER_FLAG', pa.string()),
        pa.field('PTT', pa.string()),
        pa.field('EXCHANGE', pa.string(), metadata={"req":"sensitive"}),
        pa.field('SOURCE_SYSTEM', pa.string()),
        pa.field('GEN_DATE', pa.timestamp('ns')),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })

    return target_schema



def get_target_schema_daa_oraforms_full_service_link_vdsl_daily_p(column_names):        
    target_schema = pa.schema([
        pa.field('ROW_NUM', pa.decimal128(16, 0)),
        pa.field('LOGIN_ID', pa.string()),
        pa.field('ORDER_NUM', pa.string()),
        pa.field('SERVICE_NAME', pa.string()),
        pa.field('SERVICE_TYPE', pa.string()),
        pa.field('STATUS', pa.string()),
        pa.field('TYPECP', pa.string()),
        pa.field('SITEEQID', pa.decimal128(16, 0)),
        pa.field('SITEEQNAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('A_SIDE_SITE_ID', pa.decimal128(16, 0)),
        pa.field('Z_SIDE_SITE_ID', pa.decimal128(16, 0)),
        pa.field('BANDWIDTH', pa.string()),
        pa.field('CUSTOMER_ID', pa.string()),
        pa.field('TOPOLOGY', pa.string()),
        pa.field('CIRC_PATH_INST_ID', pa.decimal128(16, 0)),
        pa.field('CIRC_PATH_HUM_ID', pa.string()),
        pa.field('LAST_MOD_TS', pa.timestamp('ns')),
        pa.field('LAST_MOD_BY', pa.string(), metadata={"req":"sensitive"}),
        pa.field('PARENT_EQ_INST_ID', pa.decimal128(16, 0)),
        pa.field('EQAMSANID', pa.decimal128(16, 0)),
        pa.field('EQAMSANNAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('EQSDFNAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('EQAMSANSHELF', pa.string()),
        pa.field('SLOT', pa.string()),
        pa.field('SLOT_INST_ID', pa.decimal128(16, 0)),
        pa.field('EPAMSANNAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('EQTYPE', pa.string()),
        pa.field('EQVENDOR', pa.string()),
        pa.field('EPAAID', pa.decimal128(16, 0)),
        pa.field('HOUSENO', pa.string(), metadata={"req":"sensitive"}),
        pa.field('FLOOR', pa.string(), metadata={"req":"sensitive"}),
        pa.field('BUILDNO', pa.string(), metadata={"req":"sensitive"}),
        pa.field('STREETTYPE', pa.string()),
        pa.field('STREETNAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('SECTION', pa.string(), metadata={"req":"sensitive"}),
        pa.field('POSTCODE', pa.string()),
        pa.field('CITY', pa.string()),
        pa.field('STATE', pa.string()),
        pa.field('COUNTRY', pa.string()),
        pa.field('PORTSDFID', pa.decimal128(16, 0)),
        pa.field('IP_DEVICE', pa.string(), metadata={"req":"sensitive"}),
        pa.field('PORT_BTU', pa.string()),
        pa.field('VLAN', pa.string()),
        pa.field('BTU_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('EQONUID', pa.decimal128(16, 0)),
        pa.field('PROVIDER_ATTR', pa.string()),
        pa.field('ACTUAL_DP_PORT', pa.string()),
        pa.field('PORT_STATUS', pa.string()),
        pa.field('EXTRA_PORT_FLAG', pa.string()),
        pa.field('ADD_POLE_FLAG', pa.string()),
        pa.field('SPLITTER_FLAG', pa.string()),
        pa.field('PTT', pa.string()),
        pa.field('EXCHANGE', pa.string(), metadata={"req":"sensitive"}),
        pa.field('SOURCE_SYSTEM', pa.string()),
        pa.field('GEN_DATE', pa.timestamp('ns')),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })

    return target_schema


def get_target_schema_daa_oraforms_full_service_link_vdsl_p(column_names):        
    target_schema = pa.schema([
        pa.field('ROW_NUM', pa.decimal128(16, 0)),
        pa.field('LOGIN_ID', pa.string(), metadata={"req":"sensitive"}),
        pa.field('ORDER_NUM', pa.string()),
        pa.field('SERVICE_NAME', pa.string()),
        pa.field('SERVICE_TYPE', pa.string()),
        pa.field('STATUS', pa.string()),
        pa.field('TYPECP', pa.string()),
        pa.field('SITEEQID', pa.decimal128(16, 0)),
        pa.field('SITEEQNAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('A_SIDE_SITE_ID', pa.decimal128(16, 0)),
        pa.field('Z_SIDE_SITE_ID', pa.decimal128(16, 0)),
        pa.field('BANDWIDTH', pa.string()),
        pa.field('CUSTOMER_ID', pa.string()),
        pa.field('TOPOLOGY', pa.string()),
        pa.field('CIRC_PATH_INST_ID', pa.decimal128(16, 0)),
        pa.field('CIRC_PATH_HUM_ID', pa.string()),
        pa.field('LAST_MOD_TS', pa.timestamp('ns')),
        pa.field('LAST_MOD_BY', pa.string()),
        pa.field('PARENT_EQ_INST_ID', pa.decimal128(16, 0)),
        pa.field('EQAMSANID', pa.decimal128(16, 0)),
        pa.field('EQAMSANNAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('EQSDFNAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('EQAMSANSHELF', pa.string()),
        pa.field('SLOT', pa.string()),
        pa.field('SLOT_INST_ID', pa.decimal128(16, 0)),
        pa.field('EPAMSANNAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('EQTYPE', pa.string()),
        pa.field('EQVENDOR', pa.string()),
        pa.field('EPAAID', pa.decimal128(16, 0)),
        pa.field('HOUSENO', pa.string(), metadata={"req":"sensitive"}),
        pa.field('FLOOR', pa.string()),
        pa.field('BUILDNO', pa.string(), metadata={"req":"sensitive"}),
        pa.field('STREETTYPE', pa.string()),
        pa.field('STREETNAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('SECTION', pa.string(), metadata={"req":"sensitive"}),
        pa.field('POSTCODE', pa.string()),
        pa.field('CITY', pa.string()),
        pa.field('STATE', pa.string()),
        pa.field('COUNTRY', pa.string()),
        pa.field('PORTSDFID', pa.decimal128(16, 0)),
        pa.field('IP_DEVICE', pa.string(), metadata={"req":"sensitive"}),
        pa.field('PORT_BTU', pa.string()),
        pa.field('VLAN', pa.string()),
        pa.field('BTU_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('EQONUID', pa.decimal128(16, 0)),
        pa.field('PROVIDER_ATTR', pa.string()),
        pa.field('ACTUAL_DP_PORT', pa.string()),
        pa.field('PORT_STATUS', pa.string()),
        pa.field('EXTRA_PORT_FLAG', pa.string()),
        pa.field('ADD_POLE_FLAG', pa.string()),
        pa.field('SPLITTER_FLAG', pa.string()),
        pa.field('PTT', pa.string()),
        pa.field('EXCHANGE', pa.string(), metadata={"req":"sensitive"}),
        pa.field('SOURCE_SYSTEM', pa.string()),
        pa.field('GEN_DATE', pa.timestamp('ns')),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })
    return target_schema



def get_target_schema_daa_oraforms_p1_ib_order_list_p(column_names):        
    target_schema = pa.schema([
        pa.field('STATE', pa.string()),
        pa.field('SITE_ID', pa.string(), metadata={"req":"sensitive"}),
        pa.field('SITE_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('LV_ID', pa.string()),
        pa.field('ORDER_ID', pa.string()),
        pa.field('LATITUDE', pa.string(), metadata={"req":"sensitive"}),
        pa.field('LONGITUDE', pa.string(), metadata={"req":"sensitive"}),
        pa.field('ENODEB_CONTAINER_TEMPLATE', pa.string()),
        pa.field('IUC_EQUIP_ID', pa.decimal128(16, 0)),
        pa.field('THE_IB_ID', pa.decimal128(16, 0)),
        pa.field('CLUSTER_NAME', pa.string()),
        pa.field('INSTALL_ADDRESS', pa.string(), metadata={"req":"sensitive"}),
        pa.field('IP_ADDRESS', pa.string(), metadata={"req":"sensitive"}),
        pa.field('VENDOR', pa.string()),
        pa.field('MGMT_TYPE', pa.string()),
        pa.field('EQUIP_TYPE', pa.string()),
        pa.field('STRUCTURE_TYPE', pa.string()),
        pa.field('TOWER_TYPE', pa.string()),
        pa.field('SITE_OWNER', pa.string()),
        pa.field('CONTACT_NO', pa.string(), metadata={"req":"sensitive"}),
        pa.field('ACCESS_AVAILABILITY', pa.string()),
        pa.field('OWNER_INSTRUCTION', pa.string()),
        pa.field('THE_REMARKS', pa.string(), metadata={"req":"sensitive"}),
        pa.field('PROJECT_TYPE', pa.string()),
        pa.field('SERO_ID', pa.string()),
        pa.field('SERO_SERV_ID', pa.string()),
        pa.field('GE_AGGREGATOR_ID', pa.string()),
        pa.field('ENODEB_ID', pa.string()),
        pa.field('ENODEB_PORT', pa.string()),
        pa.field('SERVICE_IP', pa.string(), metadata={"req":"sensitive"}),
        pa.field('ONM_IP', pa.string(), metadata={"req":"sensitive"}),
        pa.field('CABLE_INFO', pa.string()),
        pa.field('PROPERTY_TYPE', pa.string()),
        pa.field('TYPE_OF_ACCESS', pa.string()),
        pa.field('LL_SCP_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('CATLADDER', pa.string()),
        pa.field('NIS_BEARER_ID', pa.string(), metadata={"req":"sensitive"}),
        pa.field('NIS_CCT_ID', pa.string()),
        pa.field('TYPE_OF_SAFETY_ISSUE', pa.string()),
        pa.field('WORK_AT_GROUND_DURING_NIGHT', pa.string()),
        pa.field('TYPE_OF_ACCESS_KEY_MGMT', pa.string()),
        pa.field('CONTACT_PERSON', pa.string()),
        pa.field('WORK_AT_HEIGHT_DURING_NIGHT', pa.string()),
        pa.field('IUC_SERIAL_NO', pa.string()),
        pa.field('SOFTWARE_VERSION', pa.string()),
        pa.field('BDI_VLAN', pa.string()),
        pa.field('BANDWIDTH_DATA', pa.string()),
        pa.field('BANDWIDTH_ONM', pa.string()),
        pa.field('BANDWIDTH_WILL', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })
    
    return target_schema


#tm
def get_target_schema_daa_oraforms_tm_cubb_address_tab_p(column_names):        
    target_schema = pa.schema([
        pa.field('ORDER_ADDE_ID', pa.string()),
        pa.field('PROJ_TYPE2', pa.string()),
        pa.field('SITE_HUM_ID', pa.string(), metadata={"req":"sensitive"}),
        pa.field('DP_STATUS', pa.string()),
        pa.field('SITE_INST_ID', pa.decimal128(16, 0)),
        pa.field('STATE', pa.string()),
        pa.field('PREMISE_TYPE', pa.string()),
        pa.field('NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('PROJECT_TYPE', pa.string()),
        pa.field('PORT_HUM_ID', pa.string()),
        pa.field('RESOURCE_INST_ID', pa.decimal128(16, 0)),
        pa.field('SI_STATUS', pa.string()),
        pa.field('TYPE', pa.string()),
        pa.field('STREET_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('CITY', pa.string()),
        pa.field('PORT_STATUS', pa.string()),
        pa.field('CCT_ID', pa.decimal128(16, 0)),
        pa.field('ORDER_LIST', pa.string()),
        pa.field('DESCR', pa.string(), metadata={"req":"sensitive"}),
        pa.field('BUILDING_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('POSTCODE', pa.string()),
        pa.field('PHONE_NO', pa.string(), metadata={"req":"sensitive"}),
        pa.field('LAST_MOD_BY', pa.string(), metadata={"req":"sensitive"}),
        pa.field('SERVICE_CATEGORY', pa.string()),
        pa.field('STREET_TYPE', pa.string()),
        pa.field('PORT_DESCRIPTION', pa.string()),
        pa.field('P_LAST_MODIFY_TS', pa.timestamp('ns')),
        pa.field('DP_ACTUAL_NAME', pa.string()),
        pa.field('EXCHANGE_CODE', pa.string(), metadata={"req":"sensitive"}),
        pa.field('SECTION', pa.string(), metadata={"req":"sensitive"}),
        pa.field('HYBRID', pa.string()),
        pa.field('RI_STATUS', pa.string()),
        pa.field('EQUIP_INST_ID', pa.decimal128(16, 0)),
        pa.field('COUNTRY', pa.string()),
        pa.field('UPDATE_REMARKS', pa.string()),
        pa.field('STATE_QUERY', pa.string()),
        pa.field('PORT_INST_ID', pa.decimal128(16, 0)),
        pa.field('LAST_MOD_TS', pa.timestamp('ns')),
        pa.field('HOUSE_UNIT_LOT', pa.string(), metadata={"req":"sensitive"}),
        pa.field('FLOOR_NUMBER', pa.string(), metadata={"req":"sensitive"}),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })

    return target_schema


def get_target_schema_daa_oraforms_tm_cubb_address_tab_view_p(column_names):        
    target_schema = pa.schema([
        pa.field('DP_STATUS', pa.string()),
        pa.field('ORDER_ADDE_ID', pa.string()),
        pa.field('NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('STATE', pa.string()),
        pa.field('PREMISE_TYPE', pa.string()),
        pa.field('PROJECT_TYPE', pa.string()),
        pa.field('RESOURCE_INST_ID', pa.decimal128(16, 0)),
        pa.field('SI_STATUS', pa.string()),
        pa.field('TYPE', pa.string()),
        pa.field('PORT_HUM_ID', pa.string()),
        pa.field('DESCR', pa.string(), metadata={"req":"sensitive"}),
        pa.field('STREET_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('CITY', pa.string()),
        pa.field('PORT_STATUS', pa.string()),
        pa.field('CCT_ID', pa.decimal128(16, 0)),
        pa.field('ORDER_LIST', pa.string()),
        pa.field('SERVICE_CATEGORY', pa.string()),
        pa.field('BUILDING_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('POSTCODE', pa.string()),
        pa.field('PHONE_NO', pa.string(), metadata={"req":"sensitive"}),
        pa.field('EXCHANGE_CODE', pa.string()),
        pa.field('STREET_TYPE', pa.string()),
        pa.field('PORT_DESCRIPTION', pa.string()),
        pa.field('DP_ACTUAL_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('RI_STATUS', pa.string()),
        pa.field('EQUIP_INST_ID', pa.decimal128(16, 0)),
        pa.field('SECTION', pa.string(), metadata={"req":"sensitive"}),
        pa.field('HOUSE_UNIT_LOT', pa.string(), metadata={"req":"sensitive"}),
        pa.field('FLOOR_NUMBER', pa.string(), metadata={"req":"sensitive"}),
        pa.field('COUNTRY', pa.string()),
        pa.field('UPDATE_REMARKS', pa.string(), metadata={"req":"sensitive"}),
        pa.field('STATE_QUERY', pa.string()),
        pa.field('PORT_INST_ID', pa.decimal128(16, 0)),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })

    return target_schema

def get_target_schema_daa_oraforms_tm_hsbb_hsba_onu_dp_daily_tab_p(column_names):
    target_schema = pa.schema([
        pa.field('BEARER_CCT_ID', pa.decimal128(16, 0)),
        pa.field('BEARER_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('DP_PORT_ID', pa.decimal128(16, 0)),
        pa.field('DP_PORT_NAME', pa.string()),
        pa.field('DP_PORT_STATUS', pa.string()),
        pa.field('DP_EQUIP_ID', pa.decimal128(16, 0)),
        pa.field('DP_SITE_ID', pa.decimal128(16, 0)),
        pa.field('FTB_PORT_ID', pa.decimal128(16, 0)),
        pa.field('ONU_EQUIP_ID', pa.decimal128(16, 0)),
        pa.field('ONU_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('ONU_TYPE', pa.string()),
        pa.field('ONU_SITE_ID', pa.decimal128(16, 0)),
        pa.field('ONT_ID', pa.decimal128(16, 0)),
        pa.field('ONU_PASSWORD', pa.string()),
        pa.field('FDC_ID', pa.decimal128(16, 0)),
        pa.field('FDC_NAME', pa.string()),
        pa.field('FDC_SITE_ID', pa.decimal128(16, 0)),
        pa.field('FDC_PORT_ID', pa.decimal128(16, 0)),
        pa.field('PROVIDER_ATTR', pa.string()),
        pa.field('OCI_NUMBER', pa.string()),
        pa.field('TROIKA_ID', pa.string()),
        pa.field('GEN_DATE', pa.timestamp('ns')),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })

    return target_schema


#daa_oraforms_tm_hsbb_hsba_onu_dp_tab_p  
def get_target_schema_daa_oraforms_tm_hsbb_hsba_onu_dp_tab_p(column_names):
    target_schema = pa.schema([
        pa.field('BEARER_CCT_ID', pa.decimal128(16, 0)),
        pa.field('BEARER_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('DP_PORT_ID', pa.decimal128(16, 0)),
        pa.field('DP_PORT_NAME', pa.string()),
        pa.field('DP_PORT_STATUS', pa.string()),
        pa.field('DP_EQUIP_ID', pa.decimal128(16, 0)),
        pa.field('DP_SITE_ID', pa.decimal128(16, 0)),
        pa.field('FTB_PORT_ID', pa.decimal128(16, 0)),
        pa.field('ONU_EQUIP_ID', pa.decimal128(16, 0)),
        pa.field('ONU_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('ONU_TYPE', pa.string()),
        pa.field('ONU_SITE_ID', pa.decimal128(16, 0)),
        pa.field('ONT_ID', pa.decimal128(16, 0)),
        pa.field('ONU_PASSWORD', pa.string()),
        pa.field('FDC_ID', pa.decimal128(16, 0)),
        pa.field('FDC_NAME', pa.string()),
        pa.field('FDC_SITE_ID', pa.decimal128(16, 0)),
        pa.field('FDC_PORT_ID', pa.decimal128(16, 0)),
        pa.field('PROVIDER_ATTR', pa.string()),
        pa.field('OCI_NUMBER', pa.string()),
        pa.field('TROIKA_ID', pa.string()),
        pa.field('GEN_DATE', pa.timestamp('ns')),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))

    ],
    metadata={
        "Classification": "Confidential"
    })

    return target_schema


def get_target_schema_daa_oraforms_tm_hsbb_hsba_serv_daily_tab_p(column_names):        
    target_schema = pa.schema([
        pa.field('RI_ID', pa.decimal128(16, 0)),
        pa.field('RI_NAME', pa.string()),
        pa.field('RI_STATUS', pa.string()),
        pa.field('RI_MOD_DATE', pa.timestamp('ns')),
        pa.field('RI_MOD_BY', pa.string(), metadata={"req":"sensitive"}),
        pa.field('RI_TYPE', pa.string()),
        pa.field('SERV_TYPE', pa.string()),
        pa.field('PATH_ID', pa.decimal128(16, 0)),
        pa.field('PATH_NAME', pa.string()),
        pa.field('PATH_BW', pa.string()),
        pa.field('USER_FRIENDLY_ID', pa.string(), metadata={"req":"sensitive"}),
        pa.field('OLT_ID', pa.string(), metadata={"req":"sensitive"}),
        pa.field('OLT_MSAN_TYPE', pa.string()),
        pa.field('OLT_IP_ADDRESS', pa.string(), metadata={"req":"sensitive"}),
        pa.field('OLT_EQUIP_ID', pa.decimal128(16, 0)),
        pa.field('OLT_PORT', pa.decimal128(16, 0)),
        pa.field('OLT_SHELF', pa.string()),
        pa.field('OLT_SLOT', pa.string()),
        pa.field('OLT_PORT_NAME', pa.string()),
        pa.field('OLT_SITE_ID', pa.decimal128(16, 0)),
        pa.field('OLT_VLAN', pa.string()),
        pa.field('EXC_CODE', pa.string(), metadata={"req":"sensitive"}),
        pa.field('ONU_EQUIP_ID', pa.decimal128(16, 0)),
        pa.field('ONU_SITE_ID', pa.decimal128(16, 0)),
        pa.field('A_SIDE_SITE_ID', pa.decimal128(16, 0)),
        pa.field('Z_SIDE_SITE_ID', pa.decimal128(16, 0)),
        pa.field('ORDER_ID', pa.string()),
        pa.field('PORT_BTU', pa.string()),
        pa.field('ADDRESS_ID', pa.decimal128(16, 0)),
        pa.field('GEN_DATE', pa.timestamp('ns')),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })

    return target_schema



def get_target_schema_daa_oraforms_tm_hsbb_hsba_serv_tab_p(column_names):        
    target_schema = pa.schema([
        pa.field('RI_ID', pa.decimal128(16, 0)),
        pa.field('RI_NAME', pa.string()),
        pa.field('RI_STATUS', pa.string()),
        pa.field('RI_MOD_DATE', pa.timestamp('ns')),
        pa.field('RI_MOD_BY', pa.string(), metadata={"req":"sensitive"}),
        pa.field('RI_TYPE', pa.string()),
        pa.field('SERV_TYPE', pa.string()),
        pa.field('PATH_ID', pa.decimal128(16, 0)),
        pa.field('PATH_NAME', pa.string()),
        pa.field('PATH_BW', pa.string()),
        pa.field('USER_FRIENDLY_ID', pa.string(), metadata={"req":"sensitive"}),
        pa.field('OLT_ID', pa.string(), metadata={"req":"sensitive"}),
        pa.field('OLT_MSAN_TYPE', pa.string()),
        pa.field('OLT_IP_ADDRESS', pa.string(), metadata={"req":"sensitive"}),
        pa.field('OLT_EQUIP_ID', pa.decimal128(16, 0)),
        pa.field('OLT_PORT', pa.decimal128(16, 0)),
        pa.field('OLT_SHELF', pa.string()),
        pa.field('OLT_SLOT', pa.string()),
        pa.field('OLT_PORT_NAME', pa.string()),
        pa.field('OLT_SITE_ID', pa.decimal128(16, 0)),
        pa.field('OLT_VLAN', pa.string()),
        pa.field('EXC_CODE', pa.string(), metadata={"req":"sensitive"}),
        pa.field('ONU_EQUIP_ID', pa.decimal128(16, 0)),
        pa.field('ONU_SITE_ID', pa.decimal128(16, 0)),
        pa.field('A_SIDE_SITE_ID', pa.decimal128(16, 0)),
        pa.field('Z_SIDE_SITE_ID', pa.decimal128(16, 0)),
        pa.field('ORDER_ID', pa.string()),
        pa.field('PORT_BTU', pa.string()),
        pa.field('ADDRESS_ID', pa.decimal128(16, 0)),
        pa.field('GEN_DATE', pa.timestamp('ns')),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })

    return target_schema


def get_target_schema_daa_oraforms_tm_migrated_serv_n_add_p(column_names):        
    target_schema = pa.schema([
        pa.field('MIGRATED_FROM', pa.string()),
        pa.field('SERVICE_NO', pa.string()),
        pa.field('ADD_ID', pa.decimal128(16, 0)),
        pa.field('ORI_FDP', pa.string()),
        pa.field('EXCH_CODE', pa.string(), metadata={"req":"sensitive"}),
        pa.field('MIGRATED_DATE', pa.timestamp('ns')),
        pa.field('INITIAL_STATUS', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })

    return target_schema


def get_target_schema_daa_oraforms_tm_neo_data_migrate_p(column_names):        
    target_schema = pa.schema([
        pa.field('DEL_SERVICE_NUM', pa.string()),
        pa.field('LOGIN_ID', pa.string(), metadata={"req":"sensitive"}),
        pa.field('CURRENTSPEED', pa.string()),
        pa.field('MAXSPEED', pa.string()),
        pa.field('DP_ID_NIS', pa.string(), metadata={"req":"sensitive"}),
        pa.field('ADDE_NIS', pa.string(), metadata={"req":"sensitive"}),
        pa.field('ADDE_GRANITE', pa.string(), metadata={"req":"sensitive"}),
        pa.field('FDP_MSAN_ID', pa.string(), metadata={"req":"sensitive"}),
        pa.field('MATCH_ACCURACY', pa.string()),
        pa.field('NIS_DP_ID', pa.decimal128(16, 0)),
        pa.field('GRN_DP_ID', pa.decimal128(16, 0)),
        pa.field('DISTANCE', pa.decimal128(38, 10), metadata={"target_schema":"float64()"}),
        pa.field('EXCHANGE_CODE', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })

    return target_schema



def get_target_schema_daa_oraforms_tm_neta_granite_service_delta_p(column_names):
    target_schema = pa.schema([
        pa.field('LAYER3_NAME', pa.string()),
        pa.field('LEG_NAME', pa.string()),
        pa.field('LEG_ID', pa.decimal128(38, 10)),
        pa.field('PS_BS_NAME', pa.string()),
        pa.field('PS_BS_ID', pa.decimal128(38, 10)),
        pa.field('SERVICE_CATEGORY', pa.string()),
        pa.field('CPE_ID', pa.string()),
        pa.field('CPE_PORT', pa.string()),
        pa.field('CPE_PORT_ID', pa.decimal128(38, 10)),
        pa.field('CPE_VENDOR', pa.string()),
        pa.field('CPE_IP_ADDRESS', pa.string(), metadata={"req":"sensitive"}),
        pa.field('ONU_ID', pa.string()),
        pa.field('ONU_PORT', pa.string()),
        pa.field('ONU_PORT_ID', pa.decimal128(38, 10)),
        pa.field('ONU_VENDOR', pa.string()),
        pa.field('ONU_IP_ADDRESS', pa.string(), metadata={"req":"sensitive"}),
        pa.field('ONT_ID', pa.string()),
        pa.field('ONU_PASSWORD', pa.string()),
        pa.field('DP_ID', pa.string(), metadata={"req":"sensitive"}),
        pa.field('DP_PORT', pa.string()),
        pa.field('DP_PORT_ID', pa.decimal128(38, 10)),
        pa.field('DP_VENDOR', pa.string()),
        pa.field('DP_IP_ADDRESS', pa.string(), metadata={"req":"sensitive"}),
        pa.field('EPE_ID', pa.string()),
        pa.field('EPE_PORT', pa.string()),
        pa.field('EPE_PORT_ID', pa.decimal128(38, 10)),
        pa.field('EPE_VENDOR', pa.string()),
        pa.field('EPE_IP_ADDRESS', pa.string(), metadata={"req":"sensitive"}),
        pa.field('ACCESS_ID', pa.string()),
        pa.field('ACCESS_PORT', pa.string()),
        pa.field('ACCESS_PORT_ID', pa.decimal128(38, 10)),
        pa.field('ACCESS_VENDOR', pa.string()),
        pa.field('ACCESS_IP_ADDRESS', pa.string(), metadata={"req":"sensitive"}),
        pa.field('NPE_ID', pa.string()),
        pa.field('NPE_PORT', pa.string()),
        pa.field('NPE_PORT_ID', pa.decimal128(38, 10)),
        pa.field('NPE_VENDOR', pa.string()),
        pa.field('NPE_IP_ADDRESS', pa.string(), metadata={"req":"sensitive"}),
        pa.field('MSE_ID', pa.string()),
        pa.field('MSE_PORT', pa.string()),
        pa.field('MSE_PORT_ID', pa.decimal128(38, 10)),
        pa.field('MSE_VENDOR', pa.string()),
        pa.field('MSE_IP_ADDRESS', pa.string(), metadata={"req":"sensitive"}),
        pa.field('ENODEB_ID', pa.string()),
        pa.field('AVLAN', pa.string()),
        pa.field('TVLAN', pa.string()),
        pa.field('RING_NAME', pa.string()),
        pa.field('RING_ID', pa.decimal128(38, 10)),
        pa.field('CUSTOMER_ABBR', pa.string()),
        pa.field('WEBE_SERVICE', pa.string()),
        pa.field('CHANGE_IND', pa.string()),
        pa.field('VRF_NAME', pa.string()),
        pa.field('ORDER_ID', pa.string()),
        pa.field('TECHNICAL_SLA_SLG', pa.string()),
        pa.field('CONNECT_DATE', pa.timestamp('ns')),
        pa.field('FDC_ID', pa.string(), metadata={"req":"sensitive"}),
        pa.field('FDC_PORT', pa.string()),
        pa.field('FDC_PORT_ID', pa.decimal128(38, 10)),
        pa.field('FDC_VENDOR', pa.string()),
        pa.field('FDC_IP_ADDRESS', pa.string(), metadata={"req":"sensitive"}),
        pa.field('NNI_ID', pa.string()),
        pa.field('PS_BS_BW', pa.string()),
        pa.field('CHANGE_DATE', pa.timestamp('ns')),
        pa.field('ACCESS_CCT_NAME', pa.string()),
        pa.field('ACCESS_CCT_ID', pa.decimal128(38, 10)),
        pa.field('PHY_GROUP_CAT', pa.string()),
        pa.field('eEXTRACTION_TIMESTAMP', pa.string())
    ],
        metadata={
            "Classification": "Confidential"
        })
    return target_schema


#ont
#latest date 2023-10-02
def get_target_schema_daa_oraforms_tm_ont_id_p(column_names):
    target_schema = pa.schema([
        pa.field('OLT_PORT_INST_ID', pa.decimal128(16, 0)),
        pa.field('ONU_EQUIP_INST_ID', pa.decimal128(16, 0)),
        pa.field('ONT_ID', pa.decimal128(16, 0)),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
            "Classification": "Confidential"
    })

    return target_schema



def get_target_schema_daa_oraforms_tm_premise_type_map_p(column_names):        
    target_schema = pa.schema([
        pa.field('PREMISE_NAME', pa.string()),
        pa.field('PREMISE_TYPE', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })

    return target_schema


def get_target_schema_daa_oraforms_tm_serv_boundary_all_view_p(column_names):        
    target_schema = pa.schema([
        pa.field('SITE_HUM_ID', pa.string(), metadata={"req":"sensitive"}),
        pa.field('DP_STATUS', pa.string()),
        pa.field('SITE_INST_ID', pa.decimal128(16, 0)),
        pa.field('NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('PROJECT_TYPE', pa.string()),
        pa.field('STATE', pa.string()),
        pa.field('PREMISE_TYPE', pa.string()),
        pa.field('RESOURCE_INST_ID', pa.decimal128(16, 0)),
        pa.field('SI_STATUS', pa.string()),
        pa.field('TYPE', pa.string()),
        pa.field('DESCR', pa.string(), metadata={"req":"sensitive"}),
        pa.field('STREET_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('CITY', pa.string()),
        pa.field('LAST_MOD_BY', pa.string(), metadata={"req":"sensitive"}),
        pa.field('SERVICE_CATEGORY', pa.string()),
        pa.field('BUILDING_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('POSTCODE', pa.string()),
        pa.field('EXCHANGE_CODE', pa.string()),
        pa.field('STREET_TYPE', pa.string()),
        pa.field('RI_STATUS', pa.string()),
        pa.field('EQUIP_INST_ID', pa.decimal128(16, 0)),
        pa.field('SECTION', pa.string(), metadata={"req":"sensitive"}),
        pa.field('HYBRID', pa.string()),
        pa.field('LAST_MOD_TS', pa.string()),
        pa.field('HOUSE_UNIT_LOT', pa.string(), metadata={"req":"sensitive"}),
        pa.field('FLOOR_NUMBER', pa.string(), metadata={"req":"sensitive"}),
        pa.field('COUNTRY', pa.string()),
        pa.field('UPDATE_REMARKS', pa.string()),
        pa.field('STATE_QUERY', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })
    return target_schema


def get_target_schema_daa_oraforms_tm_serv_boundary_equip_view_p(column_names):        
    target_schema = pa.schema([
        pa.field('COPPER_OWN_TM', pa.string()),
        pa.field('STATE', pa.string()),
        pa.field('OPERATION_DATE', pa.timestamp('ns')),
        pa.field('PREMISE_TYPE', pa.string()),
        pa.field('RESOURCE_INST_ID', pa.decimal128(16, 0)),
        pa.field('MAIN_DP', pa.string(), metadata={"req":"sensitive"}),
        pa.field('CITY', pa.string()),
        pa.field('STREET_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('DDP', pa.string()),
        pa.field('POSTCODE', pa.string()),
        pa.field('BUILDING_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('ADDRESS_FULL', pa.string(), metadata={"req":"sensitive"}),
        pa.field('STREET_TYPE', pa.string()),
        pa.field('OPERATION_TYPE', pa.string()),
        pa.field('EQUIP_INST_ID', pa.decimal128(16, 0)),
        pa.field('SECTION', pa.string(), metadata={"req":"sensitive"}),
        pa.field('ADDR_SERVICE_CATEGORY', pa.string()),
        pa.field('COUNTRY', pa.string()),
        pa.field('HOUSE_UNIT_LOT', pa.string(), metadata={"req":"sensitive"}),
        pa.field('FLOOR_NUMBER', pa.string(), metadata={"req":"sensitive"}),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })

    return target_schema


#ap
def get_target_schema_daa_oraforms_tm_wifi_ap_report_table_p(column_names):        
    target_schema = pa.schema([
        pa.field('REGION', pa.string()),
        pa.field('STATE_NAME', pa.string()),
        pa.field('PTT_NAME', pa.string()),
        pa.field('EXCHANGE_CODE', pa.string(), metadata={"req":"sensitive"}),
        pa.field('SITE_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('SITE_ACTUAL_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('FULL_ADDRESS', pa.string(), metadata={"req":"sensitive"}),
        pa.field('TOTAL_AP', pa.decimal128(16, 0)),
        pa.field('TOTAL_SPEED', pa.string()),
        pa.field('BACKHAUL_TYPE', pa.string()),
        pa.field('SITE_CATEGORY', pa.string()),
        pa.field('AP_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('STATUS', pa.string()),
        pa.field('AP_FREE_PORT', pa.decimal128(16, 0)),
        pa.field('INSTALLATION_LOC', pa.string(), metadata={"req":"sensitive"}),
        pa.field('COVERAGE', pa.string()),
        pa.field('SSID_LIST', pa.string()),
        pa.field('LATITUDE', pa.string()),
        pa.field('LONGITUDE', pa.string()),
        pa.field('PREMISE_TYPE', pa.string()),
        pa.field('AP_GROUP_NAME', pa.string()),
        pa.field('SERVICE_ID', pa.string(), metadata={"req":"sensitive"}),
        pa.field('LOGIN_ID', pa.string()),
        pa.field('CARD_INST_ID', pa.decimal128(16, 0)),
        pa.field('SWITCH_ID', pa.decimal128(16, 0)),
        pa.field('MODEM_ID', pa.decimal128(16, 0)),
        pa.field('SITE_ID', pa.decimal128(16, 0)),
        pa.field('HOA_NUMBER', pa.string()),
        pa.field('IP_ADDRESS_AP', pa.string(), metadata={"req":"sensitive"}),
        pa.field('AC_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('AC_IP_ADDRESS', pa.string(), metadata={"req":"sensitive"}),
        pa.field('MODEM_LOCATION', pa.string(), metadata={"req":"sensitive"}),
        pa.field('MODEM_IP_ADDRESS', pa.string(), metadata={"req":"sensitive"}),
        pa.field('MODEM_SUBNET_IP', pa.string(), metadata={"req":"sensitive"}),
        pa.field('ORDER_ID', pa.string()),
        pa.field('PARTNER_NAME', pa.string()),
        pa.field('AP_MODEL', pa.string()),
        pa.field('AP_INSTALL_ADDRESS', pa.string(), metadata={"req":"sensitive"}),
        pa.field('AP_INSTALLATION_LOCATION', pa.string(), metadata={"req":"sensitive"}),
        pa.field('AP_MAC_ADDRESS', pa.string(), metadata={"req":"sensitive"}),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })

    return target_schema


def get_target_schema_daa_oraforms_tm_wifi_ap_ssid_p(column_names):
    target_schema = pa.schema([
        pa.field('AP_ID', pa.decimal128(16, 0)),
        pa.field('SSID_NAME', pa.string()),
        pa.field('CUSTOMER', pa.string(), metadata={"req":"sensitive"}),
        pa.field('RESERVATION_ID', pa.string()),
        pa.field('RESERVATION_DATE', pa.string()),
        pa.field('RESERVATION_BY', pa.string()),
        pa.field('SERVICE_ID', pa.string()),
        pa.field('COMMITMENT_PERIOD', pa.string()),
        pa.field('BILLING_START_DATE', pa.string()),
        pa.field('ACTION_CODE', pa.string()),
        pa.field('WWS_ID', pa.string()),
        pa.field('EWB_WIFI_SERVICE_ID', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })

    return target_schema


#unifi
def get_target_schema_daa_unifisearch_pilot_exchange_jendela_p(column_names):        
    target_schema = pa.schema([
        pa.field('EXCHANGE', pa.string(), metadata={"req":"sensitive"}),
        pa.field('STATE', pa.string()),
        pa.field('PILOT', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })

    return target_schema


def get_target_schema_daa_unifisearch_us_api_log_p(column_names):        
    target_schema = pa.schema([
        pa.field('US_LOG_ID', pa.decimal128(12, 0)),
        pa.field('US_API_NAME', pa.string()),
        pa.field('US_API_PROVIDER', pa.string()),
        pa.field('US_API_REQUEST', pa.string(), metadata={"req":"sensitive"}),
        pa.field('US_API_RESPONSE', pa.string(), metadata={"req":"sensitive"}),
        pa.field('US_API_REQUESTOR', pa.string(), metadata={"req":"sensitive"}),
        pa.field('US_API_DATE', pa.timestamp('ns')),
        pa.field('US_DEMAND_ID', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })
    
    return target_schema



def get_target_schema_daa_unifisearch_us_attachment_p(column_names):        
    target_schema = pa.schema([
        pa.field('US_ATTH_ID', pa.decimal128(12, 0)),
        pa.field('FILENAME', pa.string()),
        pa.field('ATTACHMENT', pa.string()),
        pa.field('DEMAND_ID', pa.string()),
        pa.field('TROIKA_ID', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ])

    return target_schema


def get_target_schema_daa_unifisearch_us_demand_capture_p(column_names):        
    target_schema = pa.schema([
        pa.field('US_ID', pa.decimal128(12, 0)),
        pa.field('DEMAND_ID', pa.string()),
        pa.field('ADDRESSID', pa.string()),
        pa.field('CREATORID', pa.string(), metadata={"req":"sensitive"}),
        pa.field('CREATORNAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('CREATORGROUP', pa.string()),
        pa.field('CREATORGROUPCATEGORY', pa.string()),
        pa.field('COMPANYNAME', pa.string()),
        pa.field('EXCHANGEID', pa.string(), metadata={"req":"sensitive"}),
        pa.field('UNITID', pa.string(), metadata={"req":"sensitive"}),
        pa.field('FLOORNO', pa.string(), metadata={"req":"sensitive"}),
        pa.field('BUILDINGNAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('STREETTYPE', pa.string()),
        pa.field('STREETNAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('SECTION', pa.string(), metadata={"req":"sensitive"}),
        pa.field('POSTCODE', pa.string()),
        pa.field('STATE', pa.string()),
        pa.field('CITY', pa.string()),
        pa.field('NEID', pa.string(), metadata={"req":"sensitive"}),
        pa.field('LATITUDE', pa.string(), metadata={"req":"sensitive"}),
        pa.field('LONGITUDE', pa.string(), metadata={"req":"sensitive"}),
        pa.field('ACCURACY', pa.decimal128(3, 0)),
        pa.field('CUSTOMERSEGMENT', pa.string()),
        pa.field('CUSTOMERIDTYPE', pa.string()),
        pa.field('CUSTOMERID', pa.string(), metadata={"req":"sensitive", "PII":"IC"}),
        pa.field('SOURCESYSTEM', pa.string()),
        pa.field('TICKETCATEGORY', pa.string()),
        pa.field('TROIKA_ID', pa.string()),
        pa.field('NBA_RESULT', pa.string()),
        pa.field('FDP_ID', pa.string(), metadata={"req":"sensitive"}),
        pa.field('PORT_NUMBER', pa.string()),
        pa.field('RFS_DATE', pa.string()),
        pa.field('DEMANDACTION', pa.string()),
        pa.field('DEMANDSTATUS', pa.string()),
        pa.field('REQUESTORID', pa.string()),
        pa.field('REMARK', pa.string()),
        pa.field('REASONMESSAGE', pa.string()),
        pa.field('CUSTOMERNAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('PICTUREID', pa.decimal128(12, 0)),
        pa.field('TIMESTAMP', pa.timestamp('ns')),
        pa.field('OUTSIDERADIUS', pa.string()),
        pa.field('DPLAT', pa.string(), metadata={"req":"sensitive"}),
        pa.field('DPLONG', pa.string(), metadata={"req":"sensitive"}),
        pa.field('DISTANCEDP', pa.string()),
        pa.field('ACCURACYLEVEL', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
        metadata={
          "Classification": "Confidential"
        })
    
    return target_schema


#prob  
def get_target_schema_daa_unifisearch_us_demand_users_p(column_names):        
    target_schema = pa.schema([
        pa.field('NAME', pa.string(), metadata={"req": "sensitive", "PII":"Yes"}),
        pa.field('STATE', pa.string()),
        pa.field('ROLE', pa.string()),
        pa.field('STAFF_ID', pa.string(), metadata={"req":"sensitive"}),
        pa.field('UNIT', pa.string()),
        pa.field('EMAIL', pa.string(), metadata={"req":"sensitive"}),
        pa.field('USER_ID', pa.decimal128(16, 0)), 
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ])

    return target_schema


def get_target_schema_daa_unifisearch_us_troika_nba_p(column_names):        
    target_schema = pa.schema([
        pa.field('NBA_ID', pa.decimal128(16, 0)),
        pa.field('NBA_RESULT', pa.string()),
        pa.field('US_STATUS', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })

    return target_schema
  


def get_target_schema_daa_xperadmin_user_inst_p(column_names):        
    target_schema = pa.schema([
        pa.field('USER_INST_ID', pa.decimal128(16, 0)),
        pa.field('USER_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('FULL_NAME', pa.string(), metadata={"req":"sensitive"}),
        pa.field('USER_PASSWD', pa.string()),
        pa.field('DEFAULT_DB', pa.string()),
        pa.field('DEPARTMENT', pa.string()),
        pa.field('TELEPHONE', pa.string(), metadata={"req":"sensitive"}),
        pa.field('EMAIL_ADDR', pa.string(), metadata={"req":"sensitive"}),
        pa.field('LAST_LOGIN', pa.timestamp('ns')),
        pa.field('COMMENTS', pa.string()),
        pa.field('PASSWD_CHG_DATE', pa.timestamp('ns')),
        pa.field('FLAGS', pa.string()),
        pa.field('LAST_PASSWD', pa.string()),
        pa.field('FAILED_ATTEMPT_CNT', pa.decimal128(16, 0)),
        pa.field('LAST_MOD_TS', pa.timestamp('ns')),
        pa.field('LAST_MOD_BY', pa.string(), metadata={"req":"sensitive"}),
        pa.field('INST_VER', pa.decimal128(16, 0)),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })
    
    return target_schema


def get_target_schema_daa_grnprd_card_inst_p(column_names):        
    target_schema = pa.schema([
        pa.field('CARD_INST_ID', pa.string()),
        pa.field('EQUIP_INST_ID', pa.string()),
        pa.field('SLOT', pa.string()),
        pa.field('TYPE', pa.string()),
        pa.field('STATUS', pa.string()),
        pa.field('ORDERED', pa.timestamp('ns')),
        pa.field('DUE', pa.timestamp('ns')),
        pa.field('INSTALLED', pa.timestamp('ns')),
        pa.field('IN_SERVICE', pa.timestamp('ns')),
        pa.field('SCHED_DATE', pa.timestamp('ns')),
        pa.field('DECOMMISSION', pa.timestamp('ns')),
        pa.field('SERIAL_NO', pa.string()),
        pa.field('BATCH_NO', pa.string()),
        pa.field('BAR_CODE', pa.string()),
        pa.field('PURCHASE_PRICE', pa.decimal128(10, 2), metadata={"target_schema":"float64()"}),
        pa.field('PURCHASE_DATE', pa.timestamp('ns')),
        pa.field('ASSET_LIFE', pa.decimal128(12, 2), metadata={"target_schema":"float64()"}),
        pa.field('MAXPORTS', pa.decimal128(9, 0), metadata={"target_schema":"uint16()"}),
        pa.field('DESCRIPTION', pa.string()),
        pa.field('UNEQUIPPED', pa.string()),
        pa.field('CARD_TPLT_INST_ID', pa.string()),
        pa.field('LAST_MOD_BY', pa.string(), metadata={"req":"sensitive"}),
        pa.field('LAST_MOD_TS', pa.timestamp('ns')),
        pa.field('PARENT_CARD_INST_ID', pa.decimal128(16, 0)),
        pa.field('GRAND_PARENT_INST_ID', pa.decimal128(16, 0)),
        pa.field('NBR_SUB_CARDS', pa.decimal128(16, 0)),
        pa.field('SLOT_OCCUPANCY', pa.decimal128(16, 0)),
        pa.field('SLOT_INST_ID', pa.decimal128(16, 0)),
        pa.field('DYN_PORT_NAME_GEN_ID', pa.decimal128(16, 0)),
        pa.field('ROLE', pa.string()),
        pa.field('NAME', pa.string()),
        pa.field('AID', pa.string()),
        pa.field('HECIG', pa.string()),
        pa.field('UNIT_OF_MEASURE', pa.string()),
        pa.field('DIRECTION', pa.string()),
        pa.field('EXTRACTION_TIMESTAMP', pa.timestamp('s'))
    ],
    metadata={
        "Classification": "Confidential"
    })

    return target_schema








