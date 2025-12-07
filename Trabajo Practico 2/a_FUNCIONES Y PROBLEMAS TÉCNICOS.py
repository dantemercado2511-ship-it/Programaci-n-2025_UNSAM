# Resolución del problema de Josefo

def josefo(n, k):
    """Devuelve la posición del sobreviviente usando recursión."""
    if n == 1:
        return 1
    return (josefo(n - 1, k) + k - 1) % n + 1

# Demostración 
if __name__ == "__main__":
    soldados = 40

    print(" Caso histórico: salto n = 1 ")
    print(f"Último sobreviviente: posición {josefo(soldados, 1)}\n")

    print(" Caso adicional: salto n = 3 ")
    print(f"Último sobreviviente: posición {josefo(soldados, 3)}\n")

    # También podés probar valores a gusto
    n = int(input("Ingrese cantidad de personas: "))
    k = int(input("Ingrese paso de eliminación k: "))
    print(f"Último sobreviviente: posición {josefo(n, k)}")
