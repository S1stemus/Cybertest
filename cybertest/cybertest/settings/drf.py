REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "EXCEPTION_HANDLER": "utils.exception_handler.drf_exception_response",
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.AllowAny",),


}