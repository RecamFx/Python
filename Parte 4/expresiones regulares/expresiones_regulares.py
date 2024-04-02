# Importamos el modulo re oficial de python
# Es el modulo mas usado para usar expresiones regulares

# Con expresiones regulares trabajamos patrones
import re

texto = """Hola buenos dias! Cadena 1
Segunda linea de texto (Linea 2)
Tercera linea de texto (Linea 30)"""

texto2 = """Hola buenos dias! Cadena 1. 
Segunda linea de texto (Linea 2).
Tercera linea de texto (Linea 30)."""

texto3 = """Hola buenos dias!
me llamo pepito
soy pepito"""

texto4 = """Holaaa!
aabbb
ababab
jijija"""

# Search es para buscar solo una coincidencia, findall es para buscar varias coincidencias


# search()
resultado = re.search("Hola", texto) # Busca la palabra hola
print(resultado) #? <re.Match object; span=(0, 4), match='Hola'>


# BUSQUEDA SIMPLE

# findall() busca todas las coincidencias en el texto y las devuelve en una lista
# El primer parametro es el texto a buscar, el segundo en donde se busca, 
# y el tercero podemos poner flags=re.IGNORECASE que lo que hace es ignorar minusculas y mayusculas
resultado = re.findall("Hola",texto,flags=re.IGNORECASE)
print(resultado) #? ['Hola']

#-------------------------------------------------------------------------------#

# Expresiones regulares
# Usando la f"" y posterior las comillas indicabamos que ibamos a concatenar
# Ahora usando la r"" indicamos que vamos a usar expresiones regulares


#\d --> Busca digitos numericos del 0 al 9
#resultado = re.findall(r"\d",texto) #? ['1', '2', '3', '0']

#\D --> Busca TODO MENOS digitos numericos del 0 al 9
#resultado = re.findall(r"\D",texto) #? ['H', 'o', 'l', 'a', ' ', 'b', 'u', 'e', 'n', 'o', 's', ' ', 'd', 'i', 'a', 's', '!', ' ', 'C', 'a', 'd', 'e', 'n', 'a', ' ', '\n', 'S', 'e', 'g', 'u', 'n', 'd', 'a', ' ', 'l', 'i', 'n', 'e', 'a', ' ', 'd', 'e', ' ', 't', 'e', 'x', 't', 'o', ' ', '(', 'L', 'i', 'n', 'e', 'a', ' ', ')', '\n', 'T', 'e', 'r', 'c', 'e', 'r', 'a', ' ', 'l', 'i', 'n', 'e', 'a', ' ', 'd', 'e', ' ', 't', 'e', 'x', 't', 'o', ' ', '(', 'L', 'i', 'n', 'e', 'a', ' ', ')']

#todo-----------------------------------------------------------------------------------------------------------------

#\w --> Busca caracteres alphanumericos [a-z A-Z 0-9 _]
#resultado = re.findall(r"\w",texto) #? ['H', 'o', 'l', 'a', 'b', 'u', 'e', 'n', 'o', 's', 'd', 'i', 'a', 's', 'C', 'a', 'd', 'e', 'n', 'a', '1', 'S', 'e', 'g', 'u', 'n', 'd', 'a', 'l', 'i', 'n', 'e', 'a', 'd', 'e', 't', 'e', 'x', 't', 'o', 'L', 'i', 'n', 'e', 'a', '2', 'T', 'e', 'r', 'c', 'e', 'r', 'a', 'l', 'i', 'n', 'e', 'a', 'd', 'e', 't', 'e', 'x', 't', 'o', 'L', 'i', 'n', 'e', 'a', '3', '0']

#\W --> Busca TODO MENOS caracteres alphanumericos [a-z A-Z 0-9 _]
#resultado = re.findall(r"\W",texto) #? [' ', ' ', '!', ' ', ' ', '\n', ' ', ' ', ' ', ' ', '(', ' ', ')', '\n', ' ', ' ', ' ', ' ', '(', ' ', ')']

#todo-----------------------------------------------------------------------------------------------------------------

#\s --> Busca espacios en blanco --> espacios, tabs y saltos de lineas
#resultado = re.findall(r"\s",texto) #? [' ', ' ', ' ', ' ', '\n', ' ', ' ', ' ', ' ', ' ', '\n', ' ', ' ', ' ', ' ', ' ']

