# Protocolo de pruebas

Pruebas **manuales**. Cada fila es un caso. Ejecutar sobre el tag que entregan.

Leyenda de resultado: `pasa` / `no pasa` / `no corrido`.

Mínimos: 8 casos escritos en E2; ejecutados en E3; 15 de regresión en E6 (pila, cola, archivos, recursión, búsquedas).

| ID | Entrega | Acción (pasos en el CLI) | Datos | Resultado esperado | Resultado | Notas |
| --- | --- | --- | --- | --- | --- | --- |
| P01 | E1 | Arrancar el programa y listar catálogo | opción 1 del menú | lista las 68 filas del catálogo, sin traceback | pasa |  |
| P02 | E1 | Elegir un ítem inexistente | ver detalle, número = 9999 | mensaje "No se encontró ningún Pokémon con..." y el menú sigue | pasa |  |
| P03 | E2 | Operación recursiva sobre un ítem con cadena | número = 4 (Charmander) | imprime Charmander -> Charmeleon -> Charizard | pasa |  |
| P03b | E2 | Operación recursiva con ramificación | número = 133 (Eevee) | imprime Eevee y sus 3 evoluciones (Vaporeon, Jolteon, Flareon) | pasa |  |
| P04 | E2 | Operación recursiva sobre un ítem sin derivados | número = 151 (Mew, no evoluciona) | solo imprime el ítem (caso base inmediato) | pasa |  |
| P05 | E3 | Agregar a la colección principal hasta el tope | equipo de 6, después un 7mo | el séptimo falla con ColeccionLlenaError | pasa |  |
| P06 | E3 | Desapilar historial vacío | pila vacía (opción 7 sin acciones previas) | PilaVaciaError, menú sigue | pasa |  |
| P07 | E3 | Desencolar cola vacía | cola vacía (opción 8 sin encolar antes) | ColaVaciaError, menú sigue | pasa |  |
| P08 | E3 | Listar colección con el iterador | equipo con 6 ítems agregados en orden | el orden coincide con las inserciones | pasa |  |
| P09 | E4 | Búsqueda lineal de un nombre que existe | opción 3, lineal, nombre = Golem | lo encuentra y lo muestra | pasa |  |
| P10 | E4 | Búsqueda lineal de un nombre que no existe | opción 3, lineal, nombre = Missingno | "No se encontró ningún Pokémon...", sin traceback, el menú sigue | pasa |  |
| P11 | E4 | Búsqueda binaria con catálogo desordenado | catálogo ordenado por número; opción 3, binaria, nombre = Golem | avisa que reordena por nombre y lo encuentra (no da falso "no encontrado") | pasa |  |
| P12 | E4 | Ordenar por un criterio y después por otro | opción 4: nombre con selección, luego número con inserción | el orden cambia correctamente en cada caso | pasa |  |
| P13 | E5 | Guardar CSV, salir, volver a entrar |  | los datos siguen | no corrido |  |
| P14 | E5 | Guardar binario y modificar un registro por id |  | al recargar, ese campo cambió | no corrido |  |
| P15 | E5 | Abrir un binario truncado o con magia mala | archivo basura | excepción de archivo inválido | no corrido |  |
