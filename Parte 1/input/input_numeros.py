# Pedirle un numero al usuario

numero = input("Dame un numero: ")
cuenta = numero * 2

print(cuenta) #? Texto que escribiste duplicado

# Porque pasa eso? 
#?  "6" * 2 = "66"
#?   6  * 2 =  12
#Como es un texto, se suman o multiplican los caracteres. En vez de numeros

# Solucion, convertirlo a numero

cuenta = int(numero) * 2 #
print(cuenta) #? Numero que escribiste por dos

# Con la funcion int() convertimos a enteros
# Y con float() a numeros con coma

# 9.0 no es igual a 9   Porque uno es un float y otro un int