total = 0.0

while True:
    entrada = input("Ingrese un monto (enter para terminar): ")

    if entrada == "":
        break

    monto = float(entrada)
    total += monto

print(f"Total acumulado: {total}")
