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
| ListaEnlazada |  |  |
| Pila |  |  |
| Cola |  |  |

Dónde se usa cada uno en el dominio.

## 5. Complejidad (E4)

| Operación | Tiempo | Espacio | Por qué |
| --- | --- | --- | --- |
|  |  |  |  |

Mediciones (`time.perf_counter`):

| Operación | n | segundos |
| --- | --- | --- |
|  |  |  |

## 6. Persistencia (E5)

- Layout del registro binario (campos, `struct`, anchos):
- Header:
- Cómo se actualiza un registro por posición:

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
|  |  |  |
