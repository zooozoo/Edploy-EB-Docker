from .base import *

f = open(os.path.join(CONFIG_SECRET_DIR, 'settings_dev.json'))
config_secret_dev_str = f.read()
f.close()
config_secret = json.loads(config_secret_dev_str)
# AWS
AWS_ACCESS_KEY_ID = config_secret_common['AWS']['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = config_secret_common['AWS']['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = config_secret_common['AWS']['AWS_STORAGE_BUCKET_NAME']
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
