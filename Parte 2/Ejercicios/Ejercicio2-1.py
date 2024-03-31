# EJERCICIO:
# El profesor falto a la clase, ahora los alumnos la van a manejar
# Pedir a todos los alumnos que vinieron hoy, el nombre y edad
# El nuevo profesor va a ser el que tiene mas edad y su asistente el que tiene menos edad
# Quienes son?


# SOLUCION:
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