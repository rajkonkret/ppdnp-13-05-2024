import pakiet  # import pakietu
from pakiet import fun  # import konkretnego pliku z pakietu
import pakiet.fun as pf  # import pliku jako alias

print(pakiet)
# <module 'pakiet' from 'C:\\Users\\CSComarch\\projekty\\ppdnp-13-05-2024\\pakiet\\__init__.py'>
fun.powitanie()  # Cześć
pf.powitanie()  # Cześć
# Po dodaniu w __init__  powitanie()
pakiet.powitanie()  # Cześć
# metoty info() nie ma w __init__
# pakiet.info()  # AttributeError: module 'pakiet' has no attribute 'info'
pf.info()  # Jestem pakietem
