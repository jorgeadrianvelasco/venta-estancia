# Skills de la venta de la estancia

Este archivo es una **nota, no un mecanismo**: escribir acá no instala nada. Las skills que funcionan
viven en `.claude/skills/<nombre>/SKILL.md` y Claude las carga solo cuando trabaja en este repositorio.

## Las que existen en este repositorio

| Skill | Para qué | Creada |
|---|---|---|
| `calificar-interesado` | Decide si una consulta es seria, cuál es el próximo paso y la anota en `interesados.md` | 15/10/2026 |
| `crear-campana` | Armar una campaña de Meta para la estancia: revisa cuenta, categoría especial, pregunta monto y horario | 15/10/2026 |
| `cerrar` (comando) | Cerrar la sesión dejando en `memory.md` lo que la próxima necesita | 15/10/2026 |

## Agentes

| Agente | Para qué |
|---|---|
| `investigador-estancia` | Investiga precios de campos, compradores y reglas de plataformas; escribe en `investigacion/` con fuentes |

## Cuándo crear una skill nueva
Cuando el mismo trabajo se repite dos veces (por ejemplo, controlar una campaña o preparar una visita).
Antes, no: una skill escrita sin haber hecho el trabajo inventa pasos.
