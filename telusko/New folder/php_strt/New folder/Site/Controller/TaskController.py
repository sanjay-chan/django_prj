# TaskController.py

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Site.Helper.TaskHelper import TaskHelper

class TaskController:
    # def __init__(self):
    #     self.task_helper = TaskHelper()
        
    @staticmethod
    def create_task():
        return TaskHelper.create_task()

    @staticmethod
    def run_task():
        return TaskHelper.run_task()
        
# TaskController.create_task()
