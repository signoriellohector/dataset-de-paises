#
# Trabajo Practico Integrador
# 
# Alumnos: 
# Gregorio Agustin Hernandez - Comisión 12
# Héctor Atilio Signoriello - Comisión 10
#
# Grupo 72
#
# Menu Sistema de Gestión de Datos de Países


# importación de módulos
import manejo_dataset # Modulo de carga de dataset paises.csv


# Función de petición de opción
def pedir_option()-> int:
    try:
        return int(input('opción: '))
    except ValueError:
        print('Error: opción invalida')
    except Exception as e:
        print(f'Error inesperado {e}')
    return 0


# Menu
if __name__=='__main__':
    option = 0 # Variable de control del menu

    # Carga de una lista de paises
    # pais = { 'nombre':'Argentina',
    # 'poblacion': 46200000,
    # 'superficie': 3761274,
    # 'continente': América}
    
    paises=manejo_dataset.cargar_paises()

    while option != 7:
        
        print(f"\n{'-'*10} MENU {'-'*10}\n")
        print('1. Agregar un País\n' \
            '2. Actualizar un País\n' \
            '3. Buscar un País por Nombre\n' \
            '4. Filtrar Países\n' \
            '5. Ordenar Países\n' \
            '6. Estadísticas de los Países\n' \
            '7. Salir')
        
        option = pedir_option()

        match option:
            case 1: # Agregar un País
                pass

            case 2: # Actualizar un País
                pass

            case 3: # Buscar un País por Nombre
                pass

            case 4: # Menu Filtrar Países
                option_submenu = 0 #

                while option_submenu != 4:
                    print(f"\n{'='*5} Filtrar Países {'='*5}\n")
                    print('1. Por Continente\n' \
                        '2. Por Rango de Población\n' \
                        '3. Por Rango de Superficie\n' \
                        '4. Salir al menu principal')
                    option_submenu = pedir_option()

                    match option:
                        case 1: # Filtrado por continente
                            pass

                        case 2: # Filtrado por rango de población
                            pass

                        case 3: # Filtrado por rango de Superficie
                            pass

                        case 4: # Salida al menu principal
                            pass
                        case _:
                            print('Error: opción fuera de rango')

            case 5: # Menu Ordenar Países
                option_submenu = 0
                while option_submenu != 4:
                    print(f"\n{'='*5} Ordenar Países {'='*5}\n")
                    print('1. Por Nombre\n' \
                        '2. Por Población\n' \
                        '3. Por Superficie\n' \
                        '4. Salir al menu principal')
                    option_submenu = pedir_option()

                    match option_submenu:
                        case 1: # Ordenado por nombre
                            pass

                        case 2: # Ordenado por población
                            pass

                        case 3: # SubMenu Ordenado por superficie
                            option_superficie = 0
                            while option_superficie != 3:
                                print(f"\n{'-'*2} Ordenar por Superficie {'-'*2}\n")
                                print('1. Ascendente (de menor a mayor)\n' \
                                    '2. Descendente (de mayor a menor)\n' \
                                    '3. Salir al menu anterior')
                                
                                option_superficie = pedir_option()

                                match option:
                                    case 1: # Ordenado Ascendente
                                        pass

                                    case 2: # Ordenado Descendente
                                        pass

                                    case 3: # Salir al menu anterior
                                        pass

                                    case _:
                                        print('Error: opción fuera de rango')

                        case 4: # Salida al menu principal
                            pass

                        case _:
                            print('Error: opción fuera de rango')


            case 6: # Menu Estadística de los Países
                option_submenu = 0
                while option_submenu != 6:
                    print(f"\n{'='*5} Estadística de los Países {'='*5}\n")
                    print('1. País Mayor Población\n' \
                        '2. País Menor Población\n' \
                        '3. Promedio general de población\n' \
                        '4. Promedio generar de superficie en km²\n'\
                        '5. Cantidad total de países por continente\n' \
                        '6. Salir al menu principal')
                    option_submenu = pedir_option()

                    match option_submenu:
                        case 1: # País con Mayor Población
                            pass

                        case 2: # País con Menor Población
                            pass

                        case 3: # Promedio general de población
                            pass

                        case 4: # Promedio general de superficie en km²
                            pass

                        case 5: # Cantidad total de países por continente
                            pass

                        case 6: # Salir al menu principal
                            pass
                        case _:
                            print('Error: opción fuera de rango')

            case 7: # Salida del programa
                pass

            case _: 
                print('Error: opción fuera de rango')