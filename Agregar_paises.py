import csv

def agregar_pais():
    # Solicita al usuario los datos del nuevo pais.
    nombre = input('Ingrese el nombre del pais: ').strip()
    
    # Verifica que el pais no exista ya en el CSV.
    with open('paises.csv', 'r', encoding='utf-8-sig') as archivo:
        lector_csv = csv.DictReader(archivo)
        for pais in lector_csv:
            if pais['nombre'].lower() == nombre.lower():
                print(f'\nEl pais "{nombre}" ya existe en el sistema.')
                return

    # Solicita el resto de los datos validando que sean numeros enteros.
    while True:
        try:
            poblacion = int(input('Ingrese la poblacion del pais: ').strip())
            break
        except ValueError:
            print('ERROR: La poblacion debe ser un numero entero.')

    while True:
        try:
            superficie = int(input('Ingrese la superficie del pais (en km²): ').strip())
            break
        except ValueError:
            print('ERROR: La superficie debe ser un numero entero.')

    continente = input('Ingrese el continente del pais: ').strip()

    # Agrega el nuevo pais al CSV.
    with open('paises.csv', 'a', encoding='utf-8-sig', newline='') as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerow([nombre, poblacion, superficie, continente])

    print(f'\nEl pais "{nombre}" fue agregado exitosamente.')
    print('-' * 60)
    print(f'  Nombre     : {nombre}')
    print(f'  Poblacion  : {poblacion:,} habitantes')
    print(f'  Superficie : {superficie:,} km²')
    print(f'  Continente : {continente}')
    print('-' * 60)

agregar_pais()
