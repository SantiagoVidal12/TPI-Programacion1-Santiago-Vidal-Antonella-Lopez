#Importa todas las funciones desde el archivo de Funciones Generales.
from Funciones_Generales import sacar_acentos
#Crea la funcion donde se filtran los continentes.
def filtrar_continente(paises, continente):
    #Crea una lista vacia.
    iguales = []
    #Crea un bucle que va a iterar tantas veces como elementos tenga la lista de paises.
    for i in paises:
        #Verifica que el elmento con la clvae de continente sea igual al continente ingresado por el usuario.
        if sacar_acentos(i['continente'].strip().lower()) == sacar_acentos(str(continente).strip().lower()):
            #En caso de serlo se agrega el elemnto a la lista de iguales.
            iguales.append(i)
    #Retorna la lista iguales.
    return iguales

#Crea la funcion donde se van a filtrar por un rango determinado por el usuario.
def filtrar_rango(paises, rango_1, rango_2, clave):
    #Crea una lista vacia.
    iguales = []
    #Crea un bucle que va a iterar tantas veces como elementos tenga la lista de paises.
    for i in paises:
        #Verifica que el elemento con la clave que se ingrese este entre el rango ingresado.
        if rango_1 <= i[clave] <= rango_2:
            #En caso de estarlo se agrega a la lista iguales.
            iguales.append(i)
    #Retorna la lista iguales.
    return iguales

#Crea la funcion donde se van a mostrar los datos filtrados.
def mostrar_filtrados(lista, clave):
    #Verifica que la lista no estes vacia.
    if len(lista) == 0:
        #En caso de estarlo se le avisa al usuario con un mensaje.
        print(f'No se encontraron elementos con {clave}...')
    #En caso de no etsar vacia.
    else:
        #Crea un bucle que va a iterar tantas veces como elementos tenga la lista que se le de como argumento a la funcion.
        for i in lista:
            #Muestra cada elemnento con su clave en cada vuelta del bucle.
            print(f'Pais: {i['nombre']:^15} | Poblacion: {i['poblacion']:^15} | Superficie: {i['superficie']:^15} | Continente: {i['continente']:^15}')