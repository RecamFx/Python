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
#?     nombre  apellido  edad
#? 0  Stephen     Curry    36
#? 1  Michael    Jordan    61
#? 2   LeBron     James    39
#? 3     Manu  Ginobili    46
#? 0  Stephen     Curry    36
#? 1  Michael    Jordan    61
#? 2   LeBron     James    39
#? 3     Manu  Ginobili    46



# --------------------------------------------------------------------------------------------------------------------------- #
print("--------------------------------")

# Accediendo a filas especificas


df = pd.read_csv("Parte 3\\archivosCSV\\leer.csv")

# Usando el metodo head() en el parentesis asignamos hasta que fila desea mostrar empezando desde arriba a abajo
primera_fila = df.head(3)
print(primera_fila)
#?     nombre apellido  edad
#? 0  Stephen    Curry    36
#? 1  Michael   Jordan    61
#? 2   LeBron    James    39


print("--------------------------------")
# Usando el metodo tail() en el parentesis asignamos hasta que fila desea mostrar empezando desde abajo a arriba
ultima_fila = df.tail(3)
print(ultima_fila)

#?     nombre  apellido  edad
#? 1  Michael    Jordan    61
#? 2   LeBron     James    39
#? 3     Manu  Ginobili    46




# --------------------------------------------------------------------------------------------------------------------------- #

# Accediento a la cantidad de filas y columnas

# Usamos el metodo shape
filas_y_columnas = df.shape
# Nos devuelve primero la cantidad de filas y despues la cantidad de columnas
print(filas_y_columnas) #? (4, 3)


# Podemos usar la funcion de desempaquetar para seprara estos valores
filas, columnas = df.shape
print(filas) #? 4
print(columnas) #? 3




# --------------------------------------------------------------------------------------------------------------------------- #

# Obteniendo datos estadisticos
# Esto es mas para analisis de datos

# Usamos el metodo describe()
df_info = df.describe()
print(df_info)

#?             edad
#? count   4.000000
#? mean   45.500000
#? std    11.150486
#? min    36.000000
#? 25%    38.250000
#? 50%    42.500000
#? 75%    49.750000
#? max    61.000000