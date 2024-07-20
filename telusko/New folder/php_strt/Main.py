# main.py
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from Core.Router import Router
from django.http import HttpRequest, HttpResponse

# Initialize Router
router = Router()

# Mock routes for demonstration
class TaskController:
    def create(self):
        return HttpResponse("Creating a task...")

router.add_route('POST', '/task/create', (TaskController, 'create'))

# Define the request handler
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.handle_request()

    def do_POST(self):
        self.handle_request()

    def handle_request(self):
        parsed_url = urlparse(self.path)
        request = HttpRequest()
        request.path = parsed_url.path
        request.method = self.command

        for route in router.routes:
            if route[1] == request.path and route[0] == request.method:
                controller_class = route[2][0]
                controller_method = route[2][1]
                controller_instance = controller_class()
                response = controller_method(controller_instance)
                self.send_response(response.status_code)
                for header, value in response.items():
                    self.send_header(header, value)
                self.end_headers()
                self.wfile.write(response.content.encode('utf-8'))
                return

        self.send_response(404)
        self.end_headers()
        self.wfile.write("404 Not Found".encode('utf-8'))

# Define server address and port
SERVER_ADDRESS = ('127.0.0.1', 8000)

def run_server():
    httpd = HTTPServer(SERVER_ADDRESS, RequestHandler)
    print(f"Starting server on {SERVER_ADDRESS[0]}:{SERVER_ADDRESS[1]}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
