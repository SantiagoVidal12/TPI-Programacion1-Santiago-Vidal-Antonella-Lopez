def ordenamiento(paises, clave, descendente=False):
    rango = len(paises)
    for i in range(rango):
        for j in range(rango - i - 1):
            if descendente:
                cumple_condicion = paises[j][clave] < paises[j+1][clave]
            else:
                cumple_condicion = paises[j][clave] > paises[j+1][clave]

            if cumple_condicion:
                temporal = paises[j]
                paises[j] = paises[j+1]
                paises[j+1] = temporal

def mostrar_ordenamiento(paises,mensaje):
    print(f'Lista ordenada por {mensaje}')
    for i in paises:
        print(f'Pais: {i['nombre']:^15} | Poblacion: {i['poblacion']:^15} | Superficie: {i['superficie']:^15} | Continente: {i['continente']:^15}')