def connect(**opcja):  # ** - dowolna ilośc argumentow nazwanych, słownikowe
    print(opcja)
    conect_param = {
        'host': '127.0.0.1',
        'port': '8080'
    }
    conect_param['pwd'] = opcja
    print(conect_param)


connect()
connect(a=9)  # {'a': 9}
connect(a=9, b=8, c=9, name="Radek")  # {'a': 9, 'b': 8, 'c': 9, 'name': 'Radek'}
d1 = {'host': '127.0.0.1',
      'port': '8080',
      'pwd': {'a': 9, 'b': 8, 'c': 9, 'name': 'Radek'}}
print(d1['pwd']['name'])  # Radek


def all_args(*args, **kwargs):
    print(args, kwargs)


all_args()  # () {}
all_args(1, 2, 3)  # (1, 2, 3) {}
all_args(a=6, b=9, d=34)  # () {'a': 6, 'b': 9, 'd': 34}
all_args(1, 2, a=90, b=456)  # (1, 2) {'a': 90, 'b': 456}
# Argumenty pozycyjne muszą byc przed nazwanymi
# all_args(a=7, 9)  # SyntaxError: positional argument follows keyword argument
