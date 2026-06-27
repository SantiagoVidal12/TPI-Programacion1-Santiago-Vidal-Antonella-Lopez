#Importa todas las funciones desde el archivo de Funciones Generales y lo guarda de forma acortada en fun.
import Funciones_Generales as fun
#Importa las funcion de agregar pais dese el alchivo de Agrgar Paises.
from Agregar_paises import agregar_pais
#Importa las funcion de actualizar pais dese el alchivo de Actualizar Paises.
from Actualizar_paises import actualizar_pais
#Importa las funcion de buscar pais dese el alchivo de Buscar Paises.
from Buscar_Paises import buscar_pais
#Importa todas las funciones desde el archivo de Filtrado y lo guarda de forma acortada en flt.
import Filtrado as flt
#Importa todas las funciones desde el archivo de Ordenamiento y lo guarda de forma acortada en orde.
import Ordenamiento as orde
#Importa todas las funciones desde el archivo de Estadisticas y lo guarda de forma acortada en est.
import Estadisticas as est

paises = []
#Llama a la funcion de crear archivo en caso de que el archivo csv no esxista previamente.
fun.crear_archvio()
opcion = False
#Crea un bucle que va a iterar hasta que la opcion ingresada sea siete.
while opcion != 7:
    print('='*60)
    print('1. Agregar Pais.\n2. Actualizar Datos.\n3. Buscar Pais.\n4. Filtrar Paises.\n5. Ordenar Paises.\n6. Estadisticas.\n7. Salir.')
    print('='*60)
    #Guarda en una variable lo que retorne la llamada a la funcion opci.
    opcion = fun.opci('Ingrese la opcion que quiere ejecutar: ', 'Error solo se permiten ingresar numeros enteros para seleccionar las opciones...')
    #Toma el valor de opcion introducido por el usuario y lo compara con los distintos casos.
    match opcion:
        case 1:
            agregar_pais()
        case 2:
            actualizar_pais(paises)
        case 3:
            buscar_pais(paises)
        case 4:
            print('='*60)
            print('1. Filtrar por continente.\n2. Filtrar por rango de poblacion.\n3.Filtrar por rango de superficie.')
            print('='*60)
            fun.datos(paises)
            #Guarda en una variable lo que retorne la llamada a la funcion opci.
            opcion = fun.opci('Ingrese la opcion que quiere ejecutar: ', 'Error solo se permiten ingresar numeros enteros para seleccionar las opciones...')
            #Toma el valor de opcion introducido por el usuario y lo compara con los distintos casos.
            match opcion:
                case 1:
                    continente = fun.verificar_solo_letras('Ingrese el nombre del continente con el que quiere filtrar: ', 'Solo se permiten letras en el nombre del continente')
                    continentes = flt.filtrar_continente(paises, continente)
                    flt.mostrar_filtrados(continentes, 'el continente buscado')
                case 2:
                    print('ALERTA: El primer numero del rango es el menor el segundo es el mayor...')
                    rango_1 = fun.generar_rango('Ingrese el primer numero que tendra de rango de poblacion: ')
                    rango_2 = fun.generar_rango('Ingrese el segundo numero que tendra de rango de poblacion: ')
                    poblacion = flt.filtrar_rango(paises, rango_1, rango_2, 'poblacion')
                    flt.mostrar_filtrados(poblacion, 'el rango de poblacion buscada')
                case 3:
                    print('ALERTA: El primer numero del rango es el menor el segundo es el mayor...')
                    rango_1 = fun.generar_rango('Ingrese el primer numero que tendra de rango de superficie: ')
                    rango_2 = fun.generar_rango('Ingrese el segundo numero que tendra de rango de superficie: ')
                    poblacion = flt.filtrar_rango(paises, 'superficie')
                    flt.mostrar_filtrados(poblacion, 'el rango de superficie buscada')
        case 5:
            print('='*60)
            print('1. Ordenar por nombre.\n2. Ordenar por poblacion.\n3. Ordenar por superficie.')
            print('='*60)
            fun.datos(paises)
            #Guarda en una variable lo que retorne la llamada a la funcion opci.
            opcion = fun.opci('Ingrese la opcion que quiere ejecutar: ', 'Error solo se permiten ingresar numeros enteros para seleccionar las opciones...')
            #Toma el valor de opcion introducido por el usuario y lo compara con los distintos casos.
            match opcion:
                case 1:
                    orde.ordenamiento(paises,'nombre')
                    orde.mostrar_ordenamiento(paises, 'nombre')
                case 2:
                    orde.ordenamiento(paises,'poblacion', descendente = True)
                    orde.mostrar_ordenamiento(paises, 'poblacion')
                case 3:
                    print('1. Acendente.\n2. Decendente.')
                    #Guarda en una variable lo que retorne la llamada a la funcion opci.
                    opcion = fun.opci('Ingrese la opcion que quiere ejecutar: ', 'Error solo se permiten ingresar numeros enteros para seleccionar las opciones...')
                    #Toma el valor de opcion introducido por el usuario y lo compara con los distintos casos.
                    match opcion:
                        case 1:
                            orde.ordenamiento(paises, 'superficie')
                            orde.mostrar_ordenamiento(paises, 'superficie de forma acendente')
                        case 2:
                            orde.ordenamiento(paises, 'superficie', descendente = True)
                            orde.mostrar_ordenamiento(paises, 'superficie de forma decendente')
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
            fun.datos(paises)
            #Guarda en una variable lo que retorne la llamada a la funcion opci.
            opcion = fun.opci('Ingrese la opcion que quiere ejecutar: ', 'Error solo se permiten ingresar numeros enteros para seleccionar las opciones...')
            #Toma el valor de opcion introducido por el usuario y lo compara con los distintos casos.
            match opcion:
                case 1:
                    lis_may, lis_men = est.may_men(paises)
                    est.mostrar_may_men(lis_may, lis_men)
                case 2:
                    promedio_poblacion = est.promedio(paises, 'poblacion')
                    promedio_superficie = est.promedio(paises, 'superficie')
                    est.mostrar_promedio(promedio_poblacion, promedio_superficie)
                case 3:
                    conteo = est.contar_por_continente(paises)
                    est.mostrar_conteo_de_continentes(conteo)
        case 7:
            #Al ingresar a la opcion ocho se le pide al usuario que confirme si quiere salir.
            confirmar = fun.opci('Esta seguro que quiere salir? (1.Si / 2.No): ', 'Solo se permiten numeros enteros...')
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