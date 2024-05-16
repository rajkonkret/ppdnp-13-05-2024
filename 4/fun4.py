# funkcja wewnętrzna, zagnieżdżona
# dekoratory - używają mechanizmu funkcji wewnętrznej

def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")

    return fun2  # zwróćenie funkcji fun2, jej adresu


fun1()  # To jest fun1
xfun = fun1()  # To jest fun1
print(xfun)  # <function fun1.<locals>.fun2 at 0x0000020C87E75620>
print(type(xfun))  # <class 'function'>
# uruchominie funkcji
# nazwa funkcji i nawiasy ()
xfun()  # To jest fun2
