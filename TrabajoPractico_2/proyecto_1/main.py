# -*- coding: utf-8 -*-
"""
Sala de emergencias
"""

import time
import datetime
import random
import modules.paciente as pac
from ayedfiuner.estructuras.ColaDePrioridad import ColaDePrioridad

n = 20  # cantidad de ciclos de simulación

# Usar una cola de prioridad (heap binario) en lugar de lista simple
# La cola priorizará pacientes por nivel de riesgo (menor número = mayor prioridad)
# y como criterio de desempate usará el orden de llegada (FIFO)
cola_de_espera = ColaDePrioridad()

# Ciclo que gestiona la simulación
for i in range(n):
    """
    Bloque: Ciclo de simulación de atención de pacientes en sala de emergencias.
    -----------------------------------------------------
    Precondiciones:
      - 'n' debe ser un número entero positivo (n > 0).
      - El módulo 'modules.paciente' debe proveer la clase 'Paciente' con métodos 'get_riesgo()'.
      
    Postcondiciones:
      - Se genera e inserta un nuevo paciente en la estructura de prioridad.
      - Con una probabilidad del 50%, se extrae y atiende al paciente de mayor prioridad (menor valor de riesgo).
      - Se imprime en consola el estado actual de la simulación, pacientes atendidos y los pacientes pendientes.

    Complejidad Temporal (Notación {O}):
      - Inserción del paciente: {O}(/log N), donde N es la cantidad de elementos en la cola.
      - Eliminación del mínimo (si se cumple la condición): {O}(/log N).
      - Obtención de tamaño ('len'): {O}(1).
      - Recorrido para mostrar pacientes restantes: {O}(N) o {O}(N /log N) .
      - Complejidad total por cada ciclo: {O}(N /log N).
    """
    # Fecha y hora de entrada de un paciente
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
    print('-*-'*15)
    print('\n', fecha_y_hora, '\n')

    # Se crea un paciente un paciente por segundo
    # La criticidad del paciente es aleatoria
    paciente = pac.Paciente()
    cola_de_espera.insertar(paciente, paciente.get_riesgo())

    # Atención de paciente en este ciclo: en el 50% de los casos
    if random.random() < 0.5 and not cola_de_espera.esta_vacia():
        # Se atiende el paciente de mayor prioridad (menor número de riesgo)
        paciente_atendido = cola_de_espera.eliminar_min()
        print('*'*40)
        print('Se atiende el paciente:', paciente_atendido)
        print('*'*40)
    else:
        # se continúa atendiendo paciente de ciclo anterior
        pass
    
    print()

    # Se muestran los pacientes restantes en la cola de espera
    print('Pacientes que faltan atenderse:', len(cola_de_espera))
    for paciente in cola_de_espera:
        print('\t', paciente)
    
    print()
    print('-*-'*15)
    
    time.sleep(1)