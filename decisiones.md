# Decisiones y por qué

No qué decidimos: **por qué**. Este archivo existe para que ninguna sesión futura vuelva a proponer algo
que ya se descartó por una razón concreta.

Si algo de acá se contradice con la realidad, **no se ignora: se actualiza**, con la fecha y el motivo.

Formato de cada decisión:

```
## [Qué se decidió]
**Decidido:** fecha.
**Por qué:**
**Qué la haría cambiar:**
```

---

## Esta venta tiene su propio repositorio
**Decidido:** 15/10/2026.
**Por qué:** Jorge arma un agente de venta por línea de negocio, cada uno en su repositorio, sin mezclar.
Kakau es el molde: de ahí se copió la estructura (reglas, memoria, hooks, receta de Meta), no el contenido.
**Qué la haría cambiar:** nada previsto.

## TikTok queda fuera de este agente
**Decidido:** 15/10/2026 (heredado de Kakau, 8/9/2026).
**Por qué:** el MCP de Meta Ads llega solo a Facebook, Instagram, Messenger, WhatsApp y Audience Network.
**Qué la haría cambiar:** nada del lado técnico. Si se pauta en TikTok, se hace por fuera.

---

## Pendientes de decidir

| Tema | Por qué importa |
|---|---|
| Qué cuenta publicitaria, página y WhatsApp usa esta línea | No se puede usar nada de Kakau (`reglas.md`, regla 2) |
| Si los teléfonos de los interesados se guardan en `interesados.md` | El repo es privado, pero lo que entra a git queda en el historial para siempre |
| Si la venta se publica también fuera de Meta (portales, grupos, boca a boca) | Define qué canales se miden en `interesados.md` |
