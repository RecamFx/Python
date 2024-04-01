import modulo_saludar # Importamos un codigo


respuesta = modulo_saludar.saludar("Stephen") # Ahora llamamos al codigo y le pedimos ejecutar la funcion saludar
print(respuesta) #? Hola Stephen!



#--------------------------------------------------------------------------------------------------------------------#


# Usando la funcion as
# Esta sentencia hace que podamos renombrar el nombre de un modulo, para no tener que llamarlo como el archivo
import modulo_saludar as ms # La renombramos a "ms"

respuesta = ms.saludar("Stephen2") # Ahora llamamos al codigo y le pedimos ejecutar la funcion saludar
print(respuesta) #? Hola Stephen2!



#--------------------------------------------------------------------------------------------------------------------#


# Importamos de a funciones, en vez de a codigo
from modulo_saludar import saludar as jiji2, saludar2 as jiji # Podemos renmombrar las funciones de los modulos
print(jiji2 ("Stephen3")) #? Hola Stephen3!
print(jiji("Stephen3")) #? NASHEI Stephen3!


#--------------------------------------------------------------------------------------------------------------------#



# Importando todos las funciones sin tener que utilizar el nombre del modulo
from modulo_saludar import * # Con el asterisco importamos todas las funciones sin usar el "modulo.funcion()"
# Esto es una mala practica, porque si el modulo es muy extenso, el programa se sobrecarga
# Preferible es importar solo lo necesario



#--------------------------------------------------------------------------------------------------------------------#
# Tambien se pueden importar variables

# Inecesario
# Podemos usar el metodo name para ver el nombre de un modulo
import modulo_saludar as kkkk 
hola =  kkkk.__name__
print(hola) #? modulo_saludar
print(__name__) # Nos va a tirar main porque se le define main al modulo que se ejecute, que es este. #? __main__



#--------------------------------------------------------------------------------------------------------------------#
# Importando modulos desde una carpeta
# Enrutamiento de modulos

import funcionesModulos.moduloEjemplo

print(funcionesModulos.moduloEjemplo.saludar("Stephen")) #? Hola Stephen!
print(funcionesModulos.moduloEjemplo.saludar2("Stephen")) #? NASHEI Stephen!