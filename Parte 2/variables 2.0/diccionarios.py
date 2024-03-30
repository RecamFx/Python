# Creamos un diccionario con la funcion dict()

diccionario = dict(nombre = "Stephen", apellido = "Curry")
print(diccionario) #? {'nombre': 'Stephen', 'apellido': 'Curry'}



# -----------------------------------------------------------------------------------------------------------------#


# Los diccionarios no pueden contener listas ni conjuntos, pero si tuplas

diccionario = {('tupla', 'tupla2'): "hola"}
print(diccionario) #? {('tupla', 'tupla2'): "hola"}

#diccionario = {['tupla', 'tupla2']: "hola"}
#print(diccionario) #! TypeError: unhashable type: 'list'

# Usando la funcion frozenset() si se puede meter una lista al diccionario
diccionario = {frozenset(['tupla', 'tupla2']): "hola"}
print(diccionario) #? {frozenset({'tupla', 'tupla2'}): 'hola'}



# -----------------------------------------------------------------------------------------------------------------#


# Creando diccionarios con el metodo .fromkeys()
# Crea un diccionario sin valores
# Uso: .fromkeys(valor iterable, igualacion del valor)
# Si el valor iterable es una lista separa las palabras, en caso de que sea un string separa los caracteres
# La igualacion de valor es para decirles que todos los valores que creamos sean iguales a... Si no ponemos nada el valor por defecto va a ser "none" o ninguno!

diccionario = dict.fromkeys(["nombres", "apellidos", "edad"])
print(diccionario) #? {'nombres': None, 'apellidos': None, 'edad': None} 

diccionario = dict.fromkeys("ABCDE")
print(diccionario) #? {'A': None, 'B': None, 'C': None, 'D': None, 'E': None}

diccionario = dict.fromkeys("ABCDE", "ejemplo")
print(diccionario) #? {'A': 'ejemplo', 'B': 'ejemplo', 'C': 'ejemplo', 'D': 'ejemplo', 'E': 'ejemplo'}