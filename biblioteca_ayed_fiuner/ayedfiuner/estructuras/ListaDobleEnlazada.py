# Lista Doble Enlazada utilizando nodos y referencias

class Nodo:
    def __init__(self, dato):
        self.__dato = dato 
        self.__siguiente = None
        self.__anterior = None

    # getter y setters para los atributos del nodo
    @property
    def dato(self):
        return self.__dato

    @dato.setter
    def dato(self, nuevo_dato):
        self.__dato = nuevo_dato

    @property
    def siguiente(self):
        return self.__siguiente

    @siguiente.setter
    def siguiente(self, nuevo_siguiente):
        self.__siguiente = nuevo_siguiente

    @property
    def anterior(self):
        return self.__anterior

    @anterior.setter
    def anterior(self, nuevo_anterior):
        self.__anterior = nuevo_anterior


class ListaDobleEnlazada:
    def __init__(self):
        self.__cabeza = None
        self.__cola = None 
        self.__tamanio = 0

   # getters para los atributos de la LDE

    @property
    def cabeza(self):
        return self.__cabeza

    @property
    def cola(self):
        return self.__cola

    @property
    def tamanio(self):
        return self.__tamanio


    def agregar_al_inicio(self, dato):
        nuevo_nodo = Nodo (dato)
        if self.__cabeza is None:
            self.__cabeza = nuevo_nodo
            self.__cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.__cabeza
            self.__cabeza.anterior = nuevo_nodo
            self.__cabeza = nuevo_nodo
        self.__tamanio += 1

    def agregar_al_final(self, dato):
        nuevo_nodo = Nodo (dato)
        if self.__cabeza is None:
            self.__cabeza = nuevo_nodo
            self.__cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.__cola
            self.__cola.siguiente = nuevo_nodo
            self.__cola = nuevo_nodo
        self.__tamanio += 1

    def insertar(self, dato, posicion):
        if posicion < 0 or posicion > self.__tamanio:
            raise IndexError("Posicion invalida")
        
        if posicion == 0:
          self.agregar_al_inicio(dato)
        elif posicion == self.__tamanio:
            self.agregar_al_final(dato)
        else:
            nuevo_nodo = Nodo(dato)
            actual = self.__cabeza
            for _ in range(posicion):
                actual = actual.siguiente

            nuevo_nodo.anterior = actual.anterior
            nuevo_nodo.siguiente = actual
            actual.anterior.siguiente = nuevo_nodo
            actual.anterior = nuevo_nodo
            self.__tamanio += 1
            
    def extraer(self, posicion=None):
        '''Elimina y devuelve el item en la posicion especificada. O(1) para extraccion de los extremos'''

        #Validacion
        if self.esta_vacia():
            raise IndexError('La lista esta vacia.')
        if posicion is None:
            posicion = self.__tamanio -1
        if not isinstance (posicion,int):
            raise TypeError('La posicion del elemento debe ser un numero entero.')
        if posicion < 0 or posicion >= self.__tamanio:
            raise IndexError('Posicion del elemento fuera de rango.')

        #Extraemos primer elemento O(1)
        if posicion == 0:
            sacado = self.__cabeza.dato
            self.__cabeza = self.__cabeza.siguiente
            if self.__cabeza is not None:
                self.__cabeza.anterior = None
            else:
                self.__cola = None 

        #Extraemos el ultimo elemento O(1)
        elif posicion == self.__tamanio-1:
            sacado = self.__cola.dato
            self.__cola = self.__cola.anterior
            if self.__cola is not None:
                self.__cola.siguiente = None
            else:
                self.__cabeza = None

        #Extraemos los elementos que se encuentran entre 1º y ultimo elemento O(N)
        else:
            if posicion < self.__tamanio // 2:
                posicion_actual = self.__cabeza
                for _ in range (posicion):
                    posicion_actual = posicion_actual.siguiente
            else:
                posicion_actual=self.__cola
                for _ in range(self.__tamanio -1, posicion, -1):
                    posicion_actual = posicion_actual.anterior

            sacado = posicion_actual.dato
            posicion_actual.anterior.siguiente = posicion_actual.siguiente
            posicion_actual.siguiente.anterior = posicion_actual.anterior

        self.__tamanio -= 1
        return sacado

    def copiar(self):
        copia = ListaDobleEnlazada()
        actual = self.__cabeza
        while actual is not None:   #recorre la lista hasta encontrar None, O(N)
            copia.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return copia

    def invertir(self):
        actual = self.__cabeza
        self.__cola = self.__cabeza     #la cabeza actual se convierte en la cola
        temp = None
        while actual is not None:
            #intercambia las referencias de anterior y siguiente de cada nodo
            temp = actual.anterior
            actual.anterior = actual.siguiente
            actual.siguiente = temp
            actual = actual.anterior    #accede al siguiente nodo 
        if temp is not None:    #si la lista no estaba vacia le asigna la cabeza
            self.__cabeza = temp.anterior

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
        '''Arroja valor True si la lista no tiene elementos.'''
        return self.__tamanio == 0
        
    def __len__(self):
        '''Devuelve el tamaño actualizado con cada actualizacion de la lista.'''
        return self.__tamanio
        
    def __iter__(self):
        '''Utilizamos un generador para recorrer la lista y es eficiente en memoria'''
        posicion_actual = self.__cabeza
        while posicion_actual is not None:
            yield posicion_actual.dato #Procesa un dato a la vez segun se lo necesite
            posicion_actual = posicion_actual.siguiente

    def __add__(self, otra_lista):
        '''Suma dos listas.'''
        copia = self.copiar() #crea una copia exacta de la lista de la izquierda (self) en memoria
        return copia.concatenar(otra_lista) 
    
    def __str__(self):
        '''Devuelve una representacion textual de los datos de la lista, complejidad O(N)'''

        # Si la lista esta vacia mostramos lo que corresponda.
        if self.esta_vacia():
            return '[]' 

        #inicializamos la cadena de texto de una lista, la recorremos desde el inicio convirtiendo los datos de los nodos en tipo str, al finalizar cerramos la lista.
        dato_str = '['
        posicion_actual = self.__cabeza
        while posicion_actual is not None:
            dato_str += str(posicion_actual.dato)
            if posicion_actual.siguiente is not None:
                dato_str += ' <-> ' #indica nodos por ser una lista doble enlazada
            posicion_actual = posicion_actual.siguiente
        dato_str += ']'

        #Mostramos la lista.
        return dato_str

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