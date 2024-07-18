# AllRoutes.py
from .TaskRouter import TaskRouter

def get_routes():
    task_router = TaskRouter()
    routes = []
    routes += task_router.register_routes()
    return routes
