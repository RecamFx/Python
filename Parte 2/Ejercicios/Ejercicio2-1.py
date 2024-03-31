# EJERCICIO:
# El profesor falto a la clase, ahora los alumnos la van a manejar
# Pedir a todos los alumnos que vinieron hoy, el nombre y edad
# El nuevo profesor va a ser el que tiene mas edad y su asistente el que tiene menos edad
# Quienes son?


#todo SOLUCION 1 :
alumnos = []
edad = []

cantidadAlumnos = input("Cuantos alumnos vinieron hoy a clase: ")

for i in range(int(cantidadAlumnos)):
    alumnos.append(input("Nombre: "))
    edad.append(input("edad: "))

mayor = max(edad)
menor = min(edad)

profe = alumnos[edad.index(mayor)]
asistente = alumnos[edad.index(menor)]

print(f"Su nuevo profesor es: {profe}, y su asistente: {asistente}") 




#todo SOLUCION 2:

#funciòn para obtener al asistente y al profesor segun la edad.
def obtener_compañeros(cantidad_de_compañeros):
    
    #creando la lista con los compañeros
    compañeros = []
    
    #ejecutando un for para pedir informaciòn de cada compañero
    for i in range(cantidad_de_compañeros):
        nombre = input("ingrese el nombre del compañero: ")
        edad = int(input("ingrese la edad del compañero: "))
        compañero = (nombre,edad)
        
        #agregando la informaciòn a la lista
        compañeros.append(compañero)
        
    #ordenandolos de menor a mayor segùn su edad    
    compañeros.sort(key=lambda x:x[1])
    
    #compañeros[x] devuelve una tupla con (nombre,edad) y despues accedemos al nombre
    #para definir al asistente y al profesor.
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    
    #retornamos una tupla
    return asistente,profesor

#desempaquetamos lo que nos retorna la funciòn
asistente,profesor = obtener_compañeros(5)

#mostrando el resultado
print(f"El profesor es: {profesor} y su asistente es {asistente}")