class MonticuloBinario:     # Crea la clase monticulo binario
    def __init__(self):     # Inicializa la lista del montículo y el tamaño actual
        """ Precondición: Ninguna
            Postcondición: Crea un monticulo binario vacio inicializado en la posicion 0 y con un tamaño actual de 0
        """
        self.listaMonticulo = [0]
        self.tamanoActual = 0


    def infiltArriba(self,i):     # Infiltra el elemento en la posición i hacia arriba para mantener la propiedad del montículo
        """ Precondición: 'i' es un índice válido dentro de la lista del montículo
            Postcondición: Infiltra el elemento hacia arriba restableciendo la propiedad del monticulo binario
        """
        while i // 2 > 0:
            if self.listaMonticulo[i] < self.listaMonticulo[i // 2]:     # verifica si el hijo es menor que el padre
                tmp = self.listaMonticulo[i // 2]     # guarda temporalmente el valor del padre
                self.listaMonticulo[i // 2] = self.listaMonticulo[i]     # intercambia el valor del hijo con el padre
                self.listaMonticulo[i] = tmp     # asigna el valor del padre al hijo
            i = i // 2     # sube un nivel mas arriba apuntando al indice del padre


    def insertar(self,k):     # Inserta un nuevo elemento k al final del montículo y lo Infiltra hacia arriba
        """
        Precondición: 'k' debe ser un elemento de un tipo comparable
        Postcondición: Agrega 'k' al montículo reordenándolo para mantener la propiedad de montículo y aumenta el tamaño en 1
        """
        self.listaMonticulo.append(k)
        self.tamanoActual = self.tamanoActual + 1     # aumenta 1 al tamaño actual del montículo
        self.infiltArriba(self.tamanoActual)


    def infiltAbajo(self,i):        # Infiltra el elemento en la posición i hacia abajo para mantener la propiedad del montículo 
        """
        Precondición: 'i' es un índice válido dentro del montículo
        Postcondición: Infiltra el elemento hacia abajo restableciendo la propiedad de orden del montículo.
        """  
        while (i * 2) <= self.tamanoActual:     # mientras el hijo izquierdo exista
            hm = self.hijoMin(i)     # obtiene el índice del hijo menor
            if self.listaMonticulo[i] > self.listaMonticulo[hm]:     # verifica si el padre es mayor que el hijo menor
                tmp = self.listaMonticulo[i]     # guarda temporalmente el valor del padre
                self.listaMonticulo[i] = self.listaMonticulo[hm]     # intercambia el valor del padre con el hijo menor
                self.listaMonticulo[hm] = tmp     # asigna el valor del padre al hijo menor
            i = hm     # baja un nivel apuntando al indice del hijo menor


    def hijoMin(self,i):     
        """
        Precondición: El nodo en la posición 'i' tiene al menos un hijo izquierdo
        Postcondición: Devuelve el índice del hijo con el menor valor
        """
        if i * 2 + 1 > self.tamanoActual:     # si el hijo derecho no existe, devuelve el índice del hijo izquierdo
            return i * 2
        else:
            if self.listaMonticulo[i*2] < self.listaMonticulo[i*2+1]:     # compara los valores de los hijos izquierdo y derecho y devuelve el índice del hijo menor
                return i * 2
            else:
                return i * 2 + 1


    def eliminarMin(self):
        """
        Precondición: El montículo no debe estar vacío
        Postcondición: Elimina y retorna la clave de menor valor (raiz), manteniendo la estructura y disminuyendo el tamaño en 1
        """
        valorSacado = self.listaMonticulo[1]     # guarda el valor del elemento mínimo (raíz del montículo)
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]     # asigna el último elemento del montículo a la raíz
        self.tamanoActual = self.tamanoActual - 1     # disminuye el tamaño actual del montículo
        self.listaMonticulo.pop()     # elimina el último elemento del montículo (ya que se ha movido a la raíz)
        self.infiltAbajo(1)     # Infiltra el nuevo elemento en la raíz hacia abajo para mantener la propiedad del montículo
        return valorSacado     # devuelve el valor del elemento mínimo eliminado

    