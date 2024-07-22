# Site/Routes/AllRoutes.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Site.Routes.TaskRouter import TaskRouter

class AllRoutes:
    def get_routes(self):
        # print('calling task router')
        task_router = TaskRouter()
        return task_router.get_routes()
    
# route = AllRoutes.get_routes()
# for rt in route:
#     rt[2]()
# AllRoutes.get_routes()
