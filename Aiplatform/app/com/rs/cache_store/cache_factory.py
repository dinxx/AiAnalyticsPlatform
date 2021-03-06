from Aiplatform.app.com.rs.cache_store.couchbase_cache import CouchBaseCache
from Aiplatform.app.com.rs.cache_store.interface_file_cache import ICache
from Aiplatform.app.com.rs.cache_store.product_taxonomy_cache import ProductTaxonomyCache
from Aiplatform.app.com.rs.config.load_config import ConfigReader


class CacheFactory():
    __instance = None
    __cache_type_instance : ICache = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if CacheFactory.__instance == None:
            CacheFactory()
        return CacheFactory.__instance

    def __init__(self):
        """ Virtually private constructor. """

        if CacheFactory.__instance != None:
            pass
        else:
            self.__load_cache_factory()
            CacheFactory.__instance = self

    def get_cache_type(self):
        return self.__cache_type_instance

    def __load_cache_factory(self):
        config = ConfigReader.getInstance().get_system_config_info()
        cache_type = config.get("cache.enabled", "cache")

        if cache_type == 'inMemory':
            self.__cache_type_instance = ProductTaxonomyCache().getInstance()
        elif cache_type == 'couchBase':
            self.__cache_type_instance = CouchBaseCache()
        else:
            raise Exception("invalid Cache config --> ",cache_type)
