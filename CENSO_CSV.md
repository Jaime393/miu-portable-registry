# CENSO_CSV — Jaime393/miu-portable-registry

- Total: **37 archivos CSV, 142.353 bytes, 312 líneas, 275 filas de datos** (312 líneas menos 37 encabezados).
- Fuente: borrador `~/workspace/mineria/miu-portable-registry/MINERIA.md` §1.5 (Parte 1, solo SÉ).

## Tandas cubiertas y tandas que faltan

- Los CSV cubren las tandas 09–19 (11 archivos) y 25–35 (12 archivos).
- No hay archivos para las tandas 01–08 ni 20–24 en este repo.

## Filas de datos por archivo

| Archivo | Filas | Líneas |
|---|---:|---:|
| tanda-09_temas-nuevos.csv | 15 | 16 |
| tanda-10_transfer-entropy-percolacion.csv | 13 | 14 |
| tanda-11_metabolic-scaling.csv | 13 | 14 |
| tanda-12_informacion-algoritmica.csv | 11 | 12 |
| tanda-13_dinamica-opiniones.csv | 8 | 9 |
| tanda-14_teoria-colas-trafico.csv | 8 | 9 |
| tanda-15_criticidad-autoorganizada-biologica.csv | 7 | 8 |
| tanda-16_redes-multicapa.csv | 6 | 7 |
| tanda-17_control-redes-complejas.csv | 6 | 7 |
| tanda-18_sueno-memoria.csv | 6 | 7 |
| tanda-19_epidemias-redes-temporales.csv | 6 | 7 |
| 2026-07-04_tanda-25_teoria-aprendizaje-estadistico.csv | 6 | 7 |
| 2026-07-04_tanda-26_escalamiento-urbano.csv | 6 | 7 |
| 2026-07-04_tanda-27_conectomica.csv | 6 | 7 |
| 2026-07-04_tanda-28_fermi-seas-fraccionarios-bose1d.csv | 6 | 7 |
| 2026-07-04_tanda-29_criticidad-redes-neuronales-artificiales.csv | 6 | 7 |
| 2026-07-04_tanda-30_multifractalidad-turbulencia.csv | 6 | 7 |
| 2026-07-04_tanda-31_transiciones-fase-cuanticas.csv | 6 | 7 |
| 2026-07-04_tanda-32_paisajes-fitness-evolutivo.csv | 6 | 7 |
| 2026-07-04_tanda-33_complejidad-economica-comercio.csv | 6 | 7 |
| 2026-07-04_tanda-34_motivos-red-biologia-sistemas.csv | 6 | 7 |
| 2026-07-04_tanda-34_network-motifs.csv | 6 | 7 |
| 2026-07-04_tanda-35_fallos-cascada-redes-infraestructura.csv | 5 | 6 |
| CITATIONS_ADAPTIVE_NETWORKS.csv | 6 | 7 |
| CITATIONS_CATASTROPHE_THEORY.csv | 6 | 7 |
| CITATIONS_ECONOPHYSICS.csv | 6 | 7 |
| CITATIONS_EXOTIC_3.csv | 12 | 13 |
| CITATIONS_EXOTIC_4.csv | 8 | 9 |
| CITATIONS_EXOTIC_5.csv | 7 | 8 |
| CITATIONS_EXOTIC_6.csv | 7 | 8 |
| CITATIONS_EXOTIC_7.csv | 6 | 7 |
| CITATIONS_EXOTIC_8.csv | 5 | 6 |
| CITATIONS_KAUFFMAN.csv | 8 | 9 |
| CITATIONS_KURAMOTO.csv | 6 | 7 |
| CITATIONS_RANDOM_GRAPHS.csv | 7 | 8 |
| CITATIONS_VALIDATED.csv | 15 | 16 |
| CITATIONS_VALIDATED_2.csv | 6 | 7 |
| **Total (37 archivos)** | **275** | **312** |

## Encabezados

