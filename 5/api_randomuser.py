import requests as re

url = 'https://randomuser.me/api/'

response = re.get(url)
print(response.text)
data_response = response.json()
user = data_response['results'][0]
print(user)
# {'gender': 'male', 'name': {'title': 'Monsieur', 'first': 'Bekim', 'last': 'Denis'},
#  'location': {'street': {'number': 4567, 'name': 'Rue Duquesne'}, 'city': 'Isone', 'state': 'Zug',
#               'country': 'Switzerland', 'postcode': 5408,
#               'coordinates': {'latitude': '-61.6576', 'longitude': '-171.4860'},
#               'timezone': {'offset': '-11:00', 'description': 'Midway Island, Samoa'}},
#  'email': 'bekim.denis@example.com',
#  'login': {'uuid': '1307e6f5-7409-405d-8d42-c2f47899c157', 'username': 'crazycat785', 'password': 'sounds',
#            'salt': 'DtaKauZW', 'md5': '722e5fe081600f543593a79ee5c9bfe1',
#            'sha1': 'c4804099c1deaec85e52e2405e55a32b79907bf7',
#            'sha256': 'ce69e4cdf6d000e00a85483e4ca70ade6ca526a310056ae95fda52d642ab1a6b'},
#  'dob': {'date': '1954-07-09T02:37:12.644Z', 'age': 69}, 'registered': {'date': '2022-02-26T05:31:51.042Z', 'age': 2},
#  'phone': '077 667 13 43', 'cell': '076 467 80 72', 'id': {'name': 'AVS', 'value': '756.1341.9005.10'},
#  'picture': {'large': 'https://randomuser.me/api/portraits/men/28.jpg',
#              'medium': 'https://randomuser.me/api/portraits/med/men/28.jpg',
#              'thumbnail': 'https://randomuser.me/api/portraits/thumb/men/28.jpg'}, 'nat': 'CH'}
# wypisac first name, last name
print("Imię:", user['name']['first'])
print("NAzwisko:", user['name']['last'])
# Imię: Sophia
# NAzwisko: Ross
# linki do zdjęć
# picture
print(user['picture'])
# {'large': 'https://randomuser.me/api/portraits/women/56.jpg',
#  'medium': 'https://randomuser.me/api/portraits/med/women/56.jpg',
#  'thumbnail': 'https://randomuser.me/api/portraits/thumb/women/56.jpg'}
photo_url = user['picture']['large']
print(f"Link do zdjęcia: {photo_url}")

response_photo = re.get(photo_url)
# print(response_photo.content)
with open('user_photo.jpg', 'wb') as f:
    f.write(response_photo.content)
print("Zdjęcie zostało zapisane")
