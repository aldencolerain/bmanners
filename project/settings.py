import os


# Base
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Secrets
try: import secrets
except ImportError: pass


# Environment
ENVIRONMENT = os.environ.get('ENVIRONMENT', 'production').lower()


# Development
if ENVIRONMENT == 'development':
	DEBUG = True
	TEMPLATE_DEBUG = True
	DATABASE_NAME = 'development'
	EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Production
else:
	DEBUG = False
	TEMPLATE_DEBUG = False
	DATABASE_NAME = 'production'
	SESSION_COOKIE_SECURE = False
	CSRF_COOKIE_SECURE = False


# Security
ALLOWED_HOSTS = ["*"]
API_SECRET = os.environ['API_SECRET']
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Apps
INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.humanize',
	'project'
)

# Middlware
MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'django.middleware.security.SecurityMiddleware',
)


# URLs
ROOT_URLCONF = 'project.urls'
APPEND_SLASH = False
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/signin'


# Templates
TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [os.path.join(BASE_DIR, 'project/templates')],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
			],
		},
	},
]


# WSGI
WSGI_APPLICATION = 'project.wsgi.application'


# Database
if ENVIRONMENT == 'development':
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.postgresql_psycopg2',
			'NAME': DATABASE_NAME,
			'USER': 'django',
			'PASSWORD': 'django',
			'HOST': '127.0.0.1',
			'PORT': '5432',
		}
	}
else:
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.postgresql_psycopg2',
			'NAME': DATABASE_NAME,
			'USER': 'django',
			'PASSWORD': os.environ.get('DB_PASSWORD'),
			'HOST': '127.0.0.1',
			'PORT': '5432',
		}
	}

# Logging
if ENVIRONMENT == 'production':
	LOGGING = {
		'version': 1,
		'disable_existing_loggers': False,
		'handlers': {
			'console': {
				'level': 'INFO',
				'class': 'logging.StreamHandler'
			},
		},
		'loggers': {
			'django': {
				'handlers': ['console'],
				'level': 'INFO',
				'propagate': True,
			},
			'django.request': {
				'handlers': ['console'],
				'level': 'ERROR',
				'propagate': False,
			},
		},
		'root': {
			'handlers': ['console'],
			'level': 'INFO'
		}
	}

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
