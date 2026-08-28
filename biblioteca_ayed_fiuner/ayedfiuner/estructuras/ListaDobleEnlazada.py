# Lista Doble Enlazada utilizando nodos y referencias

class Nodo:
    def __init__(self, dato):
        self.dato = dato 
        self.siguiente = None
        self.anterior = None

    # getter y setters para los atributos del nodo

class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None 
        self.tamanio = 0

   # getters y setters para los atributos de la LDE

    def agregar_al_inicio(self, dato):
        nuevo_nodo = Nodo (dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        self.tamanio += 1

    def agregar_al_final(self, dato):
        nuevo_nodo = Nodo (dato)
        if self.cabeza is None:
                self.cabeza = nuevo_nodo
                self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo


    def insertar(self, dato, posicion):
        if posicion < 0 or posicion > self.tamanio:
            raise Exception("Posición inválida")
        if posicion == 0:
          self.agregar_al_inicio(dato)
        elif posicion == self.tamanio:
            self.agregar_al_final(dato)
        else:
            nuevo_nodo = Nodo(dato)
            actual = self.cabeza
            for _ in range(posicion):
                actual = actual.siguiente
                nuevo_nodo.anterior = actual.anterior
                nuevo_nodo.siguiente = actual
                actual.anterior.siguiente = nuevo_nodo
                actual.anterior = nuevo_nodo
            self.tamanio += 1
            
    def extraer(self, posicion=None):
        pass

    def copiar(self):
        pass

    def invertir(self):
        pass

    def concatenar(self, otra_lista):
        pass        

    def esta_vacia(self):
        pass

    def __len__(self):
        pass

    def __iter__(self):
        pass

    def __add__(self, otra_lista):
        pass
    
    def __str__(self):
        pass

if __name__ == "__main__":
    #prueba de metodos
    lista = ListaDobleEnlazada()

    lista.agregar_al_inicio(1)
    lista.agregar_al_inicio(2)
    lista.agregar_al_inicio(3)
    lista.agregar_al_final(4)
    lista.agregar_al_final(5)
    lista.agregar_al_final(6)
    
    print(lista)