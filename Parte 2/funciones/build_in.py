# Las funciones build in son funciones ya creadas por python
# Ejemplos: 

#---------------------------------------------------------------------------------------------------------#

# MAX y MIN
# Numero maximo y minimo
numeros = [6,2,9,7,8]
numeroMasAlto = max(numeros)
print(numeroMasAlto) #? 9
numeroMasBajo = min(numeros)
print(numeroMasBajo) #? 2


#---------------------------------------------------------------------------------------------------------#



# ROUND()
# Redondeando un numero a 6 decimales

# Forma anterior de rendondear decimales
numero = 10.345678
print(round(numero * 100) / 100) #? 10.35

# Forma nueva
print(round(numero,2)) # Primer parametro el numero, el segundo parametro, la cantidad de decimales #? 10.34



#---------------------------------------------------------------------------------------------------------#


# BOOL()
# La funcion bool retorna False si el valor es: 0, vacio, False, none

resultadoBooleano = bool(0)
print(resultadoBooleano) #? False

resultadoBooleano = bool([]) # Valor vacio de una lista
print(resultadoBooleano) #? False

resultadoBooleano = bool()
print(resultadoBooleano) #? False

resultadoBooleano = bool(False)
print(resultadoBooleano) #? False

resultadoBooleano = bool(None)
print(resultadoBooleano) #? False



#---------------------------------------------------------------------------------------------------------#


# ALL()
# Retorna true si todos los valores son verdaderos
# Es decir, retorna false si algunos de estos elementos se presentan: 0, vacio, False, none

resultadoALL = all([192, "asd", [5877, "hf"]])
print(resultadoALL) #? True


#---------------------------------------------------------------------------------------------------------#

# SUM()
# Suma todos los valores de un iterable

numeoros = [10, 34, 278]
print(sum(numeoros)) #? 322


#---------------------------------------------------------------------------------------------------------#

# FILTER()
# Le envia a una funcion un objeto iterable separado por sus caracteres, es decir en este caso 1,2,3,4,5,6,7,8,9. 
# Y los mete en una lista a los que se les returnea True

# Es decir, numero al que le returneemos true, lo filtramos en una lista aparte, eso es lo que hace Filter()

# En este caso decimos que a los numeros pares les returneamos True
# Por ende se van a mostrar solo esos

lista = [1,2,3,4,5,6,7,8,9]
def funcion(num):
    if(num%2 == 0): # Par impar
        return True

variable = filter(funcion, lista)
print(list(variable)) #? [2, 4, 6, 8]