"""
Objeto de dominio: Pokemon.

Por qué una clase y no seguir con dict:
- Agrupa los campos con nombre (pokemon.nombre en vez de p["nombre"]).
- Deja lugar para agregar comportamiento propio más adelante
  (por ejemplo, un método que sepa compararse para ordenar).
- numero, nombre y generación son, en la práctica, INMUTABLES
  (no deberían cambiar una vez creado el Pokémon).
- tipo lo dejamos como lista porque un Pokémon puede tener 1 o 2 tipos.
"""


class Pokemon:
    def __init__(self, numero, nombre, tipo, generacion):
        self.numero = numero
        self.nombre = nombre
        self.tipo = list(tipo)
        self.generacion = generacion

    @classmethod
    def desde_dict(cls, d):
        """Convierte uno de los dicts viejos de pokedex.py en un Pokemon."""
        return cls(
            numero=d["numero"],
            nombre=d["nombre"],
            tipo=d["tipo"],
            generacion=d["generacion"],
        )

    def __str__(self):
        tipos = ", ".join(self.tipo)
        return f'#{self.numero:>3}  {self.nombre:<12}  {tipos:<20}  {self.generacion}'

    def __repr__(self):
        return f"Pokemon({self.numero}, {self.nombre!r})"
