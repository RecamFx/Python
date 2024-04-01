# Modificamos la W por la A
# A de append:
# Write siempre sobreescribe el texto, append agrega texto

with open("Parte 3\\archivosTXT\\agregar.txt", "a", encoding="UTF-8") as archivoTXT:
    archivoTXT.write("Texto agregado!\n")