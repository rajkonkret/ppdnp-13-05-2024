# baza danych - przechowywanie danych
# sql, nosql
import sqlite3

try:
    conn = sqlite3.connect('baza_sqlite.db')
    c = conn.cursor()
    print("Baza danych została podłaczona")
except sqlite3.Error as e:
    print("Błąd podczas połączenia", e)
finally:
    if conn:
        conn.close()
        print("Połączenie zostało zamkniete")
