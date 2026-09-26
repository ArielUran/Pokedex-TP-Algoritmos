"""
CLI de la Pokédex - TP integrador Algoritmos y Estructuras de Datos

Este archivo es el "menú" que conecta al usuario con la lógica del
catálogo, el equipo, el historial y la cola de turnos.
"""

from src.dominio.pokedex import catalogo
from src.dominio.evoluciones import (
    construir_mapa_evoluciones,
    imprimir_cadena_evoluciones,
)
from src.dominio.equipo import Equipo
from src.tads.pila import Pila
from src.tads.cola import Cola
from src.excepciones import (
    ItemNoEncontradoError,
    ColeccionLlenaError,
    ColeccionVaciaError,
    PilaVaciaError,
    ColaVaciaError,
)

# ---------------------------------------------------------------------
# Estado del programa (vive mientras el CLI está corriendo).
# equipo:    la colección principal del dominio (ListaEnlazada por dentro).
# historial: pila de acciones sobre el equipo, para poder deshacer.
# turnos:    cola de Pokémon esperando su turno de combate.
# ---------------------------------------------------------------------
equipo = Equipo()
historial = Pila()
turnos = Cola()


def _buscar_en_catalogo(numero):
    for pokemon in catalogo:
        if pokemon.numero == numero:
            return pokemon
    return None


# ---------------------------------------------------------------------
# 1-5: catálogo y recursión (ya existían, sin cambios de lógica)
# ---------------------------------------------------------------------

def listar_catalogo():
    """1. Listar catálogo."""
    print("\n--- Catálogo de Pokémon ---")
    for pokemon in catalogo:
        print(pokemon)


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

    # TODO (E4): reemplazar por un algoritmo de ordenamiento propio
    # (selección, inserción, etc.) en vez de usar sorted().
    if criterio == "1":
        print("(pendiente E4: ordenar por número con algoritmo propio)")
    elif criterio == "2":
        print("(pendiente E4: ordenar por nombre con algoritmo propio)")
    else:
        print("Opción inválida.")


def cadena_evoluciones():
    """5. Operación recursiva del dominio: cadena de evoluciones."""
    dato = input("Número del Pokémon para ver su cadena de evolución: ").strip()

    if not dato.isdigit():
        print("Eso no es un número válido.")
        return

    numero = int(dato)
    pokemon = _buscar_en_catalogo(numero)

    if pokemon is None:
        print(f"No se encontró ningún Pokémon con número {numero}.")
        return

    print(f"\n--- Cadena de evolución de {pokemon.nombre} ---")
    mapa = construir_mapa_evoluciones()
    imprimir_cadena_evoluciones(numero, catalogo, mapa)


# ---------------------------------------------------------------------
# 6: equipo (ABM sobre ListaEnlazada) + historial para deshacer
# ---------------------------------------------------------------------

def _agregar_al_equipo():
    dato = input("Número del Pokémon a agregar al equipo: ").strip()
    if not dato.isdigit():
        print("Eso no es un número válido.")
        return

    pokemon = _buscar_en_catalogo(int(dato))
    if pokemon is None:
        print(f"No existe ningún Pokémon con número {dato} en el catálogo.")
        return

    # Puede lanzar ColeccionLlenaError -> lo captura el main().
    equipo.agregar(pokemon)
    historial.apilar(("agregar", pokemon))
    print(f"{pokemon.nombre} se agregó al equipo ({equipo.tamanio()}/6).")


def _quitar_del_equipo():
    dato = input("Número del Pokémon a quitar del equipo: ").strip()
    if not dato.isdigit():
        print("Eso no es un número válido.")
        return

    # Puede lanzar ItemNoEncontradoError -> lo captura el main().
    pokemon = equipo.quitar(int(dato))
    historial.apilar(("quitar", pokemon))
    print(f"{pokemon.nombre} se sacó del equipo.")


