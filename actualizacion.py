#
# Trabajo Practico Integrador
# 
# Alumnos: 
# Gregorio Agustin Hernandez - Comisión 12
# Héctor Atilio Signoriello - Comisión 10
#
# Grupo 72
#
# Modulo de actualización de países

import csv
import busqueda

#Funcion Actualizar los datos de Población y Superficie de un País.

def actualizar_pais(paises: list):
    # la función recibe la lista de países
    # retorna True si la actualización fue exitosa, False si no
    
    print('---- Actualizar los datos de Población y Superficie de un País. ----')
    nombre = input('Ingrese el nombre del país a actualizar: ')

    # buscamos el país en la lista
    coincidencias = busqueda.busqueda_por_nombre(paises, nombre)
    
    # si no existe mostramos error y salimos
    if coincidencias == []:
        print('Error: el país no fue encontrado')
        return False
    else:
        # pedimos al usuario ingresar poblacion y superficie nueva
        poblacion = int(input("Ingrese el nuevo dato de poblacion: "))
        superficie = int(input("Ingrese el nuevo dato de superficie: "))
        
        # actualizamos los datos
        coincidencias[0]['poblacion'] = poblacion
        coincidencias[0]['superficie'] = superficie
        
        #abrimos el archivo en modo escritura para reemplazar.
        with open('paises.csv', 'w', encoding='utf-8') as archivo:            
            #objeto escritor
            escritor = csv.DictWriter(archivo, ['nombre','poblacion','superficie','continente'])
            #escribe la primera línea del csv
            escritor.writeheader()
            #actualizamos los datos en el csv
            escritor.writerows(paises)
            
            return True



