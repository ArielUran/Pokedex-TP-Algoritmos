from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import PilaVaciaError


class Pila:
    """
    TAD pila (LIFO — el último que entra es el primero que sale),
    implementada ARRIBA de ListaEnlazada (no sobre list de Python).

    Se apila y desapila siempre por la cabeza de la lista interna,
    así las dos operaciones son O(1).
    """

    def __init__(self):
        self._lista = ListaEnlazada()

    def apilar(self, dato):
        self._lista.insertar_al_inicio(dato)

    def desapilar(self):
        if self.esta_vacia():
            raise PilaVaciaError("No se puede desapilar: la pila está vacía.")
        return self._lista.quitar_del_inicio()

    def ver_tope(self):
        if self.esta_vacia():
            raise PilaVaciaError("La pila está vacía, no hay tope.")
        return self._lista.primero()

    def esta_vacia(self):
        return self._lista.esta_vacia()

    def __len__(self):
        return self._lista.tamanio()
