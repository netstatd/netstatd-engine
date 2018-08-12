from flask_restplus import Resource, Namespace
from netstatd_engine.common.logging_utils import get_logger

logger = get_logger(__name__)

api = Namespace('system-resources', validate=True,
                description='Get of all current system resources')


@api.route('')
class SystemResources(Resource):
    resources = []

    def get(self):
        """get system resources"""
        return self.resources, 200
