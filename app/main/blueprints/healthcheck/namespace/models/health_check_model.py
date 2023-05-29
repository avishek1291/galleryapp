from flask_restx import fields

health_check_response_data_model = {
    "Status": fields.String(example ="Runing successfully")
}