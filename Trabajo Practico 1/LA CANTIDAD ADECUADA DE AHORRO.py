pago_inicial = 0.25 * 1000000   # 25% de 1 millón
r = 0.04                        # retorno anual
aumento_semi_anual = 0.07       # aumento del 7%
meses_objetivo = 36

salario_anual = float(input("Introduzca su salario anual: "))
salario_mensual = salario_anual / 12

# Búsqueda de la tasa de ahorro (entre 0 y 1), pero usando 0–10000
low = 0
high = 10000

pasos = 0

def ahorro_en_36_meses(tasa_entera):
    """
    tasa_entera: entero entre 0 y 10000
    Devuelve el ahorro acumulado después de 36 meses.
    """
    tasa = tasa_entera / 10000  # conversión a decimal
    ahorro = 0.0
    salario = salario_mensual

    for mes in range(1, meses_objetivo + 1):
        ahorro *= (1 + r / 12)
        ahorro += salario * tasa

        if mes % 6 == 0:
            salario *= (1 + aumento_semi_anual)

    return ahorro

# Es imposible desde el principio?
if ahorro_en_36_meses(10000) < pago_inicial - 100:
    print("No es posible el pago total en 3 años")
else:
    # Búsqueda por bisección
    while True:
        pasos += 1
        mid = (low + high) // 2     # tasa de ahorro candidata (entera)
        ahorro = ahorro_en_36_meses(mid)

        # margen de ±100 dólares
        if abs(ahorro - pago_inicial) <= 100:
            break

        if ahorro < pago_inicial:
            low = mid
        else:
            high = mid

        # condición de seguridad
        if pasos > 50:  
            break

    mejor_tasa = mid / 10000  # conversión final

    print(f"Tasa de ahorro máxima: {mejor_tasa:.4f}")
    print(f"Pasos en la búsqueda de bisección: {pasos}")
