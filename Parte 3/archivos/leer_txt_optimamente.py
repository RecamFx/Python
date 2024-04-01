# Con with hacemos una mini funcion la cual:
# Abre el txt, ejecuta el codigo, y se cierra el txt al terminar
# Al cerrarse el txt es mejor, ya que no consume tanto a la PC

with open("Parte 3\\archivos\\notas.txt"):
    print("Hola") #? Hola
    
# -------------------------------------------------------------------------------------------------------------#
# Para asignarle un nombre usamos el as nombre
# Y para asignarle de que queremos que sea, ya sea de lectura, escritura,etc. Ponemos coma despues del archivo y entre comillas R (read), W(write)
# Por defecto viene de lectura (r)

with open("Parte 3\\archivos\\notas.txt", "r") as archivo:
    print("Hola") #? Hola
    
# -------------------------------------------------------------------------------------------------------------#
# Leerlo de forma optima

with open("Parte 3\\archivos\\notas.txt", encoding="UTF-8") as archivoTXT:
    print(archivoTXT.read())
    #? Buenos dias, como estás?
    #? Stephen Curry