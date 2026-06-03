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

# Modulo utilidades
import utilidades

#----------------------Funcion para filtrar por continente--------------------------------#

def filtrar_por_continente(paises:list):
    
    utilidades.limpiar_pantalla()
    print('===== Filtrar por Continentes =====\n')
    #pedimos al usuario el continente a ingresar    
    continente = input("Ingrese continente: ").strip().lower()
    
    # verificación de que el continente es una entrada valida
    if not continente.strip():
        raise ValueError('continente no puede estar vació')

    #creamos lista vacía para las coincidencias
    resultado = []
    
    #recorremos la lista y vamos agregando las coincidencias
    for pais in paises:
            if pais['continente'].strip().lower() == continente:
                resultado.append(pais)
    
    #retorno el resultado
    return resultado

#----------------------Funcion para filtrar por rango de poblacion-------------------------------#

def filtrar_por_rango_poblacion(paises: list):
    utilidades.limpiar_pantalla()
    print('===== Filtrar por rango de poblacion =====\n')

    #creamos lista vacía para las coincidencias
    resultado = []

    # pido al usuario un mínimo y un máximo de población para filtrar, 
    # verifico que sea un numero si no corto la función con una lista vacía
    try:
        min_poblacion = int(input("Ingrese el minimo de poblacion: "))
        max_poblacion = int(input("Ingrese el maximo de poblacion: "))
        if min_poblacion < 0:
            raise ValueError
        
    except ValueError:
        raise ValueError("Ingrese un numero entero mayor de 0")
    
    #verifico que el mínimo que ingresa no sea mayor que el máximo
    if min_poblacion > max_poblacion:
        raise ValueError("El mínimo no puede ser mayor al máximo")
    
    #recorro países y verifico las opciones que están en el rango
    for pais in paises:
        if min_poblacion <= pais['poblacion'] <= max_poblacion:
            resultado.append(pais)
    
    #retorno resultados
    return resultado

#----------------------Función para filtrar por rango de superficie----------------------#
# misma situación cambiando de población a superficie

def filtrar_por_rango_superficie(paises: list):

    utilidades.limpiar_pantalla()
    print('===== Filtrar por rango de superficie =====\n')

    #creamos lista vacía para las coincidencias
    resultado = []

    #pido al usuario un mínimo y un máximo de superficie para filtrar, 
    # verifico que sea un numero si no corto la función con una lista vacía
    try:
        min_superficie = int(input("Ingrese el minimo de superficie: "))
        max_superficie = int(input("Ingrese el maximo de superficie: "))
        if min_superficie < 0:
            raise ValueError
    except ValueError:
        raise ValueError("Ingrese un numero entero mayor a 0")

    
    #verifico que el mínimo que ingresa no sea mayor que el máximo
    if min_superficie > max_superficie:
        raise ValueError("El mínimo no puede ser mayor al máximo")
    
    #recorro paises y verifico las opciones que están en el rango
    for pais in paises:
        if min_superficie <= pais['superficie'] <= max_superficie:
            resultado.append(pais)
    
    #retorno resultados
    return resultado