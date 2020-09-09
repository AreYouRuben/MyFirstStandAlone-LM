class DevelopmentConfig():
    DEBUG = True #si True, server reinicia con cada cambios

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}