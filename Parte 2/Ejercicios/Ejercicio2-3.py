# EJERCICIO 3:
# Muestra la serie de fibonacci desde el 1 hasta el numero que se dijo

#todo MI SOLUCION:

numero = int(input("Ingresa un numero: "))
anterior = 1
valor = 1
bucle = True

while bucle:
    anterior2 = valor
    valor = valor + anterior
    anterior = anterior2
    if valor>numero: 
        bucle = False
    else:
        print(valor)
        
        
#todo OTRA SOLUCION:

#creando una funcion que muestre la serie fibonacci entre 0 el numero dado

def fibonacci(num):
    a,b = 0,1
    fibonacci_lista = [0]
    for i in range(num):
        if b > num: return fibonacci_lista
        else: 
            fibonacci_lista.append(b)
            a,b = b,a+b

resultado = fibonacci(34)
print(resultado)