# Receta para armar un repo de venta nuevo (tubos, abanicos, carteras…)

Aprendido armando la venta de Calocha (15 y 16/10/2026). Este repo se armó copiando la forma del de Kakau. **El próximo se
copia de este** y se salta todo lo que acá costó horas. Cada línea va en su propio repo y no se mezcla con las otras.

## 0. Antes de abrir la sesión (Jorge, ~15 min) — lo que más tiempo hizo perder

| Qué | Por qué | Cómo |
|---|---|---|
| **Acceso a la red completo** en el entorno | Con la red bloqueada fallaron Moda, Canva, Google Maps, las fotos de Meta y Creative Claw. Se perdió más de una hora | Barra de título de la sesión → menú del entorno → Editar → Acceso a la red → **Completo** (no había "Limitado") |
| **Repo público o repo de imágenes público** | Meta solo sube imágenes desde un link público. Los links de un repo privado vencen en minutos, y el control de seguridad frena pasarlos a Meta ("fuga de credenciales") | Si no va a haber datos de clientes en el repo: **público desde el día 1**. Si va a haber: repo privado + repo público aparte `<línea>-imagenes` |
| **Crear el repo en GitHub lo hace Jorge** | La integración de GitHub de la sesión no puede crear repos ni cambiar su visibilidad (error 403) | github.com/new → nombre → Public/Private → Create. Darle acceso a la app de Claude si está en "repos seleccionados" |
| **Conectores encendidos al arrancar** | Los conectores se conectan al abrir la sesión. Si en ese momento la red está bloqueada, fallan y no vuelven hasta la sesión siguiente | Meta Ads (oficial), Moda (opcional), Creative Claw (opcional) |
| **Fotos reales originales** | Las capturas del celular pierden calidad y hay que recortarles los bordes negros | Mandarlas por el chat al empezar, en lo posible los archivos originales |
| **Pin de Google Maps** del lugar o del local, si corresponde | Sirve para el mapa de la presentación | Pegar el link `maps.app.goo.gl/...`: con la red completa se abre solo |

## 1. Estructura del repo (copiar de `venta-estancia` y vaciar el contenido)

| Archivo | Para qué |
|---|---|
| `CLAUDE.md` | Qué se vende, qué leer antes de actuar, lo mínimo que no se puede olvidar |
| `reglas.md` | Las reglas que no se negocian (no crear campañas sin pedido, no usar Kakau, no inventar datos, solo fotos reales…) |
| `negocio.md` | Ficha del producto con fecha de confirmación de cada dato · precio y condiciones · publicidad (cuenta, página, WhatsApp) · campañas |
| `decisiones.md` | Cada decisión con su porqué, para no volver a discutirla |
| `plan.md` | Los 10 pasos en orden y en cuál vamos |
| `memory.md` | "Estado actual" (máx. 20 líneas, se reescribe) + bitácora fechada (no se reescribe). El hook de inicio la muestra |
| `como-trabaja-jorge.md`, `comprador.md`, `interesados.md`, `respuestas.md`, `textos-anuncios.md`, `competencia.md` | Igual que acá |
| `como-crear-campana.md` | La receta del MCP de Meta con sus trampas (copiar entera: sirve igual) |
| `.claude/` | Hooks de inicio, commit y cierre · comando `/cerrar` · skills `calificar-interesado` y `crear-campana` · agente `investigador-…` |
| `fotos/` + `fotos/README.md` | Fotos reales con catálogo: qué muestra cada una y para qué se usa |
| `presentacion/` + `presentacion/fuente/` | Láminas exportadas y el código que las genera |

## 2. Orden que funcionó (los 10 pasos de `plan.md`, adaptados)

1. **Ficha:** de a 3 o 4 preguntas por vez, cada respuesta anotada con fecha. Lo que no se sabe queda como "pendiente".
2. **Papeles o condiciones** (garantía, factura, entrega, etc.).
3. **A quién se le vende:** 2 o 3 perfiles de comprador, que elige Jorge.
4. **Mercado:** el agente investigador, con fuente y fecha, y sin mezclar promedios con estimaciones.
5. **Fotos reales** → `fotos/` con catálogo.
6. **Filtro de curiosos y primera respuesta** aprobados por Jorge. Tono camba, como habla él.
7. **Página de Facebook + WhatsApp Business** conectado a la página.
8. **Textos del anuncio:** 2 o 3 versiones, Jorge elige una.
9. **Presentación + campaña en borrador** (ver 3 y 4). Se publica solo con su "publicala".
10. **Seguimiento de interesados.**

## 3. Meta Ads: la receta que quedó armada

- **Identidad:** `ads_get_ad_accounts` primero. Nunca la cuenta, la página ni el WhatsApp de Kakau.
- **Campaña:** `OUTCOME_ENGAGEMENT`, presupuesto en cada conjunto (`lifetime_budget` en centavos: 3750 = 37,50 Bs). El mínimo diario de la cuenta en BOB fue 11,95 Bs.
- **Conjuntos:** `CONVERSATIONS` → `WHATSAPP`, `promoted_object` con el `page_id`. Las ciudades van por radio con `custom_locations`, porque el MCP no busca ciudades.
  - Edad mínima mayor a 25 → `advantage_audience: 0`.
  - Solo `facebook` / `feed` si no se usa Instagram.
