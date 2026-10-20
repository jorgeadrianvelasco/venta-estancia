# Cómo armar una campaña por el MCP de Meta

Receta **probada en Kakau** entre el 24/9 y el 14/10/2026 (campañas de mensajes por WhatsApp). En esta línea
**todavía no se probó nada**: lo que funcione o falle acá se anota en `memory.md` y se corrige este archivo.

**Antes de nada:** `reglas.md`, regla 1. Solo se crea si Jorge lo pide, y antes de crear o activar algo que
gaste plata se le pregunta con AskUserQuestion **el monto exacto, el día y el horario**. Sin esa pregunta el
clasificador de permisos bloquea crear o activar conjuntos con presupuesto.

## Datos fijos

| | |
|---|---|
| Cuenta publicitaria | pendiente — **no la de Kakau** |
| Página de Facebook | pendiente |
| Instagram | pendiente |
| WhatsApp de destino | pendiente |
| El MCP actúa como | verificar con `ads_get_ad_accounts` antes de cada diagnóstico |

## Antes de la primera campaña de esta línea

- **Categoría especial de vivienda** (`reglas.md`, regla 5): no hace falta con público en Bolivia. Sí, si el público
  incluye EE. UU., Canadá o ciertos países de Europa.
- **Hace falta una página de Facebook**: el MCP no puede impulsar publicaciones de Marketplace. Lo que crea por API va
  con una página (`negocio.md`).
- Definir con Jorge el objetivo: mensajes por WhatsApp (lo que se usó en Kakau) u otro.

## Paso a paso (receta de Kakau)

0. **Antes del arranque:** `ads_get_ad_accounts` y mirar que la cuenta esté en `account_status: ACTIVE`. Si dice
   `UNSETTLED` (pago pendiente), la campaña no va a salir aunque todo figure ACTIVE.
1. **El post.** Buscar el ID del post de Instagram con `ads_get_ig_media`.
2. **Campaña.** `ads_create_campaign` con objetivo `OUTCOME_ENGAGEMENT`, sin presupuesto de campaña. Queda en pausa.
3. **Conjunto.** `ads_create_ad_set`:
   - `optimization_goal` CONVERSATIONS, `destination_type` WHATSAPP, `billing_event` IMPRESSIONS.
   - `promoted_object` `{"page_id":"<página>"}`.
   - `bid_strategy` LOWEST_COST_WITHOUT_CAP y `lifetime_budget` en centavos (50 Bs = 5000).
   - `start_time` y `end_time` con `-0400`. **Poner el inicio en la hora real**: una vez pasada, no se puede cambiar.
   - `targeting` con `targeting_automation.advantage_audience: 0` si se quiere que Meta respete edad e intereses.
4. **Anuncio.** `ads_create_ad` con el post:
   `{"source_instagram_media_id":"<ID>","object_id":"<página>","instagram_user_id":"<IG>","call_to_action":{"type":"WHATSAPP_MESSAGE","value":{"app_destination":"WHATSAPP","link":"https://api.whatsapp.com/send"}}}`.
5. **Activar de arriba hacia abajo:** campaña, conjunto y anuncio, con `ads_activate_entity`.
6. **Verificar** con `ads_get_ad_entities` y `ads_get_errors`. Si la lectura trae `next_actions`, correr las
   consultas que pide antes de responder.
7. **Controles** con `send_later` (hora UTC = Bolivia + 4). Anotar cada lectura en `memory.md`.

## Horario
- Franja horaria: `pacing_type ["day_parting"]` + `adset_schedule [{"start_minute":540,"end_minute":1200,"days":[2,3,4],"timezone_type":"ADVERTISER"}]`
  (0 es domingo). Solo con presupuesto total.
- **Solo horas enteras**, y de al menos una hora (12:30 fue rechazado en Kakau).

## Trampas conocidas (de Kakau)
- **El MCP no puede pagar** ni ver el saldo. Cambiar la tarjeta no salda la deuda: hay que tocar "Pagar ahora".
- **Si la entrega se corta en seco** con todo ACTIVE y `ads_get_errors` vacío: mirar `account_status` y el log de
  actividad. En Kakau la cuenta pasó a "Payment Needed" y `ads_get_errors` no lo mostró.
- **Editar la franja o la segmentación puede pausar el conjunto** (`status_forced_to_paused: true`). Mirar siempre
  esa respuesta y, si vino en true, reactivar.
