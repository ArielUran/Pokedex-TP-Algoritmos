from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import ColaVaciaError


class Cola:
    """
    TAD cola (FIFO — el primero que entra es el primero que sale),
    implementada ARRIBA de ListaEnlazada (no sobre list de Python).

    Se encola por el final y se desencola por el frente (la cabeza).
    Encolar es O(n) porque ListaEnlazada no guarda puntero a la cola;
    desencolar es O(1).
    """

    def __init__(self):
        self._lista = ListaEnlazada()

    def encolar(self, dato):
        self._lista.insertar_al_final(dato)

    def desencolar(self):
        if self.esta_vacia():
            raise ColaVaciaError("No se puede desencolar: la cola está vacía.")
        return self._lista.quitar_del_inicio()

    def ver_frente(self):
        if self.esta_vacia():
            raise ColaVaciaError("La cola está vacía, no hay frente.")
        return self._lista.primero()

    def esta_vacia(self):
        return self._lista.esta_vacia()

    def __len__(self):
        return self._lista.tamanio()
