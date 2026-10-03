# -*- coding: utf-8 -*-
from ayedfiuner.estructuras.MonticuloBinario import MonticuloBinario

class ColaDePrioridad:     # Crea la clase ColaDePrioridad 
    def __init__(self):
        self.__monticulo = MonticuloBinario()     # Inicializa un montículo binario privado para gestionar los elementos por prioridad
        self.__contador_llegada = 0     # Inicializa un contador privado para registrar el orden de llegada

    def insertar(self, elemento, prioridad):     
        """
        Inserta cualquier tipo de elemento con una prioridad determinada.
        Mantiene el orden de llegada (FIFO) para prioridades iguales.
        """
        self.__contador_llegada += 1     # Incrementa en 1 el contador para marcar la posicion temporal de llegada
        item = (prioridad, self.__contador_llegada, elemento)     # Crea una tupla conteniendo prioridad, orden de llegada y el elemento
        self.__monticulo.insertar(item)     # Inserta la tupla en el monticulo binario

    def eliminar_min(self):
        """Devuelve el elemento con la prioridad más alta (menor valor numérico)."""
        if self.esta_vacia():     # Verifica si la cola de prioridad está vacía antes de intentar eliminar un elemento
            return None
        prioridad, orden, elemento = self.__monticulo.eliminarMin()     # Extrae la tupla de menor prioridad del monticulo
        return elemento     # Retorna solo el elemento, ignorando la prioridad y el orden de llegada

    def esta_vacia(self):
        return self.__monticulo.tamanoActual == 0     # Evalua si la cantidad de elementos en el monticulo es igual a cero

    def __len__(self):
        return self.__monticulo.tamanoActual     # Retorna la cantidad actual de elementos almacenados en el monticulo

    def __iter__(self):
        for item in self.__monticulo.listaMonticulo[1:]:     # Recorre los elementos del monticulo binario, ignorando el primer elemento (índice 0) que es un marcador
            yield item[2]     # Devuelve solo el elemento, ignorando la prioridad y el orden de llegada