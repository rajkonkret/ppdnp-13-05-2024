# stworzyć funkcję kantor
# ma posiadać dwie funkcje wewnętrzne usd, eur
# w zależności od parametru zwraca wybraną funkcji
# mozliwość przekazania dowolnej kwoty
def kantor(waluta):
    print("Uruchomienie kantoru", waluta)

    def usd(kwota=0):
        print("Wymieniam dolary", kwota * 3.92)

    def eur(kwota=0):
        print("Wymieniam euro", kwota * 4.26)

    if waluta == 'usd':
        return usd  # bez nawiasów bo zwracamy adres funkcji!!!
    else:
        return eur


kantor_usd = kantor("usd")
kantor_usd()  # Wymieniam dolary
kantor_usd(10000)  # Wymieniam dolary 39200.0

kantor_eur = kantor('eur')
kantor_eur(5000)  # Wymieniam euro 21300.0
