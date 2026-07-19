peso = float(input("Por favor ingrese su peso "))

altura = float(input("Por favor ingrese su altura "))

imc = peso / (altura ** 2) 


print(f"Peso (kg) {peso}")
print(f"Altura (m) {altura}")
print(f"Tu IMC es de {imc:.2f}")
