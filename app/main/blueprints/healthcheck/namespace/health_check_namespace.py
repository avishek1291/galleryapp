from flask_restx import Namespace, Resource
from .models.health_check_model import health_check_response_data_model

namespace = Namespace('healthcheck', health_check_response_data_model)
