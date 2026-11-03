from pathlib import Path
from ayedfiuner.estructuras.Grafo import Grafo
from ayedfiuner.algoritmos.dijkstra import dijkstra, dijkstra_mod

'''
Notación:
  V = cantidad de vértices (ciudades)
  E = cantidad de aristas (rutas)
Supuestos:
  - Grafo guarda los vértices en un diccionario:
    agregarArista y obtenerVertice son O(1).
  - dijkstra usa un montículo binario de mínimos y dijkstra_mod uno de máximos:
    insertar, actualizar clave y eliminar_min / eliminar_max son O(log V).
  - Por lo tanto, ambos algoritmos son O((V + E) log V).
'''

ORIGEN = "CiudadBs.As."

def cargar_rutas(ruta_archivo):
    """Devuelve una lista de tuplas (origen, destino, capacidad, precio), una por línea.
 
    Pre:  ruta_archivo existe y es legible.
          Cada línea no vacía tiene el formato "origen, destino, capacidad, precio",
          con capacidad y precio convertibles a float.
    Post: devuelve una lista con exactamente una tupla por cada línea no vacía,
          en el mismo orden del archivo. Las líneas vacías se ignoran.
 
    Complejidad: tiempo O(n), espacio O(n).
    """
    rutas = []
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea:
                a, b, cap, precio = [x.strip() for x in linea.split(",")]
                rutas.append((a, b, float(cap), float(precio)))
    return rutas


def pesos_maximos(rutas):
    
    """Ítem 1: devuelve el grafo con la capacidad máxima en cada vértice.
 
    Pre:  rutas es una lista de tuplas (a, b, cap, precio) con cap >= 0. (cap=capacidad)
          ORIGEN aparece en alguna ruta (si no, obtenerVertice devuelve None y falla).
    
    Post: g contiene un vértice por cada ciudad de rutas.
          Para cada vértice v alcanzable desde ORIGEN, v.obtenerDistancia() es la
          capacidad máxima de un camino ORIGEN -> v (maximiza el mínimo de capacidades del camino) y 
          v.obtenerPredecesor() deja reconstruir ese camino.
          Los vértices inalcanzables quedan con distancia 0.
 
    Complejidad: tiempo O(n + V + (V + E) log V) = O((V + E) log V) con E <= n;
                 espacio O(V + E).
    """
    g = Grafo()
    for a, b, cap, _ in rutas:                  # O(n)
        g.agregarArista(a, b, cap)              # ponderación = capacidad
    for v in g:                                 # O(V)
        v.asignarDistancia(0)                   # dijkstra_mod necesita arrancar en 0
    dijkstra_mod(g, g.obtenerVertice(ORIGEN))   # O((V + E) log V)
    return g


def precios_minimos(rutas, w):
    """Ítem 2: devuelve el grafo con el precio mínimo usando solo rutas con capacidad >= w.
 
    Pre:  rutas es una lista de tuplas (a, b, cap, precio) con precio >= 0 (Dijkstra no admite pesos negativos).
          w >= 0 (w = weight o peso), y ORIGEN es extremo de alguna ruta con cap >= w
          (si no, obtenerVertice devuelve None y falla).
    
    Post: g contiene solo las aristas con cap >= w, ponderadas por precio.
          Para cada vértice v alcanzable desde ORIGEN con esas aristas,
          v.obtenerDistancia() es el precio mínimo de un camino ORIGEN -> v y
          v.obtenerPredecesor() deja reconstruir ese camino.
          Los vértices inalcanzables quedan con distancia infinita.
 
    Complejidad: tiempo O(n + (V + E') log V), con E' <= E la cantidad de aristas
                 con cap >= w; espacio O(V + E').
    """
    g = Grafo()
    for a, b, cap, precio in rutas:
        if cap >= w:
            g.agregarArista(a, b, precio)   # ponderación = precio
    dijkstra(g, g.obtenerVertice(ORIGEN))   # los vértices ya arrancan en infinito
    return g


def reconstruir_camino(vertice):
    """Devuelve la lista de ids del camino desde ORIGEN hasta vertice.
 
    Pre:  vertice no es None y ya se ejecutó Dijkstra sobre su grafo
          (la cadena de predecesores es finita y sin ciclos).

    Post: devuelve [id_origen, ..., id_vertice] siguiendo los predecesores en orden
          inverso. Si vertice no es alcanzable, devuelve solo [id_vertice].
 
    Complejidad: tiempo O(V) con V siendo la cantidad de vértices del camino.
    """
    camino = []
    while vertice is not None:
        camino.append(vertice.obtenerId())
        vertice = vertice.obtenerPredecesor()
    return camino[::-1]


if __name__ == "__main__":
    # Complejidad total del programa: O((V + E) log V)
    rutas = cargar_rutas(Path(__file__).resolve().parent / "data" / "rutas.txt") # O(E)

    g_cap = pesos_maximos(rutas)            #O((V + E) log V)
    print(f"Peso máximo desde {ORIGEN}:")
    for v in sorted(g_cap, key=lambda x: x.obtenerId()):    # O(V log V)
        if v.obtenerId() != ORIGEN:
            print(f"  {v.obtenerId()}: {v.obtenerDistancia():g}")

    destino = input("\nCiudad de destino: ").strip()
    v_dest = g_cap.obtenerVertice(destino)
    if v_dest is None or destino == ORIGEN or v_dest.obtenerDistancia() == 0:
        raise SystemExit("Destino inválido o inalcanzable.")

    w = v_dest.obtenerDistancia()           # w = capacidad máxima del camino ORIGEN -> destino
    g_precio = precios_minimos(rutas, w)    #O((V + E) log V)
    d = g_precio.obtenerVertice(destino)
    print(f"\nW hacia {destino}: {w:g}")
    print(f"Precio mínimo: {d.obtenerDistancia():g}")
    print("Camino:", " -> ".join(reconstruir_camino(d)))    #O(V)

   