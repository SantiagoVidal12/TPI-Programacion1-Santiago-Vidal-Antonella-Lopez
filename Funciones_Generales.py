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
               
               i['poblacion'] = int(i['poblacion'])
               i['superficie'] = int(i['superficie'])
               lista_convertida.append(i)

          paises.extend(lista_convertida)