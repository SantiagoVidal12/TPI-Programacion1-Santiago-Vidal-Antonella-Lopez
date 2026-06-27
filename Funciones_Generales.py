#Importa el modulo csv.
import csv

#Crea la funcion que se encarga de verificar que la opcion que se ingrese sea un numero positivo.
def opci(mensaje,error):
    #Crea un bucle que va a iterar hasta que se fuerze su salida.
    while True:
        try:
            #Intenta pedirle al usuario que ingrese un numero entero.
            opcion = int(input(mensaje))
            #En caso de no haber errores se retorna el valor ingresado.
            return opcion
        #Se ejecuta solo si el usuario intenta ingerea cualquier cosa que no sea un numero entero.
        except ValueError:
            print(f'ERROR: {error}')
        #Se ejecuta solo si se produce algun error no esperado.
        except Exception as e:
                print(f'Se produjo un error inesperado: {e}')

#Crea la funcion donde se crea el archivo csv es caso de que no exista.
def crear_archvio():
    try:
        #Trata de crar el archivo en caso de que no exista.
        with open('paises.csv', 'x', encoding='utf-8') as archivo:
            #Crea una lista con varios datos de distintos paises para que el archivo contenga informacion antes de empezar en caso de que le archivo no exista previamente.
            inicio = ['nombre,poblacion,superficie,continente\n','Argentina,45376763,2780400,America\n','Japon,125800000,377975,Asia\n','Brasil,213993437,8515767,America\n','Alemania,83149300,357022,Europa' ]
            #Escribe la estructura base (cabecera) y los primeros registros en el nuevo archivo.
            archivo.writelines(inicio)
    #Se ejecuta solo si el archivo ya esxiste.
    except FileExistsError:
         #En caso de que el archivo exista se captura el error pero no se le muestra nada al usurio.
         pass
    
#Crea la funcion donde se bajaran los datos del archivo csv a una lista de diccionarios.
def datos(paises):
    #Limpia la lista de paises para que los datos que se cargue sean completamente nuevos y no se repitan.
    paises.clear()
    #Abre el archivo en modo lectura y guarda lo que este en el archivo en la varible archivo.
    with open('paises.csv', 'r', encoding='utf-8-sig') as archivo:
        #Crea un lector que transforma cada fila del csv en un diccionario, usando la primera linea como clases.
        lector_csv = csv.DictReader(archivo)
        #Crea una lista vacia para guardar los diccionarios procesados y limpios.
        lista_convertida = []
        #Crea un bucle que va a iterar por cada elemento de lector csv.
        for i in lector_csv:
            #Saca los espacios en blanco adicionales al inicio y final de cada clave y valor.
            fila_limpia = {clave.strip(): valor.strip() for clave, valor in i.items()}
            #Convierte el texto de la poblacion a un numero entero para poder hacer calculos numericos.
            fila_limpia['poblacion'] = int(fila_limpia['poblacion'])
            #Convierte el texto de la superfice a un numero entero para poder hacer calculos numericos.
            fila_limpia['superficie'] = int(fila_limpia['superficie'])
            #Agrega el diccionario del pais completamente limpio y formateado a la lista temporal.
            lista_convertida.append(fila_limpia)
        #Agrea la lista de paises la lista temporal la cual ya esta limpia.
        paises.extend(lista_convertida)

#Crea la funcion donde se va a verificar que el usuario solo se ingresen letras.
def verificar_solo_letras(mensaje, error):
        #Le pide al usuario que ingrese un texto con el mensaje que se le de a la funcion como argumento.
        texto = input(mensaje).strip().capitalize()
        #Verifoca que el texto solo contenga letras.
        while not texto.isalpha():
            #En caso de no contener solo letras muestra un mensaje de error.
            print(f'ERRORR: {error}')
            #Pide de nuevo el texto al usuario.
            texto = input(mensaje).strip().capitalize()
        #En caso de que el texto sea valido retorna el texto ingresado.
        return texto

#Crea la funcion que se encarga de sacara los acentos a las palabras del texto.
def sacar_acentos(texto):
        #Crea una lista de tuplas con las equivalencias para saber que vocal con tilde se cambia por cual sin tilde.
        reemplazos = [("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u")]
        #Convierte el valor del texto, lo pasa a minusculas y elimini los espacios en blanco.
        texto_limpio = str(texto).lower().strip()
        #Crea un bucle que va a iterar por cada elemento de la lista de remplazos.
        for con_tilde, sin_tilde in reemplazos:
            #Reemplaza todas las apariciones de la vocal con tilde por su versión limpia y actualiza la cadena.
            texto_limpio = texto_limpio.replace(con_tilde, sin_tilde)
        #Retorna el texto limpio.
        return texto_limpio

#Crea la funcion donde se genera un numero entero que no sea negativo.
def generar_rango(mensaje):
    #Crea un bucle que va a iterar hasta que se fuerze su salida.
    while True:        
        try:
            #Intenta pedirle al ususario que ingrese un numero entero.
            rango = int(input(mensaje))
            #Verifica si el numero ingresado es positivo.
            if rango < 0:
                #En caso de no serlo fuerza un error con un mensaje que se le de como argumento.
                raise ValueError('ERROR: No se permiten rangos negativos...')
            #En caso de que no haya errores retorna el numero ingresado por el ususario.
            return rango
        #Se ejecuta solo si el usuario intenta ingerea cualquier cosa que no sea un numero entero.
        except ValueError as e:
            if 'invalid literal for int()' in str(e):
                print('Error en el rango: Debe ingresar un numero entero valido (no se permiten letras)...')
            else:
                print(f'Error en el rango: {e}')
        #Se ejecuta solo si se produce algun error no esperado.
        except Exception as e:
            print(f'Se produjo un error inesperado: {e}')