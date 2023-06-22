import threading
import multiprocessing
import requests
import json
import time

def save_1_todo(num):
    res = requests.get(f"https://jsonplaceholder.typicode.com/todos/{num}")
    todo = res.json()
    with open(f"temp/todo{num}.json", "w") as file:
        json.dump(todo, file)

@decorator_time_measure
def save_10_todo_sync():
    for i in range(1, 10+1):
        save_1_todo(i)

@decorator_time_measure
def save_10_todo_threading():
    thread_list = []
    for i in range(1, 10+1):
        thread_list.append(threading.Thread(target=save_1_todo, args=(i,),kwargs={}))
    for thread in thread_list:
        thread.start()
    for thread in thread_list():
        thread.join()
    for i in range(1, 10+1):
        save_1_todo(i)

@decorator_time_measure
def save_10_todo_multiprocessing():
    process_list = []
    for i in range(1, 10+1):
        process_list.append(multiprocessing.Process(target=save_1_todo, args=(i,),kwargs={}))
    for process in process_list:
        process.start()
    for process in process_list:
        process.join()



def decorator_time_measure(func):
    def wrapper(*args, **kwargs):
        time_start = time.perf_counter()

        result = func(*args, **kwargs)

        print("elapsed_time(s): ", round(time.perf_counter() - time_start, 6))
        return result

    return wrapper


if __name__ == "__main__":
    #save_10_todo_sync()
    #save_1_todo(10)
    #save_10_todo_threading()
    #save_10_todo_multiprocessing()

