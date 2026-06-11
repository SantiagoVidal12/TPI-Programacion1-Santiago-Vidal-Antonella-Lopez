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