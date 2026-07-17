import random 

p1 = input("ingrese la primera palabra ")
p2 = input("ingrese la segunda palabra ")
p3 = input("ingrese la tercera palabra ")

numero_alatorio1 = random.randint(10, 99)

numero_alatorio2 = random.randint(10, 99)

numero_alatorio3 = random.randint(10, 99)

print(f"su password = {p1}{numero_alatorio1}{p2}{numero_alatorio2}{p3}{numero_alatorio3} ")

