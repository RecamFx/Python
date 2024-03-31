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