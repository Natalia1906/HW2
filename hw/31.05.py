#TODO задание 1

import requests
import json

number = int(input("Введите число: "))

url = f"https://jsonplaceholder.typicode.com/todos/{number}"

try:
    response = requests.get(url)
    response.raise_for_status()

    todo = response.json()

    filename = f"{todo['id']}.json"
    with open(filename,mode = "w", encoding = "utf-8") as file:
        json.dump(todo, file)
    print(f"Данные сохранены в файл: {filename}")
except Exception as error:
    print(error)
    print("Ошибка")




#TODO задание 2

try:
    def plus_two(number: int ):
        print(2 + number)
    plus_two("hi")
except TypeError as error:
    print(error)
    print("Ожидаемый тип данных — число!")



#TODO задание 3

try:
    def element_of_array(arr, index):
        element = arr[index]
        print("Элемент: ", element)
    element_of_array([1, 4, 5], 5)
except IndexError as error:
    print("Индекс выходит за границы массива")
