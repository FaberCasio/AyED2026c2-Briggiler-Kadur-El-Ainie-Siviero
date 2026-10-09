import random
import time


def ordenamiento_burbuja(lista):
    lista = lista.copy()  # crea una copia de la lista para no modificar la original
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
    # lista mayor a 500 elementos de 5 digitos
    prueba = [random.randint(10000, 99999) for _ in range(600)]
    esperado = sorted(prueba)

    print("¿Burbuja correcto?:", ordenamiento_burbuja(prueba) == esperado)

# medicion para tamaños de N (1-1000)
    tamanios = list(range(1, 1001, 20))
    t_burbuja = []
    
    for n in tamanios:
        base = [random.randint(10000, 99999) for _ in range(n)]

        # Burbuja
        t0 = time.perf_counter()
        ordenamiento_burbuja(base)
        t_burbuja.append(time.perf_counter() - t0)

