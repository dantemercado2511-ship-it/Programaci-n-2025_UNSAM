#  Quicksort
def lomuto_partition(A, lo, hi):
    pivot = A[hi]
    print(f"\nParticionando {A[lo:hi+1]} con pivote {pivot}")
    i = lo
    for j in range(lo, hi):
        print(f"Comparando {A[j]} con pivote {pivot}")
        if A[j] <= pivot:
            A[i], A[j] = A[j], A[i]
            print("  Swap →", A)
            i += 1
    A[i], A[hi] = A[hi], A[i]
    print("Colocando pivote →", A)
    return i

def quicksort(A, lo=0, hi=None):
    if hi is None:
        hi = len(A) - 1
    if lo < hi:
        p = lomuto_partition(A, lo, hi)
        quicksort(A, lo, p - 1)
        quicksort(A, p + 1, hi)
    return A

# Ejemplo de uso
if __name__ == "__main__":
    lista = [22, 36, 6, 79, 26, 45, 75, 13]
    print("Lista inicial:", lista)
    quicksort(lista)
    print("\nResultado final:", lista)
