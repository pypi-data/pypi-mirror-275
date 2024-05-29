__version__ = "0.2.2"

__all__ = [
    "TDImportServiceClient",
    "TDBundleUploadSFTPClient",
    "TDBundleImportModel",
    "TDBundleUploadModel",
]

try:
    # Attempts to import the client class
    # Allowed to fail importing so the package metadata can be read for building
    from .tdimport_client import TDImportServiceClient  # noqa: F401
    from .sftp_client import TDBundleUploadSFTPClient  # noqa: F401
    from .models import TDBundleImportModel, TDBundleUploadModel  # noqa: F401
except (ImportError, ModuleNotFoundError):  # pragma: no cover
    pass  # pragma: no cover
