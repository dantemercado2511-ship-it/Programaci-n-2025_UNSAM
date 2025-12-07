# Raíz cúbica por método de bisección


x = float(input("Ingrese un número (positivo o negativo): "))

# MÉTODO DE BISECCIÓN
if x >= 0:
    low = 0
    high = max(1, x)
else:
    low = min(-1, x)
    high = 0

tolerancia = 1e-6
pasos_biseccion = 0

while True:
    pasos_biseccion += 1
    mid = (low + high) / 2
    cubo = mid**3

    if abs(cubo - x) <= tolerancia:
        raiz_biseccion = mid
        break

    if cubo < x:
        low = mid
    else:
        high = mid

print("\n--- MÉTODO DE BISECCIÓN ---")
print(f"Raíz cúbica aproximada: {raiz_biseccion}")
print(f"Pasos ejecutados: {pasos_biseccion}")


# MÉTODO DE NEWTON–RAPHSON
tolerancia = 1e-6
pasos_newton = 0
y = x if x != 0 else 1  # linea que da una estimación inicial


while True:
    pasos_newton += 1
    f = y**3 - x
    df = 3 * y**2

    if df == 0:  # linea que evita división por cero
        y += 1
        continue

    y_new = y - f/df

    if abs(y_new - y) < tolerancia:
        raiz_newton = y_new
        break

    y = y_new

print("\n MÉTODO DE NEWTON–RAPHSON ")
print(f"Raíz cúbica aproximada: {raiz_newton}")
print(f"Pasos ejecutados: {pasos_newton}")


# COMPARACIÓN FINAL
print("\n COMPARACIÓN ")
print(f"Diferencia entre métodos: {abs(raiz_biseccion - raiz_newton)}")
print(f"Newton fue {pasos_biseccion / pasos_newton:.2f} veces más rápido (en número de iteraciones).")
