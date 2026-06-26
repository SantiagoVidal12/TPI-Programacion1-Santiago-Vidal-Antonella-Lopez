import csv

def actualizar_pais():
    # Carga los datos del CSV.
    paises = []
    with open('paises.csv', 'r', encoding='utf-8-sig') as archivo:
        lector_csv = csv.DictReader(archivo)
        paises.extend(lector_csv)

    # Solicita el nombre del pais a actualizar.
    nombre = input('Ingrese el nombre del pais que desea actualizar: ').strip()

    # Busca el pais en la lista.
    pais_encontrado = None
    for pais in paises:
        if pais['nombre'].lower() == nombre.lower():
            pais_encontrado = pais
            break

    if not pais_encontrado:
        print(f'\nNo se encontro ningun pais con el nombre "{nombre}".')
        return

    # Muestra los datos actuales del pais.
    print(f'\nDatos actuales de {pais_encontrado["nombre"]}:')
    print('-' * 60)
    print(f'  1. Nombre     : {pais_encontrado["nombre"]}')
    print(f'  2. Poblacion  : {int(pais_encontrado["poblacion"]):,} habitantes')
    print(f'  3. Superficie : {int(pais_encontrado["superficie"]):,} km²')
    print(f'  4. Continente : {pais_encontrado["continente"]}')
    print('-' * 60)

    # Solicita que campo actualizar.
    print('¿Que dato desea actualizar?')
    print('1. Nombre\n2. Poblacion\n3. Superficie\n4. Continente')
    
    while True:
        try:
            opcion = int(input('Ingrese la opcion: ').strip())
            if opcion not in [1, 2, 3, 4]:
                print('ERROR: Ingrese una opcion valida (1-4).')
                continue
            break
        except ValueError:
            print('ERROR: Solo se permiten numeros enteros.')

    # Actualiza el campo seleccionado.
    match opcion:
        case 1:
            nuevo_valor = input('Ingrese el nuevo nombre: ').strip()
            pais_encontrado['nombre'] = nuevo_valor
        case 2:
            while True:
                try:
                    nuevo_valor = int(input('Ingrese la nueva poblacion: ').strip())
                    pais_encontrado['poblacion'] = nuevo_valor
                    break
                except ValueError:
                    print('ERROR: La poblacion debe ser un numero entero.')
        case 3:
            while True:
                try:
                    nuevo_valor = int(input('Ingrese la nueva superficie (en km²): ').strip())
                    pais_encontrado['superficie'] = nuevo_valor
                    break
                except ValueError:
                    print('ERROR: La superficie debe ser un numero entero.')
        case 4:
            nuevo_valor = input('Ingrese el nuevo continente: ').strip()
            pais_encontrado['continente'] = nuevo_valor

    # Reescribe el CSV con los datos actualizados.
    with open('paises.csv', 'w', encoding='utf-8-sig', newline='') as archivo:
        campos = ['nombre', 'poblacion', 'superficie', 'continente']
        escritor_csv = csv.DictWriter(archivo, fieldnames=campos)
        escritor_csv.writeheader()
        escritor_csv.writerows(paises)

    print(f'\nEl pais fue actualizado exitosamente.')
    print('-' * 60)
    print(f'  Nombre     : {pais_encontrado["nombre"]}')
    print(f'  Poblacion  : {int(pais_encontrado["poblacion"]):,} habitantes')
    print(f'  Superficie : {int(pais_encontrado["superficie"]):,} km²')
    print(f'  Continente : {pais_encontrado["continente"]}')
    print('-' * 60)