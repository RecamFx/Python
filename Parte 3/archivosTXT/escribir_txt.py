# Abrimos el archivo, y decimos que es de escritura poniendo "w"

with open("Parte 3\\archivos\\escritura.txt", "w", encoding="UTF-8") as archivoTXT: # En caso de no encontrar un archivo, lo crea
    #archivoTXT.write("JIJIJA") # El metodo write() reescribe el archivo. Solo compatible con strings
    
    # Usando writelines podemos poner listas
    archivoTXT.writelines(["Hola", " como", " estas?", "\nEspaciado de lineas"]) # Con el \n hacemos espaciados de lineas
    


# Escribiendo varias veces
with open("Parte 3\\archivos\\escritura2.txt", "w", encoding="UTF-8") as archivoTXT2:
    archivoTXT2.write("Hola buenos dias!\n")
    archivoTXT2.write("Como andas?")
    
    

#todo WRITE: Escribe cadenas de texto
#todo WRITELINES: Escribe listas de texto