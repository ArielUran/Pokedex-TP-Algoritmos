from src.tads.nodo import Nodo
from src.excepciones import ItemNoEncontradoError


class ListaEnlazada:
    """
    TAD lista enlazada simple, con un solo puntero (siguiente) por nodo.

    No usa list de Python por debajo: la única referencia que guarda
    la lista es self._cabeza (el primer Nodo); todo lo demás se llega
    recorriendo nodo.siguiente.
    """

    def __init__(self):
        self._cabeza = None
        self._tamanio = 0

    def esta_vacia(self):
        return self._cabeza is None

    def tamanio(self):
        return self._tamanio

    def insertar_al_inicio(self, dato):
        """O(1): el nuevo nodo pasa a ser la cabeza."""
        nuevo = Nodo(dato, siguiente=self._cabeza)
        self._cabeza = nuevo
        self._tamanio += 1

    def insertar_al_final(self, dato):
        """O(n): hay que recorrer hasta el último nodo para engancharlo."""
        nuevo = Nodo(dato)

        if self._cabeza is None:
            self._cabeza = nuevo
        else:
            actual = self._cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo

        self._tamanio += 1

    def insertar_ordenado(self, dato, clave):
        """
        Inserta manteniendo el orden ascendente según `clave`.

        `clave` es una función que, dado un elemento de la lista,
        devuelve el valor por el que se ordena. Por ejemplo, para
        ordenar Pokémon por número: clave=lambda p: p.numero
        """
        nuevo = Nodo(dato)
        valor_nuevo = clave(dato)

        # Caso 1: lista vacía o el nuevo dato va antes que la cabeza actual.
        if self._cabeza is None or valor_nuevo <= clave(self._cabeza.dato):
            nuevo.siguiente = self._cabeza
            self._cabeza = nuevo
            self._tamanio += 1
            return

        # Caso 2: buscar el nodo anterior al lugar donde va el nuevo dato.
        actual = self._cabeza
        while actual.siguiente is not None and clave(actual.siguiente.dato) < valor_nuevo:
            actual = actual.siguiente

        nuevo.siguiente = actual.siguiente
        actual.siguiente = nuevo
        self._tamanio += 1

    def eliminar(self, dato):
        """
        Elimina la primera aparición de `dato` (comparado con ==).
        Lanza ItemNoEncontradoError si no está en la lista.
        """
        anterior = None
        actual = self._cabeza

        while actual is not None:
            if actual.dato == dato:
                if anterior is None:
                    self._cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                self._tamanio -= 1
                return
            anterior = actual
            actual = actual.siguiente

        raise ItemNoEncontradoError(f"No se encontró el ítem a eliminar: {dato!r}")

    def buscar(self, dato):
        """
        Busca `dato` (comparado con ==) y lo devuelve si lo encuentra.
        Lanza ItemNoEncontradoError si no está.
        """
        for elemento in self:
            if elemento == dato:
                return elemento

        raise ItemNoEncontradoError(f"No se encontró el ítem: {dato!r}")

    def primero(self):
        """
        Devuelve el dato de la cabeza sin sacarlo (para que Pila.ver_tope
        y Cola.ver_frente puedan mirar sin modificar la lista).
        """
        if self._cabeza is None:
            raise ItemNoEncontradoError("La lista está vacía, no hay primer elemento.")
        return self._cabeza.dato

    def quitar_del_inicio(self):
        """
        Saca y devuelve el dato de la cabeza. O(1): es exactamente lo
        que necesitan Pila.desapilar y Cola.desencolar para no tener
        que recorrer toda la lista solo para sacar la punta.
        """
        if self._cabeza is None:
            raise ItemNoEncontradoError("La lista está vacía, no hay nada que quitar.")
        dato = self._cabeza.dato
        self._cabeza = self._cabeza.siguiente
        self._tamanio -= 1
        return dato

    def __iter__(self):
        """
        Iterador propio, con yield. Permite hacer:
            for elemento in mi_lista:
                ...
        recorriendo nodo por nodo sin exponer los Nodo hacia afuera.
        """
        actual = self._cabeza
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente

    def __len__(self):
        # Extra: permite usar len(mi_lista); no es obligatorio pero es
        # una sola línea y hace más cómodo usar la lista en el resto del código.
        return self._tamanio
