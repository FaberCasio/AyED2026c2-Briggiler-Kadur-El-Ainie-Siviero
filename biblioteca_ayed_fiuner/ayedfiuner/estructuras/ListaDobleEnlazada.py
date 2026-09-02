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
            raise IndexError("Posicion invalida")
        
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
            raise IndexError('La lista esta vacia.')
        if posicion is None:
            posicion = self.tamanio -1
        if not isinstance (posicion,int):
            raise TypeError('La posicion del elemento debe ser un numero entero.')
        if posicion < 0 or posicion >= self.tamanio:
            raise IndexError('Posicion del elemento fuera de rango.')

        #Extraemos primer elemento O(1)
        if posicion == 0:
            sacado = self.cabeza.dato
            self.cabeza = self.cabeza.siguiente
            if self.cabeza is not None:
                self.cabeza.anterior = None
            else:
                self.cola = None 

        #Extraemos el ultimo elemento O(1)
        elif posicion == self.tamanio-1:
            sacado = self.cola.dato
            self.cola = self.cola.anterior
            if self.cola is not None:
                self.cola.siguiente = None
            else:
                self.cabeza = None

        #Extraemos los elementos que se encuentran entre 1º y ultimo elemento O(N)
        else:
            if posicion < self.tamanio // 2:
                posicion_actual = self.cabeza
                for _ in range (posicion):
                    posicion_actual = posicion_actual.siguiente
            else:
                posicion_actual=self.cola
                for _ in range(self.tamanio -1, posicion, -1):
                    posicion_actual = posicion_actual.anterior

            sacado = posicion_actual.dato
            posicion_actual.anterior.siguiente = posicion_actual.siguiente
            posicion_actual.siguiente.anterior = posicion_actual.anterior

        self.tamanio -= 1
        return sacado

    def copiar(self):
        copia = ListaDobleEnlazada()
        actual = self.cabeza
        while actual is not None: #recorre la lista hasta encontrar None, O(N)
            copia.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return copia

    def invertir(self):
        actual = self.cabeza
        self.cola = self.cabeza     #la cabeza actual se convierte en la cola
        temp = None
        while actual is not None:
            #intercambia las referencias de anterior y siguiente de cada nodo
            temp = actual.anterior
            actual.anterior = actual.siguiente
            actual.siguiente = temp
            actual = actual.anterior    #accede al siguiente nodo 
        if temp is not None:    #si la lista no estaba vacia le asigna la cabeza
            self.cabeza = temp.anterior

    def concatenar(self, otra_lista):
        '''Concatena una lista doblemente enlazada al final de esta. O(N)'''

        #Validamos tipo de dato, lanzamos un mensaje de error en caso de que el argumento no sea de tipo lista doble enlazada.
        if not isinstance (otra_lista, ListaDobleEnlazada):
            raise TypeError ('El argumento debe ser una lista doblemente enlazada')

        #Recorremos la otra lista y agregamos al final. O(N)
        for i in otra_lista:
            self.agregar_al_final(i)

        #Devolvemos la lista en si modificada
        return self
        

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