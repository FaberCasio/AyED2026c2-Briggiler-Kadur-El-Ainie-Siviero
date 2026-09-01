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
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.tamanio += 1

    def insertar(self, dato, posicion):
        if posicion < 0 or posicion > self.tamanio:
            raise Exception("Posicion invalida")
        
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
        '''Elimina y devuelve el item en la posicion especificada. O(1) para extraccion de los extremos'''

        #Validacion
        if self.esta_vacia():
            raise IndexError ('La lista esta vacia.')
        if posicion is None:
            posicion=self._tamanio-1
        if not isinstance (posicion,int):
            raise TypeError ('La posicion del elemento debe ser un numero entero.')
        if posicion<0 or posicion>=self._tamanio:
            raise IndexError ('Posicion del elemento fuera de rango.')

        #Extraemos primer elemento O(1)
        if posicion ==0:
            sacado=self._cabeza.dato
            self._cabeza=self._cabeza.siguiente
            if self._cabeza is not None:
                self._cabeza.anterior=None
            else:
                self._cola=None 

        #Extraemos el ultimo elemento O(1)
        if posicion ==self.tamanio-1:
            sacado=self._cola.dato
            self._cola=self._cola.anterior
            if self._cola is not None:
                self._cola.siguiente=None
            else:
                self._cabeza=None

        #Extraemos los elementos que se encuentran entre 1º y ultimo elemento O(N)
        else:
            if posicion < self.tamanio//2:
                posicion_actual = self._cabeza
                for _ in range (posicion):
                    posicion_actual=posicion_actual.siguiente
            else:
                posicion_actual=self._cola
                for _ in range(self._tamanio -1,posicion,-1):
                    posicion_actual=posicion_actual.anterior

            sacado=posicion_actual.dato
            posicion_actual.anterior.siguiente=posicion_actual.siguiente
            posicion_actual.siguiente.anterior=posicion_actual.anterior

        self._tamanio=-1
        return sacado

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