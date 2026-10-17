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
- **Estancia:** Calocha, **530 ha tituladas** (500 de arrocillo natural, 30 de monte), predio **urbano** de gran
  extensión en Cercado, sobre la laguna Suárez (**800 m colindantes + 1,3 km a 10 m de la orilla**), a 6,6 km de
  Trinidad, 600 m de la carretera a Loreto, acceso todo el año. Alambrado perimetral, 4 pozas, corral con brete,
  corralón, casa (motor, agua de lluvia). **Se vende sin ganado; todo lo demás queda.** La franja de 10 m es de un
  vecino: **frente propio = 800 m.** Pago negociable, sin intermediario. **Dueño y quien decide el precio: Jorge.**
- **Objetivo (Jorge):** compradores serios de estancias, no curiosos. **El precio no se publica** (`decisiones.md`).
- **Aviso anterior:** boost de Marketplace del 17 al 20/10/2025 (cuenta personal `64830109`): 20,57 Bs, 6
  conversaciones, ninguna seria: "preguntan el precio y se van" (`textos-anuncios.md`).
- **Meta:** cuenta publicitaria **personal de Jorge, `64830109`** (no se mueve al portfolio). Página **"Venta
  estancias" (`1445747361945494`)** en el portfolio "Jorge Velasco". WhatsApp del **padre de Jorge** (compartido con
  tubos) **conectado**: el borrador lo muestra (15/10/2026). Sin Instagram.
- **Categoría especial de vivienda:** no hace falta para un público en Bolivia (`reglas.md`, regla 5).
- **Plan (`plan.md`):** pasos 1, 3, 5, 6 y 8 hechos (texto **V1** aprobado, logo **B2**); 2 lo maneja Jorge en persona;
  4 a medias (sin comparables); 7 casi listo (página, logo, portada, primera publicación y WhatsApp).
- **Paso 9 — CAMPAÑA PUBLICADA (15/10 22:00 Bolivia, "publicala" de Jorge)** `52537356511050`, cuenta `64830109`: conjuntos
  **Trinidad** `52537356525250` (40 km) y **Santa Cruz** `52537356542650` (80 km), 30-65+, feed de Facebook, **37,50 Bs c/u
  (75 Bs total)**, a WhatsApp, intereses agro. **Corre del viernes 16/10 08:00 al domingo 18/10 23:59** (hora de Bolivia).
- **Anuncios:** carrusel de las **8 láminas cuadradas** + texto V1 + botón de WhatsApp (Trinidad `52537366868250`, Santa Cruz
  `52537366894650`). **Controles** (send_later): 16/10 07:30 ✅, 09:30 ✅, 17/10 09:00 ✅ y 12:00 ✅ (sin saldo), queda 19/10 00:30.
- **⚠️ FRENADA DESDE ~10:00 DEL 16/10: SIN SALDO.** La cuenta `64830109` es **prepaga (fondos disponibles)**: tenía 21 Bs
  cargados en 2025, se gastaron 20,57 en el boost y los 0,43 que quedaban hoy. Jorge tiene que **agregar fondos** (75 Bs);
  el MCP no puede. Al cargar, los anuncios vuelven solos. Jorge cambió de idea: **lo hace hoy 16/10** (13:55). Link de pagos: `business.facebook.com/billing_hub/payment_settings/?asset_id=64830109`.
- **Repo público** (decisión de Jorge): nada de nombres ni teléfonos de interesados acá. Receta para otras líneas:
  `receta-repo-nuevo.md`. Construir sí, lotear no. **Tono: camba, firmado como el dueño.** Ojo: **el domingo es 18**.

## Bitácora

Las entradas del 15/10 hasta el carrusel cuadrado están en `memoria/2026-10.md`.

### 16 de octubre de 2026 — Repo público, carrusel en el borrador y receta para los tubos
- **Jorge** hizo público el repo ("si no hay contraseñas, no me importa"). Revisión del historial: sin claves. Decisión en
  `decisiones.md`: nada de datos de interesados mientras sea público.
- **Imágenes 1:1 subidas** con links `raw` públicos (commit `9556392`): hashes `62729c9ddcf3802e744fbf4b3ad4935c`,
  `cc2a2037a5eb16b994c3ca8f51706ba5`, `2ed6f1bbb042f77123f325cbc9e30a05`, `013bd8363b9ca07aef4ad0ffa2e85526`,
  `a088bbd2b25bf1d90ddebdfe7fc9882e`, `32f760a91e1db011d99a7f14a34da94c`, `c9eb640bf12989dc6d82cfda00b753df`,
  `a951e14d75d3a1fb00b1dbe35753d153` (en orden 01 a 08).
- **Anuncios creados en borrador, sin errores:** Trinidad `52537366868250`, Santa Cruz `52537366894650`. Carrusel en orden
  fijo, sin tarjeta final, texto V1, CTA WhatsApp. Vista previa generada con `ads_get_ad_preview`.
