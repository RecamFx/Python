# Creando un diccionario
diccionario = {
    "nombre": "Stephen",
    "appelido": "Curry",
    "edad": "36"
}

# Diccionario {"clave o key": "valor o value"}

# Imprime solo las claves del diccionario
for i in diccionario:
    print(i)

#? nombre
#? appelido
#? edad

# Imprimir los valores usando el metodo item()
# En metodos de diccionario se explico que item sirve para iterar elementos
for i in diccionario.items():
    clave = i[0]
    valor = i[1]
    print(f"Clave: {clave}, Valor: {valor}")

#? Clave: nombre, Valor: Stephen
#? Clave: appelido, Valor: Curry
#? Clave: edad, Valor: 36