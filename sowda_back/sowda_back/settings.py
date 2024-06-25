from pathlib import Path
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-z6el!rs_1beoky0^2#q1iof)2$eqlsua43_=%ubt&d&4*-oyz4'
DEBUG = True
# ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = ['127.0.0.1','localhost','10.10.73.81']

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tinymce',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    # 'imagekit',
    # 'djoser',
    'django_filters',
    "debug_toolbar",

    'api',
    'car',
    'other',
    'logist',
    'service',
    'elin',
]
# UNFOLD = {
#     "SITE_TITLE": 'Seýir',
#     "SITE_HEADER": 'Seýir',
#     "SITE_URL": "/",
#     "SITE_ICON": lambda request: static("logo.svg"),
#     "DASHBOARD_CALLBACK": "sowda_back.dashboard_callback",
#     "LOGIN": {
#         "image": lambda r: static("sample/login-bg.jpg"),
#         # "redirect_after": lambda r: reverse_lazy("admin:APP_MODEL_changelist"),
#     },
#     "STYLES": [
#         lambda request: static("css/style.css"),
#     ],
#     "SCRIPTS": [
#         lambda request: static("js/script.js"),
#     ],
#     "COLORS": {
#         "primary": {
#             "50": "250 245 255",
#             "100": "243 232 255",
#             "200": "233 213 255",
#             "300": "216 180 254",
#             "400": "192 132 252",
#             "500": "168 85 247",
#             "600": "147 51 234",
#             "700": "126 34 206",
#             "800": "107 33 168",
#             "900": "88 28 135",
#         },
#     },
#     "EXTENSIONS": {
#         "modeltranslation": {
#             "flags": {
#                 "en": "🇬🇧",
#                 "fr": "🇫🇷",
#                 "nl": "🇧🇪",
#             },
#         },
#     },
#     "SIDEBAR": {
#         "show_search": False,  # Search in applications and models names
#         "show_all_applications": False,  # Dropdown with all applications and models
#         "navigation": [
#             {
#                 "title": _("Navigation"),
#                 "separator": True,  # Top border
#                 "items": [
#                     {
#                         "title": _("Dashboard"),
#                         "icon": "dashboard",  # Supported icon set: https://fonts.google.com/icons
#                         "link": reverse_lazy("admin:index"),
#                         "badge": "sowda_back.badge_callback",
#                     },
#                     {
#                         "title": _("Users"),
#                         "icon": "people",
#                         "link": reverse_lazy("admin:users_user_changelist"),
#                     },
#                 ],
#             },
#         ],
#     },
#     "TABS": [
#         {
#             "models": [
#                 "app_label.model_name_in_lowercase",
#             ],
#             "items": [
#                 {
#                     "title": _("Your custom title"),
#                     "link":reverse_lazy("")
#                     # "link": reverse_lazy("admin:app_label_model_name_changelist"),
#                 },
#             ],
#         },
#     ],
# }


# def dashboard_callback(request, context):
#     """
#     Callback to prepare custom variables for index template which is used as dashboard
#     template. It can be overridden in application by creating custom admin/index.html.
#     """
#     context.update(
#         {
#             "sample": "example",  # this will be injected into templates/admin/index.html
#         }
#     )
#     return context


# def badge_callback(request):
#     return 3
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = 'sowda_back.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'sowda_back.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://localhost:60058",
    "http://127.0.0.1:60058",
    "http://10.0.2.2:8000",
]

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')

MEDIA_URL='/media/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = "api.UserProd"

# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#                'rest_framework.authentication.TokenAuthentication',
#     ),
#     'DEFAULT_PERMISSION_CLASSES':(
#                 'rest_framework.permissions.IsAuthenticated',
#     ),

# }