# dekoratory wykurzystuja mechaniz funkcji wewnętrznej
# dekorator przyjmuje funkcje jako argument i dodaje nową funkcjonalnosć
def dekor(func):
    def wew():
        print('Dekorujemy')
        return func()

    return wew


def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()

    return wrapper


@dekor  # dodanie dekoratora o nazwie dekor()
def hej():
    print("Hej")


@uppercase_decorator
def greeting():
    return "Hello World!!!"


# bez dekoratora wynik: Hej
# po dodaniu dekoratora wynik:
# Dekorujemy
# Hej
hej()
print(greeting())  # HELLO WORLD!!!
