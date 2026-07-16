monto = float(input("Ingrese su monto "))

porcentaje = float(input("ingrse su porcentaje de propina 10, 15, 20% "))

propina = (monto * porcentaje / 100)

total = monto + propina

print(f"Subtotal: ${monto}")
print(f"Propina: ${propina}")
print(f"Total: ${total}")