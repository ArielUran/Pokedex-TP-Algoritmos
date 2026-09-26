"""
Equipo de combate: la colección PRINCIPAL del dominio Pokédex.

Vive sobre ListaEnlazada (no sobre list de Python), tiene un máximo
de 6 Pokémon, y soporta alta (agregar) y baja (quitar). La
modificación de un Pokémon del equipo se hace vía el catálogo mismo
(sección 2 y 3 del menú), no acá.
"""

from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import ColeccionLlenaError, ItemNoEncontradoError

MAX_EQUIPO = 6


class Equipo:
    def __init__(self):
        self._lista = ListaEnlazada()

    def agregar(self, pokemon):
        """
        Alta: agrega un Pokémon al final del equipo.
        Lanza ColeccionLlenaError si ya hay 6.
        """
        if self._lista.tamanio() >= MAX_EQUIPO:
            raise ColeccionLlenaError(
                f"El equipo ya tiene el máximo de {MAX_EQUIPO} Pokémon."
            )
        self._lista.insertar_al_final(pokemon)

    def quitar(self, numero):
        """
        Baja: saca del equipo al Pokémon con ese número.
        Devuelve el Pokémon sacado (para poder deshacer después).
        Lanza ItemNoEncontradoError si no está en el equipo.
        """
        objetivo = None
        for pokemon in self._lista:
            if pokemon.numero == numero:
                objetivo = pokemon
                break

        if objetivo is None:
            raise ItemNoEncontradoError(
                f"No hay ningún Pokémon con número {numero} en el equipo."
            )

        self._lista.eliminar(objetivo)
        return objetivo

    def listar(self):
        """Devuelve los Pokémon del equipo, en orden."""
        return list(self._lista)

    def tamanio(self):
        return self._lista.tamanio()

    def esta_vacio(self):
        return self._lista.esta_vacia()
