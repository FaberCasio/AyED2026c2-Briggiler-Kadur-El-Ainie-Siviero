from ayedfiuner.estructuras.Vertice import Vertice
from ayedfiuner.estructuras.GraficadorGrafo import graficar_grafo

class Grafo:
    def __init__(self):
        self.listaVertices = {}
        self.numVertices = 0

    def agregarVertice(self,clave):
        self.numVertices = self.numVertices + 1
        nuevoVertice = Vertice(clave)
        self.listaVertices[clave] = nuevoVertice
        return nuevoVertice

    def obtenerVertice(self,n):
        if n in self.listaVertices:
            return self.listaVertices[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.listaVertices

    def agregarArista(self,de,a,costo=0):
        if de not in self.listaVertices:
            nv = self.agregarVertice(de)
        if a not in self.listaVertices:
            nv = self.agregarVertice(a)
        self.listaVertices[de].agregarVecino(self.listaVertices[a], costo)

    def obtenerVertices(self):
        return self.listaVertices.keys()

    def __iter__(self):
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

    graficar_grafo(g)