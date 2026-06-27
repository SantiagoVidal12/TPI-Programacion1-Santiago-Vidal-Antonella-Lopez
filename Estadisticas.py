#Crea la funcion donde se van buscar los paises con mayor y menor poblacion.
def may_men(paises):
    #Crea la variable mayor seteandola con el primer elemento de la lista de paises con la clave de poblacion.
    mayor = paises[0]['poblacion']
    #Crea la variable menor seteandola con el primer elemento de la lista de paises con la clave de poblacion.
    menor = paises[0]['poblacion']
    #Crea lista donde se van a guardar los elementos con mayor poblacion.
    lis_may = [paises[0]]
    #Crea lista donde se van a guardar los elementos con menor poblacion.
    lis_men = [paises[0]]
    #Crea un bucle que va a iterar desde el segundo elemento de la lista paises hasta el final.
    for i in paises[1:]:
        #Verifica si el elmento actual con la clave de poblacion es mayor al que se encuentra en la variable mayor.
        if i['poblacion'] > mayor:
            #En caso de serlo remplaza en la varible mayor con el elemento con la clave poblacion.
            mayor = i['poblacion']
            #Guarda en la lista el elemento actual borrando el anterior elemento en caso de haberlo.
            lis_may = [i]
        #En caso de que no sea mayor verifica que el elemento actual sea igual al que se encuentra en la variable mayor.
        elif i['poblacion'] == mayor:
            #En caso de serlo lo agrega a la lista el elemento actual. 
            lis_may.append(i)
        
        #Verifica si el elmento actual con la clave de poblacion es menor al que se encuentra en la variable menor.
        if i['poblacion'] < menor:
            #En caso de serlo remplaza en la varible menor con el elemento con la clave poblacion.
            menor = i['poblacion']
            #Guarda en la lista el elemento actual borrando el anterior elemento en caso de haberlo.
            lis_men = [i]
        #En caso de que no sea menor verifica que el elemento actual sea igual al que se encuentra en la variable menor.
        elif i['poblacion'] == menor:
            #En caso de serlo lo agrega a la lista el elemento actual. 
            lis_men.append(i)
    #Retorna la lista list may y lis men.
    return lis_may, lis_men

#Crea la funcion donde se va a mostrar los resultados de busqueda de los paises con mayor y menor poblacion.
def mostrar_may_men(mayor, menor):
    print("=" * 60)
    print("REPORTE DE POBLACION MUNDIAL")
    print("=" * 60)

    print('Pais(es) con Mayor poblacion:')
    #Crea un bucle que va a iterar tantas veces como elementos tenga la lista de mayor.
    for i in mayor:
        #Muestra cada elemento con su clave en cado vuelta de bucle.
        print(f'Pais: {i['nombre']:^15} | Poblacion: {i['poblacion']:^15}')
    
    print("=" * 60)

    print('Pais(es) con Menor poblacion:')
    #Crea un bucle que va a iterar tantas veces como elementos tenga la lista de menor.
    for j in menor:
        #Muestra cada elemento con su clave en cado vuelta de bucle.
        print(f'Pais: {j['nombre']:^15} | Poblacion: {j['poblacion']:^15}')

#Crea la funcion donde se calcula el promedio.
def promedio(paises, clave):
    #Crea la variable donde se guarda la cantidad de elementos que tiene la lista
    cantidad = len(paises)
    #Crea la variable donde se guardara la suma de los elemntos con la clave que se ingrese como argumento.
    suma = sum(pais[clave] for pais in paises)
    #Crea la variable donde se guarara el resultado del calculo del promedio.
    prom = suma / cantidad
    #Retorna el promedio.
    return prom

#Crea la funcion donde se va a mostrar los resultados del promedio.
def mostrar_promedio(prom_poblacion, prom_superficie):
    print("=" * 60)
    print('PROMEDIOS:')
    print("=" * 60)

    #Muestra el resultado del promedio de poblacion.
    print(f'Promedio de Poblacion: {prom_poblacion:,.2f} hab.')
    #Muestra el resultado del promedio de superficie.
    print(f'Promedio de Superficie: {prom_superficie:,.2f} km²')
    print("=" * 60)

#Crea la funcion donde se va contar la cantidad de paises que hay por continentes.
def contar_por_continente(paises):
    #Crea un diccionario vacio.
    conteo = {}
    #Crea un bucle que va a iterar tantas veces como elementos tenga la lista de paises.
    for i in paises:
        #Crea una variable donde guarda el elemento actual con la clave de continente.
        continente = i['continente']
        #Guarda en el diccionario conteo con la clave continente y verifica con .get si ya existe el continente en el diccionario y en caso de existir lo crea en cero y despues se le suma 1 al conteo.
        conteo[continente] = conteo.get(continente, 0) + 1

    #Retorna el diccionario conteo.
    return conteo

#Crea la funcion donde se va a mostrar el conteo de continentes.
def mostrar_conteo_de_continentes(conteo):
    print("=" * 60)
    print("CANTIDAD DE PAISES POR CONTINENTE")
    print("=" * 60)

    print(f"{'Continente':^15} | {'Cantidad':^15}")

    #Crea un bucle que va a iterar entre los items del diccionario conteo.
    for continente, cantidad in conteo.items():
        #Muestra el continente y la cantidad de paises que tienen.
        print(f'{continente:^15} | {cantidad:^15} paises')
    
    print("=" * 60)