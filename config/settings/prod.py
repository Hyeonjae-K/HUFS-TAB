from config.settings.__init__ import *

DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = secret.DATABASES

STATIC_ROOT = os.path.join(BASE_DIR, '.static_root')

SESSION_COOKIE_AGE = 300
SESSION_SAVE_EVERY_REQUEST = True
