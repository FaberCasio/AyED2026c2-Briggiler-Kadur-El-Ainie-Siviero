import matplotlib.pyplot as plt
import time

#importamos la clasde LDE desde la carpeta estructuras
from ayedfiuner.estructuras.ListaDobleEnlazada import ListaDobleEnlazada

#N elementos para evaluar.
muestra_N = [100, 500, 1000, 2000, 4000, 6000, 8000, 10000]

#Recipientes para almacenar los datos tiempo
tiempo_len=[]
tiempo_copiar=[]
tiempo_invertir=[]

#Recorremos por N tamaño
for n in muestra_N:
    lista=ListaDobleEnlazada() #lista para meter los N elementos
    for i in range(n):
        lista.agregar_al_final(i)

    #len
    inicio_tiempo = time.perf_counter()
    _=len(lista) #Las inicializamos asi porque no nos interesa guardar nada, solo invocar el metodo
    fin_tiempo=time.perf_counter()
    tiempo_ejecucion_len=fin_tiempo-inicio_tiempo
    tiempo_len.append(tiempo_ejecucion_len)

    #copiar
    inicio_tiempo=time.perf_counter()
    _=lista.copiar() #Las inicializamos asi porque no nos interesa guardar nada, solo invocar el metodo
    fin_tiempo=time.perf_counter()
    tiempo_ejecucion_copiar=fin_tiempo-inicio_tiempo
    tiempo_copiar.append(tiempo_ejecucion_copiar)

    #invertir
    inicio_tiempo=time.perf_counter()
    _=lista.invertir() #Las inicializamos asi porque no nos interesa guardar nada, solo invocar el metodo
    fin_tiempo=time.perf_counter()
    tiempo_ejecucion_invertir=fin_tiempo-inicio_tiempo
    tiempo_invertir.append(tiempo_ejecucion_invertir)

    #Graficamos
plt.figure(figsize=(10,6))

plt.plot(muestra_N, tiempo_len, label='__len__()', marker='o')
plt.plot(muestra_N, tiempo_invertir, label='copiar()', marker='s')
plt.plot(muestra_N, tiempo_copiar, label='invertir()', marker='^')

plt.title('muestra de N elementos vs tiempo de ejecucion metodos LDE')
plt.xlabel('Cantidad de elementos (N)')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.grid(True)
plt.legend()
plt.tight_layout()

#mostramos
plt.show()