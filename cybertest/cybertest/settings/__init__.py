from split_settings.tools import include

settings = [
    "django.py",
    "logs.py",
    "app_settings.py",
    "db_settings.py",
    "drf.py",
]

include(*settings)