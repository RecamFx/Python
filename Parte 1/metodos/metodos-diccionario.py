diccionario = {
    "Nombre" : "Stephen",
    "Apellido" : "Curry",
    "Edad" : 36
}


#------------------------------------------------------------------------------------------------------#

# KEYS Devuelve las claves (las claves son en este caso nombre, apellido y edad. Y los valores de las claves son los asignados, ej: Stephen, Curry, 36)
claves = diccionario.keys()
print(claves) #? dict_keys(['Nombre', 'Apellido', 'Edad'])


#------------------------------------------------------------------------------------------------------#

# GET Devuelve el valor de la clave llamada, en este caso llamamos a nombre, y su valor es "Stephen"
# Podemos pedirle un valor al diccionario asi: diccionario["Valor"], esto nos returnea a lo que es igual, pero si no lo encuentra nos manda error
# En cambio al usar get que es lo mismo que lo anterior pero si no encuentra el valor en vez de saltar error salta "None"
obtenerClaves = diccionario.get("Nombre")
print(obtenerClaves) #? Stephen
obtenerClaves = diccionario.get("asdasdasd")
print(obtenerClaves) #? None
#obtenerClaves = diccionario["asdasdasd"] #! Esto nos da error porque no lo encuentra


#------------------------------------------------------------------------------------------------------#

# CLEAR Todos los elementos del diccionario
#todo diccionario.clear()
#todo print(diccionario) #? {}


#------------------------------------------------------------------------------------------------------#

# POP Elimina solo un elemento del diccionario
#todo diccionario.pop("Nombre")
#todo print(diccionario) #? {'Apellido': 'Curry', 'Edad': 36}
# Ademas si la clave ingresada no se encuentra, devolvera lo que escribamos a continuacion 
print(diccionario.pop("Nombres", "Jijijija")) # Como no encuentra Nombres devuelve Jijijija #? Jijijija


#------------------------------------------------------------------------------------------------------#

# ITEMS Devuelve una lista con los keys y los values del diccionario, pero lo necesitamos transformar en una lista antes de usarlo
diccionario2 = diccionario.items()
# print(diccionario2[1]) #! Error
print(list(diccionario2)[1]) #? ('Apellido', 'Curry')
print(list(diccionario2)) #? [('Nombre', 'Stephen'), ('Apellido', 'Curry'), ('Edad', 36)]