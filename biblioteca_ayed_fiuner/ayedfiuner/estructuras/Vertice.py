class Vertice:
    """Vértice de un grafo dirigido y ponderado.
 
    Atributos:
        id          : clave que identifica al vértice.
        conectadoA  : diccionario {Vertice vecino: ponderación} (aristas salientes).
        distancia   : valor que usa Dijkstra; arranca en infinito.
        predecesor  : vértice anterior en el camino hallado; arranca en None.
 
    Invariante: cada vecino aparece una sola vez en conectadoA
                (las claves del diccionario son únicas).
 
    Espacio: O(g) por vértice (g = cant de vecinos conectados); O(V + E) en el grafo completo.
    """
    def __init__(self, clave):
        """Crea un vértice sin vecinos.
 
        Pre:  clave es el identificador del vértice.
        Post: id == clave, conectadoA == {}, distancia == infinito,
              predecesor == None.
 
        Complejidad: O(1).
        """
        self.id = clave
        self.conectadoA = {}
        self.distancia = float('inf')
        self.predecesor = None

    def agregarVecino(self, vecino, ponderacion=0):
        """Agrega la arista saliente self -> vecino con la ponderación dada.
 
        Pre:  vecino es un Vertice. ponderacion es numérica.
        Post: conectadoA[vecino] == ponderacion.
              Si ya existía una arista hacia ese vecino, se pisa la ponderación
              anterior (no se guardan aristas paralelas).
 
        Complejidad: O(1).
        """
        self.conectadoA[vecino] = ponderacion

    def __str__(self):
        """Devuelve una cadena con el id y los ids de sus vecinos.
 
        Pre:  ninguna.
        Post: devuelve "<id> conectadoA: [<ids de vecinos>]". No modifica el vértice.
 
        Complejidad: O(g).
        """
        return str(self.id) + ' conectadoA: ' + str([x.id for x in self.conectadoA])

    def obtenerConexiones(self):
        """Devuelve los vecinos de este vértice.
 
        Pre:  ninguna.
        Post: devuelve una vista de las claves de conectadoA (objetos Vertice),
              no una copia. No modifica el vértice.
 
        Complejidad: O(1) para obtener la vista, O(g) para recorrerla.
        """
        return self.conectadoA.keys()

    def obtenerId(self):
        """Devuelve el id del vértice.
 
        Pre:  ninguna.
        Post: devuelve self.id.
 
        Complejidad: O(1).
        """
        return self.id

    def obtenerPonderacion(self, vecino):
        """Devuelve la ponderación de la arista self -> vecino.
 
        Pre:  vecino es vecino de este vértice (está en conectadoA).
        Post: devuelve conectadoA[vecino]. Si vecino no es vecino, lanza KeyError.
 
        Complejidad: O(1).
        """
        return self.conectadoA[vecino]

    def asignarDistancia(self, distancia):
        """Asigna la distancia del vértice.
 
        Pre:  distancia es numérica (o infinito).
        Post: self.distancia == distancia.
 
        Complejidad: O(1).
        """
        self.distancia = distancia

    def obtenerDistancia(self):
        """Devuelve la distancia del vértice.
 
        Pre:  ninguna.
        Post: devuelve self.distancia (infinito si nunca se asignó).
 
        Complejidad: O(1).
        """
        return self.distancia

    def asignarPredecesor(self, predecesor):
        """Asigna el predecesor del vértice en el camino hallado.
 
        Pre:  predecesor es un Vertice o None.
        Post: self.predecesor == predecesor.
 
        Complejidad: O(1).
        """
        self.predecesor = predecesor

    def obtenerPredecesor(self):
        """Devuelve el predecesor del vértice.
 
        Pre:  ninguna.
        Post: devuelve self.predecesor (None si no tiene).
 
        Complejidad: O(1).
        """
        return self.predecesor