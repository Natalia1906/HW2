#TODO задание 1

import requests
import json

number = input("Введите число: ")
url = "https://jsonplaceholder.typicode.com/todos/№"
_id = requests.get(url)

with open("_id.json()", mode = "w", encoding = "utf-8") as file:
    _id.json = json.dump(file)



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
