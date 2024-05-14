# słownik - para klucz - wartość
# {'user': user, 'age': wiek}
# {'klucz': 'wartośc'}
# klucze nie mogą się powtarzać
# odpowiednik jsona w pythonie

# pusty słownik
dictionary = dict()
print(dictionary)  # {} - pusty słownik

dictionary1 = {}  # tworzenie pustego słownika
print(dictionary1)  # {}
print(type(dictionary))  # <class 'dict'>
print(type(dictionary1))  # <class 'dict'>

print(dictionary.keys())  # dict_keys([])
print(dictionary.values())  # dict_values([])
print(dictionary.items())  # dict_items([])

# dodanie elemntu do słownika
dictionary['imie'] = "Radek"
print(dictionary)  # {'imie': 'Radek'}
dictionary['wiek'] = 39
print(dictionary)  # {'imie': 'Radek', 'wiek': 39}

# nadpisanie wartości dla istniejacego klucza
dictionary['imie'] = "Zenek"
print(dictionary)  # {'imie': 'Zenek', 'wiek': 39}
print(dictionary.keys())  # dict_keys(['imie', 'wiek'])
print(dictionary.values())  # dict_values(['Zenek', 39])
print(dictionary.items())  # dict_items([('imie', 'Zenek'), ('wiek', 39)])

dictionary.update({'date': '12-12-2024'})
print(dictionary)  # {'imie': 'Zenek', 'wiek': 39, 'date': '12-12-2024'}

dict_small = {'x': 2}
dict_small.update([('y', 3), ('z', 4)])
print(dict_small)  # {'x': 2, 'y': 3, 'z': 4}

print(dictionary['imie'])  # Zenek
# print(dictionary['Imie'])  # KeyError: 'Imie'
print(dictionary.get('imie'))  # Zenek
print(dictionary.get('Imie', 'default'))  # default - zwraca wartość domyślną
