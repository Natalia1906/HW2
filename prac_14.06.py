
import datetime
import time


def decorator(func):
    def wrapper(*args, **kwargs):
        date = datetime.datetime.now()
        time_start = time.perf_counter()
        res = func(*args, **kwargs)

        time_stop = time.perf_counter()
        end = round(time_stop - time_start, 6)

        with open("log.txt", "a", encoding= "utf-8") as file:
            text = f"{date} | {end} \n"
            file.write(text)
        return res
    return wrapper


@decorator
def multiplay(a, b, c):
    return a * b * c


@decorator
def division(a, b):
    return a // b

@decorator
def sum(a, b, c):
    return a + b + c

print(multiplay(1, 1, 1))
print(division(1, 1))
print(sum(1, 0, 0))