"""
Django settings for postcard project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=4_f!#ikwmwl5$dqt4dmr6j+api@khqk$0r&!l%m7v_i(f-+7p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'postcard.urls'

WSGI_APPLICATION = 'postcard.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

SECRET_KEY = "2d1484bc-aaa2-4bd4-b0b3-f4e0ddcffb35a9491e47-b954-4db5-95b9-785e3fbfb4dfa4c472eb-f860-435d-befc-a89fef91bd2a"
NEVERCACHE_KEY = "b684ed01-74f6-4d90-8162-9d21df32b7d626a180f0-b9fd-4de1-98e5-18166c6f9dec27faf333-53cd-4931-a14e-06ca6080f8de"
ALLOWED_HOSTS = ["instapage.pythonanywhere.com",]
FABRIC = {
     "SSH_USER": "flaunt", # SSH username
     "SSH_PASS":  "", # SSH password (consider key-based authentication)
     "SSH_KEY_PATH":  "/home/bamby/.ssh/id_rsa.pub", # Local path to SSH key file, for key-based auth
     "HOSTS": ["188.166.7.218"],
     "DOMAINS": ALLOWED_HOSTS, # List of hosts to deploy to
     "VIRTUALENV_HOME":  "/home/flaunt/virtenv", # Absolute remote path for virtualenvs
     "PROJECT_NAME": "postcard", # Unique identifier for project
     "REQUIREMENTS_PATH": "requirements.txt", # Path to pip requirements, relative to project
     "GUNICORN_PORT": 8000, # Port gunicorn will listen on
     "LOCALE": "en_US.UTF-8", # Should end with ".UTF-8"
     "LIVE_HOSTNAME": "postcard.a2b.am", # Host for public site.
     #"REPO_URL": "https://github.com/davit-gh/a2b.git", # Git or Mercurial remote repo URL for the project
     "DB_PASS": "thisisaproductiondatabase", # Live database password
     "ADMIN_PASS": "scanyoga", # Live admin user password
     "SECRET_KEY": SECRET_KEY,
     "NEVERCACHE_KEY": NEVERCACHE_KEY,
}
debug = False
