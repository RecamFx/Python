# Como manejar excepciones
# Vamos a dar un ejemplo sumando dos numeros de lo cual el primero va a ser una palabra

def sumar():
    while True:
        a = input("Numero 1: ") #? Numero 1:
        b = input("Numero 2: ") #? Numero 2:
        # Usamos la sentencia try
        try: # Intenta ejecutar el codigo
            return int(a)+int(b)
        except Exception as e: # en caso de una excepcion se ejecuta except #todo Podemos poner Exception despues del except para que nos diga que tipo de error ocurrio
            print("Te pedi un numero") #? Te pedi un numero
            print(f"ERROR: {e}")
        else:
            break # Rompemos el while si se ejecuta try
        finally: # El finally se ejecuta siempre, sin importar el resultado del try o del except. #todo Rara vez es util
            print("Manejo de excepcion finalizado")


# Etonces la logica es la siguiente:
# Creamos un bucle que nos pida dos numeros para sumarlos
# Intentamos hacer la suma con try
# En caso de lograrlo, como try no tiro error pasamos al else, donde se cierra el bucle
# En caso de que tire un error que seria si escribimos algo que no sea un numero, ejecutar el except y volver al bucle

#todo IMPORTANTE: El else se ejectura unicamente si el try funciona. Si el try no funciona y pasa al except, el else no se ejecuta
print(sumar()) #? Suma