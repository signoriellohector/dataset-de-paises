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
    return 0

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def impresion_lista_paises(paises:list):
    if paises == []:
        raise RuntimeError ('País no encontrado')
    for pais in paises:
        print(f'Pais: {pais['nombre']:>10} | Población: {pais['poblacion']:>10} | ' \
            f'Superficie: {pais['superficie']:<10} | Continente: {pais['continente']:<10}')
        
def pedir_nombre()->str:

    nombre = input('Ingrese el nombre del país: ')
    # Verifica que el nombre no sea vació
    if not nombre.strip(): 
        # raise devuelve un ValueError ya que el nombre se encuentra vació
        raise ValueError ('El nombre no puede estar vació, ' \
        'por favor ingrese un nombre valido')
    if nombre[0].isdigit():
        raise ValueError('El nombre no puede comenzar con un numero')
    
    return nombre
