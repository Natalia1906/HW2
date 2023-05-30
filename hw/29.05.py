#TODO 1 задание

def find_pieces(a, b) : #определение функции для НОК
    def nod(a ,b) : #определение функции для НОД
        while b :
            a, b = b, a % b
        return a

    nod_value = nod(a, b)
    d = a * b // nod(a, b)
    return (d)

a = 15
b = 15
print(find_pieces(a, b))

#TODO 2 задание

cards = [5, 1, 2, 3, 4]     #номера карточек
def find_card(cards, N) :   # N - общее количество карточек
    total_sum = (N * (N + 1)) // 2      #сумма всех номеров
    sum_of_cards = sum(cards)           #сумма данных карточек
    missing_card = total_sum - sum_of_cards
    return missing_card

print(find_card(cards, 5))

#TODO 3 задание

def number(N) :
    a = 1
    while a ** 2 < N :
        print(a ** 2)
        a += 1

number(50)





