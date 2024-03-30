# for in
# Recorriendo una lista:
animales = ["Pez", "Perro", "Gato", "Cocodrilo"]
# Le decimos que verifique con i (que empieza valiendo 0) mira la posicion 0 de animales, pum! Encontro Pez, abajo lo imprime, asi hasta cocodrilo
# Como no encontro nada mas termina el bucle
# La variable animales va a ejecutar tantas veces como la cantidad de elementos en la lista
for i in animales:
    print(i) 
#? Pez
#? Perro
#? Gato
#? Cocodrilo


# ---------------------------------------------------------------------------------- #


# Recorrer dos listas
# Para eso tienen que tener la misma cantidad de caracteres
# Usamos la funcion zip
lista1 = [1,2,3,4,5]
lista2 = ["hola", "buenos", "dias", "como", "estas"]

for i,a in zip(lista1,lista2):
    print(f"Lista 1: {i}")
    print(f"Lista 2: {a}")
    
#? Lista 1: 1
#? Lista 2: hola
#? Lista 1: 2
#? Lista 2: buenos
#? Lista 1: 3
#? Lista 2: dias
#? Lista 1: 4
#? Lista 2: como


# ---------------------------------------------------------------------------------- #


# Otra forma de iterar listas
# Usando la funcion range()

for i in range(3,10): # Si ecribo dos valores va a empezar a contar desde el primer valor hasta el ultimo (sin contar el ultimo)
    print(i)
    
#? 5
#? 7
#? 3
#? 6
#? 9
#? 8
#? 4


for i in range(5): # Si le ponemos un numero arranca desde el 0 hasta el numero que le pusimos (sin contar el ultimo)
    print(i)
    
#? 0
#? 1
#? 2
#? 3
#? 4


# ---------------------------------------------------------------------------------- #


lista3 = ["hola", "buenos", "dias", "como", "estas"]

# Forma no optima de reccorer una lista con su indice
for i in range(len(lista3)): #! No funciona para conjuntos
    print(lista3[i])
#? hola
#? buenos
#? dias
#? como
#? estas

# Forma optima de reccorer una lista con su indice
# La funcion enumerate() junta el numero del inice con el valor de la lista y lo imprime como una #!TUPLA
for i in enumerate(lista3):
    print(i)
    
# Indice y su valor
#? (0, 'hola')
#? (1, 'buenos')
#? (2, 'dias')
#? (3, 'como')
#? (4, 'estas')



for i in enumerate(lista3):
    print(f"Indice: {i[0]}, Valor: {i[1]}")

#? Indice: 0, Valor: hola
#? Indice: 1, Valor: buenos
#? Indice: 2, Valor: dias
#? Indice: 3, Valor: como
#? Indice: 4, Valor: estas


# ---------------------------------------------------------------------------------- #



# Usando el for/else:
# Si no quedan elementos por recorrer se va al else

for i in range(5):
    print(i)
else:
    print("El bucle termino!")

#? 0
#? 1
#? 2
#? 3
#? 4
#? El bucle termino





#todo FUNCIONA IGUAL PARA TUPLAS Y CONJUNTOS