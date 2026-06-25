from Funciones_Generales import quitar_acentos
def filtrar_continente(paises, continente):
    iguales = []
    for i in paises:
        if quitar_acentos(i['continente'].strip().lower()) == quitar_acentos(str(continente).strip().lower()):
            iguales.append(i)
    return iguales

def filtrar_rango(paises, rango_1, rango_2, clave):
    iguales = []
    for i in paises:
        if rango_1 <= i[clave] <= rango_2:
            iguales.append(i)
    return iguales

def mostrar_filtrados(lista, clave):
    if len(lista) == 0:
        print(f'No se encontraron elementos con {clave}...')
    else:
        for i in lista:
            print(f'Pais: {i['nombre']:^15} | Poblacion: {i['poblacion']:^15} | Superficie: {i['superficie']:^15} | Continente: {i['continente']:^15}')