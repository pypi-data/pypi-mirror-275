import uuid
from datetime import datetime

from mypystarter.logger import app_logger, log_handlers


class RequestIDMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    @app_logger.catch(reraise=True, message="Error in middleware while processing request")
    def __call__(self, request):
        start = datetime.now()
        request.id = str(uuid.uuid4())
        logger = app_logger.bind(reqId=request.id).bind(user=request.user)
        request_data = request.__dict__.copy()
        request_data.pop('environ')
        request_data.pop('META')
        if '/swagger/' in request.path:
            logger.configure(handlers=[])
        else:
            logger.configure(handlers=log_handlers)
        logger.info(f"New {request.method} Request to {request.path} received", request=request_data)
        request.logger = logger
        response = self.get_response(request)
        time_in_seconds = (datetime.now() - start).total_seconds()
        response["X-Request-ID"] = request.id
        logger.info(f"Request {request.method} to {request.path} finished with status code {response.status_code} and took {time_in_seconds} seconds")
        return response
