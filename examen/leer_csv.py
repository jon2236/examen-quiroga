import random
from prog_funcional.funciones_prog import *




def get_path_actual(nombre_archivo):
    import os
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)

with open(get_path_actual("bicicletas.csv"), "r", encoding="utf-8") as archivo :
    lista = []
    encabezado = archivo.readline().strip("\n").split(",")

    for linea in archivo.readlines():
        bici = {}
        linea = linea.strip("\n").split(",")

        id_bike, nombre, tipo, tiempo = linea
        bici["id"] = int(id_bike)
        bici["nombre"] = nombre
        bici["tipo"] = tipo
        bici["tiempo"] = float(tiempo)
        lista.append(bici)
        

for bici in lista:
    print(bici)

print("/////////////////////////////////////////////////////////////////////////")

for i in range(len(lista)) :
    lista[i]["nombre"] = lista[i]["nombre"].upper() #reemplazar

    #3
    lista = mapear_lista(asignar_tiempo_aleato, lista)

    #4
    ganador = reduce(lambda bici1, bici2: bici1 if bici1["tiempo"] < bici2["tiempo"] else bici2, lista)

    empates = [bici for bici in lista if bici["tiempo"] == ganador["tiempo"]]

if len(empates) > 1:
    print(f"Hubo un empatecon un tiempo de {ganador['tiempo']} Los ganadores son:")
    for empate in empates:
        print(f"Nombre: {empate["nombre"]}, Tiempo: {empate["tiempo"]}")
else:
    print(f"El ganador es: {ganador["nombre"]} con {ganador["tiempo"]} minutos")

    #5

continuar = "s"

while continuar.lower() == "s":
    menu_biciletas()
    opcion = input("Ingrese el número de opción: ")

    if opcion == "1":
        get_path_actual()
    elif opcion == "2":
        pass
    elif opcion == "3":
        pass
    elif opcion == "4":
        pass
    elif opcion == "5":
        pass
    elif opcion == "6":
        pass
    elif opcion == "7":
        pass
    elif opcion == "0":
        salir = input("¿Confirma salida? (s/n): ").lower()
        if salir == "s":
            continuar = "n"
    else:
        print("opción no válida. intente nuevamente.")


    pausar()


for bici in lista:
    print(bici)

with open(get_path_actual("personas_mayusculas.csv"), "w", encoding="utf-8") as archivo :
    encabezado = ",".join(list(lista[0].keys())) + "\n"
    archivo.write(encabezado)
    for bici in lista:
        values = list(bici.values())
        l = []
        for value in values:
            if isinstance(value, int): 
                l.append(str(value))
            elif isinstance(value, float): 
                l.append(str(value))
            else:
                l.append(value)
        linea = ",".join(l) + "\n"
        archivo.write(linea)
