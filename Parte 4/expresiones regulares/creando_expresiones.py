import re
# Detectando un numero de argentina y oculatandolo

texto = "Hola soy pipipip, mi numero es: +54 11 4321-4321"

# \s espacio
# \d numero
# \ cancela el caracter especial
patron = r"\+\d{2}\s\d{2}\s\d{4}\-\d{4}"

reemplazar = re.sub(patron,"(Numero Oculto)", texto)

print(reemplazar)