import csv
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

def crear_archvio():
    try:
        with open('paises.csv', 'x', encoding='utf-8') as archivo:
            inicio = ['nombre,poblacion,superficie,continente\n','Argentina,45376763,2780400,America\n','Japon,125800000,377975,Asia\n','Brasil,213993437,8515767,America\n','Alemania,83149300,357022,Europa\n' ]
            archivo.writelines(inicio)
    except FileExistsError:
         pass
    
def datos(paises):
     paises.clear()
     with open('paises.csv', 'r', encoding='utf-8-sig') as archivo:
          lector_csv = csv.DictReader(archivo)
          lista_convertida = []
          for i in lector_csv:
               fila_limpia = {clave.strip(): valor.strip() for clave, valor in i.items()}
               fila_limpia['poblacion'] = int(fila_limpia['poblacion'])
               fila_limpia['superficie'] = int(fila_limpia['superficie'])
               lista_convertida.append(fila_limpia)

          paises.extend(lista_convertida)

def verificar_solo_letras(mensaje, error):
        texto = input(mensaje)
        while not texto.isalpha():
            print(f'ERRORR: {error}')
            texto = input(mensaje).strip().capitalize()
        return texto

def quitar_acentos(texto):
        reemplazos = [("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u")]
        texto_limpio = str(texto).lower().strip()
        for con_tilde, sin_tilde in reemplazos:
            texto_limpio = texto_limpio.replace(con_tilde, sin_tilde)
        return texto_limpio

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