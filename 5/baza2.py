# baza danych - przechowywanie danych
# sql, nosql
import sqlite3

try:
    conn = sqlite3.connect('baza_sqlite.db')
    c = conn.cursor()
    print("Baza danych została podłaczona")

    # sql
    query = '''
    CREATE TABLE IF NOT EXISTS sqliteDB_delevepoers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    joining_date DATETIME,
    salary REAL NOT NULL);
    '''

    tables = '''
    CREATE TABLE IF NOT EXISTS hardware (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL NOT NULL);
    '''
    #
    # c.execute(query)
    # conn.commit()

    c.execute(tables)
    conn.commit()
except sqlite3.Error as e:
    print("Błąd podczas połączenia", e)
finally:
    if conn:
        conn.close()
        print("Połączenie zostało zamkniete")
