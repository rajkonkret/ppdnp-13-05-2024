import random

# generowanie liczb pseudolosowych

print(random)  # <module 'random' from 'C:\\Program Files\\Python312\\Lib\\random.py'>

print(random.randint(1, 100))  # int 1..100 włącznie
print(random.randrange(1, 100))  # int 1..99
print(random.randrange(7))  # 0..6
print(random.random())  # float 0.4131340080141762od 0 doo 0.999999
print(random.random() * 10)  # float 8.073715737928037 od 0 do 9.999999

lista = [6, 12, 34, 56, 67, 89, 120]
print(random.choice(lista))  # 6

lista_kula = list(range(1, 50))  # range() generuje od do 49
# print(lista_kula)

# print(random.choice(lista_kula))
# print(random.choice(lista_kula))
# print(random.choice(lista_kula))
# print(random.choice(lista_kula))
# print(random.choice(lista_kula))
# print(random.choice(lista_kula))

# wyn = random.choice(lista_kula)
# lista_kula.remove(wyn)
# print(wyn)
# wyn = random.choice(lista_kula)
# lista_kula.remove(wyn)
# print(wyn)
# wyn = random.choice(lista_kula)
# lista_kula.remove(wyn)
# print(wyn)
# wyn = random.choice(lista_kula)
# lista_kula.remove(wyn)
# print(wyn)
# wyn = random.choice(lista_kula)
# lista_kula.remove(wyn)
# print(wyn)
# wyn = random.choice(lista_kula)
# lista_kula.remove(wyn)
# print(wyn)

print(random.choices(lista_kula, k=6))  # [7, 2, 7, 15, 17, 26] losuje z powtórzeniami
print(random.sample(lista_kula, 6))  # [23, 9, 1, 3, 16, 29]  bez powtórzen
print(random.sample(lista_kula, k=6))  # [26, 13, 47, 42, 40, 48]
