"""FilesystemParquetBuilder"""

from data_qualitator.services.filesystem.parquet.service import FilesystemParquetService


class FilesystemParquetBuilder:
    """FilesystemParquetBuilder"""

    def __init__(self):
        """__init__"""
        self._instance = None

    def __call__(self, **kwargs):
        """__call__"""
        if not self._instance:
            self._instance = FilesystemParquetService(**kwargs)
        return self._instance
