# Core/Router.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from php_strt.Site.Routes.AllRoutes import AllRoutes

class Router:
    def __init__(self):
        # print('router\' construcor')
        self.routes = AllRoutes()
        
        
    def get_routes():
        # print('calling router from router')
        all_routes = Router()
        routes = all_routes.routes.get_routes()
        return routes

    def add_routes(self, app):
        for route in self.routes:
            method, path, handler = route
            self.routes.append((method, path, handler))

# Router.get_routes()