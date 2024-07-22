# php_strt/Site/Helper/TaskHelper.py

class TaskHelper:
    
    def create_task(request_data):
        name = request_data.get('name', [''])[0] 
        return f"Task {name} Created" if name else "Task Created"

    def run_task():
        return ("Task Running")