# Los datos compuestos estan compuestos por otros tipos de datos
# Los conjuntos y tuplas son inmutables
#-------------------------------------------------------------------------------------------#
# Listas (Matriz)
lista = ["Hola", "Buenas tardes", True, 1.9]
print(lista[0]) # Entre los corchetes va la ubicacion de los arrays, en programacion se empieza a contar desde 0 #? Hola


#-------------------------------------------------------------------------------------------#
# Tuplas son como listas pero con parentesis
# La diferencia es que las listas son editables, mientras que la tuplas no
tupla = ("Holas", "Buenas")
print(tupla[1]) #? Beunas


#-------------------------------------------------------------------------------------------#
# Editar listas
lista[1] = "holaaa"
print(lista[1]) #? holaaa

# Editar tuplas es incorrecto hacerlo, son inmutables
# tupla[1] = "holaaa"
# print(tupla[1])


#-------------------------------------------------------------------------------------------#
# Conjuntos son listas pero desordenadas, es decir que un valor puede estar en cualquier posicion
conjunto = {"Hola", "Buenas tardes", True, 1.9}
print(conjunto) #? {'Buenas tardes', True, 1.9, 'Hola'}
# Los conjuntos no pueden ser editados, pero si redefinidos
# Redefiniendo:
conjunto = {'jijijija', "hola"}
print(conjunto) #? {'hola', 'jijijija'}


#-------------------------------------------------------------------------------------------#
# Dato de los conjuntos: Los datos no se pueden repetir y no se puede llamar por ubicaciones, ej: conjunto[1] (es incorrecto)
conjunto2 = {"dato 1", "dato 2", "dato 1"}
print(conjunto2) #? {'dato 2', 'dato 1'}


#-------------------------------------------------------------------------------------------#
# Diccionario (dict o sets), la estructura es key : value y separamos con comas
diccionario = {
    "Nombre": "Stephen",
    "Edad": 36,
    "Altura": 1.88
}

#En vez de imprimir por indice, es decri por numeros de ubicaciones, imprimimos por texto. Ejemplo:
print(diccionario["Nombre"]) #? Stephen