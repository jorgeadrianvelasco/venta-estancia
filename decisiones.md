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

## Categoría especial de vivienda: no hace falta para un público en Bolivia
**Decidido:** 15/10/2026, con la ayuda oficial de Meta ([acerca de los anuncios de vivienda](https://www.facebook.com/business/help/1198401317374558)).
**Por qué:** la categoría es obligatoria solo con anunciante en EE. UU. o público en EE. UU., Canadá o ciertos
países de Europa. Para Bolivia no se exige, y el público se arma sin las restricciones de esa categoría.
**Qué la haría cambiar:** apuntar al comprador extranjero en esos países. Entonces la campaña lleva la categoría.

## El precio no se publica
**Decidido:** 15/10/2026, por Jorge.
**Por qué:** *"es un valor muy elevado y no tengo interés en que se sepa el precio"*. No va en anuncios, ni en
respuestas automáticas, ni en este repositorio salvo que Jorge lo pida.
**Consecuencia:** quien solo pregunta el precio y se va es un curioso, y a Jorge **no le molesta** que se vaya. El
filtro entre curioso y comprador serio tiene que estar en el anuncio y en la primera respuesta, no en el precio.
**Qué la haría cambiar:** que Jorge decida publicarlo.

## El objetivo es interés serio, no volumen de consultas
**Decidido:** 15/10/2026, por Jorge: *"quiero que la gente se interese sobre todo pero que no sean curiosos, que más
sean personas con interés en serio en comprar estancias"*.
**Por qué:** el boost de 2025 trajo 6 conversaciones a 3,43 Bs y ninguna sirvió: preguntaron el precio y se fueron.
Una conversación barata no vale nada si no es de un comprador.
**Cómo se mide:** por interesados **serios** y **visitas** (`interesados.md`), no por conversaciones ni por costo por
conversación.

## Todo lo de Meta va en el portfolio "Jorge Velasco"
**Decidido:** 15/10/2026, por Jorge.
**Por qué:** ya existe (`160471911857072`), así que no hace falta un portfolio nuevo. La página y la cuenta
publicitaria de la venta se crean adentro. No se usa la cuenta personal `64830109`: está fuera de todo portfolio y
el MCP no puede impulsar publicaciones de Marketplace.
**Ojo:** una cuenta creada dentro de un portfolio queda en él para siempre, y un portfolio nuevo arranca con una
sola cuenta publicitaria ([Meta](https://www.facebook.com/business/help/915885887059947)).
**Qué la haría cambiar:** que el límite de cuentas publicitarias de "Jorge Velasco" no permita crear una.

---

## Pendientes de decidir

| Tema | Por qué importa |
|---|---|
| Qué WhatsApp atiende las consultas | No se puede usar el de Kakau (`reglas.md`, regla 2) |
| Cómo se filtra al curioso antes de que escriba | El precio no se publica: el filtro tiene que estar en el texto del anuncio o en un formulario con preguntas |
| Si los teléfonos de los interesados se guardan en `interesados.md` | El repo es privado, pero lo que entra a git queda en el historial para siempre |
| Si la venta se publica también fuera de Meta (portales, grupos, boca a boca) | Define qué canales se miden en `interesados.md` |
