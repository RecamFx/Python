# Importamos csv
import csv 
# Esta libreria sirve para leer archivos csv


# Leemos un archivo csv
with open("Parte 3\\archivosCSV\\leer.csv", "r", encoding="UTF-8") as archivoCSV:
    reader = csv.reader(archivoCSV)
    for i in reader:
        print(i)
    #? ['nombre', 'apellido', 'edad']
    #? ['Stephen', 'Curry', '36']
    #? ['Michael', 'Jordan', '61']     