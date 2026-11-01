from pathlib import Path
from ayedfiuner.estructuras.Grafo import Grafo
from ayedfiuner.algoritmos.dijkstra import dijkstra, dijkstra_mod     # ajustá al nombre real de tu archivo

ORIGEN = "CiudadBs.As."


def cargar_rutas(ruta_archivo):
    """Devuelve una lista de tuplas (origen, destino, capacidad, precio), una por línea."""
    rutas = []
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea:
                a, b, cap, precio = [x.strip() for x in linea.split(",")]
                rutas.append((a, b, float(cap), float(precio)))
    return rutas


def pesos_maximos(rutas):
    """Ítem 1: devuelve el grafo con la capacidad máxima en cada vértice."""
    g = Grafo()
    for a, b, cap, _ in rutas:
        g.agregarArista(a, b, cap)          # ponderación = capacidad
    for v in g:
        v.asignarDistancia(0)               # dijkstra_mod necesita arrancar en 0
    dijkstra_mod(g, g.obtenerVertice(ORIGEN))
    return g


def precios_minimos(rutas, w):
    """Ítem 2: devuelve el grafo con el precio mínimo usando solo rutas con capacidad >= w."""
    g = Grafo()
    for a, b, cap, precio in rutas:
        if cap >= w:
            g.agregarArista(a, b, precio)   # ponderación = precio
    dijkstra(g, g.obtenerVertice(ORIGEN))   # los vértices ya arrancan en infinito
    return g


def reconstruir_camino(vertice):
    camino = []
    while vertice is not None:
        camino.append(vertice.obtenerId())
        vertice = vertice.obtenerPredecesor()
    return camino[::-1]


if __name__ == "__main__":
    rutas = cargar_rutas(Path(__file__).resolve().parent / "data" / "rutas.txt")

    g_cap = pesos_maximos(rutas)
    print(f"Peso máximo desde {ORIGEN}:")
    for v in sorted(g_cap, key=lambda x: x.obtenerId()):
        if v.obtenerId() != ORIGEN:
            print(f"  {v.obtenerId()}: {v.obtenerDistancia():g}")

    destino = input("\nCiudad de destino: ").strip()
    v_dest = g_cap.obtenerVertice(destino)
    if v_dest is None or destino == ORIGEN or v_dest.obtenerDistancia() == 0:
        raise SystemExit("Destino inválido o inalcanzable.")

    w = v_dest.obtenerDistancia()
    g_precio = precios_minimos(rutas, w)
    d = g_precio.obtenerVertice(destino)
    print(f"\nW hacia {destino}: {w:g}")
    print(f"Precio mínimo: {d.obtenerDistancia():g}")
    print("Camino:", " -> ".join(reconstruir_camino(d)))