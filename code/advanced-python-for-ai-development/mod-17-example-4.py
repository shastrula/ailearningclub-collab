class Config:
    DEBUG = False
    BATCH_SIZE = 32

class DevConfig(Config):
    DEBUG = True
    BATCH_SIZE = 16

class ProdConfig(Config):
    DEBUG = False
    BATCH_SIZE = 128

env = os.getenv('ENV', 'dev')
config = DevConfig() if env == 'dev' else ProdConfig()