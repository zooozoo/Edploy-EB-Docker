from .base import *

config_secret = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())
DEBUG = False

# AWS
AWS_ACCESS_KEY_ID = config_secret["django"]['AWS']['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = config_secret["django"]['AWS']['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = config_secret["django"]['AWS']['AWS_STORAGE_BUCKET_NAME']
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_REGION_NAME = 'ap-northeast-2'

# AWS Storage
STATICFILES_LOCATION = 'static'
MEDIAFILES_LOCATION = 'media'

# S3 FileStorage
DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'
STATICFILES_STORAGE = 'config.storages.StaticStorage'

# Databases
DATABASES = config_secret["django"]["databases"]

# Allowed hosts
ALLOWED_HOSTS = [
    # 'localhost',
    '.elasticbeanstalk.com',
    '.tjr.kr',
]

print(DATABASES)
print(DEFAULT_FILE_STORAGE)
print(STATICFILES_STORAGE)