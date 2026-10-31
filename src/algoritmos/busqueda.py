"""Búsquedas propias (E4). Prohibido usar in, .index() o bisect acá."""


def busqueda_lineal(coleccion, clave, obtener_clave=None):
    """
    Recorre la colección de a un elemento y devuelve el primero cuya
    clave coincide, o None si no existe. Funciona con cualquier orden.

    obtener_clave: función que de un elemento devuelve el valor a
    comparar (ej: lambda p: p.nombre). Si es None compara el elemento entero.

    Tiempo: O(n) peor caso, O(1) mejor caso. Espacio: O(1).
    """
    for elemento in coleccion:
        if obtener_clave is None:
            if elemento == clave:
                return elemento
        elif obtener_clave(elemento) == clave:
            return elemento
    return None


def busqueda_binaria(coleccion_ordenada, clave, obtener_clave):
    """
    Búsqueda binaria. REQUIERE que la colección esté ordenada
    (ascendente) por obtener_clave. Devuelve el elemento o None.

    Tiempo: O(log n). Espacio: O(1).
    """
    izq = 0
    der = len(coleccion_ordenada) - 1

    while izq <= der:
        medio = (izq + der) // 2
        valor = obtener_clave(coleccion_ordenada[medio])

        if valor == clave:
            return coleccion_ordenada[medio]
        elif valor < clave:
            izq = medio + 1   # la clave está en la mitad derecha
        else:
            der = medio - 1   # la clave está en la mitad izquierda

    return None
