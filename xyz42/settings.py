"""
Django settings for xyz42 project.
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
SECRET_KEY = ')%_)1y6%v1ne3$t9y@4@sx%!ukr993gtg%^3-)$igufmt6j%bi'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False 


TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['91.207.28.69','localhost','127.0.0.1','ibox.kg','dev.ibox.kg','www.ibox.kg']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'static_sitemaps',
    'main',
    'postman',
    'auths',
    'fishkas',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # ... include the providers you want to enable:
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.instagram',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.odnoklassniki',
    'allauth.socialaccount.providers.vk',
    'django.contrib.admindocs',
    'django.core.mail',
    'ajax_select',
    'password_reset',
    'adminka',
    'sport',
    'tutorial'
)



MIDDLEWARE_CLASSES = (
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'xyz42.urls'

WSGI_APPLICATION = 'xyz42.wsgi.application'

STATICSITEMAPS_ROOT_SITEMAP = 'xyz42.sitemaps.sitemaps'
# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



LANGUAGE_CODE = 'ru-ru'
LANGUAGES = (
('ru-ru', ('Russian')),
)

TIME_ZONE = 'Asia/Bishkek'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static-root/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static'),
)

STATIC_DIRS = (
    os.path.join(BASE_DIR,'static'),
)

STATIC_ROOT = os.path.join(BASE_DIR,'static-root')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

# djagno all authorization 
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'postman.context_processors.inbox',
)

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

SITE_ID = 1
LOGIN_REDIRECT_URL = "/"


# here we got email settings
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'ibox.kg@gmail.com'
EMAIL_HOST_PASSWORD = 'iboxer179'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# here messaging app
POSTMAN_DISALLOW_MULTIRECIPIENTS = True
POSTMAN_DISALLOW_COPIES_ON_REPLY = True
POSTMAN_QUICKREPLY_QUOTE_BODY = False
POSTMAN_AUTO_MODERATE_AS = True
POSTMAN_AUTOCOMPLETER_APP = {
        'name': 'ajax_select',
        'field': 'AutoCompleteField',
        'arg_name': 'channel',
        'arg_default': 'user',

}

AJAX_SELECT_BOOTSTRAP = True
AJAX_SELECT_INLINES = 'inline'

AJAX_LOOKUP_CHANNELS = {
       # pass a dict with the model and the field to search against
       'user': {'model':'auth.user', 'search_field':'username'},
}