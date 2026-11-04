# miu-portable-registry

Índice de descubrimiento de los repositorios públicos del ecosistema MIU. Este repositorio conserva su documentación histórica y añade un catálogo consultable; no presenta como implementadas las APIs y carpetas imaginadas por el README anterior.

## Consultar sin ejecutar ni desplegar

```bash
python3 scripts/discover.py --validate
python3 scripts/discover.py --list-fronts
python3 scripts/discover.py --front validation-pva
python3 scripts/discover.py --query skills
python3 scripts/discover.py --id 1288146674
python3 -m unittest discover -s tests -v
```

El lector usa únicamente la biblioteca estándar de Python y el archivo local [catalog/capabilities.json](catalog/capabilities.json). No llama a servicios, lee credenciales ni ejecuta código encontrado en otros repositorios.

## Estructura real

- **Catálogo:** IDs numéricos de GitHub, rutas públicas, ramas observadas, estado de descubrimiento y propuestas con evidencia de pruebas.
- **Frentes:** rutas iniciales para skills, herramientas, registro, agentes, validación PVA, portabilidad y Grimorio. Son pistas de navegación, no servicios certificados.
- **Documentación previa:** se conserva en `docs/bibliografia/` y `registros/`; su presencia no valida sus afirmaciones.
- **Worker previo:** `worker.js` se conserva sin ejecutar ni desplegar. Esta revisión no prueba su disponibilidad.

## Continuidad verificable

Consultar primero el catálogo, seleccionar un ID, leer la fuente y sus workflows, probar una capacidad acotada, y registrar el resultado remoto con lectura de retorno. Una PR en borrador no equivale a merge, despliegue ni absorción por otros nodos.

El catálogo es una instantánea, no sincronización automática. Antes de publicar actualizaciones hay que comprobar otra vez visibilidad y permisos; nunca se debe exportar el inventario privado por confiar en un catálogo antiguo.

El procedimiento completo y los contratos de evidencia están en [docs/DISCOVERY.md](docs/DISCOVERY.md). Las nuevas capacidades de auditoría y continuidad se enlazan como PRs en borrador, sin afirmar que ya existen en sus ramas predeterminadas.
