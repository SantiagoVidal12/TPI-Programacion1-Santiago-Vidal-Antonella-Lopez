#Importa el modulo csv.
import csv
from Funciones_Generales import verificar_solo_letras

#Crea la funcion que se va a encargar de agregar paises nuevos.
def agregar_pais():
    #Pide al usuario que ingrese el nombre del nuevo pais.
    nombre = verificar_solo_letras('Ingrese el nombre del pais: ', 'Solo se permiten letras en el nombre del pais...')
    
    #Verifica que el pais no exista ya en el CSV.
    with open('paises.csv', 'r', encoding='utf-8-sig') as archivo:
        #Crea un lector que transforma cada fila del csv en un diccionario, usando la primera linea como clases.
        lector_csv = csv.DictReader(archivo)
        #Crea un bucle que va a iterar por cada elemento de lector csv.
        for pais in lector_csv:
            #Verifica si en el archivo ya se encuntra algun pais con el mismo nombre que el ingresado por el usuario.
            if pais['nombre'].lower() == nombre.lower():
                #En caso de encontrarse se le avisa al usuario con un mensaje.
                print(f'\nEl pais "{nombre}" ya existe en el sistema.')
                #Retorna para evitar que lo demas se continue ejecutanto.
                return

    #Crea un bucle que va a iterar hasta que se fuerze la salida.
    while True:
        try:
            #Inteta pedirle al usuario que ingrese la poblacion.
            poblacion = int(input('Ingrese la poblacion del pais: ').strip())
            #En caso de que no haya ningun error sale de bucle.
            break
        #Se ejecuta solo si el usuario intenta ingerea cualquier cosa que no sea un numero entero.
        except ValueError:
            print('ERROR: La poblacion debe ser un numero entero...')

    #Crea un bucle que va a iterar hasta que se fuerze la salida.
    while True:
        try:
            #Inteta pedirle al usuario que ingrese la superficie.
            superficie = int(input('Ingrese la superficie del pais (en km²): ').strip())
            #En caso de que no haya ningun error sale de bucle.
            break
        #Se ejecuta solo si el usuario intenta ingerea cualquier cosa que no sea un numero entero.
        except ValueError:
            print('ERROR: La superficie debe ser un numero entero...')

    #Pide al usuario que ingrese el nombre del continente.
    continente = verificar_solo_letras('Ingrese el continente del pais: ', 'Solo se permiten letras en el nombre del continente...')

    #Abre el archivo en modo 'a' (append) para agregar datos al final sin borrar los que ya tiene.
    with open('paises.csv', 'a', encoding='utf-8-sig', newline='') as archivo:
        #Crea un escritor que transforma una lista de datos en una fila del csv, separando cada elemento con comas.
        escritor_csv = csv.writer(archivo)
        #Toma la lista de variables y las escribe como una nueva fila estructurada con comas al final del documento
        escritor_csv.writerow([nombre, poblacion, superficie, continente])

   
    print(f'\nEl pais "{nombre}" fue agregado exitosamente.')
    print('-' * 60)
    #Muestra los datos del pais agregado.
    print(f'  Nombre     : {nombre}')
    print(f'  Poblacion  : {poblacion:,} habitantes')
    print(f'  Superficie : {superficie:,} km²')
    print(f'  Continente : {continente}')
    print('-' * 60)