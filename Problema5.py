import os

ruta_archivo = input("Ingrese la ruta del archivo.py: ")
nombre_archivo = input("Ingrese el nombre del archivo: ")

try:
    if nombre_archivo[len(nombre_archivo)-3:len(nombre_archivo)] == ".py":
        archivo = open(ruta_archivo,"r")
        conteo = 0
        for linea in archivo.readlines():
            linea = linea.strip()
            if linea == '' or linea[0] == "#" or linea[0:2] == '"""':
                conteo = conteo
            else:
                conteo = conteo + 1
        print(conteo)
    else:
        pass

except FileNotFoundError:
    pass