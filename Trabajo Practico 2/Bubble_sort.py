
# Bubble Sort
def bubble_sort(arr):
    print(f"Lista inicial: {arr}")
    n = len(arr)
    for i in range(n):
        print(f"\nPasada {i+1}:")
        for j in range(0, n - i - 1):
            print(f"Comparando {arr[j]} y {arr[j+1]}")
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print("  Swap →", arr)
            else:
                print("  Sin cambio")
        print("Fin de pasada:", arr)

    print("\nResultado final:", arr)
    return arr
  
# Ejemplo ..
if __name__ == "__main__":
    lista = [1, 7, 3, 2, 0, 8]
    bubble_sort(lista)
