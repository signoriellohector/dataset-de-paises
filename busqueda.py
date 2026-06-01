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
import manejo_dataset

def busqueda_por_nombre(paises:list,nombre:str)->list:
    # creación de lista auxiliar
    coincidencias = [] 

    # Normalizando string
    # strip() elimina espacios en blanco antes y después de la cadena de caracteres
    # lower() convierte todos los caracteres en minúsculas
    nombre= nombre.strip().lower()
    
    # recorrido de lista hasta encontrar todas las coincidencias posibles
    for pais in paises:
        if (pais['nombre'].strip().lower()) == nombre:
            coincidencias.append(pais)

    return coincidencias


def busqueda_por_nombre_parcial(paises:list, nombre:str)->list:
        # creación de lista auxiliar
    coincidencias = [] 

    # Normalizando string
    # strip() elimina espacios en blanco antes y después de la cadena de caracteres
    # lower() convierte todos los caracteres en minúsculas
    nombre= nombre.strip().lower()
    
    # recorrido de lista hasta encontrar todas las coincidencias posibles
    for pais in paises:
        nombre_pais = pais['nombre'].strip().lower()
        if nombre_pais.startswith(nombre):
            coincidencias.append(pais)

    return coincidencias


if __name__=="__main__":
    paises = manejo_dataset.cargar_paises()
    print(busqueda_por_nombre_parcial(paises,'a'))