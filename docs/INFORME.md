# Informe del TP

Completar y hacer crecer en cada entrega. No hace falta prosa larga: oraciones claras y tablas.

## 1. Grupo y tema

- Tema: Pokédex
- Por qué lo eligieron (5–8 líneas): Porque nos gustan.

## 2. Modelo

Qué es un ítem del catálogo. Qué es mutable y qué no (E1). Cómo se relacionan catálogo, colección principal, pila y cola.

```text
(pueden pegar un diagrama ASCII o una lista de clases)
```

## 3. Recursión (E2)

- Función: `imprimir_cadena_evoluciones(numero, catalogo, mapa_evoluciones, nivel)`
  en `src/dominio/evoluciones.py`.
- Caso base: `mapa_evoluciones.get(numero)` devuelve una lista vacía
  (el Pokémon no tiene ninguna evolución registrada) -> se imprime y
  se hace `return` sin volver a llamarse.
- Caso recursivo: si tiene una o más evoluciones, se imprime el actual
  y se llama a sí misma una vez por cada evolución encontrada. Esto
  permite manejar ramificaciones (un Pokémon que evoluciona a más de
  una forma, como Eevee).

Traza de un ejemplo simple — `imprimir_cadena_evoluciones(4, ...)` (Charmander):

```
llamada(4)  Charmander    -> mapa[4] = [5]   -> no es caso base, llama a llamada(5)
  llamada(5)  Charmeleon  -> mapa[5] = [6]   -> no es caso base, llama a llamada(6)
    llamada(6)  Charizard -> mapa[6] = []    -> CASO BASE, return

Salida:
Charmander
  └─> Charmeleon
    └─> Charizard
```

Traza de un ejemplo con ramificación — `imprimir_cadena_evoluciones(133, ...)` (Eevee):

```
llamada(133) Eevee -> mapa[133] = [134, 135, 136] -> no es caso base,
  se llama una vez por cada destino:
    llamada(134) Vaporeon -> mapa[134] = [] -> CASO BASE, return
    llamada(135) Jolteon  -> mapa[135] = [] -> CASO BASE, return
    llamada(136) Flareon  -> mapa[136] = [] -> CASO BASE, return

Salida:
Eevee
  └─> Vaporeon
  └─> Jolteon
  └─> Flareon
```

## 4. TADs (E3)

| TAD | Operaciones | Invariante |
| --- | --- | --- |
| ListaEnlazada | insertar_al_inicio, insertar_al_final, insertar_ordenado, eliminar, buscar, primero, quitar_del_inicio, tamanio, esta_vacia, iterador (yield) | `_tamanio` siempre coincide con la cantidad de nodos alcanzables desde `_cabeza`; `_cabeza` es None sii la lista está vacía |
| Pila | apilar, desapilar, ver_tope, esta_vacia | LIFO: el tope es siempre el último apilado; se opera solo por la cabeza de la lista interna (O(1)) |
| Cola | encolar, desencolar, ver_frente, esta_vacia | FIFO: el frente es siempre el más antiguo encolado; se encola por el final y se desencola por la cabeza |

Dónde se usa cada uno en el dominio: el **equipo** (máx. 6) vive sobre `ListaEnlazada`; el **historial** de altas/bajas del equipo es una `Pila` (permite deshacer); los **turnos de combate** son una `Cola`.

## 5. Complejidad (E4)

| Operación | Tiempo | Espacio | Por qué |
| --- | --- | --- | --- |
| Listar catálogo | O(n) | O(1) | Recorre los n elementos una sola vez. |
| Ver detalle de un ítem | O(n) | O(1) | Se busca por número o nombre recorriendo el catálogo hasta encontrarlo. |
| Búsqueda lineal | O(n) peor / O(1) mejor | O(1) | Compara de a un elemento hasta encontrarlo o llegar al final; si no existe, recorre todo. |
| Búsqueda binaria | O(log n) | O(1) | Cada comparación descarta la mitad del rango; requiere catálogo ordenado por esa clave. |
| Ordenar por selección | O(n²) siempre | O(1) | Dos bucles anidados: n + (n-1) + ... + 1 ≈ n²/2 comparaciones, aunque ya esté ordenado. No es estable. |
| Ordenar por inserción | O(n) mejor / O(n²) peor y promedio | O(1) | Si ya está ordenado hace 1 comparación por elemento; si está al revés, desplaza todo. Es estable. |
| Agregar al equipo (ListaEnlazada.insertar_al_final) | O(n) | O(1) | Hay que recorrer hasta el último nodo (la lista no guarda puntero al final). |
| Apilar / desapilar | O(1) | O(1) | Solo tocan la cabeza de la lista enlazada. |
| Encolar | O(n) | O(1) | Inserta al final recorriendo la lista. |
| Desencolar | O(1) | O(1) | Saca la cabeza. |

Costo extra de la binaria: si el catálogo no está ordenado por el criterio pedido, el menú lo reordena primero con inserción (O(n²) peor caso) y avisa con un mensaje. La búsqueda binaria en sí sigue siendo O(log n).

Estabilidad (comprobada con pares `(clave, etiqueta)` = (2,a),(1,b),(2,c),(1,d),(2,e) ordenados por clave): inserción devuelve (1,b),(1,d),(2,a),(2,c),(2,e) (conserva el orden relativo de los iguales); selección devuelve (1,b),(1,d),(2,c),(2,a),(2,e) (los mezcla).

Mediciones (`time.perf_counter`, `python -m src.algoritmos.medicion`). Datos: catálogo original (n = 70) y copias agrandadas repitiendo las filas (×10 y ×30), desordenadas con semilla fija. Búsquedas en su peor caso (nombre que no existe), promediadas sobre 2000 repeticiones; ordenamientos medidos una vez.

| Operación | n | segundos |
| --- | --- | --- |
| búsqueda lineal (nombre) | 70 | 0.000009 |
| búsqueda lineal (n × 10) | 700 | 0.000102 |
| búsqueda lineal (n × 30) | 2100 | 0.000346 |
| búsqueda binaria (nombre) | 70 | 0.000002 |
| búsqueda binaria (n × 10) | 700 | 0.000003 |
| búsqueda binaria (n × 30) | 2100 | 0.000004 |
| ordenar por selección | 70 | 0.000879 |
| ordenar por selección (n × 10) | 700 | 0.079841 |
| ordenar por selección (n × 30) | 2100 | 0.665610 |
| ordenar por inserción | 70 | 0.0001446 |
| ordenar por inserción (n × 10) | 700 | 0.044552 |
| ordenar por inserción (n × 30) | 2100 | 0.475138 |

Lectura: la búsqueda lineal crece con n (al pasar de 70 a 700 elementos, ×10, el tiempo pasa de 9 a 102 microsegundos, aproximadamente ×11); la binaria casi no cambia al agrandar el catálogo (de 2 a 4 microsegundos con n × 30), como corresponde a O(log n); los dos ordenamientos se disparan: al multiplicar n por 10 el tiempo se multiplica por ~100 (selección: 0.00088 s → 0.080 s; inserción: 0.00045 s → 0.045 s), lo esperable de O(n²). Inserción resulta más rápida que selección en datos desordenados porque su bucle interno corta apenas encuentra el lugar, mientras que selección siempre recorre todo lo que queda.
