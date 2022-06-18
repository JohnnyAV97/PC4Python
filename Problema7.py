import re

n = int(input("Cantidad de correos a ingresar: "))

lista_correo = []

for i in range(1,n+1):
    correo = input("Ingrese un correo electrónico: ")
    lista_correo.append(correo)

for j in lista_correo:
    patron = r".+@.+[.][c][o][m]"
    coinc = re.findall(patron, j)
    if j in coinc:
        print("The mail "+j+" is a valid mail")
    else:
        print("The mail "+j+" is a invalid mail")