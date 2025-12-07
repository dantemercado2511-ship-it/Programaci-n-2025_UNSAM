# Raíz cúbica por método de bisección

x = float(input("Ingrese un número (positivo o negativo): "))

if x >= 0:
    low = 0
    high = max(1, x)
else:
    low = min(-1, x)
    high = 0

tolerancia = 1e-6
pasos = 0

while True:
    pasos += 1
    mid = (low + high) / 2
    cubo = mid**3
    if abs(cubo - x) <= tolerancia:
        break
    if cubo < x:
        low = mid
    else:
        high = mid

print(f"Raíz cúbica aproximada: {mid}")
print(f"Pasos ejecutados: {pasos}")
