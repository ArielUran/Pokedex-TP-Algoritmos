"""
CLI de la Pokédex - TP integrador Algoritmos y Estructuras de Datos
Este archivo es solo el "menú" que conecta al usuario con la lógica del
catálogo. Por ahora usa la lista `catalogo` de pokedex.py directamente;
más adelante esto se va a ir reemplazando por los TADs propios
(ListaEnlazada, Pila, Cola) que pide la consigna.
"""

from src.dominio.pokedex import catalogo
from src.dominio.evoluciones import (
    construir_mapa_evoluciones,
    imprimir_cadena_evoluciones,
)


# ---------------------------------------------------------------------
# Funciones auxiliares (lógica). Están simples/incompletas a propósito:
# muchas se van a ir completando en las próximas entregas.
#
# Desde E2, `catalogo` es una lista de objetos Pokemon (antes eran
# dicts sueltos) -> se accede como pokemon.nombre, no pokemon["nombre"].
# ---------------------------------------------------------------------

def listar_catalogo():
    """1. Listar catálogo."""
    print("\n--- Catálogo de Pokémon ---")
    for pokemon in catalogo:
        print(pokemon)  # usa el __str__ de la clase Pokemon


def ver_detalle():
    """2. Ver detalle de un ítem."""
    dato = input("Buscar por número o nombre: ").strip()
    encontrado = None

    for pokemon in catalogo:
        if dato.lower() == pokemon.nombre.lower() or dato == str(pokemon.numero):
            encontrado = pokemon
            break

    if encontrado is None:
        print(f'No se encontró ningún Pokémon con "{dato}".')
        return

    print("\n--- Detalle ---")
    print(f'Número:     {encontrado.numero}')
    print(f'Nombre:     {encontrado.nombre}')
    print(f'Tipo:       {", ".join(encontrado.tipo)}')
    print(f'Generación: {encontrado.generacion}')


def buscar():
    """3. Buscar (lineal por ahora; binaria cuando el catálogo esté ordenado)."""
    termino = input("Ingresá nombre, tipo o número a buscar: ").strip().lower()
    resultados = [
        pokemon for pokemon in catalogo
        if termino in pokemon.nombre.lower()
        or any(termino == t.lower() for t in pokemon.tipo)
        or termino == str(pokemon.numero)
    ]

    if not resultados:
        print("No se encontraron coincidencias.")
        return

    print(f"\nSe encontraron {len(resultados)} resultado(s):")
    for pokemon in resultados:
        print(pokemon)


def ordenar():
    """4. Ordenar por al menos dos criterios (implementación propia, sin sorted())."""
    print("Ordenar por: 1) Número  2) Nombre")
    criterio = input("Elegí un criterio: ").strip()

    # TODO: reemplazar por un algoritmo de ordenamiento propio
    # (selección, inserción, etc.) en vez de usar sorted().
    if criterio == "1":
        print("(pendiente: ordenar por número con algoritmo propio)")
    elif criterio == "2":
        print("(pendiente: ordenar por nombre con algoritmo propio)")
    else:
        print("Opción inválida.")


def cadena_evoluciones():
    """5. Operación recursiva del dominio: cadena de evoluciones."""
    dato = input("Número del Pokémon para ver su cadena de evolución: ").strip()

    if not dato.isdigit():
        print("Eso no es un número válido.")
        return

    numero = int(dato)
    pokemon = None
    for p in catalogo:
        if p.numero == numero:
            pokemon = p
            break

    if pokemon is None:
        print(f"No se encontró ningún Pokémon con número {numero}.")
        return

    print(f"\n--- Cadena de evolución de {pokemon.nombre} ---")
    mapa = construir_mapa_evoluciones()
    imprimir_cadena_evoluciones(numero, catalogo, mapa)


def gestionar_equipo():
    """6. ABM sobre la colección principal (equipo, máx. 6)."""
    # TODO: el equipo tiene que vivir en una ListaEnlazada propia,
    # no en una list de Python.
    print("(pendiente: alta / baja / modificación del equipo)")


def historial_pila():
    """7. Push/pop de la pila (historial / deshacer)."""
    # TODO: implementar Pila sobre ListaEnlazada propia.
    print("(pendiente: apilar/desapilar acciones del historial)")


def cola_turnos():
    """8. Encolar/desencolar la cola (turnos de combate)."""
    # TODO: implementar Cola sobre ListaEnlazada propia.
    print("(pendiente: encolar/desencolar turnos)")


def guardar_cargar():
    """9. Guardar y cargar catálogo en texto simple (.txt) y en binario."""
    # TODO: esto se implementa recién en la entrega 5.
    print("(pendiente: guardar/cargar en .txt y binario con struct)")


# ---------------------------------------------------------------------
# Menú principal
# ---------------------------------------------------------------------

def mostrar_menu():
    print("\n===== POKÉDEX - MENÚ PRINCIPAL =====")
    print("1. Listar catálogo")
    print("2. Ver detalle de un ítem")
    print("3. Buscar")
    print("4. Ordenar")
    print("5. Cadena de evoluciones (recursivo)")
    print("6. Gestionar equipo (ABM)")
    print("7. Historial (pila)")
    print("8. Turnos de combate (cola)")
    print("9. Guardar / cargar catálogo")
    print("0. Salir")


def main():
    opciones = {
        "1": listar_catalogo,
        "2": ver_detalle,
        "3": buscar,
        "4": ordenar,
        "5": cadena_evoluciones,
        "6": gestionar_equipo,
        "7": historial_pila,
        "8": cola_turnos,
        "9": guardar_cargar,
    }

    while True:
        mostrar_menu()
        opcion = input("Elegí una opción: ").strip()

        if opcion == "0":
            print("¡Hasta luego, entrenador!")
            break

        accion = opciones.get(opcion)
        if accion is None:
            print("Opción inválida. Probá de nuevo.")
            continue

        try:
            accion()
        except Exception as e:
            # NOTA: esto es un placeholder. La consigna pide excepciones
            # propias (ítem no encontrado, colección llena/vacía, etc.),
            # no capturar Exception genérico. Ir reemplazando esto a
            # medida que se definan esas excepciones.
            print(f"Ocurrió un error: {e}")


if __name__ == "__main__":
    main()
