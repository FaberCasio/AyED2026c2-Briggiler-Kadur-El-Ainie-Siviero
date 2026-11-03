from ayedfiuner.estructuras.Vertice import Vertice
class Grafo:
    """Grafo dirigido y ponderado, representado con lista de adyacencia.
 
    Invariante: listaVertices asocia cada clave con su Vertice,
                y numVertices == len(listaVertices).
 
    Espacio: O(V + E).
    """
    def __init__(self):
         """Crea un grafo vacío.
 
        Pre:  ninguna.
        Post: listaVertices == {} y numVertices == 0.
 
        Complejidad: O(1).
        """
         self.listaVertices = {}
         self.numVertices = 0

    def agregarVertice(self,clave):
          """Agrega un vértice con la clave dada y lo devuelve.
 
        Pre:  clave es hashable.
        Post: listaVertices[clave] es un Vertice nuevo, numVertices aumenta en 1
              y se devuelve ese vértice.
              Si la clave ya existía, el vértice anterior (con sus vecinos) se
              reemplaza, y numVertices queda desfasado (cuenta de más).
 
        Complejidad: O(1).
        """
          self.numVertices = self.numVertices + 1
          nuevoVertice = Vertice(clave)
          self.listaVertices[clave] = nuevoVertice
          return nuevoVertice

    def obtenerVertice(self,n):
        """Devuelve el vértice con clave n, o None si no existe.
 
        Pre:  n es hashable.
        Post: devuelve listaVertices[n] si n está en el grafo; si no, None.
              No modifica el grafo.
 
        Complejidad: O(1).
        """
        if n in self.listaVertices:
            return self.listaVertices[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.listaVertices

    def agregarArista(self,de,a,costo=0):
        """Agrega la arista dirigida de -> a con el costo dado.
 
        Pre:  de y a son hashables. costo es numérico.
        Post: los vértices de y a existen en el grafo (se crean si faltaban).
              El vértice 'de' tiene a 'a' como vecino con ese costo.
              Si la arista de -> a ya existía, el comportamiento depende de
              Vertice.agregarVecino (con un diccionario, se pisa el costo anterior).
 
        Complejidad: O(1).
        """
        if de not in self.listaVertices:
            nv = self.agregarVertice(de)
        if a not in self.listaVertices:
            nv = self.agregarVertice(a)
        self.listaVertices[de].agregarVecino(self.listaVertices[a], costo)

    def obtenerVertices(self):
        """Devuelve las claves de todos los vértices.
 
        Pre:  ninguna.
        Post: devuelve una vista de las claves (no una copia); refleja los
              cambios posteriores del grafo. No modifica el grafo.
 
        Complejidad: O(1) para obtener la vista, O(V) para recorrerla.
        """
        return self.listaVertices.keys()

    def __iter__(self):
        """Permite recorrer los vértices con `for v in grafo`.
 
        Pre:  el grafo no se modifica (no se agregan vértices) durante el recorrido.
        Post: itera sobre los objetos Vertice, no sobre las claves.
 
        Complejidad: O(1) para crear el iterador, O(V) para recorrerlo completo.
        """
        return iter(self.listaVertices.values())

if __name__ == "__main__":
    g = Grafo()
    for i in range(6):
        g.agregarVertice(i)
    g.agregarArista(0, 1, 5)
    g.agregarArista(0, 5, 2)
    g.agregarArista(1, 2, 4)
    g.agregarArista(2, 3, 9)
    g.agregarArista(3, 4, 7)
    g.agregarArista(3, 5, 3)
    g.agregarArista(4, 0, 1)
    g.agregarArista(5, 4, 8)
    # for v in g:
    #     for w in v.obtenerConexiones():
    #         print(f"{v.obtenerClave()} conecta con {w.obtenerClave()} con peso {v.obtenerPonderacion(w)}")

