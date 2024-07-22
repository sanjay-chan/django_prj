# Main.py

import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
from Core.Router import Router


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.handle_request('GET')

    def do_POST(self):
        self.handle_request('POST')

    def handle_request(self, method):
        handler = self.find_handler(method, self.path)
        
        if handler:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            response = handler()  
            print(response)
            self.wfile.write(response.encode())  
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"Not found")
    
    def find_handler(self, method, path):
        route = Router.get_routes()
        for route_method, route_path, handler in route:
            if route_method == method and route_path == path:
                return handler
        
        return None
    
    def log_message(self, format, *args):
        # Override log_message to suppress logging to stdout
        pass

def run_server():
    server_address = ('127.0.0.1', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f"Starting server on http://{server_address[0]}:{server_address[1]}")
    httpd.serve_forever()

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "runserver":
        run_server()
    else:
        print("Usage: python Main.py runserver")
