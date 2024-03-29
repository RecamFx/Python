# Modificamos una lista dentro de una tupla
lista = ['hola', ['hola2', "jijija"]]
lista2 = tuple(lista)
lista2[1][1] = 19
print(lista2)