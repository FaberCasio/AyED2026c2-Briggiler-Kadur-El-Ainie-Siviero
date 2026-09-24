class ColaCircular:
    def __init__(self, tamanio):
        # Validar que el tamaño sea un entero mayor a 0
        if not isinstance(tamanio, int) or tamanio <= 0:
            raise ValueError("El tamaño debe ser un entero mayor a 0.")
            
        self.__tamanio = tamanio
        self.__items = [None] * tamanio
        self.__head = -1
        self.__tail = -1

    def esta_vacia(self):
        return self.__head == -1

    def esta_llena(self):
        if self.esta_vacia():
            return False
        return (self.__tail + 1) % self.__tamanio == self.__head

    def encolar(self, item):
        if self.esta_llena():
            raise OverflowError("La cola circular está llena.")
        
        # Caso: encolar por primera vez
        if self.esta_vacia():
            self.__head = 0
            self.__tail = 0
        else:
            # Avanza tail de forma circular (reinicia si llega al final)
            self.__tail = (self.__tail + 1) % self.__tamanio
            
        self.__items[self.__tail] = item

    def desencolar(self):
        if self.esta_vacia():
            raise IndexError("La cola circular está vacía.")
            
        item_desencolado = self.__items[self.__head]
        self.__items[self.__head] = None  # Elimina el contenido

        # Caso: se desencoló el único elemento presente
        if self.__head == self.__tail:
            self.__head = -1
            self.__tail = -1
        else:
            # Avanza head de forma circular
            self.__head = (self.__head + 1) % self.__tamanio

        return item_desencolado

    def vaciar(self):
        self.__items = [None] * self.__tamanio
        self.__head = -1
        self.__tail = -1
