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