# Selection Sort
def selection_sort(arr):
    print(f"Lista inicial: {arr}")
    n = len(arr)
    for i in range(n):
        min_idx = i
        print(f"\nSeleccionando mínimo desde índice {i}:")
        
        for j in range(i + 1, n):
            print(f"Comparando {arr[min_idx]} con {arr[j]}")
            if arr[j] < arr[min_idx]:
                min_idx = j
                print("  Nuevo mínimo encontrado:", arr[min_idx])

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"Swap → {arr}")

    print("\nResultado final:", arr)
    return arr

# Ejemplo..
if __name__ == "__main__":
    lista = [1, 7, 3, 2, 0, 8]
    selection_sort(lista)
