import random
def generate(chars: str , length: int): ->str
    password = " "
    for i in range(1, length+1):
        password += random.choice(chars)
    return password


