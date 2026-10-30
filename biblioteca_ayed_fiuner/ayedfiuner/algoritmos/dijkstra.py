from ayedfiuner.estructuras import ColaDePrioridad, Grafo, Vertice

def dijkstra(unGrafo,inicio):
    cp = ColaDePrioridad()
    inicio.asignarDistancia(0)
    cp.construirMonticulo([(v.obtenerDistancia(),v) for v in unGrafo])
    while not cp.estaVacia():
        verticeActual = cp.eliminarMin()
        for verticeSiguiente in verticeActual.obtenerConexiones():
            nuevaDistancia = verticeActual.obtenerDistancia() \
                    + verticeActual.obtenerPonderacion(verticeSiguiente)
            if nuevaDistancia < verticeSiguiente.obtenerDistancia():
                verticeSiguiente.asignarDistancia( nuevaDistancia )
                verticeSiguiente.asignarPredecesor(verticeActual)
                cp.decrementar_clave(verticeSiguiente,nuevaDistancia)

def dijkstra_mod(unGrafo,inicio):
    cp = ColaDePrioridad()
    inicio.asignarDistancia(float('inf'))
    cp.construirMonticulo([(v.obtenerDistancia(),v) for v in unGrafo])
    while not cp.estaVacia():
        verticeActual = cp.eliminarMin() #cambiar a max
        for verticeSiguiente in verticeActual.obtenerConexiones():
            nuevaDistancia = min(verticeActual.obtenerDistancia(), verticeActual.obtenerPonderacion(verticeSiguiente))
            if nuevaDistancia > verticeSiguiente.obtenerDistancia():
                verticeSiguiente.asignarDistancia( nuevaDistancia )
                verticeSiguiente.asignarPredecesor(verticeActual)
                cp.decrementar_clave(verticeSiguiente,nuevaDistancia)