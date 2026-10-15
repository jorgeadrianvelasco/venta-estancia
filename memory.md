# Memoria del agente — venta de la estancia

Claude Code no recuerda nada entre sesiones: solo sabe lo que está escrito en el repositorio.
Este archivo tiene dos partes:

1. **Estado actual**: máximo 20 líneas. **Se reescribe** cada vez que algo cambia. Es lo primero que ve
   una sesión nueva (lo muestra el hook de inicio).
2. **Bitácora**: entradas con fecha, la más nueva al final. **No se reescribe**, se agrega.

Cuando el archivo pase de ~300 líneas, las entradas viejas se mueven a `memoria/AAAA-MM.md` y acá queda
una línea que diga dónde están. (En Kakau el archivo llegó a 3.151 líneas y ninguna sesión lo leía entero.)

## Estado actual
<!-- máximo 20 líneas; se reescribe -->
- **Etapa:** armado del repositorio (15/10/2026). Ninguna campaña, ningún interesado registrado.
- **Datos de la estancia:** todos pendientes (`negocio.md`).
- **Próximo paso:** que Jorge pase el aviso que ya publicó (texto, fotos, dónde salió, cuánto pedía, qué
  consultas trajo). Después, la ficha de a 3 o 4 datos por vez.
- **Sin verificar:** si Meta pone los anuncios de inmuebles en una categoría especial y qué restringe en Bolivia.

## Bitácora

### 15 de octubre de 2026 — Creación del repositorio
- **Qué se hizo:** Jorge creó `jorgeadrianvelasco/venta-estancia` (privado). Se armó la estructura copiando de
  Kakau la forma, no el contenido: reglas, decisiones, memoria con "Estado actual", hooks de inicio, commit y
  cierre, comando `/cerrar`, receta de campañas de Meta, skills `calificar-interesado` y `crear-campana`, y el
  agente `investigador-estancia`.
- **Pendiente:** el aviso anterior de la estancia y todos los datos de `negocio.md`.