- Los 37 CSV tienen 7 columnas.
- Encabezado en 11 archivos: `tema, autor_año, titulo, venue, doi_isbn, hallazgo_clave, relevancia_gap_miu`.
- Encabezado en 26 archivos: `tema, autor_anio, titulo, venue, doi_isbn, hallazgo_clave, relevancia_gap_miu`.
- Excepción: `CITATIONS_EXOTIC_3.csv` y `CITATIONS_EXOTIC_4.csv` traen la columna como `doi_isb` (sin la `n`).
- La asignación de cada variante de encabezado a cada archivo no está registrada en el borrador (solo los conteos 11 y 26).

## Tres CSV leídos enteros (muestra)

- `tanda-09_temas-nuevos.csv` (15 filas): Hodgkin & Huxley 1952, Izhikevich 2003, Friston 2010, Landauer 1961, Still/Sivak/Bell/Crooks 2012, Parrondo/Horowitz/Sagawa 2015, Nowak & May 1992, Ohtsuki et al. 2006, Nowak 2006, Ogata 1988, Corral 2004, Ferrer i Cancho & Solé 2001 y 2003, May 1972 y 1976, con DOI por fila.
- `CITATIONS_VALIDATED.csv` (15 filas): Mandelbrot 1967, Peng 1994, Higuchi 1988, Clauset/Shalizi/Newman 2009, Scheffer 2009, Dakos 2012, Bettencourt 2007, Batty 2008, Piketty & Saez 2003, Gabaix 2009, Newman 2005, Barabási & Albert 1999, Watts & Strogatz 1998, West 2017, Falconer 2003.
- `CITATIONS_EXOTIC_3.csv` (12 filas): Kleiber 1932, West/Brown/Enquist 1997, Shannon 1948, Kolmogorov 1965, Open Science Collaboration 2015, Kass & Raftery 1995, Kuramoto 1975, Pearl 2009, Shannon–Wiener, Bettencourt 2013, Newman 2003, Goldberger et al. 2002.

## Cruces medidos

- `CITATIONS_VALIDATED.csv` y `D_f_BIBLIOGRAPHY.md` comparten 9 referencias (Mandelbrot 1967, Peng 1994, Higuchi 1988, Clauset/Shalizi/Newman 2009, Scheffer 2009, Dakos 2012, Batty 2008, Newman 2005, Falconer 2003). Solo en el MD: Mandelbrot 1982, Kantelhardt 2002, Gabaix 1999 (3). Solo en el CSV: Bettencourt 2007, Piketty & Saez 2003, Gabaix 2009, Barabási & Albert 1999, Watts & Strogatz 1998, West 2017 (6).
- Los dos archivos tanda-34 comparten 4 de 6 títulos: `Network motifs in the transcriptional regulation network of Escherichia coli`, `Network motifs: theory and experimental approaches`, `Structure and function of the feed-forward loop network motif`, `Superfamilies of Evolved and Designed Networks`. Cada uno trae 2 títulos distintos; los dos tienen el mismo tema (motivos de red en biología de sistemas (network motifs)). Sus sha256 de contenido difieren.
- Duplicación entre repos: `CITATIONS_EXOTIC_5.csv`, `CITATIONS_EXOTIC_6.csv`, `CITATIONS_EXOTIC_7.csv` y `CITATIONS_EXOTIC_8.csv` tienen el mismo sha de blob en este repo y en `Jaime393/miu-portable-extra` (`676eed12…`, `530bf02f…`, `ce74d437…`, `655fe0cb…`): byte idénticos. `CITATIONS_EXOTIC_3.csv` y `CITATIONS_EXOTIC_4.csv` tienen el mismo tamaño en ambos repos pero distinto sha de blob (aquí `7c596068…` y `a66fa658…`; en miu-portable-extra `b72862fb…` y `d92c509a…`): mismo tamaño, distinto contenido.
- `miu-portable-extra` tiene en su raíz `CITATIONS_EXOTIC_CONSOLIDADO.csv` (16.292 B). Ese archivo consolidado NO está en este repo.
