def insertion_sort(lista):
    """
    Orden lista usando el método Insertion Sort
    """
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        # Mover elementos mayores que 'clave' un lugar hacia la derecha
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
        # Insertar la clave en la posición correcta
        lista[j + 1] = clave
    
    return lista

ejemplo...
nums = [5, 2, 4, 6, 1, 3]
print(insertion_sort(nums))
