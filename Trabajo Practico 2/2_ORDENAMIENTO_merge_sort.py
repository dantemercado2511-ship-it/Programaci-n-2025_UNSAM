#Merge Sort
def merge_sort(arr, depth=0):
    indent = "  " * depth
    print(f"{indent}Dividiendo: {arr}")

    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    izquierda = merge_sort(arr[:mid], depth + 1)
    derecha = merge_sort(arr[mid:], depth + 1)

    print(f"{indent}Mezclando {izquierda} y {derecha}")

    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    print(f"{indent}Resultado parcial:", resultado)
    return resultado
  
# ejemplo...
if __name__ == "__main__":
    lista = [22, 36, 6, 79, 26, 45, 75, 13]
    print("\nRESULTADO FINAL:", merge_sort(lista))
