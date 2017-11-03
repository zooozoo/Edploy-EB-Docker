# sunderver로 실행 할 수 있는 환경

import random
import string

from. base import *

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.elasticbeanstalk.com',
    '.tjr.kr',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}

SECRET_KEY = ''.join(
    [random.choice(string.ascii_lowercase) for i in range(40)])
