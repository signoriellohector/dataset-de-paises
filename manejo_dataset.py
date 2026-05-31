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
import busqueda

# Función de creación de lista de diccionario de países
def cargar_paises():
# la función retorna una lista 
    paises =[]
    with open('paises.csv', 'r', encoding='utf-8') as archivo:
        # Creamos el lector de diccionarios
        lector_dict = csv.DictReader(archivo)

        for fila in lector_dict:
            # carga de la lista fila a fila
            # transformo poblacion y superficie de string a entero para poder trabajarlos correctamente
            fila['poblacion'] = int(fila['poblacion'])
            fila['superficie'] = int(fila['superficie'])
            paises.append(fila)
        
    # retorno de una lista de diccionarios    
    return paises


# Función de creación de país
def crear_pais()->dict:
# la función retorna un diccionario vació de no efectuarse la carga correctamente
# si la carga fue realizada correctamente retorna un diccionario 
# {'nombre'=nombre:str, 
# 'poblacion' = poblacion:int, 
# 'superficie'= superficie:int, 
# 'continente' = continente:str}


    pais = {}
    print('---- Creación de país ----')

    try:
        nombre = input('Ingrese el nombre del país: ')
        # Verifica que el nombre no sea vació
        if not nombre.strip(): 
            # raise devuelve un ValueError ya que el nombre se encuentra vació
            raise ValueError 
        if nombre[0].isdigit():
            raise TypeError
        
        poblacion = input('Ingrese la población del país: ')
        superficie = input('Ingrese la superficie en km²: ')
        try:
            # sobre escribe ValueError por TypeError para dar un mejor mensaje de error
            poblacion = int(poblacion)
            superficie = int(superficie)
        except ValueError:
            raise TypeError

        continente = input('Ingrese el continente: ')
        # Verifica que el continente no sea vació
        if not continente.strip():
            raise ValueError
        if continente[0].isdigit():
            raise TypeError
        
        # creando diccionario país
        pais['nombre'] = nombre.capitalize()
        pais['poblacion'] = poblacion
        pais['superficie'] = superficie
        pais['continente'] = continente.capitalize()
        

    except ValueError:
        print('Error: los campos no pueden estar vacíos')
    except TypeError:
        print('Error: tipo de dato incorrecto')

    # retorna el diccionario pais sea que este vació o no
    return pais
            

# Función de Agregado de un país a la lista paises y al archivo paises.csv
def agregar_pais(paises:list):
# la función recibe una lista de diccionarios 

    # genera un diccionario vació el cual es un pais a crear
    pais = {}
    while not pais:
        # se llama la funcion crear_pais(),
        # se le da la opción de seguir intentando crear un país valido
        pais = crear_pais()
        if not pais:
            print('Desea reintentar ingrasar un país?\n' \
                '1. Si\n' \
                '2. No')
            try:
                option = int(input())
                if option == 1:
                    continue
                if option == 2:
                    return False
                else:
                    print('Error: opción fuera de rango')
            except ValueError:
                print('Error: Opción invalida')
    
    # se genera una lista con las cabezeras del archivo países.csv
    columnas = ['nombre','poblacion','superficie','continente']

    # se verifica que el pais no se encuentre listado en el dataset
    existe = busqueda.busqueda_por_nombre(paises,pais['nombre'])

    # de no existir el país se procede a agregarlo a la lista y al archivo paises.csv
    if existe == []:
        paises.append(pais)
        with open('paises.csv', 'a', newline='', encoding='utf-8') as archivo:
            # creamos el objeto escritor
            escritor = csv.DictWriter(archivo, columnas)

            # Agregamos el nuevo país al archivo paises.csv
            escritor.writerow(pais)

        return True
    else:
        print('Error: El País ya se encuentra listado')
    

#Función Actualizar los datos de Población y Superficie de un País.
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
        # pedimos al usuario ingresar poblacion y superficie nueva, validamos que sea un numero
        try:
            poblacion = int(input("Ingrese el nuevo dato de poblacion: "))
            superficie = int(input("Ingrese el nuevo dato de superficie: "))
        except ValueError:
            print("Ingrese un numero valido")
            return False
        if poblacion <= 0 or superficie <= 0:
            print("Error: los valores deben ser mayores a cero")
            return False

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
        

if __name__=='__main__':
# Prueba de carga exitosa
    paises= cargar_paises()
    print(paises)

# Test modulo de busqueda por nombre
#    coincidencias = busqueda.busqueda_por_nombre(paises, 'brasil')
#    print(f'\nbusqueda {coincidencias}')

# Test función crear_pais
#    pais = crear_pais()
#    print(pais)

# Test función agregar_pais
    exito = agregar_pais(paises)
    if exito:
        print('Carga exitosa')
    else:
        print('Carga insatisfactoria')
