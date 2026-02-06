# app/core/endpoints.py
from app.core.base import API_PREFIX, API_VERSION

AUTH_BASE = f"{API_PREFIX}{API_VERSION}/auth"
USER_BASE = f"{API_PREFIX}{API_VERSION}/user"

REGISTER = "/register"
LOGIN = "/login"
PROFILE = "/profile"
