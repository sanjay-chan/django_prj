# Site/Routes/TaskRouter.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Site.Controller.TaskController import TaskController

class TaskRouter:
    # def __init__(self):
    #     self.controller = TaskController()

    def task_routes():
        routes = [
            ('GET', '/task/create', TaskController.create_task),
            ('GET', '/task/run', TaskController.run_task),
        ]
        return routes
    
    def get_routes(route):
        av_route = TaskRouter.task_routes()
        return av_route
    