- **Receta para el próximo repo** (pedido de Jorge, para los tubos): `receta-repo-nuevo.md`.
- **Pendiente:** "publicala" → activar la campaña. Después: controles (antes del arranque, 1,5 h después, al cierre).

### 16 de octubre de 2026 (21:50 en Bolivia) — Revisión del borrador y búsqueda de "la otra" publicación
- **PR [#2](https://github.com/jorgeadrianvelasco/venta-estancia/pull/2) mergeado a `main`** (pedido de Jorge). La rama se
  rehízo desde `main` para seguir.
- **Jorge:** "revisá la publicación, la campaña y sobre todo pausá la otra. No quiero gastar en otra publicación que está mala".
- **Cuenta `64830109`:** **nada gastando**. Lo único publicado es el boost de Marketplace de 2025 (`6836819733446`, PAUSED,
  0 Bs en 7 días). Registro de actividad vacío. Cuentas visibles: `64830109` y Kakau (regla 2: no se toca sin pedido expreso).
- **Si Jorge impulsó su publicación desde la página**, ese gasto no está en `64830109`: o no hay gasto (post orgánico) o se pagó
  con otra cuenta. Se le preguntó.
- **Borrador revisado:** campaña, 2 conjuntos y 2 anuncios **VALIDATED, sin errores**. WhatsApp +591 7139…629. Se corrigió
  el nombre del conjunto de Santa Cruz a **"80 km"** (decía 30). Intereses solo agro (cubren perfil C; B y D no).

### 16 de octubre de 2026 (22:00 del 15/10 en Bolivia) — Campaña publicada
- **Jorge:** "Publicala". Al confirmar monto y fechas corrigió: **"el domingo es 18"**. Error mío: yo venía diciendo
  "domingo 19" (el 19 es lunes) y había dejado los conjuntos cerrando el lunes 19 08:00. Jorge eligió **cierre domingo
  18/10 23:59**.
- **Hecho:** `end_time` de los dos conjuntos → `2026-10-18T23:59:00-0400`; `ads_activate_entity` con la campaña, los 2
  conjuntos y los 2 anuncios (`publish_as_active`) → PUBLISHING → lectura en vivo: campaña **ACTIVE**, conjuntos y anuncios
  **ACTIVE / IN_PROCESS** (revisión y arranque programado), inicio 16/10 08:00 y fin 18/10 23:59 (Bolivia), 37,50 Bs c/u.
  `ads_get_errors` vacío.
- **Controles** (send_later, triggers `trig_01F6RG5Zfz3xmYAAATTX11LB`, `trig_0154BhvtVMg25kT4Wt6j6AUv`,
  `trig_01TcGXhtnhi9qFFSwam94sWn`, `trig_01RCZVyx3aFaxoyoQ8ELGYoE`).
- **Bitácora vieja** movida a `memoria/2026-10.md`.

- **Aprobados por Meta (15/10 23:41 Bolivia):** los 2 anuncios pasaron de PENDING_REVIEW a **ACTIVE**. Empiezan a mostrarse el
  16/10 a las 08:00, que es cuando arrancan los conjuntos. Jorge (27 años) queda fuera del público de 30 a 65+, así que
  puede no verlo en su feed: para verlo, que use la vista previa o el Administrador de anuncios.
- **Vista previa (16/10, 00:00 Bolivia):** a Jorge no le abría el link de la vista previa (`&amp;` y vencimiento). Se le
  mandaron capturas reales de la vista previa de Meta (feed + las 8 tarjetas). Detalle anotado: los títulos de las tarjetas
  se cortan en el celular ("530 ha…"); no se tocó para no reabrir la revisión de Meta antes del arranque.
- **Control 1 (16/10 07:30 Bolivia):** campaña, 2 conjuntos y 2 anuncios **ACTIVE** (aprobados). `ads_get_errors` vacío.
  Cuenta `64830109` **ACTIVE** y con medio de pago. Arranca a las 08:00. Próximo control: 09:30.
- **Control 2 (16/10 09:30 Bolivia, 1,5 h de campaña):** Trinidad 0,34 Bs · 27 impresiones · 22 personas · 0 conversaciones.
  **Santa Cruz 0 Bs · 0 impresiones**, ACTIVE y sin errores; el público (80 km, 30-65+, intereses agro) está bien armado.
  El gasto va más lento de lo esperado (no se cumplió lo de "un tercio en la primera hora"). Se programó un control extra
  a las 13:00 (`trig_01Qo7nmBDZAYNz9L5nxhPG47`) para ver si Santa Cruz arranca. No se cambió nada.
- **Diagnóstico Santa Cruz (16/10 11:00 Bolivia, pedido de Jorge "hacelo funcionar"):** no era Santa Cruz. Los 2 conjuntos
  y los 2 anuncios tienen `delivery: off` con `account_spend_limit_reached`. Historial de pagos de la cuenta: **17/10/2025
  se cargaron 21,00 Bs de saldo prepago**; cobros 18 al 21/10/2025 = 1,68 + 7,96 + 5,84 + 5,09 = 20,57 Bs (el boost de
  Marketplace). Quedaban **0,43 Bs**, y Trinidad gastó exactamente 0,43 Bs hoy. Gasto total histórico de la cuenta: 21 Bs.
  **La cuenta se quedó sin fondos.** Arreglo: Jorge agrega fondos (Configuración de pagos → Fondos disponibles → Agregar
  fondos). El MCP no tiene herramienta de pagos. No se cambió nada de la campaña.
- **Saldo, para mañana (16/10 12:18 Bolivia):** Jorge, desde el celular: "lo hacemos mañana". Se borró el control extra de
  las 13:00 (ya se sabía la causa), se programó un recordatorio el **sábado 17 a las 09:00** (`trig_01BmzGuYTM4TX7QZGUukHW8w`)
  y se cambió el control de las 12:00 (`trig_01TcGXhtnhi9qFFSwam94sWn`) para que primero mire si ya hay saldo. Pendiente
  ofrecerle correr el cierre al lunes 19 para compensar el día perdido (no se cambia sin su sí).
- **Carga de saldo (16/10 14:07 Bolivia):** Jorge: "ya cargué los 75 Bs". En el historial de la cuenta **no aparece la carga**:
  el único movimiento de hoy es "Payment method removed — Credit card" (Jorge, 14:06 Bolivia). Los 2 conjuntos siguen con
  `delivery: off` / `account_spend_limit_reached`. Puede ser demora de Meta (hasta ~15 min) o que el pago no se completó.
  Re-chequeo programado a las 14:28 (`trig_01JhtNy92bMVmwmexHCG69jL`). Ojo: el historial usa la hora de la cuenta
  (Pacífico, UTC−7): 11:06 AM = 14:06 Bolivia.
- **Re-chequeo del saldo (16/10 14:28 Bolivia):** sigue **sin carga** en la cuenta `64830109`: el historial solo tiene
  "Payment method removed — Credit card" (14:06). Conjuntos con `delivery: off` / `account_spend_limit_reached`, 0,43 Bs y
  38 impresiones en el día (sin cambios). Se le pidió a Jorge una captura de "Fondos disponibles" y que confirme que la carga
  la hizo en la cuenta 64830109 y no en la de Kakau (esa no se revisa: regla 2).
- **Control 18:48 (16/10 Bolivia):** Jorge: "ya está todo hecho". **La carga sigue sin aparecer** en `64830109` (4 h y media
  después). Historial: solo la tarjeta eliminada a las 14:06. Conjuntos `delivery: off` / `account_spend_limit_reached`.
  Hipótesis: carga hecha en otra cuenta (¿Kakau?), pago pendiente (medio local o banco) o pago que no pasó. Se le ofreció
  mirar **solo el historial de pagos de Kakau, sin tocar nada**, únicamente si él lo pide (regla 2).
- **Sábado 17/10 05:46 Bolivia:** Jorge: "actívala de nuevo, no tiene fondos pero tiene refill auto funds". Campaña, conjuntos y
  anuncios ya están en **ACTIVE**: no hay nada que activar. Siguen con `delivery: off` / `account_spend_limit_reached` y
  **ningún cobro ni carga en el historial** desde el 16/10 (solo la tarjeta eliminada a las 14:06). Según Meta, la recarga
  automática carga cuando el saldo **baja** del umbral y necesita una tarjeta que acepte cobros recurrentes. Con el saldo ya
  en 0 no se disparó: hace falta **una carga manual** (Agregar fondos). No se tocó nada de la campaña.
- **Recordatorio 09:00 (sábado 17/10 Bolivia):** sigue **frenada**: `delivery: off` / `account_spend_limit_reached`, 0 Bs hoy y
  ningún movimiento nuevo en el historial (solo la tarjeta eliminada el 16/10 14:06). A las ~05:50 se le pasaron a Jorge los pasos
  para cargar desde el celular (navegador con el link, o app Meta Ads Manager). Se le recordó y se le volvió a ofrecer correr
  el cierre. Le quedan ~39 h si no se cambia.
- **Control 3 (sábado 17/10 12:00 Bolivia):** sigue **frenada sin saldo** (`delivery: off` / `account_spend_limit_reached`, 0 Bs
  hoy). Único movimiento nuevo: "Account billed" 0,43 Bs (17/10 09:12 Bolivia), el descuento de lo gastado el viernes.
  **Ninguna carga de fondos.** Se le recordó a Jorge en dos líneas. Quedan ~36 h hasta el cierre del domingo 23:59.
