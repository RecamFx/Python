# Dos listas
# Una con nombres y otra con apellidos

nombres = ["Stephen", "Michael", "Manu"]
apellidos = ["Curry", "Jordan", "Ginobili"]

# DOS FORMAS DE RESOLVERLO

# with open("Parte 3\\Resolviendo Problemas\\archivo.txt", "w",encoding="UTF-8") as txt:
#     for i in range(len(nombres)):
#         txt.write(f"{nombres[i]} {apellidos[i]} \n")

with open("Parte 3\\Problemas CSVTXT\\archivo.txt", "w",encoding="UTF-8") as txt:
    [txt.write(f"{n} {a} \n") for n,a in zip(nombres,apellidos)] # El zip lo utilizamos porque no se puede poner nombre,appellido