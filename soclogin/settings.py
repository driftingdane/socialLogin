"""
Django settings for soclogin project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-xpl2lruv9^e1$qg9u6y$ic8l8@a)(b#lh23a2^vuur8%@0=@g8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['sociallogin.onrender.com']

# Application definition

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.sites',
	'soc_login',
	'allauth',
	'allauth.account',
	'allauth.socialaccount',
	'allauth.socialaccount.providers.google',
	'allauth.socialaccount.providers.linkedin_oauth2',

]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'soclogin.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [BASE_DIR / 'templates'],
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

AUTHENTICATION_BACKENDS = [
	# Needed to login by username in Django admin, regardless of `allauth`
	'django.contrib.auth.backends.ModelBackend',
	# `allauth` specific authentication methods, such as login by e-mail
	'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'soclogin.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': BASE_DIR / 'db.sqlite3',
	}
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
	{
		'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
	},
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Set for production server
# STATIC_ROOT = BASE_DIR / 'static'

# Set for local development
STATICFILES_DIRS = [
	BASE_DIR / 'static',
]

# media folder settings
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

SITE_ID = 2
LOGIN_REDIRECT_URL = '/'

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
	'google': {
		# For each OAuth based provider, either add a ``SocialApp``
		# (``socialaccount`` app) containing the required client
		# credentials, or list them here:
		'APP': {
			'client_id': '374027176729-ibe200d6qmar89f334m9137psrsdthbo.apps.googleusercontent.com',
			'secret': 'V3nsrOhX5CR6VoArVsz6Bnrq',
			'key': ''
		}
	},
	
	'linkedin': {
		'SCOPE': [
			'r_basicprofile',
			'r_emailaddress'
		],
		'PROFILE_FIELDS': [
			'id',
			'first-name',
			'last-name',
			'email-address',
			'picture-url',
			'public-profile-url',
		]
	}
}

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
