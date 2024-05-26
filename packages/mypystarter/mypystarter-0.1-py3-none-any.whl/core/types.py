from rest_framework.request import Request

from core.logger import app_logger
from core.models import AppUser


class IRequest(Request):
    user: AppUser = None
    logger: app_logger = None
