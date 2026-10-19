class NodoArbolAVL:
    def __init__(self, clave, valor, padre=None):
        self._clave = clave
        self._valor = valor
        self._padre = padre
        self._hijo_izquierdo = None
        self._hijo_derecho = None
        self._altura = 1

    @property
    def clave(self):
        return self._clave

    @property
    def valor(self):
        return self._valor

    @property
    def padre(self):
        return self._padre

    @property
    def hijo_izquierdo(self):
        return self._hijo_izquierdo

    @property
    def hijo_derecho(self):
        return self._hijo_derecho

    @property
    def altura(self):
        return self._altura

    @clave.setter
    def clave(self, valor):
        self._clave = valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor

    @padre.setter
    def padre(self, nodo):
        self._padre = nodo

    @hijo_izquierdo.setter
    def hijo_izquierdo(self, nodo):
        self._hijo_izquierdo = nodo

    @hijo_derecho.setter
    def hijo_derecho(self, nodo):
        self._hijo_derecho = nodo

    def tiene_padre(self):
        return self._padre is not None

    def es_raiz(self):
        return self._padre is None

    def tiene_hijo_izquierdo(self):
        return self._hijo_izquierdo is not None

    def tiene_hijo_derecho(self):
        return self._hijo_derecho is not None

    def tiene_hijos(self):
        return self._hijo_izquierdo is not None or self._hijo_derecho is not None

    def tiene_ambos_hijos(self):
        return self._hijo_izquierdo is not None and self._hijo_derecho is not None

    def es_hoja(self):
        return self._hijo_izquierdo is None and self._hijo_derecho is None

    def es_hijo_izquierdo(self):
        return self.tiene_padre() and self._padre.hijo_izquierdo is self

    def es_hijo_derecho(self):
        return self.tiene_padre() and self._padre.hijo_derecho is self

    @property
    def altura_rama_izquierda(self):
        return self._hijo_izquierdo.altura if self._hijo_izquierdo else 0

    @property
    def altura_rama_derecha(self):
        return self._hijo_derecho.altura if self._hijo_derecho else 0

    def actualizar_altura(self):
        self._altura = 1 + max(self.altura_rama_izquierda, self.altura_rama_derecha)

    @property
    def factor_de_equilibrio(self):
        return self.altura_rama_izquierda - self.altura_rama_derecha


