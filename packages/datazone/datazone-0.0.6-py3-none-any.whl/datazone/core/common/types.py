from enum import Enum


class SourceType(str, Enum):
    MYSQL = "mysql"
    AWS_S3_CSV = "aws_s3_csv"
    POSTGRESQL = "postgresql"
    SAP_HANA = "sap_hana"
    AZURE_BLOB_STORAGE = "azure_blob_storage"


class ExtractMode(str, Enum):
    OVERWRITE = "overwrite"
    APPEND = "append"
