
def suma(a,b):
    return a+b

print(suma(1,2)) #? 3
# Pero que pasa si quiero sumar mas numeros, o almenos una cantidad que no conozco?

# La forma normal de hacerlo seria usando una lista:
# Forma no optima
def suma2(lista):
    sumas = 0
    for i in lista:
        sumas = sumas + i
    return sumas

print(suma2([1,2,3,4,10])) #? 20

# Pero como lo hacemos mas simple?

# Forma optima (utilizando el parametro args)
def suma3(name, *num): # El asterisco(*) junta a todos los parametros como si fueran una lista (tupla).
    print(f"{name} la suma de tus numeros es: {sum(num)}")

# DATO: Este parametro tiene que ser el ultimo en usarse, es decir, si vamos a usar parametros, queremos que este sea el utlimo
    
suma3("Stephen",1,2,3,4,5,6,7) #? 28
# Ya no necesitamos crear una lista



#--------------------------------------------------------------------------------------------------#



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