class ArbolAVL:
    def __init__(self):
        self._raiz = None
        self._tamanio = 0

    @property
    def tamanio(self):
        return self._tamanio

    @property
    def altura(self):
        return self._raiz.altura if self._raiz else 0

    @property
    def raiz(self):
        return self._raiz

    def esta_vacio(self):
        return self._tamanio == 0

    def agregar(self, clave, valor):
        if self._raiz is None:
            self._raiz = NodoArbolAVL(clave, valor)
            self._tamanio += 1
        else:
            self.__agregar(self._raiz, clave, valor)

    def __agregar(self, nodo, clave, valor):
        if clave < nodo.clave:
            if nodo.hijo_izquierdo is None:
                nodo.hijo_izquierdo = NodoArbolAVL(clave, valor, padre=nodo)
                self._tamanio += 1
                self.__rebalancear(nodo.hijo_izquierdo)
            else:
                self.__agregar(nodo.hijo_izquierdo, clave, valor)
        elif clave > nodo.clave:
            if nodo.hijo_derecho is None:
                nodo.hijo_derecho = NodoArbolAVL(clave, valor, padre=nodo)
                self._tamanio += 1
                self.__rebalancear(nodo.hijo_derecho)
            else:
                self.__agregar(nodo.hijo_derecho, clave, valor)
        else:
            nodo.valor = valor
    
    def __rebalancear(self, nodo):
        actual = nodo

        while actual is not None:
            actual.actualizar_altura()
            fe = actual.factor_de_equilibrio

            if fe > 1:
                if actual.hijo_izquierdo.factor_de_equilibrio < 0:
                    self.__rotacion_izquierda(actual.hijo_izquierdo)

                self.__rotacion_derecha(actual)

            elif fe < -1:
                if actual.hijo_derecho.factor_de_equilibrio > 0:
                    self.__rotacion_derecha(actual.hijo_derecho)

                self.__rotacion_izquierda(actual)

            # Subir desde el nodo actual hasta su padre,
            # incluso después de una rotación.
            actual = actual.padre

    def __rebalancear_nodo(self, nodo):
        nodo.actualizar_altura()
        fe = nodo.factor_de_equilibrio

        if fe > 1:
            if nodo.hijo_izquierdo.factor_de_equilibrio < 0:
                self.__rotacion_izquierda(nodo.hijo_izquierdo)

            self.__rotacion_derecha(nodo)
            return nodo.padre

        elif fe < -1:
            if nodo.hijo_derecho.factor_de_equilibrio > 0:
                self.__rotacion_derecha(nodo.hijo_derecho)

            self.__rotacion_izquierda(nodo)
            return nodo.padre

        return nodo

    def __rotacion_izquierda(self, nodo):
        hijo_der = nodo.hijo_derecho
        padre_original = nodo.padre

        nodo.hijo_derecho = hijo_der.hijo_izquierdo

        if hijo_der.hijo_izquierdo is not None:
            hijo_der.hijo_izquierdo.padre = nodo

        hijo_der.padre = padre_original

        if padre_original is None:
            self._raiz = hijo_der
        elif padre_original.hijo_izquierdo is nodo:
            padre_original.hijo_izquierdo = hijo_der
        else:
            padre_original.hijo_derecho = hijo_der

        hijo_der.hijo_izquierdo = nodo
        nodo.padre = hijo_der

        nodo.actualizar_altura()
        hijo_der.actualizar_altura()

    def __rotacion_derecha(self, nodo):
        hijo_izq = nodo.hijo_izquierdo
        padre_original = nodo.padre

        nodo.hijo_izquierdo = hijo_izq.hijo_derecho

        if hijo_izq.hijo_derecho is not None:
            hijo_izq.hijo_derecho.padre = nodo

        hijo_izq.padre = padre_original

        if padre_original is None:
            self._raiz = hijo_izq
        elif padre_original.hijo_izquierdo is nodo:
            padre_original.hijo_izquierdo = hijo_izq
        else:
            padre_original.hijo_derecho = hijo_izq

        hijo_izq.hijo_derecho = nodo
        nodo.padre = hijo_izq

        nodo.actualizar_altura()
        hijo_izq.actualizar_altura()

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

    def __inorden(self, nodo, resultado):
        if nodo is not None:
            self.__inorden(nodo.hijo_izquierdo, resultado)
            resultado.append((nodo.clave, nodo.valor))
            self.__inorden(nodo.hijo_derecho, resultado)

    def obtener(self, clave):
        '''
        Busca una clave en el arbol y retorna su valor asociado.

        PRE: clave es del mismo tipo que las claves almacenadas.
        POST: Retorna el valor asociado a la clave si existe, o None si no.

                El arbol no se modifica.

        '''
        return self.__obtener(self._raiz, clave)

    def __obtener(self, nodo, clave):
        if nodo is None:
            return None
        if clave == nodo.clave:
            return nodo.valor
        if clave < nodo.clave:
            return self.__obtener(nodo.hijo_izquierdo, clave)
        return self.__obtener(nodo.hijo_derecho, clave)

    def __setitem__(self, clave, valor):
        self.agregar(clave, valor)

    def __getitem__(self, clave):
        valor = self.obtener(clave)
        if valor is None:
            raise KeyError(f"La clave {clave} no existe en el árbol")
        return valor

    def __contains__(self, clave):
        '''
        Verifica si una clave existe en el arbol.

        PRE: clave es del mismo tipo que las claves almacenadas.
        POST: Retorna True si la clave existe, False en caso contrario.

                El arbol no se modifica.

        '''
        return self.obtener(clave) is not None

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
        nueva_raiz, eliminado = self.__eliminar(self._raiz, clave)

        if eliminado:
            self._tamanio -= 1

        # Recuperar la raiz real despues de posibles rotaciones.
        if nueva_raiz is None:
            self._raiz = None
        else:
            while nueva_raiz.padre is not None:
                nueva_raiz = nueva_raiz.padre

            self._raiz = nueva_raiz
            self._raiz.padre = None

    def __eliminar(self, nodo, clave):
        if nodo is None:
            return None, False

        if clave < nodo.clave:
            nodo.hijo_izquierdo, eliminado = self.__eliminar(
                nodo.hijo_izquierdo, clave
            )

            if nodo.hijo_izquierdo is not None:
                nodo.hijo_izquierdo.padre = nodo

        elif clave > nodo.clave:
            nodo.hijo_derecho, eliminado = self.__eliminar(
                nodo.hijo_derecho, clave
            )

            if nodo.hijo_derecho is not None:
                nodo.hijo_derecho.padre = nodo

        else:
            eliminado = True

            if nodo.es_hoja():
                return None, True

            if nodo.hijo_izquierdo is None:
                hijo = nodo.hijo_derecho
                hijo.padre = nodo.padre
                return hijo, True

            if nodo.hijo_derecho is None:
                hijo = nodo.hijo_izquierdo
                hijo.padre = nodo.padre
                return hijo, True

            sucesor = self.__obtener_minimo(nodo.hijo_derecho)
            nodo.clave = sucesor.clave
            nodo.valor = sucesor.valor
            nodo.hijo_derecho, _ = self.__eliminar(
                nodo.hijo_derecho, sucesor.clave
            )

            if nodo.hijo_derecho is not None:
                nodo.hijo_derecho.padre = nodo

        nodo = self.__rebalancear_nodo(nodo)
        return nodo, eliminado

    def __rebalancear(self, nodo):
        actual = nodo

        while actual is not None:
            actual.actualizar_altura()
            fe = actual.factor_de_equilibrio

            if fe > 1:
                if actual.hijo_izquierdo.factor_de_equilibrio < 0:
                    self.__rotacion_izquierda(actual.hijo_izquierdo)

                self.__rotacion_derecha(actual)

            elif fe < -1:
                if actual.hijo_derecho.factor_de_equilibrio > 0:
                    self.__rotacion_derecha(actual.hijo_derecho)

                self.__rotacion_izquierda(actual)

            # Continuar desde el padre del nodo que se estaba evaluando.
            actual = actual.padre

    def __obtener_minimo(self, nodo):
        actual = nodo

        while actual.hijo_izquierdo is not None:
            actual = actual.hijo_izquierdo

        return actual

    def __delitem__(self, clave):
        self.eliminar(clave)

    def inorden_con_poda(self, clave_minima, clave_maxima):
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
        self.__inorden_con_poda(self._raiz, clave_minima, clave_maxima, resultado)
        return resultado

    def __inorden_con_poda(self, nodo, clave_minima, clave_maxima, resultado):
        if nodo is not None:
            if clave_minima is None or clave_minima < nodo.clave:
                self.__inorden_con_poda(nodo.hijo_izquierdo, clave_minima, clave_maxima, resultado)
            if (clave_minima is None or clave_minima <= nodo.clave) and (clave_maxima is None or nodo.clave <= clave_maxima):
                resultado.append((nodo.clave, nodo.valor))
            if clave_maxima is None or clave_maxima > nodo.clave:
                self.__inorden_con_poda(nodo.hijo_derecho, clave_minima, clave_maxima, resultado)