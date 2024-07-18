# main.py
from Core.Router import Router
from django.http import HttpRequest, HttpResponse

# Initialize Router
router = Router()

# Mock Django request handling
request = HttpRequest()
request.path = '/task/create'
request.method = 'POST'

# Route handling function
def handle_request(request):
    for route in router.routes:
        if route[1] == request.path and route[0] == request.method:
            controller_class = route[2][0]
            controller_method = route[2][1]
            controller_instance = controller_class()
            return controller_method(controller_instance)

    return HttpResponse("404 Not Found")

# Execute main logic
if __name__ == "__main__":
    response = handle_request(request)
    print(response)  # In real Django application, this would be returned to client
