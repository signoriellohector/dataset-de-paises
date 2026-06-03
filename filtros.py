#
# Trabajo Practico Integrador
# 
# Alumnos: 
# Gregorio Agustin Hernandez - Comisión 12
# Héctor Atilio Signoriello - Comisión 10
#
# Grupo 72
#
# Modulo de filtros

#----------------------Funcion para filtrar por continente--------------------------------#

def filtrar_por_continente(paises:list):
    
    print('===== Filtrar por Continentes =====')
    #pedimos al usuario el continente a ingresar    
    continente = input("Ingrese continente: ").strip().lower()
    
    #creamos lista vacia para las coincidencias
    resultado = []
    
    #recorremos la lista y vamos agregando las coincidencias
    for pais in paises:
            if pais['continente'].strip().lower() == continente:
                resultado.append(pais)
    
    #retorno el resultado
    return resultado

#----------------------Funcion para filtrar por rango de poblacion-------------------------------#

def filtrar_por_rango_poblacion(paises: list):

    print('===== Filtrar por rango de poblacion =====')

    #creamos lista vacia para las coincidencias
    resultado = []

    #pido al usuario un minimo y un maximo de poblacion para filtrar, verifico que sea un numero si no corto la funcion con una lista vacia
    try:
        min_poblacion = int(input("Ingrese el minimo de poblacion: "))
        max_poblacion = int(input("Ingrese el maximo de poblacion: "))
    except ValueError:
        print("Ingrese un numero valido")
        return []
    
    #verifico que el minimo que ingresa no sea mayor que el maximo
    if min_poblacion > max_poblacion:
        print("ERROR: El minimo no puede ser mayor al maximo")
        return []
    
    #recoro paises y verifico las opciones que estan en el rango
    for pais in paises:
        if min_poblacion <= pais['poblacion'] <= max_poblacion:
            resultado.append(pais)
    
    #retorno resultados
    return resultado

#----------------------Funcion para filtrar por rango de superficie----------------------#

def filtrar_por_rango_superficie(paises: list):
    pass