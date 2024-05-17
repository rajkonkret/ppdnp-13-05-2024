# REST API - sposób komunikacji między klientem a serwerem
# GET, POST, PUT/PATCH, DELETE - metody http
# GET - pobierz (json, xml)
# POST - zapisz, można wysłać tresc np.: w postaci jsona czy xmla
# PUT/PATCH - update
# DELETE - usunięcie
# przeglądarka wysyła GET
import requests

# pip install requests

url = 'http://api.open-notify.org/astros.json'
# GET
response = requests.get(url)
print(response)  # <Response [200]>
# 2xx  ok 200, 204
# 3xx - przekierowania
# 4xx - 404 - brak zasobu, 400 Bad Request - błedne zapytac
# 5xx - błedy wewnętrne serwera
print(response.text)  # odczytanie jsona
print(type(response.text))  # <class 'str'>
response_data = response.json()
print(type(response_data))  # <class 'dict'>
print(response_data)

# wszystkie klucze ze słownika
print(response_data.keys())
# dict_keys(['message', 'people', 'number'])
for k, v in response_data.items():
    print(k, "=>", v)
# message = > success
# people = > [{'name': 'Jasmin Moghbeli', 'craft': 'ISS'}, {'name': 'Andreas Mogensen', 'craft': 'ISS'},
#             {'name': 'Satoshi Furukawa', 'craft': 'ISS'}, {'name': 'Konstantin Borisov', 'craft': 'ISS'},
#             {'name': 'Oleg Kononenko', 'craft': 'ISS'}, {'name': 'Nikolai Chub', 'craft': 'ISS'},
#             {'name': "Loral O'Hara", 'craft': 'ISS'}]
# number = > 7
print(response_data['people'][0])
print(response_data['people'][0]['name'])  # Jasmin Moghbeli
for p in response_data['people']:
    print(p)
# {'name': 'Jasmin Moghbeli', 'craft': 'ISS'}
# {'name': 'Andreas Mogensen', 'craft': 'ISS'}
# {'name': 'Satoshi Furukawa', 'craft': 'ISS'}
# {'name': 'Konstantin Borisov', 'craft': 'ISS'}
# {'name': 'Oleg Kononenko', 'craft': 'ISS'}
# {'name': 'Nikolai Chub', 'craft': 'ISS'}
# {'name': "Loral O'Hara", 'craft': 'ISS'}
