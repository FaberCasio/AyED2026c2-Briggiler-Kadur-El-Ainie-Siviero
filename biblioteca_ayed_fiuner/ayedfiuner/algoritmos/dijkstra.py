from ayedfiuner.estructuras import ColaDePrioridad, Grafo, Vertice

def dijkstra(unGrafo, inicio):
    """
    Precondición:
        - 'unGrafo' es un Grafo cuyas aristas tienen ponderación >= 0.
        - 'inicio' es un Vertice perteneciente a 'unGrafo'.
        - Todos los vértices tienen distancia = infinito y predecesor = None.
    Postcondición:
        - Cada vértice alcanzable desde 'inicio' queda con su distancia mínima
          (suma de ponderaciones del camino más barato) y su predecesor en ese camino.
        - 'inicio' queda con distancia 0 y sin predecesor.
        - Los vértices inalcanzables conservan distancia infinito.
    """
    cp = ColaDePrioridad()     # Cola de prioridad de mínimos
    inicio.asignarDistancia(0)     # La distancia del origen a sí mismo es 0
    # Carga todos los vértices en la cola, con su distancia como prioridad
    cp.construirMonticulo([(v.obtenerDistancia(), v) for v in unGrafo])
    while not cp.estaVacia():
        verticeActual = cp.eliminarMin()     # Extrae el vértice con menor distancia; su distancia ya es definitiva
        for verticeSiguiente in verticeActual.obtenerConexiones():
            # Costo de llegar al vecino pasando por verticeActual
            nuevaDistancia = verticeActual.obtenerDistancia() \
                    + verticeActual.obtenerPonderacion(verticeSiguiente)
            if nuevaDistancia < verticeSiguiente.obtenerDistancia():     # Relajación: encontró un camino más corto
                verticeSiguiente.asignarDistancia(nuevaDistancia)
                verticeSiguiente.asignarPredecesor(verticeActual)
                cp.decrementar_clave(verticeSiguiente, nuevaDistancia)     # Actualiza su prioridad en la cola


def dijkstra_mod(unGrafo, inicio):
    """
    Variante de Dijkstra que busca el camino de mayor "cuello de botella":
    el valor de un camino es la menor ponderación de sus aristas, y se
    maximiza ese valor (por ejemplo, ponderación = capacidad).
    Precondición:
        - 'unGrafo' es un Grafo cuyas aristas tienen ponderación >= 0.
        - 'inicio' es un Vertice perteneciente a 'unGrafo'.
        - Todos los vértices excepto 'inicio' tienen distancia = 0 y predecesor = None.
        - La cola de prioridad funciona como montículo de máximos y su
          decrementar_clave se comporta como aumento de clave.
    Postcondición:
        - Cada vértice alcanzable queda con la máxima capacidad posible desde 'inicio'
          (la arista más débil del mejor camino) y su predecesor en ese camino.
        - 'inicio' queda con distancia infinito.
        - Los vértices inalcanzables conservan distancia 0.
    """
    cp = ColaDePrioridad()     # Cola de prioridad de máximos
    inicio.asignarDistancia(float('inf'))     # El origen tiene capacidad ilimitada hacia sí mismo
    cp.construirMonticulo([(v.obtenerDistancia(), v) for v in unGrafo])
    while not cp.estaVacia():
        verticeActual = cp.eliminarMax()     # Extrae el vértice con mayor capacidad; ya es definitiva
        for verticeSiguiente in verticeActual.obtenerConexiones():
            # La capacidad del camino está limitada por su arista más débil
            nuevaDistancia = min(verticeActual.obtenerDistancia(),
                                 verticeActual.obtenerPonderacion(verticeSiguiente))
            if nuevaDistancia > verticeSiguiente.obtenerDistancia():     # Relajación: encontró un camino con más capacidad
                verticeSiguiente.asignarDistancia(nuevaDistancia)
                verticeSiguiente.asignarPredecesor(verticeActual)
                cp.decrementar_clave(verticeSiguiente, nuevaDistancia)     # Debería ser un aumento de clave