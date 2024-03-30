# Creamos un conjunto con la funcion set()

lista = ["hola", "Buenas tardes", "Jijijija"]
conjunto = set(lista)

print(conjunto) #? {'Buenas tardes', 'hola', 'Jijijija'}


# Creamos un conjunto en base a una lista dentro de otra lista
# No se pueden crear conjuntos con datos mutables, como ya sabemos, los conjuntos son datos inmutables, por ende no se puden editar
# Pero el problema viene con la lista dentro de el conjunto, porque al ser una lista es modificable y ordenada pero el conjunto no lo es. Por ende tira error!
lista2 = ["Hola", ["holaa", "hola2"]]
# conjunto = set(lista2) #! TypeError: unhashable type: 'list'

# print(conjunto) #! TypeError: unhashable type: 'list'



# Como hago para mete un conjunto dentro de otro conjunto?
# Usamos la funcion frozenset()

conjunto1 = frozenset({"Hoka", "Hola2"})
conjunto2 = {conjunto1, "Hola4"}

print(conjunto2) #? {frozenset({'Hola2', 'Hoka'}), 'Hola4'} 


# Teoria de conjuntos
conjunto1 = {1, 2, 3}
conjunto2 = {3, 2, 1, 7, 4, 9}

# El metodo issubset nos devuelve si un conjunto es un subconjunto de otro
# Un subconjunto es un conjunto chico este dentro de otro mas grande
resultado = conjunto1.issubset(conjunto2)
#todo resultado = conjunto1 <= conjunto2
print(resultado) #? True
resultado = conjunto2.issubset(conjunto1)
print(resultado) #? False

# Metodo issuperset
# Un superconjunto es si un conjunto grande posee a un conjunto chico
resultado = conjunto1.issuperset(conjunto2)
#todo resultado = conjunto1 > conjunto2
print(resultado) #? False
resultado = conjunto2.issuperset(conjunto1)
print(resultado) #? True