- **El `targeting` se reemplaza entero**: mandar siempre todo.
- **`location_types`:** mandar `["home"]`; Meta agrega `frequently_in` solo.
- **Con presupuesto total, Meta gasta cerca de un tercio en la primera hora** y después baja el ritmo. No es una falla.
- **Fase de aprendizaje:** cada conjunto nuevo aprende desde cero y sale con unas 50 conversaciones en una semana
  ([Meta](https://www.facebook.com/business/help/112167992830700)). Con pocas consultas, no sale nunca.
- **Meta cuenta conversaciones, no interesados serios.** Esos los dice Jorge y van a `interesados.md`.

## Trampas de esta línea (venta de la estancia)
- **Subir fotos por el MCP no anda en la cuenta `64830109`** (16/10/2026): `ads_creative_upload_local_image` dice que se
  está habilitando de a poco; `ads_creative_upload_media` necesita una URL pública, y el proxy de la sesión bloquea Canva
  y `fbcdn`. Salidas: que Jorge suba la foto a la biblioteca de imágenes de la cuenta (después se lee el `image_hash` con
  `ads_get_ad_images`) o que pase el link de una publicación de la página (`object_story_id` = `1445747361945494_<postID>`).
- **Desde el 16/10/2026 el entorno tiene acceso completo a la red** (lo cambió Jorge): la subida a Moda (`agents.moda.app`)
  y los pines de Google Maps ya funcionan. Probar de nuevo `fbcdn` y Canva antes de dar algo por bloqueado.
- **Imágenes a la cuenta, lo que funciona (16/10/2026):** repo público + `ads_creative_upload_media` (`URL`) con
  `https://raw.githubusercontent.com/jorgeadrianvelasco/venta-estancia/<commit>/<ruta>`. Los links con `?token=` de un repo
  privado los frena el control de seguridad ("fuga de credenciales"): no usarlos.
- **Carrusel:** en Facebook solo 1:1 (o 9:16); 4:5 es solo para catálogo. JSON que funcionó: `link_data.child_attachments`
  (una tarjeta por lámina con `image_hash`, `name` y CTA `WHATSAPP_MESSAGE` con `app_destination: WHATSAPP` y link
  `https://api.whatsapp.com/send`), `multi_share_optimized: false`, `multi_share_end_card: false`, texto en `message`.
- **El MCP no publica ni lista las publicaciones de la página**: la "publicación" sale como anuncio.
- **El MCP no lista las publicaciones de la página**: el ID del post solo sale del link que pasa Jorge.
- **Horas:** el MCP da la hora en UTC. Bolivia = UTC − 4. No confundir "ya es 16/10" en UTC con el día en Bolivia.
- **Días de la semana: verificarlos con `TZ=America/La_Paz date -d 2026-10-18 +%A` antes de escribir "el domingo"** (16/10/2026:
  se dijo "domingo 19" cuando el 19 era lunes; Jorge lo corrigió antes de publicar).
- **Publicar un borrador:** `ads_activate_entity` con `object_ids` = campaña + conjuntos + anuncios y `publish_as_active: true`;
  devuelve PUBLISHING → confirmar con `ads_get_ad_entities` en vivo (ACTIVE / IN_PROCESS es normal antes del arranque).
- **Vista previa para Jorge (16/10/2026):** el `preview_url` de `ads_get_ad_preview` viene con `&amp;` en vez de `&` y vence
  en minutos: a Jorge no le abrió. Lo que sirvió: abrirlo con Chromium (Playwright, cambiando `&amp;` por `&`), expandir "Ver
  más", recorrer el carrusel moviendo `scrollLeft` y mandarle las capturas con SendUserFile.
- **Títulos de las tarjetas del carrusel:** en el celular se cortan a unos 10 caracteres ("530 ha…") por el botón de
  WhatsApp. En la próxima campaña, usar títulos cortos o dejar que la imagen hable.
- **La cuenta `64830109` es PREPAGA ("fondos disponibles")** (16/10/2026): la campaña arrancó y se frenó a las 2 horas con
  `delivery: off` / `account_spend_limit_reached` porque el saldo era 0,43 Bs (quedaba de 2025). `ads_get_errors` vacío y
  `effective_status: ACTIVE` **no lo muestran**: hay que pedir el campo `delivery`. **Antes de publicar**, confirmar con
  Jorge que el saldo cubra el presupuesto total (historial: `ads_account_get_activity_logs` con `event_category: budget`).
  El MCP no carga saldo: lo hace Jorge en Configuración de pagos → Fondos disponibles → Agregar fondos.
- **Recarga automática ("auto reload") no reemplaza la primera carga** (17/10/2026): carga cuando el saldo *baja* del umbral y
  necesita una tarjeta que acepte cobros recurrentes. Con el saldo ya en 0 no se disparó en 15 horas. Primero, una carga
  manual; después, la automática mantiene el saldo.
- **Alargar un conjunto con presupuesto total** (20/10/2026): Meta exige un mínimo por día contando **desde el inicio original**
  del conjunto ("Budget Is Too Low: más de X Bs"). La edición queda en borrador: leer `active_errors` de `ads_update_entity`
  antes de publicar y ofrecerle a Jorge acortar o subir el monto.
- **Reactivar una campaña vieja puede no entregar** (20/10/2026): con saldo y fechas nuevas figuraba `delivery: active`, pero
  hizo 0 impresiones en 1 h 20 min, sin errores. El creativo traía en cada tarjeta un link de WhatsApp con token que vence a
  las ~24 h (sospecha, no probado). Lo que se hizo: pausar la vieja y crear campaña, conjuntos y **anuncios nuevos** (no
  reutilizar el `creative_id` viejo). Los anuncios nuevos vuelven a pasar por la revisión de Meta.
