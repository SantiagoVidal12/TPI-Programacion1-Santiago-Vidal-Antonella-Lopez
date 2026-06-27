#Importa la funcion de datos desde el archivo de Funciones Generales.
from Funciones_Generales import datos

#Crea la funcion que se encarga de buscar el pais que ingrese el usuario.
def buscar_pais(paises):
    #Llama a la funcion datos y se le da la lista de paises como argumento.
    datos(paises)
    #Solicita al usuario el nombre del pais a buscar.
    nombre = input('Ingrese el nombre del pais a buscar: ').strip()

    #Recorre la lista buscando coincidencias parciales sin importar mayusculas.
    resultados = [p for p in paises if nombre.lower() in p['nombre'].lower()]

    #Verifica que se hayan encontrado resultados.
    if resultados:
        #En caso de encontrarse.
        print(f'\nSe encontraron {len(resultados)} resultado/s:\n')
        print('-' * 60)
        #Crea un bucle que itera por cada elemento que contenga la lista de resultados.
        for pais in resultados:
            #Muestra cada clave con su valor.
            print(f'  Nombre     : {pais["nombre"]}')
            print(f'  Poblacion  : {int(pais["poblacion"]):,} habitantes')
            print(f'  Superficie : {int(pais["superficie"]):,} km²')
            print(f'  Continente : {pais["continente"]}')
            print('-' * 60)
    #En caso de no encontrarse resultados.
    else:
        #Se le avisa al usuario con un mensaje.
        print(f'\nNo se encontro ningun pais con el nombre "{nombre}".')