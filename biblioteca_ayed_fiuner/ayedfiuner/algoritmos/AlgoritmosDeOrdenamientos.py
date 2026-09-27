import random
import time
import matplotlib.pyplot as plt

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


def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2]
    izq = [x for x in lista if x < pivote]
    medio = [x for x in lista if x == pivote]
    der = [x for x in lista if x > pivote]
    return quicksort(izq) + medio + quicksort(der)


def radix_sort(lista):
    if not lista:
        return lista
    lista = lista.copy()  # crea una copia de la lista para no modificar la original
    max_val = max(lista)
    exp = 1
    while max_val // exp > 0:
        buckets = [[] for _ in range(10)]
        for num in lista:
            digito = (num // exp) % 10
            buckets[digito].append(num)
        lista = [num for bucket in buckets for num in bucket]
        exp *= 10
    return lista


if __name__ == "__main__":
    # lista mayor a 500 elementos de 5 digitos
    prueba = [random.randint(10000, 99999) for _ in range(600)]
    esperado = sorted(prueba)

    print("¿Burbuja correcto?:", ordenamiento_burbuja(prueba) == esperado)
    print("¿Quicksort correcto?:", quicksort(prueba) == esperado)
    print("¿Radix Sort correcto?:", radix_sort(prueba) == esperado)

    # medicion para tamaños de N (1-1000)
    tamanios = list(range(1, 1001, 20))
    t_burbuja, t_quick, t_radix, t_sorted = [], [], [], []

    for n in tamanios:
        base = [random.randint(10000, 99999) for _ in range(n)]

        # Burbuja
        t0 = time.perf_counter()
        ordenamiento_burbuja(base)
        t_burbuja.append(time.perf_counter() - t0)

        # Quicksort
        t0 = time.perf_counter()
        quicksort(base)
        t_quick.append(time.perf_counter() - t0)

        # Radix
        t0 = time.perf_counter()
        radix_sort(base)
        t_radix.append(time.perf_counter() - t0)

        # Built-in sorted
        t0 = time.perf_counter()
        sorted(base)
        t_sorted.append(time.perf_counter() - t0)

    # grafica comparativa de tiempos
    plt.figure(figsize=(10, 6))
    plt.plot(tamanios, t_burbuja, label="Burbuja O(n²)", color="red")
    plt.plot(tamanios, t_quick, label="Quicksort O(n log n)", color="blue")
    plt.plot(tamanios, t_radix, label="Radix Sort O(d·n)", color="green")
    plt.plot(tamanios, t_sorted, label="Python sorted() (Timsort)", color="orange")
    
    plt.xlabel("Tamaño de la lista (N)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("Comparación de Tiempos de Ejecución de Algoritmos de Ordenamiento")
    plt.legend()
    plt.grid(True)
    plt.show()