segundos = float(input("ingrese la cantidad de segundos "))
horas = segundos // 3600
segundos_restantes = segundos % 3600 
minutos = segundos // 60 
segundos_finales = segundos_restantes % 60 


print(f"{segundos:.0f} segundos = {horas:.0f} horas, {minutos:.0f} minutos, {segundos_finales:.0f} segundos")
