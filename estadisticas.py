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

def Paises_mayor_menor_poblacion(paises:list)-> tuple:
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