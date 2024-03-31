# EJERCICIO:
# Decirle un numero, y que me responda con todos los numeros primos que existen hasta el numero dicho


#todo MI SOLUCION:
def primo(num):
    
    lista = []
    numeros = [lista.append(i) for i in range(2, num)]
    
    division = filter(lambda numeritos: num%numeritos==0, lista)
    if bool(list(division)) == False:
        return 0
    else:
        return 1
        
numero = int(input("Ingrese el numero: "))
        
lista2 = []
numeros = [lista2.append(i) for i in range(2, numero+1)]


for i in lista2:
    if primo(i) == 0:
        print(f"El numero {i} es primo")
        
        
#todo OTRA SOLUCION:

