#Importa todas las funciones desde el archivo de Funciones.
from Funciones_Generales import *
from Ordenamiento import *
from Filtrado import *
from Estadisticas import *
paises = []
crear_archvio()
opcion = False
#Crea un bucle que va a iterar hasta que la opcion ingresada sea siete.
while opcion != 7:
    print('='*60)
    print('1. Agregar Pais.\n2. Actualizar Datos.\n3. Buscar Pais.\n4. Filtrar Paises.\n5. Ordenar Paises.\n6. Estadisticas.\n7. Salir.')
    print('='*60)
    #Guarda en una variable lo que retorne la llamada a la funcion opci.
    opcion = opci('Ingrese la opcion que quiere ejecutar: ', 'Error solo se permiten ingresar numeros enteros para seleccionar las opciones...')
    #Toma el valor de opcion introducido por el usuario y lo compara con los distintos casos.
    match opcion:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            print('='*60)
            print('1. Filtrar por continente.\n2. Filtrar por rango de poblacion.\n3.Filtrar por rango de superficie.')
            print('='*60)
            datos(paises)
            #Guarda en una variable lo que retorne la llamada a la funcion opci.
            opcion = opci('Ingrese la opcion que quiere ejecutar: ', 'Error solo se permiten ingresar numeros enteros para seleccionar las opciones...')
            #Toma el valor de opcion introducido por el usuario y lo compara con los distintos casos.
            match opcion:
                case 1:
                    continente = verificar_solo_letras('Ingrese el nombre del continente con el que quiere filtrar: ', 'Solo se permiten letras en el nombre del continente')
                    continentes = filtrar_continente(paises, continente)
                    mostrar_filtrados(continentes, 'el continente buscado')
                case 2:
                    print('ALERTA: El primer numero del rango es el menor el segundo es el mayor...')
                    rango_1 = generar_rango('Ingrese el primer numero que tendra de rango de poblacion: ')
                    rango_2 = generar_rango('Ingrese el segundo numero que tendra de rango de poblacion: ')
                    poblacion = filtrar_rango(paises, rango_1, rango_2, 'poblacion')
                    mostrar_filtrados(poblacion, 'el rango de poblacion buscada')
                case 3:
                    print('ALERTA: El primer numero del rango es el menor el segundo es el mayor...')
                    rango_1 = generar_rango('Ingrese el primer numero que tendra de rango de superficie: ')
                    rango_2 = generar_rango('Ingrese el segundo numero que tendra de rango de superficie: ')
                    poblacion = filtrar_rango(paises, 'superficie')
                    mostrar_filtrados(poblacion, 'el rango de superficie buscada')
        case 5:
            print('='*60)
            print('1. Ordenar por nombre.\n2. Ordenar por poblacion.\n3. Ordenar por superficie.')
            print('='*60)
            datos(paises)
            #Guarda en una variable lo que retorne la llamada a la funcion opci.
            opcion = opci('Ingrese la opcion que quiere ejecutar: ', 'Error solo se permiten ingresar numeros enteros para seleccionar las opciones...')
            #Toma el valor de opcion introducido por el usuario y lo compara con los distintos casos.
            match opcion:
                case 1:
                    ordenamiento(paises,'nombre')
                    mostrar_ordenamiento(paises, 'nombre')
                case 2:
                    ordenamiento(paises,'poblacion', descendente = True)
                    mostrar_ordenamiento(paises, 'poblacion')
                case 3:
                    print('1. Acendente.\n2. Decendente.')
                    #Guarda en una variable lo que retorne la llamada a la funcion opci.
                    opcion = opci('Ingrese la opcion que quiere ejecutar: ', 'Error solo se permiten ingresar numeros enteros para seleccionar las opciones...')
                    #Toma el valor de opcion introducido por el usuario y lo compara con los distintos casos.
                    match opcion:
                        case 1:
                            ordenamiento(paises, 'superficie')
                            mostrar_ordenamiento(paises, 'superficie de forma acendente')
                        case 2:
                            ordenamiento(paises, 'superficie', descendente = True)
                            mostrar_ordenamiento(paises, 'superficie de forma decendente')
                        case _:
                            print('El valor ingresado no es valido...')
                            print('='*60)
                case _:
                    print('El valor ingresado no es valido...')
                    print('='*60)
        case 6:
            print('='*60)
            print('1. Pais con mayor y menor poblacion.\n2. Promedios(Poblacion y superficie).\n3. Cantidad de paises por continente.')
            print('='*60)
            datos(paises)
            #Guarda en una variable lo que retorne la llamada a la funcion opci.
            opcion = opci('Ingrese la opcion que quiere ejecutar: ', 'Error solo se permiten ingresar numeros enteros para seleccionar las opciones...')
            #Toma el valor de opcion introducido por el usuario y lo compara con los distintos casos.
            match opcion:
                case 1:
                    lis_may, lis_men = may_men(paises)
                    mostrar_may_men(lis_may, lis_men)
                case 2:
                    promedio_poblacion = promedio(paises, 'poblacion')
                    promedio_superficie = promedio(paises, 'superficie')
                    mostrar_promedio(promedio_poblacion, promedio_superficie)
                case 3:
                    conteo = contar_por_continente(paises)
                    mostrar_conteo_de_continentes(conteo)
        case 7:
            #Al ingresar a la opcion ocho se le pide al usuario que confirme si quiere salir.
            confirmar = opci('Esta seguro que quiere salir? (1.Si / 2.No): ', 'Solo se permiten numeros enteros...')
            #Toma el valor de opcion introducido por el usuario y lo compara con los distintos casos.
            match confirmar:
                case 1:
                    #Si confirma la salida le muestra un mensaje de despedida.
                    print('Saliendo del sistema de gestion de paises...\nHata la proxima!')
                case 2:
                    #Si niega la salida vuelve opcion false y el programa vuelve al menu de opciones para seguir operando.
                    opcion = False
                case _:
                    print('El valor ingresado no es valido...')
                    opcion = False
        case _:
            print('El valor ingresado no es valido...')
            print('='*60)