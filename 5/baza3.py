# baza danych - przechowywanie danych
# sql, nosql
# CRUD - create, read, update, delete
# Działanie	         Instrukcja SQL	HTTP	        DDS
# Create	        INSERT	    PUT / POST	        write
# Read (Retrieve)	SELECT	    GET	read /          take
# Update	        UPDATE	    POST / PUT / PATCH	write
# Delete (Destroy)	DELETE	    DELETE	            dispose
import sqlite3

try:
    conn = sqlite3.connect('baza_sqlite.db')
    c = conn.cursor()
    print("Baza danych została podłaczona")

    insert = '''
    INSERT INTO hardware (id,name,price) VALUES (1,'Apple', 6999);
    '''

    select = """
    SELECT * FROM hardware;
    """

    update = """
    UPDATE hardware SET price=8999 WHERE id=1;
    """

    delete = '''
    DELETE FROM hardware WHERE id=1;
    '''

    # create - insert
    # c.execute(insert)
    # conn.commit()

    # read - select
    for row in c.execute(select):
        print(row)  # (1, 'Apple', 6999.0)

    # update
    # c.execute(update)
    # conn.commit()

    # delete
    c.execute(delete)
    conn.commit()
except sqlite3.Error as e:
    print("Błąd podczas połączenia", e)
finally:
    if conn:
        conn.close()
        print("Połączenie zostało zamkniete")
