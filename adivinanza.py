import random

n_aleatorio = random.randint(1, 10)


contador = 1 

while contador < 6: 
    numero = int(input("ingrese su numero " ))
    if n_aleatorio > numero: 
        print(f"intento {contador}: {numero}")
        print("El número es mayor, intentá con uno más grande")
    elif n_aleatorio < numero:
        print(f"intento {contador}: {numero}")
        print("El número es menor, intentá con uno más chico")
    else: 
        print(f"intento {contador}: {numero}")
        print(f"¡Ganaste en {contador} intentos!")
        break
    contador +=1

if contador > 5:
    print(f"Perdiste. El número era {n_aleatorio}")