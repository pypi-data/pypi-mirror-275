"""SQLBuilder"""

from data_qualitator.services.sql.service import SQLService


class SQLBuilder:
    """SQLBuilder"""

    def __init__(self):
        """__init__"""
        self._instance = None

    def __call__(self, **kwargs):
        """__call__"""
        if not self._instance:
            self._instance = SQLService(**kwargs)
        return self._instance
