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
- **El MCP no lista las publicaciones de la página**: el ID del post solo sale del link que pasa Jorge.
- **Horas:** el MCP da la hora en UTC. Bolivia = UTC − 4. No confundir "ya es 16/10" en UTC con el día en Bolivia.
