clave = input("ingrese su clave ")

tiene_m = False
tiene_n = False
tiene_l = len(clave)>=8

for i in clave: 
    if i.isupper():
        tiene_m = True
    if i.isdigit():
        tiene_n = True

puntuacion = 0 

if tiene_l:
    puntuacion+=1 
if tiene_m:
    puntuacion+=1
if tiene_n:
    puntuacion+=1

if puntuacion == 3:
    resultado = "Fuerte"
elif puntuacion == 2: 
    resultado = "Media"
else:
    resultado = "Debil"


print(f"Resultado: Tu clave es {resultado}")