#\S --> Busca TODO MENOS espacios en blanco --> espacios, tabs y saltos de lineas
#resultado = re.findall(r"\S",texto) #? ['H', 'o', 'l', 'a', 'b', 'u', 'e', 'n', 'o', 's', 'd', 'i', 'a', 's', '!', 'C', 'a', 'd', 'e', 'n', 'a', '1', 'S', 'e', 'g', 'u', 'n', 'd', 'a', 'l', 'i', 'n', 'e', 'a', 'd', 'e', 't', 'e', 'x', 't', 'o', '(', 'L', 'i', 'n', 'e', 'a', '2', ')', 'T', 'e', 'r', 'c', 'e', 'r', 'a', 'l', 'i', 'n', 'e', 'a', 'd', 'e', 't', 'e', 'x', 't', 'o', '(', 'L', 'i', 'n', 'e', 'a', '3', '0', ')']

#todo-----------------------------------------------------------------------------------------------------------------

#. --> Busca todo menos saltos de lineas
#resultado = re.findall(r".",texto) #? ['H', 'o', 'l', 'a', ' ', 'b', 'u', 'e', 'n', 'o', 's', ' ', 'd', 'i', 'a', 's', '!', ' ', 'C', 'a', 'd', 'e', 'n', 'a', ' ', '1', 'S', 'e', 'g', 'u', 'n', 'd', 'a', ' ', 'l', 'i', 'n', 'e', 'a', ' ', 'd', 'e', ' ', 't', 'e', 'x', 't', 'o', ' ', '(', 'L', 'i', 'n', 'e', 'a', ' ', '2', ')', 'T', 'e', 'r', 'c', 'e', 'r', 'a', ' ', 'l', 'i', 'n', 'e', 'a', ' ', 'd', 'e', ' ', 't', 'e', 'x', 't', 'o', ' ', '(', 'L', 'i', 'n', 'e', 'a', ' ', '3', '0', ')']

#n\ --> Busca saltos en liena
#resultado = re.findall(r"\n", texto) #? ['\n', '\n']

#todo-----------------------------------------------------------------------------------------------------------------

#\ --> Cancelar caracteres especiales
# Es decir, si quiero buscar puntos, si pongo el punto me va a saltar (Busca todo menos saltos de lineas) pero si le pongo la barra adelante
# Me va a cancelar eso y va a buscar directamente y literalmete un punto
#resultado = re.findall(r"\.", texto2) #? ['.', '.', '.']

#todo-----------------------------------------------------------------------------------------------------------------

# Armando una cadena que busque un numero, seguido de un punto y un espacio
#resultado = re.findall(r"\d\.\s",texto2) # Busca literalmente un numero cualquiera seguido de un punto y un espacio. EJEMPLO: "9. " #? ['1. ']

#todo-----------------------------------------------------------------------------------------------------------------

# Busca el comienzo de una linea
#resultado = re.findall(r"^Hola",texto2,flags=re.M) # Pregunta si "Hola" esta al principio de la cadena #? ['Hola']
# Si esta, crea una lista con el valor encontrado
# Si no esta, crea una lista vacia

# Podemos usar el flags=-re.M que significa que cada salto de liena lo interpresa como una linea nueva,
# por ende vamos a apoder buscar en todos los saltos de lineas

#todo-----------------------------------------------------------------------------------------------------------------

#$ --> Busca el final de una liena
#resultado = re.findall(r"pepito$",texto3,flags=re.M) #? ['pepito', 'pepito']

#todo-----------------------------------------------------------------------------------------------------------------

# {n} --> Busca n cantidad de veces el valor de la izquierda
# En este caso busca \d (que son numeros) en una cantidad de dos veces seguidas
#resultado = re.findall(r"\d{2}",texto2,flags=re.M) #? ['30']

#todo-----------------------------------------------------------------------------------------------------------------

# {n,m} --> Busca minimamente n y maximamente m cantidad de veces del valor de la izquierda
#resultado = re.findall(r"\d{1,3}",texto2) #? ['1', '2', '30']

# {n,m} --> Busca minimamente n y maximamente m cantidad de veces del valor de la izquierda
#resultado = re.findall(r"(ab){1,3}",texto4) #? ['ab', 'ab']
#resultado = re.findall(r"[ab]{1,3}",texto4) #? ['aaa', 'aab', 'bb', 'aba', 'bab', 'a']

#todo-----------------------------------------------------------------------------------------------------------------

# | --> Busca lo que esta a ala izquierda del operador o a la derecha
resultado = re.findall(r"\d|Hola",texto) #? ['Hola', '1', '2', '3', '0']

#todo-----------------------------------------------------------------------------------------------------------------


print(resultado)


# Faltaron los signos *, + y el -