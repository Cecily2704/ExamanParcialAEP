#Hacer que el sistema genere un numero aleatorio entre 1 y 10. 
#Luego hacer qu el usuario adivine el número. 
#La aplicación debe terminar cuando el usuario adivine.

import os, random
os.system("cls")

s = random.randint(1,10)

while True:
    n = int(input("Adivina el número del sistema (1,10):"))
    if n == s:
        print("Adivinaste!!")
        break
    else:
        print("Número incorrecto.")