# TaskRouter.py
from ..Controller.TaskController import TaskController

class TaskRouter:
    def __init__(self):
        self.controller = TaskController()

    def register_routes(self, router):
        router.add_route('POST', '/task/create', self.controller.create_task)
