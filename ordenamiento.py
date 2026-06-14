#
# Trabajo Practico Integrador
# 
# Alumnos: 
# Gregorio Agustin Hernandez - Comisión 12
# Héctor Atilio Signoriello - Comisión 10
#
# Grupo 72
#
# Modulo Ordenamientos
from operator import itemgetter
import utilidades

def ordenamiento_nombre(paises:list)-> list:
# función encargada de ordenar los países de forma alfabética
    utilidades.dataset_vacio(paises)

    # se implementa el uso de la función sorted con el valor key apuntando valor 'nombre' dentro del diccionario país
    paises_ordenado = sorted(paises,key=lambda p: p['nombre'].lower())

    return paises_ordenado


def ordenamiento_poblacion(paises:list):
# función encargada de ordenar los países por poblacion de forma ascendente
    utilidades.dataset_vacio(paises)

    paises_ordenado = sorted(paises,key=lambda p: p['poblacion'], reverse=True)

    return paises_ordenado


def ordenamiento_superficie(paises:list, ascendente=True)-> list:
# función encargada de ordenar los países por superficie de forma ascendente y descendente mediante ascendente=bool
    utilidades.dataset_vacio(paises)

    paises_ordenado = sorted(paises,key=itemgetter('superficie'), reverse=ascendente)
    
    return paises_ordenado
