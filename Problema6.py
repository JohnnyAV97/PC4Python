import re

cadena = '@robot9! @robot4& I have a good feeling that the show is going to be amazing! @robot9$ @robot7%'
patron = '@robot\d\W'

print(re.findall(patron,cadena))