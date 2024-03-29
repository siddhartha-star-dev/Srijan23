from .base import Common
from .environment import env


class Prod(Common):
    # Keep debug true in development
    DEBUG = False

    # Use local database
    DATABASES = {
        "default": env.db(
            "SRIJAN_BACKEND_DATABASE_URL_PROD",
            default="psql://srijan_backend_user:test_password@127.0.0.1:5432/srijan_backend_db",
        )
    }

    ALLOWED_HOSTS = ["*"]

    # Mail
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_PORT = env.str("SRIJAN_BACKEND_EMAIL_PORT", default="1025")
    EMAIL_HOST = env.str(
        "SRIJAN_BACKEND_EMAIL_HOST",
        default="127.0.0.1",
    )
    EMAIL_HOST_USER = env.str(
        "SRIJAN_BACKEND_EMAIL_HOST_USER",
        default="user",
    )
    EMAIL_HOST_PASSWORD = env.str(
        "SRIJAN_BACKEND_EMAIL_HOST_PASSWORD",
        default="password",
    )
    EMAIL_USE_TLS = env.bool("SRIJAN_BACKEND_EMAIL_USE_TLS", default=True)

    # Disable CORS check
    CORS_ALLOWED_ORIGINS = env.list(
        "SRIJAN_BACKEND_CORS_WHITELIST",
        default=["http://localhost:3000","http://localhost:8000", "http://127.0.0.1:8000", "https://api.srijan-iitism.com", "https://srijan-iitism.com"],
        )
#CORS_ORIGIN_ALLOW_ALL = True


    # Celery broker config
    BROKER_URL = env.str(
        "SRIJAN_BACKEND_CELERY_BROKER_PROD",
        default="amqp://srijan_backend:pass@localhost:5672/srijan_backend",
    )
