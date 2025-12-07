s = input("Ingrese una cadena: ")
s = s.lower()

vocales = "aeiou"
contador = 0
for letra in s:
    if letra in vocales:
        contador += 1

print("Número de vocales:", contador)
