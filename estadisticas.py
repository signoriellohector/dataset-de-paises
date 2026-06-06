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

def paises_mayor_menor_poblacion(paises:list)-> tuple:
    pais_mayor_poblacion = {}
    pais_menor_poblacion = {}

    for pais in paises:
        # primera pasada asignacion del primer pais a las dos variables auxiliares
        if pais_mayor_poblacion == {} and pais_menor_poblacion == {}:
            pais_menor_poblacion = pais_mayor_poblacion = pais
            continue

        if pais_mayor_poblacion['poblacion'] <= pais['poblacion']:
            pais_mayor_poblacion = pais

        if pais_menor_poblacion['poblacion'] >= pais['poblacion']:
            pais_menor_poblacion= pais

    return pais_mayor_poblacion, pais_menor_poblacion

def promedio_poblacion(paises:list)-> float:
# Función encargada de obtener el promedio de población
    total_poblacion = 0
    cantidad_paises = len(paises)

    for pais in paises:
        total_poblacion += pais['poblacion']

    promedio = total_poblacion/cantidad_paises
    return promedio

def promedio_superficie(paises:list)-> float:
# Función encargada de obtener el promedio de superficie
    total_superficie = 0
    cantidad_paises = len(paises)

    for pais in paises:
        total_superficie += pais['superficie']

    promedio = total_superficie/cantidad_paises

    return promedio

