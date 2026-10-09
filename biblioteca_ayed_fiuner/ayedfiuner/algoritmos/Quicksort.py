import random

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2]
    izq = [x for x in lista if x < pivote]
    medio = [x for x in lista if x == pivote]
    der = [x for x in lista if x > pivote]
    return quicksort(izq) + medio + quicksort(der)

if __name__ == "__main__":
    # lista mayor a 500 elementos de 5 digitos
    prueba = [random.randint(10000, 99999) for _ in range(600)]
    esperado = sorted(prueba)

    print("¿Quicksort correcto?:", quicksort(prueba) == esperado)