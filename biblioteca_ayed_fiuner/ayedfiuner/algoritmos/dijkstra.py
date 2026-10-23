import heapq
from itertools import count

def aplicar_prim(grafo, clave_inicio):
    """
    Calcula el Árbol de Expansión Mínima (MST) del grafo utilizando el algoritmo de Prim.

    Optimiza de manera local la conexión de los vértices para minimizar el costo total
    del árbol, partiendo desde un nodo inicial.

    Args:
        grafo (Grafo): Instancia de la estructura de datos Grafo que contiene los vértices y aristas.
        clave_inicio (Any): Identificador único o clave del vértice desde el cual comenzará la exploración.

    Returns:
        list[tuple]: Una lista de tuplas que representan las aristas del MST final.
            Cada tupla contiene:
            - vertice_predecesor (Vertice): Objeto del vértice de origen de la arista.
            - vertice_actual (Vertice): Objeto del vértice de destino de la arista.
            - peso_arista (int/float): El peso individual de esa conexión.
    """
    visitados = set()
    distancias = {}
    predecesores = {}
    cola_prioridad = []  # Cambiar por la estructura adecuada

    # Completar

    while not cola_prioridad.esta_vacio():
        pass  # Completar

    aristas_finales = []
    for vertice_actual, vertice_predecesor in predecesores.items():
        pass  # Completar

    return aristas_finales


def aplicar_dijkstra(grafo, clave_inicio):
    """
    Calcula el Árbol de Caminos Mínimos (SPT) desde un único origen utilizando el algoritmo de Dijkstra.

    Optimiza la distancia acumulada total desde el vértice de inicio hacia todos los demás
    nodos alcanzables en el grafo.

    Args:
        grafo (Grafo): Instancia de la estructura de datos Grafo que contiene los vértices y aristas.
        clave_inicio (Any): Identificador único o clave del vértice origen del cual se calcularán las distancias.

    Returns:
        list[tuple]: Una lista de tuplas que representan las aristas del camino mínimo óptimo.
            Cada tupla contiene:
            - vertice_predecesor (Vertice): Objeto del vértice padre en el camino óptimo.
            - vertice_actual (Vertice): Objeto del vértice de destino.
            - peso_arista (int/float): El peso individual de la última arista tomada.
            - distancia_total (int/float): La distancia mínima acumulada total desde el origen hasta vertice_actual.
    """
    visitados = set()
    distancias = {}
    predecesores = {}
    cola_prioridad = []  # Cambiar por la estructura adecuada

    # Completar

    while not cola_prioridad.esta_vacio():
        pass  # Completar

    aristas_finales = []
    for vertice_actual, vertice_predecesor in predecesores.items():
        pass  # Completar

    return aristas_finales



def dijkstra(grafo, clave_inicio):
    """
    Calcula el árbol de caminos mínimos desde un origen.

    Devuelve una lista de tuplas (predecesor, vertice, peso, distancia_total)
    para cada vertice alcanzable excepto el origen, ordenada por distancia
    total. Los pesos deben ser no negativos.
    """
    inicio = grafo.obtenerVertice(clave_inicio)
    if inicio is None:
        raise ValueError(f"No existe un vertice con clave {clave_inicio!r}")

    inf = float('inf')
    distancias = {vertice: inf for vertice in grafo}
    distancias[inicio] = 0
    predecesores = {}
    visitados = set()
    orden = count()
    cola_prioridad = [(0, next(orden), inicio)]

    while cola_prioridad:
        distancia_actual, _, vertice_actual = heapq.heappop(cola_prioridad)

        if vertice_actual in visitados:
            continue
        visitados.add(vertice_actual)

        for vecino in vertice_actual.obtenerConexiones():
            if vecino in visitados:
                continue

            peso = vertice_actual.obtenerPonderacion(vecino)
            if not (peso >= 0):  # también rechaza NaN
                raise ValueError("Dijkstra solo admite pesos no negativos")

            nueva_distancia = distancia_actual + peso
            if nueva_distancia < distancias.get(vecino, inf):
                distancias[vecino] = nueva_distancia
                predecesores[vecino] = vertice_actual
                heapq.heappush(
                    cola_prioridad, (nueva_distancia, next(orden), vecino)
                )

    aristas_finales = [
        (pred, v, pred.obtenerPonderacion(v), distancias[v])
        for v, pred in predecesores.items()
    ]
    aristas_finales.sort(key=lambda t: t[3])
    return aristas_finales


def aplicar_camino_maxima_capacidad(grafo, clave_inicio):
    """
    Calcula el camino que maximiza la capacidad de carga (cuello de botella)
    desde un nodo origen hacia todos los demás.
    """
    visitados = set()
    capacidades = {}
    predecesores = {}
    cola_prioridad = []  # Cambiar por la estructura adecuada

    # Completar

    while not cola_prioridad.esta_vacio():
        pass  # Completar

    aristas_finales = []
    for vertice_actual, vertice_predecesor in predecesores.items():
        pass  # Completar

    return aristas_finales