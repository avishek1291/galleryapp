from flask_restx import Api
from blueprints.blueprint import root_blue_print

main_api = Api(root_blue_print=root_blue_print, name="gallery apis", version=1.0, description="collection of "
                                                                                              "gallery app APIs")
