#Importa el modulo csv
import csv
from Funciones_Generales import datos, verificar_solo_letras

#Crea la funcion que se va a encargar de actualizar la informacion de los paises.
def actualizar_pais(paises):
    datos(paises)
    #Pide al usuario que ingrese el nombre del pais.
    nombre = verificar_solo_letras('Ingrese el nombre del pais que desea actualizar: ', 'Solo se permiten letras en el nombre del pais...')

    #Crea la variable donde se va a guardar el pais
    pais_encontrado = None
    #Crea un bucle que itera por cada elemento de la lista de pais.
    for pais in paises:
        #Verifica si existe algun elemento con la clave nombre igual al nombre ingresado por el usuario.
        if pais['nombre'].lower() == nombre.lower():
            #En caso de encontrarse guarda los datos del pais en la varible.
            pais_encontrado = pais
            #Fuerza la salida del bucle.
            break

    #Verifica si la bandera se activo.
    if not pais_encontrado:
        #En caso de no activarse, se le avisa al usuario que no se encontro el pais que buscaba.
        print(f'\nNo se encontro ningun pais con el nombre "{nombre}".')
        #Retorna para evitar que continue ejecutando lo siguiente.
        return

    #Muestra los datos actuales del pais.
    print(f'\nDatos actuales de {pais_encontrado["nombre"]}:')
    print('-' * 60)
    print(f'  1. Nombre     : {pais_encontrado["nombre"]}')
    print(f'  2. Poblacion  : {int(pais_encontrado["poblacion"]):,} habitantes')
    print(f'  3. Superficie : {int(pais_encontrado["superficie"]):,} km²')
    print(f'  4. Continente : {pais_encontrado["continente"]}')
    print('-' * 60)

    print('¿Que dato desea actualizar?')
    print('1. Nombre\n2. Poblacion\n3. Superficie\n4. Continente')
    
    #Crea un bucle que va a iterar hasta que se fuerze su salida.
    while True:
        try:
            #Pide al usuario que ingrese un numero entero.
            opcion = int(input('Ingrese la opcion: ').strip())
            #Verifica que la opcion se algunas de las posibles.
            if opcion not in [1, 2, 3, 4]:
                #En caso de no serlo avisa al usuario con un mensaje de error.
                print('ERROR: Ingrese una opcion valida (1-4).')
                continue
            #Fuerza la salida del bucle.
            break
        #Se ejecuta solo si el usuario intenta ingerea cualquier cosa que no sea un numero entero.
        except ValueError:
            print('ERROR: Solo se permiten numeros enteros.')

    #Toma el valor de opcion introducido por el usuario y lo compara con los distintos casos.
    match opcion:
        case 1:
            #Pide al usuario que ingrese el nuevo nombre del pais.
            nuevo_valor = verificar_solo_letras('Ingrese el nuevo nombre: ', 'Solo se permiten letras en el nombre del pais...')
            #Cambia el valor guardado en la lista por el valor ingresado por el usuario.
            pais_encontrado['nombre'] = nuevo_valor
        case 2:
            #Crea un bucle que va a iterar hasta que se fuerze su salida.
            while True:
                try:
                    #Intenta pedirle al usuario que ingrese un numero entero.
                    nuevo_valor = int(input('Ingrese la nueva poblacion: ').strip())
                    #Cambia el valor guardado en la lista por el valor ingresado por el usuario.
                    pais_encontrado['poblacion'] = nuevo_valor
                    #Fuerza la salida del bucle.
                    break
                #Se ejecuta solo si el usuario intenta ingerea cualquier cosa que no sea un numero entero.
                except ValueError:
                    print('ERROR: La poblacion debe ser un numero entero.')
        case 3:
            #Crea un bucle que va a iterar hasta que se fuerze su salida.
            while True:
                try:
                    #Intenta pedirle al usuario que ingrese un numero entero.
                    nuevo_valor = int(input('Ingrese la nueva superficie (en km²): ').strip())
                    #Cambia el valor guardado en la lista por el valor ingresado por el usuario.
                    pais_encontrado['superficie'] = nuevo_valor
                    #Fuerza la salida del bucle.
                    break
                #Se ejecuta solo si el usuario intenta ingerea cualquier cosa que no sea un numero entero.
                except ValueError:
                    print('ERROR: La superficie debe ser un numero entero.')
        case 4:
            #Pide al usuario que ingrese el nuevo nombre del continente.
            nuevo_valor = verificar_solo_letras('Ingrese el nuevo continente: ', 'Solo se permiten letras en el nombre del continente...')
            #Cambia el valor guardado en la lista por el valor ingresado por el usuario.
            pais_encontrado['continente'] = nuevo_valor

    #Abre el archivo en modo escritura.
    with open('paises.csv', 'w', encoding='utf-8-sig', newline='') as archivo:
        #Crea una lista con los nombres de las columnas que estructuran el encabezado del csv.
        campos = ['nombre', 'poblacion', 'superficie', 'continente']
        #Crea un escritor que transforma diccionarios en filas del csv, guiándose por las columnas definidas.
        escritor_csv = csv.DictWriter(archivo, fieldnames=campos)
        #Escribe la primera línea del archivo csv utilizando los nombres de los campos como encabezado.
        escritor_csv.writeheader()
        #Toma la lista completa de diccionarios y escribe todos los pases de una sola vez en el archivo.
        escritor_csv.writerows(paises)

    print(f'\nEl pais fue actualizado exitosamente.')
    print('-' * 60)
    #Muestra los datos del pais actualizado.
    print(f'  Nombre     : {pais_encontrado["nombre"]}')
    print(f'  Poblacion  : {int(pais_encontrado["poblacion"]):,} habitantes')
    print(f'  Superficie : {int(pais_encontrado["superficie"]):,} km²')
    print(f'  Continente : {pais_encontrado["continente"]}')
    print('-' * 60)