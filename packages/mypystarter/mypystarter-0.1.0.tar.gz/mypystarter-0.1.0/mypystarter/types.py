from rest_framework.request import Request

from mypystarter.logger import app_logger
from mypystarter.models import AppUser


class IRequest(Request):
    user: AppUser = None
    logger: app_logger = None
