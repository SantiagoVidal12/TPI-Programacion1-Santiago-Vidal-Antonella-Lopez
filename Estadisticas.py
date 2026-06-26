def may_men(paises):
    mayor = paises[0]['poblacion']
    menor = paises[0]['poblacion']
    lis_may = [paises[0]]
    lis_men = [paises[0]]
    for i in paises[1:]:
        if i['poblacion'] > mayor:
            mayor = i['poblacion']
            lis_may= [i]
        elif i['poblacion'] == mayor:
            lis_may.append(i)
        if i['poblacion'] < menor:
            menor = i['poblacion']
            lis_men = [i]
        elif i['poblacion'] == menor:
            lis_men.append(i)
    return lis_may, lis_men

def mostrar_may_men(mayor, menor):
    print("=" * 60)
    print("REPORTE DE POBLACION MUNDIAL")
    print("=" * 60)

    print('Pais(es) con Mayor poblacion:')
    for i in mayor:
        print(f'Pais: {i['nombre']:^15} | Poblacion: {i['poblacion']:^15}')
    
    print("=" * 60)

    print('Pais(es) con Menor poblacion:')
    for j in menor:
        print(f'Pais: {j['nombre']:^15} | Poblacion: {j['poblacion']:^15}')

def promedio(paises, clave):
    cantidad = len(paises)
    suma = sum(pais[clave] for pais in paises)
    promedio = suma / cantidad
    return promedio

def mostrar_promedio(prom_poblacion, prom_superficie):
    print("=" * 60)
    print('PROMEDIOS:')
    print("=" * 60)

    print(f'Promedio de Poblacion: {prom_poblacion:,.2f} hab.')
    print(f'Promedio de Superficie: {prom_superficie:,.2f} km²')
    print("=" * 60)

def contar_por_continente(paises):
    conteo = {}
    for i in paises:
        continente = i['continente']
        conteo[continente] = conteo.get(continente, 0) + 1

    return conteo

def mostrar_conteo_de_continentes(conteo):
    print("=" * 60)
    print("CANTIDAD DE PAISES POR CONTINENTE")
    print("=" * 60)

    print(f"{'Continente':^15} | {'Cantidad':^15}")

    for continente, cantidad in conteo.items():
        print(f'{continente:^15} | {cantidad:^15} paises')
    
    print("=" * 60)