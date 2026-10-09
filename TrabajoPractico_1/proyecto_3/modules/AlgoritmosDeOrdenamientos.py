import random
import time
import  sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from ayedfiuner.algoritmos.Burbuja import ordenamiento_burbuja
from ayedfiuner.algoritmos.Quicksort import quicksort
from ayedfiuner.algoritmos.Radixsort import radix_sort


if __name__ == "__main__":
    import matplotlib.pyplot as plt

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