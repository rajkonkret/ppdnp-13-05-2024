def allparams(a, b, /, c=42, d=256):
    print("a, b", a, b)
    print("c, d", c, d)


allparams(1, 2)
# allparams(1)  # TypeError: allparams() missing 1 required positional argument: 'b'
allparams(1, 2, d=78, c=9)
allparams(1, 2, d=78)  # c, d 42 78


# allparams(a=1, b=2, d=78)
# # a, b 1 2
# # c, d 42 78
# Po dodaniu / w argumentach
#     allparams(a=1, b=2, d=78)
# TypeError: allparams() got some positional-only arguments passed as keyword arguments: 'a, b'
# argumenty a i b mogą być przekazane tylko jako pozycyjne (positional-only)

def allparams_2(a, b, /, c=42, *args, d=256, **kwargs):
    print("a, b", a, b)
    print("c, d", c, d)
    print("args", args)
    print("kwargs", kwargs)


allparams_2(1, 2, )  # a, b 1 2
allparams_2(1, 2, 3)  # c, d 3 256
allparams_2(1, 2, c=3)  # c, d 3 256
# d musimy po nazwie bo jest po *args
allparams_2(1, 2, 3, d=890)  # c, d 3 890
allparams_2(1, 2, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 100)  # args (1, 2, 3, 4, 5, 6, 7, 8, 9, 100)
allparams_2(1, 2, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 100, d=8)  # c, d 3 8
allparams_2(1, 2, 3, 4, 5, 6, d=90, name="Radek")  # kwargs {'name': 'Radek'}
allparams_2(1, 2, 3, 4, 5, 6, d=90, name="Radek", a=7)  # kwargs {'name': 'Radek', 'a': 7}
