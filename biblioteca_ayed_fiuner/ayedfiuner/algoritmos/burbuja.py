def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n):
        hubo_intercambio = False
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
                hubo_intercambio = True
        if not hubo_intercambio:
            break
    return lista


if __name__ == "__main__":
    # Prueba local del algoritmo de ordenamiento burbuja
    ejemplo_lis = [64, 34, 25, 12, 22, 11, 90]
    lis_ordenada = ordenamiento_burbuja(ejemplo_lis)
    print("Lista ordenada:", lis_ordenada)