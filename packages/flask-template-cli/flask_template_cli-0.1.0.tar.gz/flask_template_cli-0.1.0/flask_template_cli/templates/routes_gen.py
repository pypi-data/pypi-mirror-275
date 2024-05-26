"""
Generate routes.py file for the package
"""
import os


def routes_gen(project):
    if project.project_type == "full_stack":
        _full_stack_routes_gen(project)
    else:
        _api_routes_gen(project)


def _full_stack_routes_gen(project):
    file_location = os.path.join(project.name, "app/routes/routes.py")

    with open(file_location, "w") as f:
        f.write(f"from flask import Blueprint\n\n")
        f.write(f"my_routes = Blueprint('my_routes', __name__)\n\n")
        f.write(f"""
    @my_routes.route('/')
    def index():  
        return "Hello World"

            """)
        f.write(f"\n")


def _api_routes_gen(project):
    init_file_location = os.path.join(project.name, "app/routes/__init__.py")

    with open(init_file_location, "w") as f:
        f.write(f"from flask_restful import Api \n\n\n")
        f.write(f"api = Api(prefix='/api/v1')\n\n")

    resource_file_location = os.path.join(project.name, "app/routes/resources.py")
    with open(resource_file_location, "w") as f:
        f.write(f"from flask_restful import Resource\n\n")
        f.write(f"from . import api\n\n")
        f.write(f"""
class HelloWorld(Resource):
    def get(self):
        return {{'hello': 'world'}}
            
            """)

        f.write(f"\n")

        f.write(f"api.add_resource(HelloWorld, '/')\n\n")
