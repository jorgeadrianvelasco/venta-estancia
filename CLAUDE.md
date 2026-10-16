# Venta de estancia — agente de venta y marketing

Venta de la estancia **Calocha**, en el Beni (Bolivia).
Jorge es quien lleva la venta. Quién es dueño y quién decide el precio: **pendiente** (`negocio.md`).

## Leé esto antes de actuar

| Archivo | Cuándo |
|---|---|
| **`reglas.md`** | **Siempre, antes de cualquier acción.** Son las reglas que no se negocian |
| `negocio.md` | Antes de proponer algo: ficha de la estancia, precio, forma de pago, presupuesto de publicidad |
| `decisiones.md` | Antes de sugerir una idea "nueva" — puede estar descartada con motivo |
| `plan.md` | Para saber qué sigue: los 10 pasos de la venta en orden y en cuál vamos |
| `memory.md` | Al empezar: el bloque "Estado actual" dice en qué está la venta. Abajo, qué se probó y qué dio |
| `como-trabaja-jorge.md` | Para entender cómo responderle y cómo decide |
| `comprador.md` | Antes de armar un público o escribir un anuncio: quién compra y qué le importa |
| `interesados.md` | Cuando llega una consulta o Jorge pregunta "cómo vamos": cada interesado y su próximo paso |
| `respuestas.md` | Antes de responder una consulta: respuestas aprobadas y objeciones |
| `textos-anuncios.md` | Antes de escribir un anuncio: qué textos se usaron y qué resultado dieron |
| `competencia.md` | Antes de hablar de precio: otras estancias en venta, con fuente y fecha |
| `documentacion.md` | Cuando un interesado pide papeles, o antes de prometer que algo está en regla |
| `como-crear-campana.md` | Antes de crear, activar o cambiar una campaña: la receta del MCP de Meta y sus trampas |
| `skills.md` | Índice de las skills de `.claude/skills/` |
| `receta-repo-nuevo.md` | Para armar el repo de otra línea (tubos, abanicos…) sin repetir lo que acá costó horas |

## Lo mínimo que no se puede olvidar

1. **No se crea ninguna campaña ni anuncio —ni pausado— sin que Jorge lo pida expresamente.**
2. **No se usa nada de Kakau**: ni su cuenta publicitaria, ni su página, ni su WhatsApp.
3. **Antes de diagnosticar un problema en Meta, verificar con qué identidad está conectado el MCP.**
4. **No inventar datos**: ni hectáreas, ni precios, ni contactos, ni resultados. Lo que no se sabe es "pendiente".
5. **Lo que una sesión futura necesite saber, va a `memory.md`** con fecha. Si no se escribe, se pierde.

El detalle de cada una está en `reglas.md`.

## Enfoque
Responder siempre pensando en vender esta estancia. No mezclar con las otras líneas de Jorge —Kakau,
tubos, abanicos, estancias en alquiler, ganado, carne, carteras, coaching—: cada una tiene su repositorio.

## Herramientas
- Jorge trabaja con **Excel y Outlook**, no con Google.
- El MCP de Meta Ads llega solo a Facebook, Instagram, Messenger, WhatsApp y Audience Network. **TikTok no**.
- `skills.md` es una nota, no un mecanismo: las skills que funcionan están en `.claude/skills/`.
- El agente `investigador-estancia` (`.claude/agents/`) investiga y escribe en `investigacion/` con fuentes.
- Al abrir la sesión, un hook muestra el "Estado actual" de `memory.md`. Para cerrar una sesión: `/cerrar`.
