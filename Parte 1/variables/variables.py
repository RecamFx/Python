# Las variables almacenan valores
# Las variables se declaran y se definen
print("Variables: ") #? Variables:

a = 1
b = 2
c = a + b
ejemplo = "hola"

print(c) #? 3
print(ejemplo) #? hola

# Ejemplos:
print("Ejemplos: ") #? Ejemplos:

num = 10
num += 1 # Dice que el numero mas (en este caso es el operador) lo que va despues del igual

print(num) #? 11

# Concatenacion
print("Concatenacion: ") #? Concatenacion:

bienvenida = "Hola "
nombre = "Stephen"
bienvenida2 = bienvenida + nombre

print(bienvenida + nombre) #? Hola Stephen
print(bienvenida2) #? Hola Stephen

# Concatenacion con "f strins"
print("F strins: ") #? F struns

name = 'Luis'
number = 2
boolean = True
example = f"Hola {name} como estas?" # En vez de escribir "Hola " + nombre + " como estas?"
example = f"Buenas {name}, con el numero {number} y un boleano {boolean}"
# Lo que hace esto es que agarra un tipo de dato y lo transforma automaticamente a un string
# Se usa poniendo la f antes del texto y dentro del texto las llaves {variable} con el nombre de la variable

#Eliminar una variable

ejemplo2 = "Hola"
print(ejemplo2) #? Hola

#del ejemplo2 # Eliminamos la variable ejemplo 2
print(ejemplo2) #? Hola


# Operador in
ex = "hola buenos dias"
print("hola" in ex) # in lo que haces es buscar el valor asignado en una variable, como hola esta en la variable ex nos arroja que es verdadero #? True
print("ejemplo" not in ex) # ahora esto busca lo que no esta, la palabra ejemplo no esta en ex, por eso nos arroja true #? True
# Si la palabra no la escribimos correctamente (Mayusculas y minusculas) no lo va a detectar, es sensitive (sensibel a minusculas y mayusculas)