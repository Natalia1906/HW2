import requests
import json
import time

def save_todo():
    res = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    todo = res.json()
    with open("temp/todo.json", "w") as file:
        json.dump(todo, file)

save_todo()

def save10_todo(func):
    for i in range(1, 10+1):

def decorator(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        stop = time.perf_counter()
        print(stop - start)
        return res
    return wrapper


