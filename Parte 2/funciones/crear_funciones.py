# Como crear una funcion

# def nombre_de_la_funcion(parametros)
def saludar():
    print("Hola buenos dias")
    
# Ejecutando una funcion
saludar() #? Hola buenos dias



#---------------------------------------------------------------------------------------------------------#


# Un parametro es una variable la cual solo existe dentro de la funcion, se crea unicamente para la funcion
# Funcion con parametros

def saludo(nombre, genero):
    if genero == "hombre":
        print(f"Hola {nombre} maestro! Como estas?")
    else:
        print(f"Hola {nombre} maestra! Como estas?")
    
saludo("Stephen", "hombre") #? Hola Stephen maestro! Como estas?


#---------------------------------------------------------------------------------------------------------#


# Crear una funcion que retorne valores

def cuentas(num):
    jijijija = num * 2
    return jijijija # Returnea el valor

# Cuando un valor es returneado automaticamente la funcion en este caso "cuenta(2)" se transforma en un valor
# Por ende el valor si lo ponemos en la nada va a desaparecer
# Entonces lo imprimimos

print(cuentas(2)) #? 4



# Retornar multiples valores

def jiji(num):
    multiplicacion = num * 2
    suma = num + 2
    resta = num - 2
    
    return [multiplicacion,suma,resta]

# Nos returnea dependo lo que hayamos hecho anteriormente, como lo puse en corchetes, nos returnea una lista
# Por defecto si no le ponemos nada, nos returnea una tupla
print(type(jiji(10))) #? List
print(jiji(10)) #? [20, 12, 8]

# Desempaquetando:
mutli,sumita,restita = jiji(10)
print(mutli)