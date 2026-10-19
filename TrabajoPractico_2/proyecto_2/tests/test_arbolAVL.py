import math
import random
import unittest

from ayedfiuner.estructuras.ArbolAVL import ArbolAVL


class TestArbolAVL(unittest.TestCase):
    """Suite de pruebas unitarias exhaustivas para la estructura de datos Árbol AVL."""

    def setUp(self):
        """Se ejecuta automáticamente antes de cada método de prueba."""
        self.arbol = ArbolAVL()
        random.seed(42)

    def _validar_invariantes_avl(self, arbol):
        """Método 'oráculo' que verifica las reglas matemáticas del árbol AVL."""
        recorrido = list(arbol.inorden())
        claves = [item[0] for item in recorrido]

        # 1. Validación de Propiedad de Orden BST
        self.assertEqual(
            claves,
            sorted(claves),
            "Fallo de orden BST: Las claves en inorden no están estrictamente ordenadas.",
        )

        # 2. Validación de Claves Únicas
        self.assertEqual(
            len(set(claves)),
            len(claves),
            "Fallo de integridad: Existen claves duplicadas en la estructura.",
        )

        # 3. Validación de Consistencia de Tamaño
        self.assertEqual(
            len(claves),
            arbol.tamanio,
            f"Fallo de contabilidad: El tamaño reportado ({arbol.tamanio}) "
            f"no coincide con la cantidad real de nodos ({len(claves)}).",
        )

        # 4. Validación de la Cota de Altura Máxima
        if arbol.tamanio > 0:
            altura_maxima = max(2, math.floor(1.44 * math.log2(arbol.tamanio + 1) - 0.33))
            self.assertLessEqual(
                arbol.altura,
                altura_maxima,
                f"Fallo de altura: La altura actual ({arbol.altura}) excede el límite ({altura_maxima}) para N={arbol.tamanio}.",
            )

    # -------------------------------------------------------------------------
    # 1. Casos Borde y Estado Inicial
    # -------------------------------------------------------------------------
    def test_arbol_vacio_inicial(self):
        self.assertEqual(self.arbol.tamanio, 0, "Un árbol nuevo debe tener tamaño 0.")
        self.assertEqual(
            list(self.arbol.inorden()),
            [],
            "El inorden de un árbol vacío debe ser una lista vacía.",
        )
        with self.assertRaises((KeyError, ValueError)):
            _ = self.arbol[99]

    # -------------------------------------------------------------------------
    # 2. Pruebas Explícitas de las 4 Rotaciones AVL
    # -------------------------------------------------------------------------
    def test_rotacion_simple_derecha_LL(self):
        for k in [30, 20, 10]:
            self.arbol[k] = str(k)
        self.assertEqual(self.arbol.raiz.clave, 20, "Rotación LL fallida.")
        self._validar_invariantes_avl(self.arbol)

    def test_rotacion_simple_izquierda_RR(self):
        for k in [10, 20, 30]:
            self.arbol[k] = str(k)
        self.assertEqual(self.arbol.raiz.clave, 20, "Rotación RR fallida.")
        self._validar_invariantes_avl(self.arbol)

    def test_rotacion_doble_izquierda_derecha_LR(self):
        for k in [30, 10, 20]:
            self.arbol[k] = str(k)
        self.assertEqual(self.arbol.raiz.clave, 20, "Rotación LR fallida.")
        self._validar_invariantes_avl(self.arbol)

    def test_rotacion_doble_derecha_izquierda_RL(self):
        for k in [10, 30, 20]:
            self.arbol[k] = str(k)
        self.assertEqual(self.arbol.raiz.clave, 20, "Rotación RL fallida.")
        self._validar_invariantes_avl(self.arbol)

    # -------------------------------------------------------------------------
    # 3. Operaciones de Consulta y Modificación (Diccionario)
    # -------------------------------------------------------------------------
    def test_busqueda_y_sobrescritura(self):
        self.arbol[10] = "valor_inicial"
        self.assertEqual(self.arbol[10], "valor_inicial")
        self.arbol[10] = "valor_actualizado"
        self.assertEqual(self.arbol[10], "valor_actualizado")
        self.assertEqual(self.arbol.tamanio, 1)

    # -------------------------------------------------------------------------
    # 4. Casos Borde en Eliminaciones
    # -------------------------------------------------------------------------
    def test_eliminar_unica_raiz(self):
        self.arbol[10] = "raiz"
        self.arbol.eliminar(10)
        self.assertEqual(self.arbol.tamanio, 0)
        self.assertEqual(list(self.arbol.inorden()), [])

    def test_eliminar_nodo_con_dos_hijos(self):
        for k in [10, 5, 15]:
            self.arbol[k] = k
        self.arbol.eliminar(10)
        self._validar_invariantes_avl(self.arbol)

    # -------------------------------------------------------------------------
    # 5. Prueba de Estrés, Rebalanceo en Cascada y Poda
    # -------------------------------------------------------------------------
    def test_estres_insercion_eliminacion_y_poda(self):
        N = 500
        lista = random.sample(range(0, 10000), N)

        # Fase 1: Inserción masiva
        for i, clave in enumerate(lista):
            self.arbol[clave] = i
        self._validar_invariantes_avl(self.arbol)

        # Fase 2: Recorrido acotado por rango (Poda)
        min_rango, max_rango = 100, 500
        recorrido_poda = list(self.arbol.inorden_con_poda(min_rango, max_rango))
        for clave_poda, valor_poda in recorrido_poda:
            self.assertTrue(
                min_rango <= clave_poda <= max_rango,
                f"El nodo {clave_poda} está fuera del rango [{min_rango}, {max_rango}].",
            )

        # Fase 3: Eliminación masiva
        for clave in lista[:450]:
            self.arbol.eliminar(clave)
        self._validar_invariantes_avl(self.arbol)


if __name__ == "__main__":
    unittest.main()