frutas = ["manzana", "banana", "naranja", "uva", "pera", "sandía"]

# Usar la sentencia continue
# El continue hace que se saltee al siguiente bucle
for fruta in frutas:
    if fruta == "uva":
        continue
    print(fruta)
    
#? manzana
#? banana
#? naranja
#? pera
#? sandía
    
# BREAK
# Break corta el bucle, es la finalizacion de este
for fruta in frutas:
    print(fruta)
    if fruta == "naranja":
        break

# El break corta todo, es decir, si ponemos un else si el bucle termina por un break se corta todo (ni si quiera se ejecuta el else)
    
#? manzana
#? banana
#? naranja

