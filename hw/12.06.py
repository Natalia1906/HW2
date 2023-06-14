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