def gestionar_equipo():
    """6. ABM sobre la colección principal (equipo, máx. 6)."""
    print("\n--- Equipo actual ---")
    if equipo.esta_vacio():
        print("(vacío)")
    else:
        for pokemon in equipo.listar():
            print(pokemon)

    print("\n1. Agregar al equipo")
    print("2. Quitar del equipo")
    print("3. Volver")
    opcion = input("Elegí una opción: ").strip()

    if opcion == "1":
        _agregar_al_equipo()
    elif opcion == "2":
        _quitar_del_equipo()
    elif opcion == "3":
        return
    else:
        print("Opción inválida.")


def historial_pila():
    """7. Push/pop de la pila (historial / deshacer sobre el equipo)."""
    print(f"\nAcciones en el historial: {len(historial)}")
    print("1. Ver última acción (tope)")
    print("2. Deshacer última acción")
    print("3. Volver")
    opcion = input("Elegí una opción: ").strip()

    if opcion == "1":
        # Puede lanzar PilaVaciaError -> lo captura el main().
        tipo, pokemon = historial.ver_tope()
        print(f"Última acción: {tipo} -> {pokemon.nombre}")

    elif opcion == "2":
        # Puede lanzar PilaVaciaError -> lo captura el main().
        tipo, pokemon = historial.desapilar()
        if tipo == "agregar":
            # Deshacer un "agregar" es sacarlo del equipo.
            equipo.quitar(pokemon.numero)
            print(f"Deshecho: se sacó a {pokemon.nombre} del equipo.")
        elif tipo == "quitar":
            # Deshacer un "quitar" es volver a agregarlo.
            equipo.agregar(pokemon)
            print(f"Deshecho: se volvió a agregar a {pokemon.nombre} al equipo.")

    elif opcion == "3":
        return
    else:
        print("Opción inválida.")


# ---------------------------------------------------------------------
# 8: cola de turnos de combate
# ---------------------------------------------------------------------

def cola_turnos():
    """8. Encolar/desencolar la cola (turnos de combate)."""
    print(f"\nPokémon esperando turno: {len(turnos)}")
    print("1. Encolar un Pokémon del equipo")
    print("2. Desencolar (le toca pelear al frente)")
    print("3. Ver quién está al frente")
    print("4. Volver")
    opcion = input("Elegí una opción: ").strip()

    if opcion == "1":
        if equipo.esta_vacio():
            print("El equipo está vacío, no hay a quién encolar.")
            return
        dato = input("Número del Pokémon del equipo a encolar: ").strip()
        if not dato.isdigit():
            print("Eso no es un número válido.")
            return
        pokemon = next((p for p in equipo.listar() if p.numero == int(dato)), None)
        if pokemon is None:
            print("Ese Pokémon no está en el equipo.")
            return
        turnos.encolar(pokemon)
        print(f"{pokemon.nombre} se sumó a la cola de turnos.")

    elif opcion == "2":
        # Puede lanzar ColaVaciaError -> lo captura el main().
        pokemon = turnos.desencolar()
        print(f"¡Le toca pelear a {pokemon.nombre}!")

    elif opcion == "3":
        # Puede lanzar ColaVaciaError -> lo captura el main().
        pokemon = turnos.ver_frente()
        print(f"Al frente de la cola: {pokemon.nombre}")

    elif opcion == "4":
        return
    else:
        print("Opción inválida.")


def guardar_cargar():
    """9. Guardar y cargar catálogo en texto simple (.txt) y en binario."""
    # TODO: esto se implementa recién en la entrega 5.
    print("(pendiente E5: guardar/cargar en .txt y binario con struct)")


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
    print("7. Historial (pila / deshacer)")
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

        # Excepciones propias, cada una con un mensaje usable.
        # Nada de "except Exception" pelado: si algo no capturado
        # explota, tiene que verse el traceback y arreglarse.
        try:
            accion()
        except (
            ItemNoEncontradoError,
            ColeccionLlenaError,
            ColeccionVaciaError,
            PilaVaciaError,
            ColaVaciaError,
        ) as e:
            print(f"⚠ {e}")


if __name__ == "__main__":
    main()
