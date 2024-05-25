"""DataQualityFactory"""


class DataQualityFactory:
    """DataQualityFactory"""

    def __init__(self):
        """__init__"""
        self._builders = {}

    def register(self, format, creator):
        """register"""
        self._builders[format] = creator

    def create(self, key, **kwargs):
        """create"""
        builder = self._builders.get(key)
        return builder(**kwargs)
