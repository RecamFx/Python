# Para ahorrarnos escribir funciones cortas podemos usar lambda

# Funciones anonimas
mutliplicar = lambda num,asd: num*asd
# Esto es igual a:
# def multiplicar(num,asd):
#     return num*asd

# Primero lo almacenamos en una variable
# Despues usamos la palabra clave lambda y seguido el o los parametros, dos puntos, y lo que hace la funcion, en este caso mutliplicar

print(mutliplicar(5, 2)) #? 10

# Esta es solo apta para hacer 1 linea de codigo, si la funcion contiene mas habria que crear una funcion con def