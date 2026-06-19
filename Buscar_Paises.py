import csv

def buscar_pais():
    # Carga los datos del CSV.
    paises = []
    with open('paises.csv', 'r', encoding='utf-8-sig') as archivo:
        lector_csv = csv.DictReader(archivo)
        paises.extend(lector_csv)

    # Solicita al usuario el nombre del pais a buscar.
    nombre = input('Ingrese el nombre del pais a buscar: ').strip()

    # Recorre la lista buscando coincidencias parciales sin importar mayusculas.
    resultados = [p for p in paises if nombre.lower() in p['nombre'].lower()]

    if resultados:
        print(f'\nSe encontraron {len(resultados)} resultado/s:\n')
        print('-' * 60)
        for pais in resultados:
            print(f'  Nombre     : {pais["nombre"]}')
            print(f'  Poblacion  : {int(pais["poblacion"]):,} habitantes')
            print(f'  Superficie : {int(pais["superficie"]):,} km²')
            print(f'  Continente : {pais["continente"]}')
            print('-' * 60)
    else:
        print(f'\nNo se encontro ningun pais con el nombre "{nombre}".')

buscar_pais()
