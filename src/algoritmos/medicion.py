"""
Mediciones de E4 con time.perf_counter.

Se corre desde la raíz del repo:   python -m src.algoritmos.medicion

Mide búsqueda lineal, búsqueda binaria y los dos ordenamientos sobre el
catálogo original (x1) y sobre copias agrandadas repitiendo las filas
(x10 y x30). Las búsquedas se miden en su PEOR caso (nombre que no
existe) y se promedian sobre muchas repeticiones porque una sola es
demasiado rápida para el reloj.
"""

import random
import time

from src.dominio.pokedex import catalogo
from src.algoritmos.busqueda import busqueda_lineal, busqueda_binaria
from src.algoritmos.ordenamiento import ordenar_seleccion, ordenar_insercion

FACTORES = (1, 10, 30)
REPETICIONES = 2000
CLAVE = lambda p: p.nombre.lower()


def medir_busqueda(funcion, *args):
    """Tiempo promedio (segundos) de una llamada, sobre REPETICIONES."""
    inicio = time.perf_counter()
    for _ in range(REPETICIONES):
        funcion(*args)
    fin = time.perf_counter()
    return (fin - inicio) / REPETICIONES


def medir_orden(algoritmo, datos):
    """Tiempo (segundos) de ordenar una copia de `datos` una vez."""
    copia = list(datos)
    inicio = time.perf_counter()
    algoritmo(copia, CLAVE)
    fin = time.perf_counter()
    return fin - inicio


def main():
    random.seed(1)  # misma mezcla en cada corrida
    print(f"{'Operación':<34}{'n':>6}{'segundos':>14}")
    print("-" * 54)

    for factor in FACTORES:
        datos = list(catalogo) * factor
        random.shuffle(datos)  # desordenado para los ordenamientos
        n = len(datos)

        t_sel = medir_orden(ordenar_seleccion, datos)
        t_ins = medir_orden(ordenar_insercion, datos)

        ordenados = list(datos)
        ordenar_insercion(ordenados, CLAVE)  # la binaria necesita orden

        t_lin = medir_busqueda(busqueda_lineal, datos, "zzz", CLAVE)
        t_bin = medir_busqueda(busqueda_binaria, ordenados, "zzz", CLAVE)

        print(f"{'búsqueda lineal (peor caso)':<34}{n:>6}{t_lin:>14.6f}")
        print(f"{'búsqueda binaria (peor caso)':<34}{n:>6}{t_bin:>14.6f}")
        print(f"{'ordenar por selección':<34}{n:>6}{t_sel:>14.6f}")
        print(f"{'ordenar por inserción (desord.)':<34}{n:>6}{t_ins:>14.6f}")
        print()


if __name__ == "__main__":
    main()
