import os
import secrets

secret =secrets.token_urlsafe(32)

class Config:
  SECRET_KEY = 'secret'
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
  MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
  QUOTE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL','')
    
    if SQLALCHEMY_DATABASE_URI.startswith('postgres://'):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace('postgres://', "postgresql://", 1)

class DevConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://joseph:nyaga@localhost/josephdb'
  DEBUG = True

config_options = {
  'development':DevConfig,
  'production':ProdConfig
}