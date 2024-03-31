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