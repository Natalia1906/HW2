#TODO задание 2
from openpyxl import Workbook, load_workbook
combined_file = Workbook()
combined_sheet = combined_file.active

files = ['Лист1.xlsx', 'Лист2.xlsx', 'Лист3.xlsx']

for file in files:
    workbook = load_workbook(file)
    sheet = workbook.active
    for row in sheet.iter_rows(values_only=True):
        combined_sheet.append(row)
combined_file.save('combined_file.xlsx')

#TODO Домашнее задание №26. Регулярные выражения
#1
import re
emails_list = ["admin@gmail.com", "user@email.com", "admin123@gmail.com", "user34@email.com"]
def extract_domains(emails):
    domains = []
    pattern = r'@([\w.-]+)'

    for email in emails:
        match = re.search(pattern, email)
        if match:
            domain = match.group()
            domains.append(domain)
    return domains
print(extract_domains(emails_list))

#2
def words(text):
    pattern1 = r'\b\w*[aeiouAEIOU]\w*\b'
    need_word = re.findall(pattern1, text)
    return need_word
print(words("Apple is a fruit"))

#3
def string(text2):
    pattern2 = r'[,;\s]'
    splitted = re.split(pattern2, text2)
    return splitted
print(string("apple;banana,cherry,orange"))

#TODO Домашнее задание №27. Модули и пакеты

candidates = ["Аскаров", "Бекмуханов", "Ернур", "Пешая", "Карим", "Шаримазданов"]

def search_winner(candidates, votes):
    vote_counts = {candidate: votes.count(candidate) for candidate in candidates}
    max_votes = max(vote_counts.values())
    winners = [candidate for candidate, count in vote_counts.items() if count == max_votes]
    winner = min(winners,key = len)
    return winner, max_votes

votes = []
while True:
    vote = input("Вы отдаете голос за(Enter для завершения голосования): ")
    if vote == "":
        break
    votes.append(vote)
print(search_winner(candidates, votes))
