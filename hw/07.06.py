#todo 1 задание

import re

#email = input("Введите почту: ")
#password = input("Введите пароль: ")
def register(email, password):
    pattern = (r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,}$")
    if not re.match(pattern, email):
        print("Неверная почта")
        return
    if len(password) < 6:
        print("Длинный пароль")
        return
    print("Пользователь зарегистрирован")
#register(email, password)

#todo 2 задание ????

import requests

url = "https://jsonplaceholder.typicode.com/posts"
res = requests.get(url)
print(res.json())
posts = [x for x in res.json() if x["id"]% 2 == 0]
print(posts)

#todo Домашнее задание №13. Списки

numbers =[]
while True:
    num = int(input("Введите число: "))
    numbers.append(num)
    if sum(numbers) == 0:
        break
sum_sqrt = sum([x ** 2 for x in numbers])
#print(sum_sqrt)

#todo Домашнее задание №14: Строки.Списки
#1

grades = input().split()
grades = list(map(int, grades))
print(grades)

two = grades.count(2)
three = grades.count(3)
free = grades.count(4)
five = grades.count(5)
average_mark = sum(grades) / len(grades)
#print(f"5: {five}, 4: {free}, 3: {three}, 2: {two}")
#print(average_mark)

#2
grades_2 = input()
grades_2 = grades_2.replace('2', '3')
print(grades_2)




