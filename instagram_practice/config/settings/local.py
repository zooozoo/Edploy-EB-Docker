# sunderver로 실행 할 수 있는 환경

import random
import string
import logging

from .base import *

logger = logging.getLogger(__name__)  # __name__을 추가해 놓으면 해당 모듈의 이름의 log를 불러온다.

DEBUG = False

ALLOWED_HOSTS = [
    # 'localhost',
    # '127.0.0.1',
    '.elasticbeanstalk.com',
    '.tjr.kr',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(ROOT_DIR, '.log', 'django.log')
        },
    },
    'loggers': {
        'django': {
            'handlers': [
                'console',
                'file',
            ],
            'level': 'DEBUG',
            'propagate': True,
        }
    }
}

# 버젼은 기본값
# 핸들러는 어떻게 처리 해주는지에 대한 설정
#

SECRET_KEY = ''.join(
    [random.choice(string.ascii_lowercase) for i in range(40)])
