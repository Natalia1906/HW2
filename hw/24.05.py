
# TODO грязные функции
m = 2000
def sum(s , p) :
    if m >= s + p :
        print("Да, сможет позволить себе покупку")
    else:
        print("Нет, не сможет позволить себе покупку")
sum(500, 600)



m = 1000
def sum(s , p) :
    if m >= s + p :
        print("Да, сможет позволить себе покупку")
    else:
        print("Нет, не сможет позволить себе покупку")
sum(700, 800)


# TODO чистые функции
m = 2000
res1 = 0
def sum(s , p) :
    if m >= s + p :
        print("Да, сможет позволить себе покупку")
    else:
        print("Нет, не сможет позволить себе покупку")
    return m
res1 = sum (500,600)


m = 1000
res2 = 0
def sum(s , p) :
    if m >= s + p :
        print("Да, сможет позволить себе покупку")
    else:
        print("Нет, не сможет позволить себе покупку")
    return m
res2 = sum (700,800)
