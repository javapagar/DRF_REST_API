import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n$o-5o^x82bf766sc8kr+@foi3ime+i9@$4=-1d#yv(betz3!s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '{0}/db.sqlite3'.format(BASE_DIR),
    }
}

ROOT_URLCONF = 'StocksAPI.urls'

INSTALLED_APPS = [
    # base apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    #third apps
    'rest_framework',
    #local apps
    'api_trade',
]

TEST_RUNNER = 'xmlrunner.extra.djangotestrunner.XMLTestRunner'
TEST_OUTPUT_FILE_NAME = 'unit.xml'
