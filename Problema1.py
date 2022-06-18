import random

def get_int(msg: str='Ingrese un número entero: ')->int:
    """Solicita un número entero"""
    try:
        x = int(input(msg))
        return x
    except:
        return get_int(msg)

n = get_int("Ingresar el nivel del juego: ")
numero_adivinar = random.randint(1,n)

print("Level: "+str(n))

while True:
    numero_ingresado = get_int("Guess: ")

    if numero_ingresado < numero_adivinar:
        print("¡Demasiado pequeño!")
            
    elif numero_ingresado > numero_adivinar:
        print("¡Te pasaste!")
            
    elif numero_ingresado == numero_adivinar:
        print("¡Adivinaste!")
        break
pass