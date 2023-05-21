class Config:
    SECRET_KEY = 'M3s33g3r'

class DevelopmentConfig(Config):
    DEBUG=True

config = {
    'development': DevelopmentConfig
}