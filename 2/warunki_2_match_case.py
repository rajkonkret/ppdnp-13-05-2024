# match case
# od Python 3.10

lista = []

lang = input("Podaj znany Ci język programowania")

match lang.lower().replace(" ", ""):
    case "python":
        lista.append("Python")
    case "java":
        lista.append("Java")
    case "c++":
        lista.append("C++")
    case _:  # warunek domyslny, else
        print("Nie znaleziono języka programowania")

print(lista)  # ['Java']
