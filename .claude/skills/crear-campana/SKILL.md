---
name: crear-campana
description: Crear una campaña de Meta Ads para la venta de la estancia (Facebook o Instagram, mensajes por WhatsApp) por el MCP oficial. Usar cuando Jorge pida armar, programar o lanzar una campaña o propaganda de la estancia. Revisa identidad y cuenta, la categoría especial de inmuebles, pregunta monto y horario, crea todo y programa los controles.
---

# Crear una campaña de la estancia

La receta técnica (parámetros exactos de cada llamada) está en `como-crear-campana.md`. Esta Skill es el orden de
trabajo y los controles que no se pueden saltear. Adaptada de la de Kakau el 15/10/2026; **todavía no se usó**.

## 0. Antes de tocar nada
1. Leé `reglas.md`. **Regla 1: solo se crea si Jorge lo pidió con esas palabras.**
2. `ads_get_ad_accounts`: confirmá la identidad del MCP y la cuenta de esta línea (`negocio.md`).
   - **Si la única cuenta disponible es la de Kakau: frená.** No se usa (`reglas.md`, regla 2).
   - Si la cuenta dice `UNSETTLED`: no se puede crear nada. El MCP no paga. Avisale a Jorge y frená.
3. **Categoría especial de inmuebles** (`reglas.md`, regla 5). Si sigue sin verificar, verificala ahora con
   `ads_get_help_article` y anotá el resultado en `decisiones.md` antes de seguir.

## 1. Armar la propuesta
- Público dentro de lo que permita la categoría especial, a partir de `comprador.md`.
- Texto desde `textos-anuncios.md`: qué se usó y qué dio.
- Números: presupuesto total y costo máximo por interesado serio (`negocio.md`). Si están en "pendiente",
  **preguntarlos antes**: ninguna propuesta de pauta sin números.

## 2. Preguntar antes de gastar
`AskUserQuestion` con **monto exacto, días y horario**, además de post y plataforma si no están claros.

## 3. Crear
Paso a paso de `como-crear-campana.md`. Todo se crea **pausado** y se activa solo con la aprobación de Jorge.
Después de crear, leé el conjunto de nuevo y compará el `targeting` con lo que mandaste.

## 4. Programar los controles
Con `send_later` (hora UTC = Bolivia + 4): antes del arranque (cuenta ACTIVE, anuncio aprobado), una hora y media
después del arranque, y al cierre.

## 5. Dejarlo escrito
- `memory.md`: entrada con fecha, IDs de campaña, conjunto y anuncio, lo aprobado por Jorge y los IDs de los controles.
  Actualizar el "Estado actual".
- `negocio.md`: fila nueva en la tabla de campañas.
- Cada consulta que traiga, a `interesados.md` con la Skill `calificar-interesado`.
