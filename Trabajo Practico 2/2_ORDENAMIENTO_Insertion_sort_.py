# Insertion Sort

def insertion_sort(arr):
    print(f"Lista inicial: {arr}")
    for i in range(1, len(arr)):
        clave = arr[i]
        j = i - 1
        print(f"\nInsertando {clave}...")
        while j >= 0 and arr[j] > clave:
            arr[j + 1] = arr[j]
            j -= 1
            print(arr)
        arr[j + 1] = clave
        print(arr)
    print("\nResultado final:", arr)
    return arr

# Ejemplo 
if __name__ == "__main__":
    lista = [1, 7, 3, 2, 0, 8]
    insertion_sort(lista)
