"""Ordenamientos propios (E4). Prohibido sorted() y list.sort()."""


def ordenar_seleccion(coleccion, clave):
    """
    Ordenamiento por selección, ascendente, IN PLACE. NO es estable.

    Para cada posición i busca el mínimo de lo que queda a la derecha
    y lo intercambia con el de la posición i.

    Tiempo: O(n²) siempre. Espacio: O(1).
    """
    n = len(coleccion)
    for i in range(n - 1):
        pos_min = i
        for j in range(i + 1, n):
            if clave(coleccion[j]) < clave(coleccion[pos_min]):
                pos_min = j
        coleccion[i], coleccion[pos_min] = coleccion[pos_min], coleccion[i]
    return coleccion


def ordenar_insercion(coleccion, clave):
    """
    Ordenamiento por inserción, ascendente, IN PLACE. SÍ es estable.

    Toma cada elemento y lo inserta en su lugar entre los ya ordenados,
    desplazando a la derecha los que son mayores.

    Tiempo: O(n) mejor caso, O(n²) peor y promedio. Espacio: O(1).
    """
    for i in range(1, len(coleccion)):
        actual = coleccion[i]
        j = i - 1
        while j >= 0 and clave(coleccion[j]) > clave(actual):
            coleccion[j + 1] = coleccion[j]
            j -= 1
        coleccion[j + 1] = actual
    return coleccion
