import re

# Texto
texto = "La fecha es 02/04/2024 y el telefono es +1-555-555-5555"

# Patron a buscar
patron = r"\d{2}/\d{2}/\d{4}"

# Por que lo vamos a reemplazar?
remplazar = "Fecha oculta"

# Reemplazando
# sub(el patron a buscar, por que lo queremos reemplazar, el texto a reemplazar)
nuevoTexto = re.sub(patron, remplazar, texto)

print(nuevoTexto)