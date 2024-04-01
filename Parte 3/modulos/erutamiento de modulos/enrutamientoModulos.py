# Importando modulos desde una carpeta
# Enrutamiento de modulos

# Importando modulos que estan en la ruta
import modulosJIJI.moduloEjemplo

print(modulosJIJI.moduloEjemplo.saludar("Stephen")) #? Hola Stephen!
print(modulosJIJI.moduloEjemplo.saludar2("Stephen")) #? NASHEI Stephen!


#-----------------------------------------------------------------------------------------------------------------#


# Importando modulos que estan fuera del directorio

import sys # Importa un modulo creado por python

sys.path.append("ruta de su modulo") # path es la ruta y append que le agregamos

#import su_modulo