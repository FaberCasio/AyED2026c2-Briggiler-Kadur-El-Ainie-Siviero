import random

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

    print("¿Radixsort correcto?:", radix_sort(prueba) == esperado)
