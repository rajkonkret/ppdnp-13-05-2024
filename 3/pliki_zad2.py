import chardet

# pip install chardet
# pip list - lista zainstalowanych pakietów

# chardet wymaga odczytu bajtowo 'rb'
with open('test.log', 'rb') as file:
    raw_data = file.read()

# print(raw_data)  # b'Radek\r\nDodane\r\nDodane dwa\r\nDodane trzy\r\nDo\xc5\x9bdane trzy\r\n'
result = chardet.detect(raw_data)
print(result)
# {'encoding': 'Windows-1254', 'confidence': 0.6332532790369307, 'language': 'Turkish'}
# Po dodaniu do pliku więcej polskich znaków
# {'encoding': 'utf-8', 'confidence': 0.938125, 'language': ''}
encoding = result['encoding']

print(raw_data.decode(encoding=encoding))
# Dodane
# Dodane dwa
# Dodane trzy
# Dośćąźdane trzy
