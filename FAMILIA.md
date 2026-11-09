# FAMILIA — Jaime393/miu-portable-registry

- Fuente: borrador `~/workspace/mineria/miu-portable-registry/MINERIA.md` §1.4–1.5 (Parte 1, solo SÉ).

## Este repo en la familia miu-portable-

- El repo se llama "registry" y su contenido real es la biblioteca de citas del corpus: 37 CSV de bibliografía (275 filas) y un MD de bibliografía. No hay código, ni API, ni catálogo de módulos en disco.
- El README describe el patrón de la familia con sus propias palabras: "miu-portable-* = módulos portables del ecosistema".
- Los 11 commits de `MIU Hub de Ingesta` llevan `(aporte instancia miu-portable-extra)` en el mensaje: el vertido de julio llegó desde la instancia miu-portable-extra.

## Duplicación medida con miu-portable-extra

- `CITATIONS_EXOTIC_5.csv`, `CITATIONS_EXOTIC_6.csv`, `CITATIONS_EXOTIC_7.csv` y `CITATIONS_EXOTIC_8.csv` son byte idénticos en ambos repos (mismo sha de blob: `676eed12…`, `530bf02f…`, `ce74d437…`, `655fe0cb…`).
- `CITATIONS_EXOTIC_3.csv` y `CITATIONS_EXOTIC_4.csv` tienen el mismo tamaño en ambos repos pero distinto sha de blob (aquí `7c596068…` y `a66fa658…`; en miu-portable-extra `b72862fb…` y `d92c509a…`): mismo tamaño, distinto contenido.
- `miu-portable-extra` tiene en su raíz `CITATIONS_EXOTIC_CONSOLIDADO.csv` (16.292 B). Ese archivo consolidado NO está en este repo.

## No registrado en el borrador

- El papel de los demás hermanos de la familia (`miu-portable-data`, `miu-portable-private`, `miu-portable-skills`) no está registrado en la Parte 1 del borrador: no se afirma aquí. Queda bloqueado, no rellenado.
