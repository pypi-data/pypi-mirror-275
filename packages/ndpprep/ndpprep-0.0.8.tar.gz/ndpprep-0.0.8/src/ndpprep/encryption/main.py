import pyarrow.parquet.encryption as pe
from pyarrow.tests.parquet.encryption import InMemoryKmsClient
import pyarrow.parquet as pq

def encrypt_table(tbl, output_file, secret_key):
    # Encryption configuration using the processed table tbl and its columns
    encryption_config = pe.EncryptionConfiguration(
        footer_key="footer",
        column_keys={
            "columns": tbl.schema.names,
        },
        encryption_algorithm="AES_GCM_V1",
        data_key_length_bits=128
    )
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

    # Encrypt the table
    encryption_properties = (
        crypto_factory.file_encryption_properties(
            kms_connection_config,
            encryption_config
        )
    )
    # Write encrypted PyArrow Table to a Parquet file
    with pq.ParquetWriter(
            output_file,
            tbl.schema,
            encryption_properties=encryption_properties
    ) as writer:
        writer.write_table(tbl)
        