#
# Trabajo Practico Integrador
# 
# Alumnos: 
# Gregorio Agustin Hernandez - Comisión 12
# Héctor Atilio Signoriello - Comisión 10
#
# Grupo 72
#
# Modulo de estadísticas
import utilidades

def paises_mayor_menor_poblacion(paises:list)-> tuple:
    utilidades.dataset_vacio(paises)

    pais_mayor_poblacion = {}
    pais_menor_poblacion = {}

    for pais in paises:
        # primera pasada asignacion del primer pais a las dos variables auxiliares
        if pais_mayor_poblacion == {} and pais_menor_poblacion == {}:
            pais_menor_poblacion = pais_mayor_poblacion = pais
            continue

        # comparo si el país es mas grande que el anterior guardado lo almaceno en su lugar
        if pais_mayor_poblacion['poblacion'] <= pais['poblacion']:
            pais_mayor_poblacion = pais

        # comparo si el país es mas pequeño que el anterior guardado lo almaceno en su lugar
        if pais_menor_poblacion['poblacion'] >= pais['poblacion']:
            pais_menor_poblacion= pais

    return pais_mayor_poblacion, pais_menor_poblacion

def promedio_poblacion(paises:list)-> float:
# Función encargada de obtener el promedio de población
    utilidades.dataset_vacio(paises)

    total_poblacion = 0
    cantidad_paises = len(paises)

    for pais in paises:
        total_poblacion += pais['poblacion']

    promedio = total_poblacion/cantidad_paises
    return promedio

def promedio_superficie(paises:list)-> float:
# Función encargada de obtener el promedio de superficie
    utilidades.dataset_vacio(paises)

    total_superficie = 0
    cantidad_paises = len(paises)

    for pais in paises:
        total_superficie += pais['superficie']

    promedio = total_superficie/cantidad_paises

    return promedio

def total_paises_continente(paises:list)-> dict:
# Función encargada de obtener el recuento de paises por continente
    utilidades.dataset_vacio(paises)
    # creacion de diccionario para almacenar los continentes listados
    paises_continente = {}


    for pais in paises:
        # comprobando la existencia del continente en el diccionario
        if pais['continente'] in paises_continente.keys():
            # de existir incrementar en 1 el continente correspondiente en el diccionario
            paises_continente[pais['continente']] += 1
        else:
            # de no existir inicializar el continente en el diccionario con 1
            paises_continente[pais['continente']] = 1    

    return paises_continente