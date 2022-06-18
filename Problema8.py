import re

tarjeta = input("Ingrese el número de tarjeta: ")
tarjeta1 = tarjeta.replace('-','')
tarjeta2 = tarjeta1.strip()

def tiene16():
    if len(tarjeta2) == 16:
        return True

def patron():
    patron = r"[456][0-9]{15}"
    coinc = re.findall(patron, tarjeta2)
    if coinc != []:
        if coinc[0] == tarjeta2:
            return True
        else:
            pass
    else:
        return False

def consecutivos():
    i=0
    while i+3<len(tarjeta2):
        n = tarjeta2[i]
        if f"{n*4}" == f"{tarjeta2[i]}{tarjeta2[i+1]}{tarjeta2[i+2]}{tarjeta2[i+3]}":
            return False
        i+=1
    return True


if (patron() and tiene16() and consecutivos())== True:
    print("Valid")
else:
    print("Invalid")