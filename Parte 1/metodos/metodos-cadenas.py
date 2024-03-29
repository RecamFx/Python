# DIR no es un metodo, es una funcion
# DIR permite ver todos los atributos que se le puden aplicar a este objeto
cadena1 = "Stephen"
print(dir(cadena1)) #? ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

# Los metodos son ejecutados de la siguiente forma: variable.metodo()
#------------------------------------------METODOS DE CADENAS------------------------------------------#

#------------------------------------------------------------------------------------------------------#
# UPPER Convierte toda la cadena de texto en mayuscula
resultado = cadena1.upper()
resultado2 = "Buenas tardes".upper()
print(resultado) #? Stephen
print(resultado2) #? BUENAS TARDES

# LOWER Convierte toda la cadena de texto a minusculas
resultado = cadena1.lower()
resultado2 = "Buenas tardes".lower()
print(resultado) #? Stephen
print(resultado2) #? buenas tardes

# CAPITALIZE Convierte solo la primera letra a mayuscula y todas las demas letras en minusculas
resultado = "hOLa".capitalize()
print(resultado) #? Hola


#------------------------------------------------------------------------------------------------------#
# FIND Busca una cadena dentro de otra cadena
# FIND Devuelve la posicion en la que se encuentra lo pedido, en el caso de no encontrarlo devuleve el valor -1
cadenaejemplo = "Hola buenas tardes"
busqueda = cadenaejemplo.find("a")
print(busqueda) #? 3

# INDEX Busca una cadena dentro de otra cadena
busqueda = cadenaejemplo.index("a")
print(busqueda) #? 3
# FIND e INDEX hacen lo mismo, la unica diferencia es que find devuelve -1 si no encuentra el valor, en cambio index devuelve un error


#------------------------------------------------------------------------------------------------------#
# ISNUMERIC Verifica si el valor es numerico (Numerico pero solo de strings)
busqueda = "hola".isnumeric()
busqueda2 = "3".isnumeric()
busqueda3 = "3asd".isnumeric()
print(busqueda) #? False
print(busqueda2) #? True
print(busqueda3) #? False

# ALFANUMERICO Verifica si el valor contiene numeros y letras (nada de signos ni espacios)
busqueda = "hola23".isalnum()
busqueda2 = "hola 23".isalnum()
print(busqueda) #? True
print(busqueda2) #? False


#------------------------------------------------------------------------------------------------------#
# COUNT Cuenta cuantas veces esta precente el valor que le indicamos
busqueda = "a a b a b c d e".count("a")
print(busqueda) #? 3

# LEN Cuenta la cantidad de caracteres que tiene una cadena
# LEN NO ES UN METODO! ES UNA FUNCION!
busqueda = "Hola buenas tardes"
print(len(busqueda)) #? 18


#------------------------------------------------------------------------------------------------------#
# STARTSWITH Verifica si una cadena empieza con el valor que proporcionamos
busqueda = "Buenos Dias".startswith("Bue")
print(busqueda) #? True

# ENDSWITH Verifica si una cadena termina con el valor que proporcionamos
busqueda = "Hola".endswith("la")
print(busqueda) #? True


#------------------------------------------------------------------------------------------------------#
# REPLACE Reemplaza un valor por otro .replace("valor antiguo", :"valor nuevo")
# En el caso de que no encuentre el valor antiguo simplemente no se va a modificar nada, se va a devolver el valor original
busqueda = "Hola".replace("la", "lu")
print(busqueda) #? Holu

# SPLIT Crea una lista donde el valor que le asignemos a split va a ser donde se separen los valores de la lista
busqueda = "Hola,buenos,dias".split(",")
print(busqueda) #? ['Hola', 'buenos', 'dias']