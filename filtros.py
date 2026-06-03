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

#----------------  Funcion para filtrar por continente -------------------------------

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

#----------------  Funcion para filtrar por continente -------------------------------

def filtrar_por_rango_poblacion(paises: list):
    pass

#----------------  Funcion para filtrar por rango de superficie -------------------------------

def filtrar_por_rango_superficie(paises: list):
    pass