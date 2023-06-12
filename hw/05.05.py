
#todo Домашнее задание №21: Кортежи

# №1
#shift = int(input("Введите сдвиг: "))
#text = input("Введите текст: ")
def code(text, shift):
    encrypted = ""
    for i in text:
        if i.isupper(): #проверить, является ли буква заглавной
            i_index = ord(i) - ord('A')
            i_shifted = (i_index + shift) % 26 + ord('A')
            i_new = chr(i_shifted)
            encrypted += i_new
        elif i.islower(): #проверить, является ли буква маленькой
            i_index = ord(i) - ord('a')
            i_shifted = (i_index + shift) % 26 + ord('a')
            i_new = chr(i_shifted)
            encrypted += i_new
        else:
            # если нет буквы алфавита,то оставить все как есть
            encrypted += i
    return encrypted
#res = code(text, shift)
#print(res)

#2
fruits =  ("banana", "apple", "bananamango", "mango", "strawberry-banana", "orange", "grape", "grape",)
#fruit = input("Назовите фрукт: ")
#print(fruits.count(fruit))

#3
#count = sum(i.count(fruit) for i in fruits)
#print(count)

#4
car_brands = ("Ford", "Toyota", "Chevrolet", "BMW", "Honda", "BMW")
#brand = input("Введите заменяемое слово: ")
#search = input("Введите слово на замену: ")
def replace(car_brands, brand, search):
    new_car_brands = []
    for i in car_brands:
        if i == brand:
            new_car_brands.append(search)
        else:
            new_car_brands.append(i)
    return (tuple(new_car_brands))
#res1 = replace(car_brands, brand, search)
#print(res1)



#todo Домашнее задание №22: Множества
#1

val1 = {1, 4, 6 ,7}
val2 = {1, 4, 6 ,7}
def superset(val1, val2):
    if val1 == val2:
        print("Множества равны")
    elif val1.issuperset(val2):
        print(f"Объект {val1} является чистым супермножеством")
    elif val2.issuperset(val1):
        print(f"Объект {val2} является чистым супермножеством")
    else:
        print("Супермножество не обнаружено")

#superset(val1, val2)

#2

dictionary = {}

def add_word():
    eng_word = input("Введите слово на английском: ")
    fr_word = input("Введите перевод на французский: ")
    dictionary[eng_word] = fr_word
    print("Слово успешно добавлено в словарь")
#add_word()


def remove_word():
    eng_word = input("Введите слово на английском для удаления: ")
    if eng_word in dictionary:
        del dictionary[eng_word]
        print("Слово удалено из словаря")
    else:
        print("Слово не найдено")
#remove_word()

def search_word():
    eng_word = input("Введите слово на английском для поиска: ")
    if eng_word in dictionary:
        print(dictionary[eng_word])
    else:
        print("Слово не найдено")
#search_word()

def replace_word():
    eng_word = input("Введите слово на английском для замены: ")
    if eng_word in dictionary:
        new_word = input("Введите новый перевод на французский: ")
        dictionary[eng_word] = new_word
        print("Перевод слова заменен")
    else:
        print("Слово не найдено")
#replace_word()

#3

numbers = [1, 5, 7, 7, 9, 10, 9, 9, 7]
def set_gen(numbers):
    res_set = set(numbers)
    for i in numbers:
        if numbers.count(i) > 1:
            number = str(i) * numbers.count(i)
            res_set.add(number)
    return res_set
res5 = set_gen(numbers)
#print(res5)

#todo задание 1

from datetime import datetime
import json

day1 = 'Monday'
day2 = 'Wednesday'

date1 = datetime.strptime(day1, "%A")
date2 = datetime.strptime(day2, "%A")

print(date1)

difference = abs(date2 - date1)
print(difference)

hours_left = difference.total_seconds() / 3600
print("Осталось", hours_left)

data = {"day1": day1, "day2": day2}
with open("dates.json", "w") as file:
    json.dump(data, file)


