'''Realizar una gráfica de N (cantidad de elementos) vs tiempo de ejecución para los siguientes métodos: len, copiar e invertir
(verificar que los hayan implementado de la forma más eficiente posible). Explicar los resultados y deducir
los órdenes de complejidad a partir de las gráficas'''

import  sys, os 
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))  # Agrega el directorio padre al path para importar módulo
import timeit
import random
import matplotlib.pyplot as plt
from ayedfiuner.estructuras.ListaDobleEnlazada import ListaDobleEnlazada

"""
Módulo de Benchmarking para la estructura Lista Doble Enlazada (LDE).

Este script realiza un análisis empírico de la complejidad temporal de los métodos 
principales de una LDE, comparándolos con las funciones nativas de Python.

PRE:
    - El módulo 'modules.LDE' debe estar disponible y contener la clase 'ListaDobleEnlazada'.
    - La clase 'ListaDobleEnlazada' debe implementar: __len__, agregar_al_final, copiar e invertir.
    - Las librerías 'matplotlib', 'timeit' y 'random' deben estar instaladas en el entorno.

POST:
    - Se genera una comparativa de tiempos de ejecución para tamaños de N entre 1 y 1000.
    - Se visualizan las curvas de complejidad (O(1), O(n) y O(n log n)) mediante Matplotlib.
    - Se exporta el archivo 'grafica_complejidad.png' con los resultados del análisis.
"""

# Configuramos los tamaños de N (de 1 a 1000 como pide la consigna)
paso = 50
valores_n = range(1, 1001, paso)

tiempos_len = []
tiempos_copiar = []
tiempos_invertir = []


for n in valores_n:
    # Creamos una lista con n números aleatorios
    datos = [random.randint(10000, 99999) for _ in range(n)]
    lde = ListaDobleEnlazada()
    for d in datos:
        lde.agregar_al_final(d)
    
    # Medimos cada método (ejecutamos varias veces para promedio)
    t_len = timeit.timeit(lambda: len(lde), number=100)
    t_copiar = timeit.timeit(lambda: lde.copiar(), number=100)
    t_invertir = timeit.timeit(lambda: lde.invertir(), number=100)
    
    
    tiempos_len.append(t_len)
    tiempos_copiar.append(t_copiar)
    tiempos_invertir.append(t_invertir)

# 3. Crear la gráfica
plt.figure(figsize=(10, 6))

plt.plot(valores_n, tiempos_len, label='len() - O(1)', marker='o')
plt.plot(valores_n, tiempos_copiar, label='copiar() - O(n)', marker='s')
plt.plot(valores_n, tiempos_invertir, label='invertir() - O(n)', marker='^')


plt.title('Complejidad Temporal: N vs Tiempo de Ejecución')
plt.xlabel('Cantidad de elementos (N)')
plt.ylabel('Tiempo total (segundos)')
plt.legend()
plt.grid(True)

# Guardar la imagen para el informe PDF
plt.savefig('grafica_complejidad.png')
plt.show()