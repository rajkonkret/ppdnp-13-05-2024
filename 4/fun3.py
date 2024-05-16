a = 10
b = 10


def dodaj():
    a = 6  # definicja lokalnej zmiennej o nazwie a
    b = 7
    print(a + b)


def dodaj2():
    print(a + b)  # przyjmie wartości zmiennych globalnych


def dodaj3():
    global a  # oznaczemy, że będziemy używać globalnej zmiennej a
    a = 8  # zmienimy wartość globalnego a
    b = 9
    print(a + b)


print("Wartość a z góry (globalna)", a)  # Wartość a z góry (globalna) 10
dodaj()  # 13
print("Wartość a z góry (globalna)", a)  # Wartość a z góry (globalna) 10
dodaj2()  # 20
print("Wartość a z góry (globalna)", a)  # Wartość a z góry (globalna) 10
dodaj3()  # 17
print("Wartość a z góry (globalna)", a)  # Wartość a z góry (globalna) 8
dodaj2()  # 18
