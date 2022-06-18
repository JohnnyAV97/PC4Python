import requests

def get_int(msg: str='Ingrese un número entero: ')->int:
    """Solicita un número entero"""
    try:
        x = int(input(msg))
        return x
    except:
        return get_int(msg)

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
response = requests.get(url)
data = response.json()
tipo_cambio = data['bpi']['USD']['rate']

tipo_cambio = float(tipo_cambio.replace(",",""))


n = get_int('Ingrese su cantidad de Bitcoins: ')
costo_actual = tipo_cambio * n
print("El costo actual es: {:,.2f}".format(costo_actual))