# context manager - do usprawnienia pracy z plikami
# with
# Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================
with open('test.log', 'w', encoding='utf-8') as fh:  # filehandler - uchwyt do pliku
    fh.write("Powitanie\n")
    fh.write("Kolejne\n")
    fh.write("Jeszcze jedno\n")

# w - tworzy nowy plik, usunie gdy już istnieje
with open('test.log', 'w', encoding='utf-8') as file:
    file.write("Radek\n")

# a - dopisanie danych na końcu pliku
with open('test.log', 'a', encoding='utf-8') as f:
    f.write("Dodane\n")
    f.write("Dodane dwa\n")
    f.write("Dodane trzy\n")
    f.write("Dośdane trzy\n")

# r - odczytywanie
with open('test.log', 'r', encoding='utf-8') as f:
    lines = f.read()

print(lines)
# Dodane
# Dodane dwa
# Dodane trzy
# Dośdane trzy
