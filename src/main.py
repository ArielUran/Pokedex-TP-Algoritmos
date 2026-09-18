from src.config import TEMA

TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}


def main():
    if TEMA not in TEMAS:
        print("Seteá TEMA en src/config.py: 'pokedex', 'recetario' o 'musica'.")
        return

    if TEMA == "pokedex":
        # Delega en el menú real del dominio (src/dominio/cli.py).
        # A medida que sumemos ListaEnlazada/Pila/Cola, el menú real
        # se va a ir completando ahí, no acá.
        from src.dominio.cli import main as main_pokedex
        main_pokedex()
    else:
        print(f"El tema '{TEMA}' todavía no tiene menú implementado.")


if __name__ == "__main__":
    main()
