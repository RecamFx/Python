# Importamos la libreria pandas como pd
import pandas as pd

# Esta libreria hay que instalarla manualmente:
# 1. Abrimos el cmd como administrador
# 2. escribimos: py -m pip install pandas


# Si vas a trabajar en ciencia de datos vas a utilizar jupiter notebook
# Se escribe en la barra de busqueda superior, >jupiter

# Esto es un df o data frame, tiene dos valores, filas y columnas
DataFrame = pd.read_csv("Parte 3\\archivosCSV\\leer.csv")
print(DataFrame)
#?     nombre  apellido  edad
#? 0  Stephen     Curry    36
#? 1  Michael    Jordan    61
#? 2   LeBron     James    39
#? 3     Manu  Ginobili    46

print(DataFrame["nombre"])
#? 0    Stephen
#? 1    Michael
#? 2     LeBron
#? 3       Manu



# --------------------------------------------------------------------------------------------------------------------------- #


# Podemos cambiar el encabezado
print("--------------------------------")

# Con el atributo names= le podemos decir como se va a llamar cada columna
DataFrame2 = pd.read_csv("Parte 3\\archivosCSV\\leer.csv", names=["name", "lastname", "age"])
print(DataFrame2)
#?       name  lastname   age
#? 0   nombre  apellido  edad
#? 1  Stephen     Curry    36
#? 2  Michael    Jordan    61
#? 3   LeBron     James    39
#? 4     Manu  Ginobili    46


# La diferencia es que ahora nos muestra nombre, apellid y edad, porque es como que lo toma parte