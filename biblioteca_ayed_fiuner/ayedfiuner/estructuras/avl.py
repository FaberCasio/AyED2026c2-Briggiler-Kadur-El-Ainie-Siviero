class NodoAVL:
    def __init__(self, clave, valor):
        self._clave = clave
        self._valor = valor
        self._izquierdo = None
        self._derecho = None
        self._altura = 1

    @property
    def clave(self):
        return self._clave

    @clave.setter
    def clave(self, valor):
        self._clave = valor

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor

    @property
    def izquierdo(self):
        return self._izquierdo

    @izquierdo.setter
    def izquierdo(self, nodo):
        self._izquierdo = nodo

    @property
    def derecho(self):
        return self._derecho

    @derecho.setter
    def derecho(self, nodo):
        self._derecho = nodo

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        self._altura = valor


class ArbolAVL:
    def __init__(self):
        self._raiz = None
        self._tamanio = 0

    @property
    def raiz(self):
        return self._raiz

    @property
    def tamanio(self):
        return self._tamanio

    def __altura(self, nodo):
        if nodo is None:
            return 0
        return nodo.altura

    def __actualizar_altura(self, nodo):
        if nodo is None:
            return
        nodo.altura = 1 + max(self.__altura(nodo.izquierdo), self.__altura(nodo.derecho))

    def __factor_equilibrio(self, nodo):
        if nodo is None:
            return 0
        return self.__altura(nodo.izquierdo) - self.__altura(nodo.derecho)

    def __rotacion_simple_derecha(self, y):
        x = y.izquierdo
        t2 = x.derecho
        x.derecho = y
        y.izquierdo = t2
        self.__actualizar_altura(y)
        self.__actualizar_altura(x)
        return x

    def __rotacion_simple_izquierda(self, x):
        y = x.derecho
        t2 = y.izquierdo
        y.izquierdo = x
        x.derecho = t2
        self.__actualizar_altura(x)
        self.__actualizar_altura(y)
        return y

    def __balancear(self, nodo):
        if nodo is None:
            return None
        self.__actualizar_altura(nodo)
        fe = self.__factor_equilibrio(nodo)
        if fe > 1:
            if self.__factor_equilibrio(nodo.izquierdo) >= 0:
                return self.__rotacion_simple_derecha(nodo)
            else:
                nodo.izquierdo = self.__rotacion_simple_izquierda(nodo.izquierdo)
                return self.__rotacion_simple_derecha(nodo)
        if fe < -1:
            if self.__factor_equilibrio(nodo.derecho) <= 0:
                return self.__rotacion_simple_izquierda(nodo)
            else:
                nodo.derecho = self.__rotacion_simple_derecha(nodo.derecho)
                return self.__rotacion_simple_izquierda(nodo)
        return nodo

    def __insertar(self, nodo, clave, valor):
        if nodo is None:
            self._tamanio += 1
            return NodoAVL(clave, valor)
        if clave < nodo.clave:
            nodo.izquierdo = self.__insertar(nodo.izquierdo, clave, valor)
        elif clave > nodo.clave:
            nodo.derecho = self.__insertar(nodo.derecho, clave, valor)
        else:
            nodo.valor = valor
            return nodo
        return self.__balancear(nodo)

    def insertar(self, clave, valor):
        '''
        Inserta un par clave-valor en el arbol AVL.
        Si la clave ya existe, actualiza su valor.
        Luego de insertar, balancea el arbol automaticamente.

        PRE: clave es comparable (implementa __lt__, __gt__, __eq__).
             valor puede ser cualquier tipo de dato.
        POST: El par clave-valor queda almacenado en el arbol.
              Si la clave no existia, _tamanio aumenta en 1.
              El arbol permanece balanceado (AVL).
        '''
        self._raiz = self.__insertar(self._raiz, clave, valor)

    def __buscar(self, nodo, clave):
        if nodo is None:
            return None
        if clave == nodo.clave:
            return nodo.valor
        if clave < nodo.clave:
            return self.__buscar(nodo.izquierdo, clave)
        return self.__buscar(nodo.derecho, clave)

    def buscar(self, clave):
        '''
        Busca una clave en el arbol y retorna su valor asociado.

        PRE: clave es del mismo tipo que las claves almacenadas.
        POST: Retorna el valor asociado a la clave si existe, o None si no.
              El arbol no se modifica.
        '''
        return self.__buscar(self._raiz, clave)

    def contiene(self, clave):
        '''
        Verifica si una clave existe en el arbol.

        PRE: clave es del mismo tipo que las claves almacenadas.
        POST: Retorna True si la clave existe, False en caso contrario.
              El arbol no se modifica.
        '''
        return self.__buscar(self._raiz, clave) is not None

    def __minimo(self, nodo):
        actual = nodo
        while actual.izquierdo is not None:
            actual = actual.izquierdo
        return actual

    def __eliminar(self, nodo, clave):
        if nodo is None:
            raise ValueError(f"No se encontró la clave '{clave}' en el árbol")
        if clave < nodo.clave:
            nodo.izquierdo = self.__eliminar(nodo.izquierdo, clave)
        elif clave > nodo.clave:
            nodo.derecho = self.__eliminar(nodo.derecho, clave)
        else:
            self._tamanio -= 1
            if nodo.izquierdo is None:
                return nodo.derecho
            if nodo.derecho is None:
                return nodo.izquierdo
            sucesor = self.__minimo(nodo.derecho)
            nodo.clave = sucesor.clave
            nodo.valor = sucesor.valor
            nodo.derecho = self.__eliminar(nodo.derecho, sucesor.clave)
        return self.__balancear(nodo)

    def eliminar(self, clave):
        '''
        Elimina un par clave-valor del arbol AVL.
        Luego de eliminar, balancea el arbol automaticamente.

        PRE: clave existe en el arbol.
        POST: El par clave-valor es eliminado. _tamanio disminuye en 1.
              El arbol permanece balanceado (AVL).

        Lanza:
        - ValueError: si la clave no existe o el arbol esta vacio.
        '''
        if self._raiz is None:
            raise ValueError("El árbol está vacío")
        self._raiz = self.__eliminar(self._raiz, clave)

    def __inorden(self, nodo, resultado):
        if nodo is not None:
            self.__inorden(nodo.izquierdo, resultado)
            resultado.append((nodo.clave, nodo.valor))
            self.__inorden(nodo.derecho, resultado)

    def inorden(self):
        '''
        Recorre el arbol en orden (izquierdo-raiz-derecho).

        PRE: Ninguna.
        POST: Retorna una lista de tuplas (clave, valor) ordenadas por clave.
              El arbol no se modifica.
        '''
        resultado = []
        self.__inorden(self._raiz, resultado)
        return resultado

    def __inorden_rango(self, nodo, min_clave, max_clave, resultado):
        if nodo is None:
            return
        if min_clave is not None and nodo.clave < min_clave:
            self.__inorden_rango(nodo.derecho, min_clave, max_clave, resultado)
            return
        if max_clave is not None and nodo.clave > max_clave:
            self.__inorden_rango(nodo.izquierdo, min_clave, max_clave, resultado)
            return
        self.__inorden_rango(nodo.izquierdo, min_clave, max_clave, resultado)
        resultado.append((nodo.clave, nodo.valor))
        self.__inorden_rango(nodo.derecho, min_clave, max_clave, resultado)

    def inorden_rango(self, clave_min=None, clave_max=None):
        '''
        Recorre el arbol en orden dentro de un rango de claves.

        PRE: clave_min y clave_max son del mismo tipo que las claves almacenadas.
             Si se especifican ambos, clave_min <= clave_max.
        POST: Retorna una lista de tuplas (clave, valor) cuyas claves estan
              en el rango [clave_min, clave_max] inclusive.
              Si clave_min es None, no hay limite inferior.
              Si clave_max es None, no hay limite superior.
              El arbol no se modifica.
        '''
        resultado = []
        self.__inorden_rango(self._raiz, clave_min, clave_max, resultado)
        return resultado