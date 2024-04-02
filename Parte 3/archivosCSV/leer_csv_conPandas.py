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
print("--------------------------------")


# Podemos cambiar el encabezado
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


# --------------------------------------------------------------------------------------------------------------------------- #
print("--------------------------------")


# Ordenando los valores segun (en este cado la edad)
DataFrame3 = pd.read_csv("Parte 3\\archivosCSV\\leer.csv")


# Forma ascendente
# Usando el metodo sort_values() dentro del parentesis ponemos el valor a ordenar
DataFrame3_Ordenado_Asendente = DataFrame3.sort_values("edad") # Es importante almacenarlo en otro valor ya que es un valor anonimo

print(DataFrame3_Ordenado_Asendente)
#?     nombre  apellido  edad
#? 0  Stephen     Curry    36
#? 2   LeBron     James    39
#? 3     Manu  Ginobili    46
#? 1  Michael    Jordan    61


print("--------------------------------")

# Forma descendente
DataFrame3_Ordenado_Desendente = DataFrame3.sort_values("edad", ascending=False) 
# Usamos el atributo ascending, que ordena de forma ascendente por defecto, y lo configuramos false para que ordene de forma descendente

print(DataFrame3_Ordenado_Desendente)
#?     nombre  apellido  edad
#? 1  Michael    Jordan    61
#? 3     Manu  Ginobili    46
#? 2   LeBron     James    39
#? 0  Stephen     Curry    36



# --------------------------------------------------------------------------------------------------------------------------- #
print("--------------------------------")


# Que pasa si quiero concatenar dos data frames?

df1 = pd.read_csv("Parte 3\\archivosCSV\\leer.csv")
df2 = pd.read_csv("Parte 3\\archivosCSV\\leer.csv")


# Usando el metodo concat() y dentro del parentesis le pasamos una lista con los archivos a concatenar
df_Concatenado = pd.concat([df1, df2])

print(df_Concatenado)