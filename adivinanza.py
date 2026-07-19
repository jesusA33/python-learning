import random

n_aleatorio = random.randint(1, 100)


contador = 1 

while contador < 6: 
    numero = int(input("ingrese su numero " ))
    if n_aleatorio > numero: 
        print(f"intento {contador}: {numero}")
        print("es mayor")
    elif n_aleatorio < numero:
        print(f"intento {contador}: {numero}")
        print("es menor")
    else: 
        print(f"intento {contador}: {numero}")
        print("ganaste")
        contador = 5
    contador +=1
