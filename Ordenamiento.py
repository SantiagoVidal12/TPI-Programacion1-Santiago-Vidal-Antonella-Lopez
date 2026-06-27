#Crea la funcion donde van a ordenar los elemntos de la lista dependiendo de la clave que se le pase como argumento.
def ordenamiento(paises, clave, descendente=False):
    #Crea una variable donde va a guradar la cantidad de elementos que tiene la lista paises.
    rango = len(paises)
    #Crea un bucle que va a iterar tantas veces como cantidad de elementos tenga la lista paises
    for i in range(rango):
        #Crea un bucle que va a iterar tantas veces como de el resultado de a la cantidad de elemntos tenga la lista se le reste el elemento ieterado en el anterior bucle menos uno.
        for j in range(rango - i - 1):
            #Verifica si el argumento descendente que se le da a la funcio esta en true.
            if descendente:
                #Verifica si el elemento actual es menor que el siguiente
                cumple_condicion = paises[j][clave] < paises[j+1][clave]
            #En caso de que el argumento descendente no este activado.
            else:
                ##Verifica si el elemento actual es mayor que el siguiente
                cumple_condicion = paises[j][clave] > paises[j+1][clave]

            #Verifica si se cumple la condicion.
            if cumple_condicion:
                #En caso de cumplirse guarda el pais actual en una variable auxiliar para no perderlo.
                temporal = paises[j]
                #Desplaza el pais siguiente a la posicion del pais actual.
                paises[j] = paises[j+1]
                #Coloca el pais guardado en la posicion de siguiente 
                paises[j+1] = temporal

#Crea la funcion donde se van a mostrar los paises ordenados,
def mostrar_ordenamiento(paises,mensaje):
    print(f'Lista ordenada por {mensaje}')
    #Crea un bucle que va a iterar tantas veces como elementos tenga la lista de paises.
    for i in paises:
        #Muestra cada elemnento con su clave en cada vuelta del bucle.
        print(f'Pais: {i['nombre']:^15} | Poblacion: {i['poblacion']:^15,} | Superficie: {i['superficie']:^15,} | Continente: {i['continente']:^15}')