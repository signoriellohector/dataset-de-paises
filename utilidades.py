#
# Trabajo Practico Integrador
# 
# Alumnos: 
# Gregorio Agustin Hernandez - Comisión 12
# Héctor Atilio Signoriello - Comisión 10
#
# Grupo 72
#
# Modulo de utilidades funciones secundarias

import os

# Función de petición de opción
def pedir_option()-> int:
    try:
        return int(input('opción: '))
    except ValueError:
        raise ValueError('opción invalida')
    except Exception as e:
        raise Exception(f'inesperado {e}')


def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def imprimir_pais(pais:dict):
# función encargada de la impresión de un pais con sus datos
    print(f'Pais: {pais['nombre']:<20} | Población: {pais['poblacion']:>12} | ' \
                f'Superficie: {pais['superficie']:>12} | Continente: {pais['continente']:<10}')

def impresion_lista_paises(paises:list):
# la función se encarga de la impresión en pantalla de una lista de países
# sigue el siguiente formato:
# País: 'nombre' | Población: 'poblacion' | Superficie: 'superficie' | Continente: 'continente'

    if paises == []:
        raise RuntimeError ('País no encontrado')
    for pais in paises:
        # :>10 dejan espacio especifico para que las variables puedan usar, normalizando la impresión
        imprimir_pais(pais)
        
def pedir_nombre()->str:
# función auxiliar para la petición del nombre con su respectiva validación

    nombre = input('Ingrese el nombre del país: ')
    # Verifica que el nombre no sea vació
    if not nombre.strip(): 
        # raise devuelve un ValueError ya que el nombre se encuentra vació
        raise ValueError ('El nombre no puede estar vació, ' \
        'por favor ingrese un nombre valido')
    if nombre[0].isdigit():
        raise ValueError('El nombre no puede comenzar con un numero')
    
    return nombre

def imprimir_continentes(continentes:dict):
# Función encargada de la impresión del diccionario de continentes con la cantidad de países
    print(f'| {'Continente':>10} | {'Países':>10} |')
    print(f'{'-'*27}')
    for continente, cantidad in continentes.items():
        print(f'| {continente:<10} | {cantidad:>10} |')
        print(f'{'-'*27}')
        