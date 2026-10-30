from pathlib import Path

from ayedfiuner.estructuras.ColaDePrioridad import ColaDePrioridad, ColaDePrioridadMax  # ajustá el import a tu proyecto

ORIGEN = "CiudadBs.As."
COL_CAPACIDAD = 2     # posición de la capacidad (peso máximo) en cada línea
COL_COSTO = 3         # posición del costo en cada línea


def cargar_rutas(ruta_archivo):
    """
    Precondición: cada línea del archivo es 'origen,destino,capacidad,costo'.
    Postcondición: devuelve {ciudad: [(vecino, capacidad, costo), ...]}.
                   Las rutas se cargan en ambos sentidos.
    """
    ady = {}
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if not linea:
                continue
            partes = [p.strip() for p in linea.split(",")]
            if len(partes) != 4:
                raise ValueError(f"Línea inválida: {linea}")
            a, b = partes[0], partes[1]
            cap = float(partes[COL_CAPACIDAD])
            costo = float(partes[COL_COSTO])
            ady.setdefault(a, []).append((b, cap, costo))
            ady.setdefault(b, []).append((a, cap, costo))
    return ady


def reconstruir_camino(pred, destino):
    camino = []
    actual = destino
    while actual is not None:
        camino.append(actual)
        actual = pred.get(actual)
    return camino[::-1]


def pesos_maximos(ady, origen):
    """
    Ítem 1: máximo cuello de botella desde 'origen' hacia cada ciudad.
    Precondición: 'origen' está en 'ady' y las capacidades son >= 0.
    Postcondición: devuelve (cap, pred), donde cap[c] es el w_max hacia c
                   (0 si es inalcanzable) y pred permite reconstruir el camino.
    """
    cap = {c: 0 for c in ady}
    cap[origen] = float("inf")

    for v in ady:
        print (type(v))
        v.distancia = 0
    pred = {origen: None}

    cp = ColaDePrioridadMax()
    for c in ady:
        cp.insertar(c, cap[c])          # prioridad negada: más capacidad = sale antes

    while not cp.esta_vacia():
        u = cp.eliminar_max()
        for v, capacidad, _ in ady[u]:
            nueva = min(cap[u], capacidad)      # la ruta más débil limita el camino
            if nueva > cap[v]:
                cap[v] = nueva
                pred[v] = u
                cp.aumentar_clave(v, nueva)
    return cap, pred


def costo_minimo(ady, origen, destino, w):
    """
    Ítem 2: camino más barato de 'origen' a 'destino' usando solo rutas con capacidad >= w.
    Postcondición: devuelve (costo, pred); costo es infinito si no hay camino válido.
    """
    dist = {c: float("inf") for c in ady}
    dist[origen] = 0
    pred = {origen: None}

    cp = ColaDePrioridad()
    for c in ady:
        cp.insertar(c, dist[c])

    while not cp.esta_vacia():
        u = cp.eliminar_min()
        if u == destino:                 # su distancia ya es definitiva
            break
        for v, capacidad, costo in ady[u]:
            if capacidad < w:            # el mobiliario no pasa por esta ruta
                continue
            nueva = dist[u] + costo
            if nueva < dist[v]:
                dist[v] = nueva
                pred[v] = u
                cp.decrementar_clave(v, nueva)
    return dist[destino], pred


if __name__ == "__main__":
    ruta_archivo = Path(__file__).resolve().parent / "data" / "rutas.txt"
    ady = cargar_rutas(ruta_archivo)

    if ORIGEN not in ady:
        raise SystemExit(f"'{ORIGEN}' no figura en el archivo.")

    # Ítem 1
    cap, pred_cap = pesos_maximos(ady, ORIGEN)
    print(f"Peso máximo transportable desde {ORIGEN}:")
    for ciudad in sorted(ady):
        if ciudad != ORIGEN:
            print(f"  {ciudad}: {cap[ciudad]:g}")

    # Ítem 2
    destino = input("\nCiudad de destino: ").strip()
    if destino not in ady or destino == ORIGEN:
        raise SystemExit("Destino inválido.")

    w_max = cap[destino]
    if w_max == 0:
        raise SystemExit(f"No hay ruta de {ORIGEN} a {destino}.")

    costo, pred_costo = costo_minimo(ady, ORIGEN, destino, w_max)
    print(f"\nw_max hacia {destino}: {w_max:g}")
    print(f"Precio mínimo: {costo:g}")
    print("Camino:", " -> ".join(reconstruir_camino(pred_costo, destino)))