- **Intereses:** el MCP no tiene buscador. Los agrega Jorge en el Administrador, sobre el borrador. Nunca inventar IDs.
- **Modo borrador:** todo lo que crea el MCP queda en "draft". `ads_activate_entity` lo pone ACTIVO y empieza a gastar.
- **Formato del anuncio:**

  | Formato | Proporción | Cuándo |
  |---|---|---|
  | Imagen única | **4:5** (1080×1350), la recomendada en el feed | Una sola pieza fuerte |
  | **Carrusel** | **1:1** (1080×1080). El 4:5 en carrusel es solo para catálogo ([Meta](https://www.facebook.com/business/help/1114358518575630)) | La presentación completa, lámina por lámina |

- **Carrusel a WhatsApp (el JSON que funcionó):** `object_story_spec.link_data` con:
  - `child_attachments`: una tarjeta por lámina, con `image_hash`, `name` (máx. 40 caracteres) y `call_to_action` `{"type":"WHATSAPP_MESSAGE","value":{"app_destination":"WHATSAPP","link":"https://api.whatsapp.com/send"}}`;
  - `multi_share_optimized: false`, para que respete el orden;
  - `multi_share_end_card: false`.

  El texto principal va en `message`.
- **Subir imágenes a la cuenta:** `ads_creative_upload_media` con `upload_source: URL` y el link `raw.githubusercontent.com/<dueño>/<repo>/<commit>/<ruta>` de un repo **público**.
  - `ads_creative_upload_local_image`: "se está habilitando de a poco", no anduvo.
  - Links con `?token=` de un repo privado: los frena el control de seguridad.
- **Lo que el MCP no hace:** publicar posts comunes en la página, listarlos o pagar. La publicación sale como anuncio.
- **Vista previa:** `ads_get_ad_preview` con el `ad_id`. **No le pases el link a Jorge**: viene con `&amp;` en lugar de `&`
  y vence en minutos, así que a él no le abre. Abrilo con Chromium (Playwright), expandí "Ver más", recorré el
  carrusel y mandale las capturas (feed + todas las tarjetas) con SendUserFile.
- **Saldo:** si la cuenta es prepaga ("fondos disponibles"), **confirmar que el saldo cubra todo el presupuesto antes de
  publicar**. Con Calocha se frenó a las 2 h por falta de saldo, y ni `ads_get_errors` ni `effective_status` lo mostraban:
  pedir el campo `delivery` (`account_spend_limit_reached`).
- **Antes de publicar:** confirmar con Jorge el monto exacto, el día y la hora (la receta lo exige) y **verificar el día de
  la semana con `date`** (con Calocha se dijo "domingo 19" y el 19 era lunes). Publicar con `ads_activate_entity`
  (`object_ids` de todo + `publish_as_active`) y programar controles con `send_later`.

## 4. Imágenes: qué funcionó y qué no

| Herramienta | Resultado | Usar para |
|---|---|---|
| ✅ **HTML + Chromium del entorno** (`presentacion/fuente/laminas.py`, `laminas_cuadradas.py`, `render.js`) | Diseño exacto, fotos reales, **sin sello**, versiones 4:5 y 1:1. Se rehace en minutos | **Las láminas finales.** Copiar los scripts y cambiar textos, fotos y colores |
| ✅ Moda (conector) | Lienzo editable y **mapa real** (Mapbox). El plan gratis le pone **sello "moda.app"** a lo que exporta. El marcador del mapa siempre va al centro; `satellite` y `marker="lon,lat"` se ignoran | Borradores y el mapa (se recorta de la exportación) |
| ❌ Canva `create-design` | Mete **fotos de stock que no son del producto**: Jorge las rechazó ("es falsa"). Pasarlo a vertical desarmó el diseño y gastó una prueba Pro | No usar para piezas con producto |
| ⚠️ Canva `generate-image` | Sirve para logos. Las primeras rondas "se notan IA" y son "básicas". Funcionó: un agente investiga la identidad visual de la competencia → prompts → elegir entre varias | Logo y portada de la página, **nunca** fotos del producto |
| ❌ Imágenes del producto hechas con IA | Prohibido (`reglas.md`, regla 4). Solo fotos reales, como mucho recortadas | — |
| ⚠️ Creative Claw | No conectó porque arrancó con la red bloqueada | Probar en una sesión con la red completa desde el inicio |

**Sistema visual que gustó:**
- Paleta del logo: azul marino `#18222F`, ocre `#C8963E`, crema `#F2ECE1`.
- Títulos en Cormorant Garamond y texto en Work Sans.
- Motivo propio de la línea (acá un alambrado; para tubos, por ejemplo, una línea de tubos).
- Número de lámina "01 / 08". Foto arriba y panel abajo, o foto a pantalla completa con degradé.

**Antes de mostrarle láminas a Jorge:**
1. Recortar cada foto a la proporción de su marco (PIL) y dejar las originales en `fotos/`.
2. Pasarle los textos a un agente revisor, que los compare con `negocio.md` y las reglas.
3. Mirar cada lámina renderizada.

## 5. Cómo trabajar con Jorge (atajos)

- Quiere que **lo hagas vos**: pocas preguntas, de a 3 o 4, y tablas.
- Él aprueba textos y piezas. Nada se publica sin su "publicala".
- Prefiere Facebook antes que Instagram. Usa Excel y Outlook, no Google.
- Si algo falla por la red o los permisos, decile qué host o permiso falta y cómo habilitarlo, en pocas líneas.

## 6. Tiempos con esta receta (estimación)

| Bloque | Con Calocha | Con la receta |
|---|---|---|
| Armar el repo | ~1 h | 15 min (copiar y vaciar) |
| Ficha + perfiles + textos | ~2 h | ~1 h (las preguntas ya están) |
| Página, logo y WhatsApp | ~3 h (logos rechazados, WhatsApp compartido) | ~1 h |
| Presentación de 8 láminas | ~4 h (Canva → Moda → HTML) | ~1 h (HTML directo) |
| Campaña en borrador con carrusel | ~2 h (subida de imágenes trabada) | 20 min |
