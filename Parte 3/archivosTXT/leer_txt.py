# OPEN
# Open es como un import pero para archivos que no son python

# El encoding="UTF-8 sirve para que funcionen las tildes
archivo = open("Parte 3\\archivosTXT\\notas.txt", encoding="UTF-8")


# -----------------------------------------------------------------------------------------------------------------------#
# Dato: Los archivos solo pueden leerse 1 vez
# Es decir, no podemos poner .read() y despues .readlines()

# -----------------------------------------------------------------------------------------------------------------------#
# Usamos el metodo read() para leer un txt
#todo print(archivo.read())
#? Buenos dias, como estás?
#? Stephen Curry

# -----------------------------------------------------------------------------------------------------------------------#
# Para leer lineas del archivo txt usamos readlines()
# Los \n son separaciones entre lineas
#todo print(archivo.readlines())
#? ['Buenos dias, como estás?\n', 'Stephen Curry']

# -----------------------------------------------------------------------------------------------------------------------#
# Podemos usar readline()
# Sirve para leer la primera linea o una cantidad de caracteres asignados
print(archivo.readline(10)) # Leemos diez caracteres 
#? Buen Dia

# -----------------------------------------------------------------------------------------------------------------------#
# Cerrar el archivo
archivo.close()
# Al usar close se cierra el archivo, si lo queremos leer otra vez, tenemos que poner un open()