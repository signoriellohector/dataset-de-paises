#
# Trabajo Practico Integrador
# 
# Alumnos: 
# Gregorio Agustin Hernandez - Comisión 12
# Héctor Atilio Signoriello - Comisión 10
#
# Grupo 72
#
# Modulo de búsqueda


def busqueda_por_nombre(paises:list,nombre:str):
    # creacion de lista auxiliar
    coincidencias = [] 

    # Normalizando string
    # strip() elimina espacios en blanco antes y después de la cadena de caracteres
    # lower() convierte todos los caracteres en minúsculas
    nombre= nombre.strip().lower()
    
    # recorrido de lista hasta encontrar todas las coincidencias posibles
    for pais in paises:
        if (pais['nombre'].lower()) == nombre:
            coincidencias.append(pais)

    return coincidencias

