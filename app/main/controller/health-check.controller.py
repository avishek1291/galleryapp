from flask_restx import Resource
from ..blueprints.healthcheck.namespace.health_check_namespace import namespace as health_ns


class HealthCheck(Resource):
    @health_ns.route("/health-check")
    def get(self):
        return {"status": "ok", "status": 200}
