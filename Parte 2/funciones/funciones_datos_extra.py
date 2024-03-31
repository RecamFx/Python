# PARAMETROS NO POSICIONALES
def asd(nombre, apellido):
    print(f"Hola {nombre} {apellido}")
    
# Definimos los parametros con igual
asd(apellido="Curry", nombre="Stephen") # Son parametros forzados #? Hola Stephen Curry



#--------------------------------------------------------------------------------------------------#



# Cambiando un parametro opcional
# El parametro apellido ya viene por defecto con un valor, es opcional cambiarlo
def prueba(nombre, apellido = "pruebadeapellido"):
    print(f"Hola {nombre} {apellido}")
    
prueba("Stephen")  #? Hola Stephen pruebadeapellido
prueba("Stephen", "Curry")  #? Hola Stephen Curry
prueba("Stephen", apellido="Curry")  #? Hola Stephen Curry