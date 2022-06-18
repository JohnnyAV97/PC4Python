import os

BIENVENIDA = "Bienvenido al menú interactivo"
MSG = """¿Qué quieres hacer? Escribe una opción
    1) Crear tabla
    2) Mostrar tabla
    3) Mostrar línea de tabla
    4) Salir
    Opcion: """

def main():
    print(BIENVENIDA)
    while True:
        opcion = input(MSG)

        if opcion == '1':
            os.chdir('c:/Users/Jhony Aybar/Desktop/PC4/Problema4')
            n = int(input("Ingrese un número entero entre 1 y 10: "))
            with open('./tabla-'+str(n)+'.txt','w') as f:
                for i in range(1,13):
                    producto = n * i
                    texto=(str(n)+"*"+str(i)+"="+str(producto)+"\n")
                    f.write(texto)

        elif opcion == '2':
            os.chdir('c:/Users/Jhony Aybar/Desktop/PC4/Problema4')
            n = int(input("Ingrese un número entero entre 1 y 10: "))
            try:
                with open('./tabla-'+str(n)+'.txt','r') as f:
                    print(f.read())
            except:
                print("Fichero no existe.")

        elif opcion == '3':
            os.chdir('c:/Users/Jhony Aybar/Desktop/PC4/Problema4')
            n = int(input("Ingrese el valor de n (entre 1 y 10): "))
            m = int(input("Ingrese el valor de m (entre 1 y 12): "))
            try:
                with open('./tabla-'+str(n)+'.txt','r') as f:
                    print(f.readlines()[m-1])
            except:
                print("Fichero no existe.")

        elif opcion == '4':
            print("¡Hasta luego! Ha sido un placer ayudarte")
            break
    pass

main()