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


def ordenamiento_nombre(paises:list):
# función encargada de ordenar los países de forma alfabética
    # se implementa el uso de la función sorted con el valor key apuntando valor 'nombre' dentro del diccionario país
    paises_ordenado = sorted(paises,key=lambda p: p['nombre'].lower())

    return paises_ordenado


def ordenamiento_poblacion(paises:list):
# función encargada de ordenar los países por poblacion de forma ascendente
# se utiliza un algoritmo merge sort para el método de ordenamiento de forma iterativa
    size = len(paises)
    paises_ordenado = paises
    # variable auxiliar
    # empieza fusionando pares de 1 elemento
    auxiliar = 1 

    while auxiliar < size:
        for inicio in range(0, size, auxiliar * 2):
            medio = min(inicio + auxiliar, size)
            fin = min(inicio + auxiliar*2, size)

            izquierda = paises_ordenado[inicio:medio]
            derecha = paises_ordenado[medio:fin]

            # fusionar en su lugar
            i = j = 0
            k = inicio
            while i < len(izquierda) and j < len(derecha):
                if izquierda[i]['poblacion'] < derecha[j]['poblacion']:
                    paises_ordenado[k] = izquierda[i]
                    i += 1
                else:
                    paises_ordenado[k] = derecha[j]
                    j += 1
            while i < len(izquierda):
                paises_ordenado[k] = izquierda[i]
                i += 1
                k += 1
            while j < len(derecha):
                paises_ordenado[k]
                j += 1
                k += 1

        auxiliar *=2
    #paises_ordenado = sorted(paises,key=lambda p: p['poblacion'], reverse=True)

    return paises_ordenado
