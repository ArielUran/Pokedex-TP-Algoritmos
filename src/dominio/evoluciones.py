"""
Relación de evoluciones y operación recursiva del dominio (E2).

Igual que con pokedex.py: el dataset de evoluciones se arma A MANO en el
código por ahora (mismos pares que después van a vivir en
data/evoluciones.csv, que recién se lee a partir de E5).

Un Pokémon puede evolucionar a MÁS de uno (ej: Eevee -> Vaporeon/Jolteon/
Flareon), por eso el mapa guarda una LISTA de destinos, no un solo valor.
"""

# Cada tupla es (numero_origen, numero_destino): "origen evoluciona a destino".
_PARES_EVOLUCION = [
    (1, 2), (2, 3),
    (4, 5), (5, 6),
    (7, 8), (8, 9),
    (10, 11), (11, 12),
    (16, 17), (17, 18),
    (19, 20),
    (172, 25), (25, 26),
    (35, 36),
    (37, 38),
    (43, 44), (44, 45),
    (58, 59),
    (63, 64), (64, 65),
    (66, 67), (67, 68),
    (74, 75), (75, 76),
    (81, 82),
    (92, 93), (93, 94),
    (129, 130),
    (133, 134), (133, 135), (133, 136),  # Eevee evoluciona a 3 formas
    (147, 148), (148, 149),
    (152, 153), (153, 154),
    (155, 156), (156, 157),
    (175, 176),
    (179, 180), (180, 181),
    (246, 247), (247, 248),
]


def construir_mapa_evoluciones(pares=_PARES_EVOLUCION):
    """
    Arma un diccionario {numero_origen: [numero_destino, ...]}.

    OJO: este dict es solo una estructura auxiliar para no recorrer
    la lista de pares una y otra vez; el catálogo en sí sigue viviendo
    en la lista de objetos Pokemon.
    """
    mapa = {}
    for origen, destino in pares:
        mapa.setdefault(origen, []).append(destino)
    return mapa


def _buscar_por_numero(catalogo, numero):
    for pokemon in catalogo:
        if pokemon.numero == numero:
            return pokemon
    return None


def imprimir_cadena_evoluciones(numero, catalogo, mapa_evoluciones=None, nivel=0):
    """
    Función RECURSIVA de verdad.

    Caso base: el Pokémon actual no tiene evoluciones registradas
               (mapa_evoluciones.get(numero) da lista vacía) -> se imprime
               y se corta la recursión, sin volver a llamarse.
    Caso recursivo: el Pokémon SÍ tiene una o más evoluciones -> se imprime
               el actual y se llama a sí misma una vez por cada evolución
               (si tiene más de una, como Eevee, se ramifica).
    """
    if mapa_evoluciones is None:
        mapa_evoluciones = construir_mapa_evoluciones()

    pokemon = _buscar_por_numero(catalogo, numero)
    nombre = pokemon.nombre if pokemon else f"(desconocido #{numero})"
    print("  " * nivel + f"{'└─>' if nivel else ''} {nombre}")

    siguientes = mapa_evoluciones.get(numero, [])

    if not siguientes:
        return  # <-- CASO BASE: no hay más evoluciones, se corta acá.

    for numero_siguiente in siguientes:  # <-- CASO RECURSIVO
        imprimir_cadena_evoluciones(
            numero_siguiente, catalogo, mapa_evoluciones, nivel + 1
        )
