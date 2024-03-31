frutas = ["manzana", "banana", "naranja", "uva", "pera", "sandía"]

# Usar la sentencia continue
# El continue hace que se saltee al siguiente bucle
for fruta in frutas:
    if fruta == "uva":
        continue
    print(fruta)
    
#? manzana
#? banana
#? naranja
#? pera
#? sandía
    
    
    
# --------------------------------------------------------------------------------------------------------------#
    
    
    
# BREAK
# Break corta el bucle, es la finalizacion de este
for fruta in frutas:
    print(fruta)
    if fruta == "naranja":
        break

# El break corta todo, es decir, si ponemos un else si el bucle termina por un break se corta todo (ni si quiera se ejecuta el else)
    
#? manzana
#? banana
#? naranja


# --------------------------------------------------------------------------------------------------------------#

# Recorrer una cadena de texto
texto = "Hola Mundo"

# Forma mala de hacerlo    
#for i in range(len(texto)):
#    print(texto[i])

# Forma correcta
for letra in texto:
    print(letra)

#? H
#? o
#? l
#? a
#? 
#? M
#? u
#? n
#? d
#? o


# --------------------------------------------------------------------------------------------------------------#


# Como duplico numeros de una lista? (es un ejemplo)
numeros = [2,6,5,10]

numeros_duplicados = [x*2 for x in numeros] # Le decimos que X se multiplique el valor, y a X le asignamos un valor de la lista, pero como era X*2 si le ponemos un numero lo multiplica por dos
print(numeros_duplicados) #? [4, 12, 10, 20]

