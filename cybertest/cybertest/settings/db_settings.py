import environ

env = environ.Env()
environ.Env.read_env()

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("DB_NAME", cast=str, default="cybertest"),
        "USER": env("DB_USER", cast=str, default="postgres"),
        "PASSWORD": env("DB_PASSWORD", cast=str,default="12345"),
        #docker
        "HOST": "db",
        #local
        #"HOST": "localhost",
        "PORT": 5432,
    }
}
