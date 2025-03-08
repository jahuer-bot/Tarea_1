print("Operaciones")

num1 = float(input("Ingresar 1er numero: "))
num2 = float(input("Ingresar 2do numero: "))

Divicion = num1 / num2 if num2 != 0 else "Indefinido (no se puede dividir por 0)"

print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Multiplicacion: {num1 * num2}")
print(f"Divicion: {Divicion}")