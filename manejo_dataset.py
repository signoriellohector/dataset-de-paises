#
# Trabajo Practico Integrador
# 
# Alumnos: 
# Gregorio Agustin Hernandez - Comisión 12
# Héctor Atilio Signoriello - Comisión 10
#
# Grupo 72
#
# Modulo de manejo del dataset paises.csv

import csv
#import busqueda

# Función de creación de lista de diccionario de países
def cargar_paises():
    paises =[]
    with open('paises.csv', 'r', encoding='utf-8') as archivo:
        # Creamos el lector de diccionarios
        lector_dict = csv.DictReader(archivo)

        for fila in lector_dict:
            # carga de la lista fila a fila
            paises.append(fila)
        
    # retorno de una lista de diccionarios    
    return paises


if __name__=='__main__':
# Prueba de carga exitosa
    paises= cargar_paises()
    print(paises)

# Test modulo de busqueda por nombre
#    coincidencias = busqueda.busqueda_por_nombre(paises, 'brasil')
#    print(f'\nbusqueda {coincidencias}')