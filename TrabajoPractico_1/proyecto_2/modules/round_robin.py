from ayedfiuner.estructuras.ColaCircular import ColaCircular

class Proceso:  # clase que representa un proceso en el sistema operativo.

    def __init__(self, pid, arrival_time, burst_time):

        self.pid = pid
        self.arrival_time = arrival_time    # tiempo de llegada del proceso
        self.burst_time = burst_time    # tiempo total de CPU que requiere
        self.remaining_time = burst_time    # tiempo de CPU restante por ejecutar
        self.completion_time = 0    # tiempo de finalización del proceso
        self.turnaround_time = 0    # tiempo total en el sistema (completion - arrival)
        self.waiting_time = 0    # tiempo total de espera (turnaround - burst)

# simula la planificacion de procesos mediante Round Robin
def round_robin(procesos_lista, tq, capacidad_cola):   

    # verifica los parametros de entrada
    if not procesos_lista or tq <= 0 or capacidad_cola <= 0:
        raise ValueError("Parámetros de entrada no válidos.")

    ready_queue = ColaCircular(capacidad_cola)
    tiempo_actual = 0
    completados = []    # lista de procesos completados

    # ordenar por tiempo de llegada
    entrantes = sorted(procesos_lista, key=lambda p: p.arrival_time)

    # encola el primer proceso en llegar
    if entrantes:
        proximo = entrantes.pop(0)
        tiempo_actual = proximo.arrival_time
        ready_queue.encolar(proximo)

    while not ready_queue.esta_vacia() or entrantes:

        # si la CPU no tiene ningún proceso para ejecutar, salta al tiempo de llegada del siguiente proceso y lo encola
        if ready_queue.esta_vacia() and entrantes:
            proximo = entrantes.pop(0)
            tiempo_actual = max(tiempo_actual, proximo.arrival_time)
            ready_queue.encolar(proximo)

        # desencola el proceso a ejecutar en la CPU
        proceso = ready_queue.desencolar()

        # determina el tiempo de ejecución en la CPU 
        tiempo_ejecucion = min(proceso.remaining_time, tq)
        tiempo_actual += tiempo_ejecucion
        proceso.remaining_time -= tiempo_ejecucion

        # encola los procesos que llegaron durante la ejecución anterior
        nuevos = [p for p in entrantes if p.arrival_time <= tiempo_actual]
        for p in nuevos:
            ready_queue.encolar(p)
            entrantes.remove(p)

        # reencola o finaliza el tiempo de ejecución del proceso actual
        if proceso.remaining_time > 0:
            ready_queue.encolar(proceso)
        else:
            proceso.completion_time = tiempo_actual
            proceso.turnaround_time = (proceso.completion_time - proceso.arrival_time)
            proceso.waiting_time = proceso.turnaround_time - proceso.burst_time
            completados.append(proceso)

    return completados  # devuelve la lista de los procesos completados con sus tiempos finales.


if __name__ == "__main__":
    procesos_prueba = [
        Proceso("P1", 0, 5),
        Proceso("P2", 2, 3),
        Proceso("P3", 3, 1),
        Proceso("P4", 5, 2),
        Proceso("P5", 6, 5),
        Proceso("P6", 8, 4),
    ]

    tq_prueba = 2
    capacidad_prueba = 10

    resultados = round_robin(procesos_prueba, tq_prueba, capacidad_prueba)

resultados.sort(key=lambda p: p.pid)

print(
    f"{'ProcessID':>10} {'ArrivalTime':>12} {'BurstTime':>10} {'TurnaroundTime':>16} {'WaitingTime':>12}"
)
for p in resultados:
    print(
        f"{p.pid:>10} {p.arrival_time:>12} {p.burst_time:>10} {p.turnaround_time:>16} {p.waiting_time:>12}"
    )
    