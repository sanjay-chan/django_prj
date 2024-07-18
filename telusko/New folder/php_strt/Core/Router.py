# Router.py
from ..site.Routes.AllRoutes import get_routes

class Router:
    def __init__(self):
        self.routes = get_routes()

    def add_routes(self, app):
        for route in self.routes:
            app.add_route(route[1], route[2], route[3])
