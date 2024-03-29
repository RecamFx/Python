# Crar tuplas


# Con la funcion tuple() es como la funcion list() pero para tuplas
lista = ["hola", "Buenas tardes", "Jijijija"]
tupla = tuple(lista)
print(tupla) #? ('hola', 'Buenas tardes', 'Jijijija')

# Otra forma de crear tuplas con varios datos
tupla = "tupla","tupla2"

print(tupla) #? ('tupla', 'tupla2')

# Crear tupla con 1 solo dato
tupla = "jijija",

print(tupla) #? ('jijija',)




#todo Cuando creamos tuplas? Sirven para datos que son solo de lectura!
#todo Las tuplas se almacenan en 1 solo lugar de la memoria, mejorando la optimizacion
#todo A diferencia de las listas que ocupan 2 lugares, el cual 1 de ellos es para que se lea y el otro para que se edite la lista
#todo Por eso las tuplas son mas rapidas