import random

def mapear_lista(procesadora, lista:list) -> list:
    lista_retorno = []
    for el in lista:
        lista_retorno.append(procesadora(el))
    return lista_retorno


def filtra_lista(filtradora, lista: list) -> list:
    lista_filtrada = []
    for el in lista:
        if filtradora(el):
            lista_filtrada.append(el)
    return lista_filtrada


def for_each_lista(funcion, lista:list) -> None:
    for i in range(len(lista)):
        lista[i] = funcion(lista[i])


def get_path_actual(nombre_archivo):
    import os
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)


def reduce(funcion, lista:list) -> any:
    ant = lista[0]
    for el in lista[1:]:
        ant = funcion(ant, el)
    return ant

def calcular_promedio(lista:list) -> float:
    if isinstance(lista, list):
        suma = len(lista)
        if suma == 0:
            raise ValueError("no esta definido el promedio de una lista vacia")
        return totalizar_lista(lista) / suma
    

def totalizar_lista(lista:list) -> int:
    total = 0
    for valor in (lista):
        total += valor
    return total


def altura_a_float(lista):
    for i in lista:
        i["altura"] = float(i["altura"])

def peso_a_float(lista):
    for i in lista:
        i["peso"] = float(i["peso"])




def asignar_tiempo_aleato(bici):
        bici["tiempo"] = random.randint(50, 120)
        return bici


def menu_biciletas():
    print("///////////////Menu de opciones:///////////////////  ")
    print("1- Cargar archivo .CSV")
    print("2-  Imprimir lista")
    print("3-  Asignar tiempos")
    print("4-  Informar ganador")
    print("5- Filtrar por tipo")
    print("6- Informar promedio por tipo")
    print("7-  Mostrar posiciones")
    print("0- Salir")


def pausar():
    """Pausa la ejecucion del programa hasta que el usuario presione una tecla
    """
    from os import system
    system("pause")


def validartiposdatos(value, expected_type):
    """ Valida que los valores en el diccionario args correspondan a los tipos especificados.
    Args:
        value: Nombre del argumento.
        excpectedtype: El tipo de dato esperado del valor (value).

    Raises:
        TypeError: Si algún valor no corresponde con el tipo esperado.
    """
    if not isinstance(value, expected_type):
            raise TypeError(f"El argumento '{value}' debe ser de tipo {expected_type.__name}, pero se recibió {type(value).__name}.")
    

    
    
    
    def mapear_datos_personajes(lista:list, sector:str)->list: #MAPEO GENERAL
        """Recorre los elementos de una lista y carga del sector elegido los datos en una nueva lista.

        Args:
            lista (list): Lista de diccionarios, donde cada diccionario representa a un personaje con varias propiedades.
            sector (str): String que representa la clave(key) del diccionario cuyo valor se quiere extraer de cada personaje en la lista.

        Raises:
        TypeError: Si algún valor no corresponde con el tipo esperado.

        Returns:
            list: Nueva lista que contiene los valores correspondientes a la clave (sector) para cada personaje de la lista original.
        """
    validar_tipos_datos(lista, list)
    validar_lista_vacia(lista)
    validar_tipos_datos(sector, str)

    lista_retorno = []
    for el in lista:
        lista_retorno.append(el[sector])
    return lista_retorno




def convertir_lista_a_float(lista):
    """
    Convierte todos los valores de una lista a enteros.

    Args:
        lista (list): Lista de valores.

    Returns:
        list: Lista de valores convertidos a enteros donde sea posible.
    """


    lista_convertida = []
    for valor in lista:
        try:
            lista_convertida.append(float(valor))
        except (ValueError, TypeError):
            lista_convertida.append(valor)
    return lista_convertida


