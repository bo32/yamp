from player.global_properties import global_properties

# Singleton
class UrlService(object):

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print('Initializing Url Service...')
            cls._instance = super(UrlService, cls).__new__(cls)
            print('Url Service initialized...')
        return cls._instance

    def get_url(self, key):
        return global_properties['urls'][key]
