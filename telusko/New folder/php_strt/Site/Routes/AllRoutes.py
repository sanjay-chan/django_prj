 # AllRoutes.py
from Site.Routes.TaskRouter import TaskRouter

def get_routes():
    task_router = TaskRouter()
    routes = []
    routes += task_router.register_routes()
    return routes
