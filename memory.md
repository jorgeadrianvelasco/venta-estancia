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
- **Repo = venta de estancias y terrenos de Jorge** (índice `propiedades/README.md`). **Orden fijo desde 12/11: primero la
  publicación en la página "Venta estancias", después la campaña con esa publicación** (`reglas.md` regla 1).
- **Calocha:** 530 ha, laguna Suárez, frente 800 m, a 6,6 km de Trinidad; sin ganado; **precio no se publica** (`negocio.md`).
  Tercera campaña `52544422357250` (Trinidad `52544422384650`, Santa Cruz `52544422387450`), 36 Bs c/u, 11/11 08:00 → 12/11
  23:59, WhatsApp "Estoy interesado en la estancia Calocha. Quiero más información." **Cerrada: 70,77 Bs, 9 conversaciones** (5 Trinidad, 4
  Santa Cruz; 7,86 Bs c/u, más del doble que en octubre). Interesados serios: pendiente que diga Jorge. Falta: chats del padre, lámina 3.
- **Lotes San Ignacio de Moxos** (`propiedades/lotes-san-ignacio.md`): 10 lotes de 642 a 1.641 m², esquina Av. Circunvalación
  y Av. al Aeropuerto, **desde 13 $US el m²** (lote más chico), plano aprobado. Post carrusel de 6 imágenes publicado por Jorge.
  **Campaña única `52545260604850`** (conjunto `52545260627850`): 13 Bs/día, 182 Bs, sáb 14/11 08:00 → 27/11 23:59, solo
  Facebook, San Borja 30 mi + San Ignacio 50 mi + Trinidad 25 mi, Advantage+ audiencia, intereses de Jorge; WhatsApp "Quiero más
  información de los terrenos de San Ignacio." **Falta el anuncio:** `52545260642250` en borrador; Jorge eligió (13/11) armarlo
  como **carrusel de las 6 imágenes 1:1** (hashes en la bitácora) con botón de WhatsApp en cada foto, y publicarlo antes del
  sábado 08:00. Pendiente: analizar si Advantage+ vale la pena tras unos días. Saldo ≈ 240 Bs.
- **Meta:** cuenta personal **`64830109` prepaga** (leer `delivery`); página "Venta estancias" `1445747361945494`; WhatsApp del
  padre (compartido con tubos). Sin Instagram. Nada de Kakau. Crear o activar campañas: solo con pedido expreso de Jorge.
- **Herramientas:** Canva y Moda para diseño (permisos automáticos para Canva e imágenes de Higgsfield); Higgsfield gratis: el
  upscale inventa números → nunca sobre textos o planos. **Con Jorge, solo hora de Bolivia (Santa Cruz).**
- **Repo público:** sin nombres ni teléfonos de interesados; el plano de los lotes no se sube (tiene nombres).
- **Imágenes:** Higgsfield → Moda → Canva (`guias/imagenes.md`, skill `generar-imagenes`); fotos premium: skill `fotos-premium`
  (aprobada por Jorge 13/11). Carruseles: Canva (Moda gratis pone sello). Higgsfield: 120 créditos al 13/11.

## Bitácora

Las entradas de octubre de 2026 (15 al 28/10) están en `memoria/2026-10.md`.

### 9 de noviembre de 2026 (23:50 Bolivia) — Tercera campaña armada en borrador
- **Qué se probó:** Jorge pidió otra campaña, que Claude corrija lo del Administrador y que al papá le llegue de qué anuncio es.
  Eligió 3 días, las dos ciudades, 20 Bs por día por ciudad, desde el miércoles. Se creó todo en borrador: campaña
  `52544422357250`, conjuntos `52544422384650` (Trinidad) y `52544422387450` (Santa Cruz), anuncios `52544422438250` y
  `52544422500650`, con 30-54 años (A+A apagado por edad máxima), solo celular, intereses agro iguales y el **mensaje prellenado**
  "Hola, vi en Trinidad / Santa Cruz el aviso de la estancia Calocha. Quiero más información." (receta en `como-crear-campana.md`).
- **Resultado:** Meta lo validó sin errores. No se publicó. Saldo verificado en el historial: 75,17 Bs (faltan ~45 para 120).
- **Qué aprendimos / qué cambiar:** el MCP no busca intereses aunque Jorge dé permiso: los nuevos los agrega él en el borrador.
  A la pregunta del mensaje, Jorge respondió *"le llega un simple mensaje de Hola quiero más información"*: se tomó como la
  descripción del problema y se puso el mensaje con ciudad; confirmarlo con él. Falta comprobar con el primer chat real que el
  prellenado llega bien.

### 10 de noviembre de 2026 (04:00 Bolivia) — Tercera campaña publicada
- **Qué se probó:** Jorge (desde Madrid) pidió: mensaje igual en los dos anuncios ("Estoy interesado en la estancia Calocha.
  Quiero más información."), 18 Bs por día y 2 días porque no tiene saldo, arrancar "mañana igual" (mié 11/11), y que le deje los
  pasos para agregar bienes raíces, inversión y turismo, con un recordatorio a la 1 pm de Madrid. Se cambió el creativo en el
  borrador (`ads_update_entity`), se bajó a 36 Bs por conjunto con fin el 12/11 23:59 y se publicó todo (`ads_activate_entity`).
- **Resultado:** conjuntos y anuncios publicados, en revisión (`IN_PROCESS` / `pending_process`), arranque programado. Controles:
  `trig_01FLkBTgyz7uS2PDEB7kd8xW` (recordatorio), `trig_01A5n5gWpLavrZnPEXyGTA6G`, `trig_017GiLXyuKxCwBKecNKRXJ7H`,
  `trig_01FMvfocwFTB7wAARrN8RKC6` (cierre).
- **Qué aprendimos / qué cambiar:** "18 Bs" se interpretó como por día por ciudad (72 Bs en total, entra en el saldo de 75,17).
  El nombre de la campaña dice "11 al 13 nov" pero termina el 12.
- **10/11 12:00 UTC (recordatorio de Jorge, 13:00 Madrid):** anuncios `52544422438250` y `52544422500650` **aprobados**
  (`ACTIVE`, `ad_set_scheduled`), conjuntos `ACTIVE`. Bienes raíces, inversión y turismo **todavía no** están en el `targeting`
  de ninguno de los dos conjuntos. Se le mandó notificación y los pasos.
- **10/11 (mañana, Bolivia) — intereses cargados:** Jorge, desde la app **Meta Ads Manager** del iPhone, agregó en Santa Cruz bienes
  raíces, inversión y turismo (con capturas, paso a paso). Se sacaron loteadores, corredores, tasadores, banca, etc. Claude copió
  el público de Santa Cruz a Trinidad y sacó Dairy farming y Rural area de los dos (Jorge: *"quiero darte el permiso para hacer
  las dos cosas"*). Publicado y leído de vuelta: los dos conjuntos tienen **exactamente los mismos intereses**. Arranque sin
  cambios: mié 11/11 08:00 Bolivia. Jorge: *"no me hables nunca más de horario de Madrid"*.
- **10/11 — próximo pedido de Jorge (no empezado):** campaña para **10 u 11 terrenos en San Ignacio** (no recuerda cuántos);
  solo tiene imágenes de los planos y las va a pasar. Quiere un anuncio "igual que el anterior" (a WhatsApp con mensaje propio),
  "sencillo y que no necesite mucha gente", y él dirá las ubicaciones. **Pendiente de definir:** si va en este repo o en uno
  aparte (regla 7: una línea por repo), qué San Ignacio, página y WhatsApp. El control de cierre (13/11 00:30) le avisa con
  notificación y le recuerda los planos.
- **10/11 — lotes de San Ignacio de Moxos (decidido por Jorge):** van en **este repo**, misma página "Venta estancias", mismo
  WhatsApp. Mensaje: *"Estoy interesado en los lotes de San Ignacio de Mojos. ¿Me podrías dar más información?"* (87 caracteres;
  probar tal cual). Esperando planos, cantidad de lotes, tamaños y ubicaciones. Detalle en `decisiones.md`.
- **10/11 — alcance del repo (Jorge):** venta de **estancias y terrenos en general**, no solo Calocha (CLAUDE.md, reglas 7,
  decisiones). Mensaje de reserva para los lotes si Meta corta el de 87 caracteres: *"Tengo interés en los terrenos de San
  Ignacio. Dame información."*

### 11 de noviembre de 2026
- **07:07 Bolivia (control antes del arranque):** cuenta `64830109` ACTIVE; anuncios `52544422438250` y `52544422500650` **aprobados**
  (`ACTIVE`, `ad_set_scheduled`); conjuntos ACTIVE, `scheduled`, 36 Bs c/u, del 11/11 08:00 al 12/11 23:59 (Bolivia); los dos con
  los mismos intereses (agro + bienes raíces, inversión, turismo). Saldo: sin cobros ni cargas desde el 24/10 → **75,17 Bs**,
  alcanza para 72. Todo en orden: no se le mandó notificación a Jorge.
- **09:30 Bolivia (1 h 30 después del arranque):** las dos ciudades entregando (`delivery: active`). Trinidad **2,84 Bs · 174
  impresiones · 139 personas**; Santa Cruz **1,34 Bs · 92 · 75**. Todavía 0 conversaciones (normal a esta hora). Sin aviso a Jorge.
- **14:42 Bolivia (Jorge: "dame resumen"):** Trinidad **7,81 Bs · 520 impresiones · 354 personas · 2 conversaciones (3,91 c/u)**;
  Santa Cruz **7,34 Bs · 479 · 378 · 0 conversaciones**. Total 15,15 de 72 Bs. Se le pidió confirmar si los 2 chats llegaron con
  el mensaje nuevo ("Estoy interesado en la estancia Calocha...").
- **17:39 Bolivia (Jorge: "dame un nuevo resumen"):** Trinidad **10,73 Bs · 723 · 488 personas · 2 conversaciones (5,37 c/u)**;
  Santa Cruz **11,70 Bs · 699 · 561 · 1 conversación (11,70)**. Total **22,43 de 72 Bs · 3 conversaciones**.
- **Jorge pidió empezar otra campaña de otra estancia** (en este repo; *"no solo la mía"*). Se armó `propiedades/README.md`
  (índice) y `propiedades/_plantilla.md` (ficha). Esperando qué estancia es y sus datos.
- **Lotes de San Ignacio de Moxos = la "otra campaña"** (Jorge, 11/11): son **suyos**, no es una estancia; lotes de diferentes
  dimensiones sobre la circunvalación, carretera al aeropuerto. Manda planos y letrero; fotos lindas, pocas. Mensaje de
  WhatsApp nuevo: *"Estoy interesado en los lotes de San Ignacio. Quiero más información."* Ficha: `propiedades/lotes-san-ignacio.md`.
- **Lotes de San Ignacio — material recibido (11/11):** plano aprobado por la Alcaldía (10 lotes, de 642 a 1.641 m², esquina
  Av. Circunvalación y Av. al Aeropuerto), foto del letrero y diseño digital "desde 67.000 Bs". Todo en
  `propiedades/lotes-san-ignacio.md`. El diseño quedó en `fotos/lotes-san-ignacio/`; el plano no (tiene nombres). Por confirmar
  con Jorge: precio publicado, "financiamiento con banco", servicios, lugares del público.

- **Lotes — precio corregido (11-12/11):** Jorge: *"El precio real es de desde 13 dólares el metro cuadrado. Por el más
  pequeño"*; el "67.000 Bs" del letrero y del diseño estaba mal. Pidió corregirlo **en Canva, en las dos fotos, sin cambiar
  nada más**. Se armó el diseño Canva `DAHapnjJYhI` ("Lotes San Ignacio - precio corregido"): pág. 2 = diseño digital con
  "13 $US/M2" sobre el "DESDE"; pág. 3 = foto del letrero con "13 $US / M2" en el mismo lugar; pág. 1 = fondo que Canva creó
  al abrir el archivo (la herramienta no borra páginas). Cómo se hizo: subir las fotos con `create-upload-url` (POST de bytes),
  `add_page` del tamaño exacto, `insert_fill`, parche (`insert_shape` con path) del color del fondo y `add_text`.
  **Trampa:** la transacción de edición de Canva se pierde si se reinicia la sesión; no se guarda nada hasta el `commit`.
  Ficha actualizada (`propiedades/lotes-san-ignacio.md`).
- **Lotes — fotos para el anuncio (12/11):** Jorge: las fotos estaban *"muy feas para subirlas. La única buena es la que dice
  venta de lotes. Esa no la cambies"*; pidió nitidez y color con generadores de imágenes, y que después se arme la campaña.
  Guardado en Canva `DAHapnjJYhI` (las transacciones anteriores se perdieron con los reinicios): pág. 2 = diseño con
  "13 $US/M2" (exportado a `fotos/lotes-san-ignacio/2026-11-12-diseno-venta-de-lotes-13-usd-m2.jpg`), pág. 3 = letrero mejorado
  2160×3840 con el precio nuevo (`...-letrero-mejorado-13-usd-m2.jpg`). Ambos enviados a Jorge.
  **Higgsfield (plan gratis, 10 créditos → quedan 6):** la edición con generador (`gpt_image_2_6`) **exige plan pago**; solo
  anda el `upscale_image` (2 créditos, 1 trabajo a la vez). **El upscale inventa números y letras:** en el plano cambió
  "648.19"→"643.49", "LOTE 10"→"LOTE 19", "1105.39"→"1405"; en el cartel puso "VIVIEADA" y "LBTE". Por eso: letrero = paisaje
  del upscale + cartel original (ampliado y enfocado sin IA); plano = solo ajustes de contraste/nitidez sin IA (enderezado,
  sin la pantalla del celular). El plano mejorado no va al repo (tiene nombres de personas y firmas).
- **Permisos automáticos (12/11):** Jorge: *"Quiero que todos estos permisos sean automáticos... te doy permiso"* (por el
  aviso de Canva `edit-design`). En `.claude/settings.json` → `permissions.allow`: `mcp__Canva` (todas sus herramientas) y las
  de imágenes de Higgsfield que se usan (subir, upscale, generar, esperar, saldo). **Meta Ads no se tocó**: crear o activar
  campañas sigue pidiendo confirmación y la regla 1 de `reglas.md` sigue igual.
- **Lotes — nueva forma de trabajar (12/11):** Jorge: *"a partir de ahora todo, primero lo publiquemos y después recién lo
  hagamos el meta ads y la campaña"* (anotado en `reglas.md` regla 1 y `decisiones.md`). La publicación de los lotes se hace con
  **Moda** (no Canva), inspirada en Pinterest y en letreros de urbanizaciones de Santa Cruz (dos agentes investigando →
  `investigacion/2026-11-12-*`). En Moda (plan gratis, sin kit de marca) ya están subidos el diseño
  (`file_3BWD27QQ0E847802F853C06WKP`) y el letrero mejorado (`file_0YR7D4JHJF9XGA1J1JNA5GR180`). Jorge pidió que Moda *"nos
  haga la publicación"* → `task_delegate` (gasta créditos de Moda).
- **Lotes — publicación lista (12/11, 14:45 UTC):** Moda entregó el post (2 imágenes 4:5) en el canvas
  `994ea7e4-0ac7-4164-8ea4-128019e8512d`; datos revisados; PNG en `fotos/lotes-san-ignacio/2026-11-12-publicacion-moda-*`. Se le
  mandó a Jorge con un texto propuesto. **No hay herramienta para publicar en la página desde acá** (el MCP de Meta solo crea
  anuncios): la publica Jorge y pasa el link; después, campaña con ese post.
- **Lotes — propaganda premium con Higgsfield (12/11):** Jorge contrató un plan pago de Higgsfield (*"ya me contraté el mejor
  modelo y tengo créditos"*) y pidió una propaganda *"premium"*, *"mucho mejor que las otras"*: **primera imagen = el diseño
  "Venta de lotes" con 13 $US/M2** (la que mandó), última = *"la imagen de venta de lotes"* (se toma como la foto del letrero;
  a confirmar con Jorge). Antes de gastar créditos, un agente investiga cómo trabajar mejor en Higgsfield →
  `investigacion/2026-11-12-higgsfield-como-trabajar.md`. Después: prompt y generación.
- **Higgsfield — frenado por Jorge (12/11):** *"Para al agente"* y *"Ya estoy haciendo esto en otro lugar y no quiero gastar más
  créditos"*. El agente se detuvo sin gastar: saldo **126 créditos, plan basic** (último gasto: los 2 upscales de las 13:40 UTC).
  Su investigación quedó a medias en `investigacion/2026-11-12-higgsfield-como-trabajar.md` (borrador, no seguir sin pedido).
  **No usar Higgsfield desde acá salvo pedido expreso de Jorge.**
### 12 de noviembre de 2026 — Imágenes: orden Higgsfield → Moda → Canva
- **Qué se hizo:** a pedido de Jorge se trajo de la base (`base-de-todo`) `guias/imagenes.md` (orden Higgsfield → Moda →
  Canva, reglas para gastar pocos créditos) y la skill `generar-imagenes`. En la estancia, el paso 0 dice que Higgsfield
  solo mejora las fotos reales de Calocha (resolución, encuadre, cielo, luz) y nunca agrega lo que el predio no tiene.
  `receta-repo-nuevo.md` quedó marcado como reemplazado por la base y su sección de imágenes apunta a la guía nueva.
- **Resultado:** no se generó ninguna imagen; Higgsfield sigue **sin probar**.
- **Próximo paso:** si Jorge pide fotos mejoradas para la próxima campaña, usar la skill y cotizar antes.
- **Lotes — carrusel premium (12/11):** Jorge: *"con todo lo aprendido y mergeado nuevo, hacé las imágenes"*. Se mergeó `main`
  (guía `guias/imagenes.md` + skill `generar-imagenes`) y se siguió la skill. Carrusel en `fotos/lotes-san-ignacio/carrusel/`:
  1 = diseño de Jorge sin cambios; 2 "Elegí tu lote" (plano dibujado con los 10 lotes y m²); 3 "Para vivir o para invertir"
  (números grandes); 4 foto real del letrero + "Venta directa del dueño" + WhatsApp. Texto con script
  (`presentacion/lotes-san-ignacio/`), estilo de las láminas de Calocha. **0 créditos.** Pendiente: OK de Jorge para gastar
  **2 créditos** de Higgsfield (`nano_banana_pro` 2K, modo restyle) en cielo y luz de atardecer sobre la foto real.
  Mapa de ubicación: no se hizo (Overpass/OSM bloqueado y no hay coordenadas verificadas).
- **Lotes — campaña pedida (12/11, 15:55 Bolivia):** Jorge: *"Publicalo en facebook y arma la propaganda para empezar... la misma
  segmentación... en Trinidad a 40 km y en San Ignacio de Moxos a 40 km"*. Monto: **13 Bs por día en cada ciudad, por 2 semanas**
  (= 182 Bs por ciudad, 364 Bs en total). Segmentación a copiar: la de `52544422384650` (30-54, feed FB celular, intereses agro
  + bienes raíces + inversión + turismo, empleadores y cargos; `advantage_audience: 0`). San Ignacio de Moxos: -14.99444,
  -65.64028 (Wikipedia); Trinidad -14.8333, -64.9; quedan a ~82 km, los radios de 40 km no se pisan. **Saldo: ~3 Bs** cuando
  termine Calocha (75,17 − 72) → Jorge tiene que cargar antes. **El post lo publica Jorge** (el MCP no publica en la página).
- **Lotes — imágenes, nuevo pedido (13/11):** no le gustó la 3.ª lámina ("Para vivir o para invertir"). Pide 3 prompts para
  Higgsfield y 3 opciones de imagen generada, coherentes con *"terrenos en áreas urbanas en un pueblo boliviano"*: una foto de
  San Ignacio de Moxos (para la 2.ª) y una de terrenos urbanos/rurales (para la 3.ª); él elige cuáles entran y dónde.
- **Lotes — 3 opciones con Higgsfield (13/11, ~23:30 Bolivia del 12/11):** prompts en `propiedades/lotes-san-ignacio-prompts-higgsfield.md`.
  `nano_banana_pro` 2K 4:5, cada una con una **foto real de San Ignacio de Moxos de Wikimedia Commons** (CC BY-SA 4.0: hay que
  nombrar a los autores en el post) como referencia: 1 = letras MOXOS en la plaza, 2 = el pueblo desde el aire con lotes verdes,
  3 = un lote con estacas e hilo junto a casas de ladrillo (**referencial**, no es el lote real). **6 créditos (quedan 120).**
  Primero se hizo 1 y se revisó; después 2 y 3. Las tres salieron bien a la primera. Esperando que Jorge elija.
- **Lotes — carrusel final (13/11):** Jorge aprobó las fotos de Higgsfield (*"ahora sí me gusta... quedó perfecto"*) y pidió
  guardar la forma de trabajo como skill → **`.claude/skills/fotos-premium/`** (Higgsfield, `nano_banana_pro`, foto real de
  referencia de Wikimedia o de Jorge, prompt por secciones, de a una imagen). Carrusel armado **en Canva** (Moda gratis pone un
  sello "moda.app"; lo tiene también el post de Moda del 12/11), diseño `DAHaxI4fAd0`, sin gastar créditos de Higgsfield. Orden
  de Jorge: 1 diseño "Venta de lotes" · 2 MOXOS · 3 "Elegí tu lote" · 4 pueblo desde el aire · 5 lote urbano-rural
  ("Imagen referencial") · 6 "Para vivir o para invertir" con la foto aérea arriba (antes tenía la foto fea del letrero).
  Archivos: `fotos/lotes-san-ignacio/carrusel-final/`. Falta: Jorge lo publica en la página y pasa el link; cargar saldo (364 Bs).
- **Calocha — cierre de la tercera campaña (13/11, 00:30 Bolivia):** Trinidad 35,21 Bs, 2.268 impresiones, 1.155 personas,
  **5 conversaciones (7,04 Bs c/u)**; Santa Cruz 35,56 Bs, 1.603 impresiones, 1.133 personas, **4 (8,89 c/u)**. Total **70,77 de
  72 Bs, 9 conversaciones, 7,86 Bs c/u**. Comparación: 20-22/10 → 74,81 Bs, 22 conversaciones, 3,40 c/u; boost 2025 → 20,57 Bs, 6,
  3,43 c/u. Esta vez el costo por conversación fue **más del doble**: público más chico (30-54, solo celular) y más intereses
  (bienes raíces, inversión, turismo). Lo que importa sigue sin saberse: **cuántos son serios** y si el WhatsApp llegó con el
  mensaje de Calocha. Se le avisó a Jorge con PushNotification. Saldo restante ≈ 75,17 − 70,77 ≈ **4,4 Bs**.
- **Lotes — promoción publicada sin querer y pausada (13/11):** Jorge publicó el carrusel en la página y sin querer lo
  promocionó: campaña `52545259104250` ("Post: ¿Y vos ya tenés tu lote?"), conjunto `52545259109850`, a WhatsApp,
  **38 Bs por día**, sin fecha de fin, 18-65, San Borja 30 mi + San Ignacio 50 mi + Trinidad 25 mi, todas las ubicaciones
  (FB, IG, Audience Network, WhatsApp), Advantage+ prendido. **Gasto 0 Bs** (no había saldo, `no_ads`). La pausé a pedido de
  Jorge (*"Paralo"*). Él quiere poner la segmentación y bajar el monto. Falta el link/ID del post para armar la buena.
- **Lotes — campaña nueva en BORRADOR (13/11, ~00:50 Bolivia):** Jorge: *"Crealo vos todo a partir de la publicación"*, 13 Bs/día
  total, 2 semanas desde sáb 14/11 08:00. Post `1445747361945494_122116283907511431`. Campaña `52545260604850` (OUTCOME_ENGAGEMENT),
  conjunto `52545260627850` (CONVERSATIONS → WhatsApp, **182 Bs total** = 13×14, 14/11 08:00 → vie 27/11 23:59 −04:00, 30-54, feed FB
  celular, intereses de Calocha, `advantage_audience 0`, ubicaciones de Jorge: San Borja 30 mi, San Ignacio de Moxos 50 mi,
  Trinidad 25 mi). Anuncio `52545260642250` con el post y WhatsApp prellenado **"Quiero más información de los terrenos de San
  Ignacio."** (Jorge lo pidió así). **Trampa:** reusar el `creative_id` del boost (`1214082897934692`) dio "Page Post Can't Be
  Used"; con `object_story_id` + CTA + `page_welcome_message` inline quedó sin errores. La promoción vieja `52545259104250` sigue
  pausada. **Falta:** que Jorge cargue 182 Bs y diga "publicala" → `ads_activate_entity`.
- **Lotes — publicada (13/11):** Jorge: *"Publicalo"*. Campaña `52545260604850` y conjunto `52545260627850` publicados (arranca sáb
  14/11 08:00, termina vie 27/11 23:59, 182 Bs). Después Jorge pidió *"que solo se vea en Facebook"* → `publisher_platforms:
  ["facebook"]` (todas las ubicaciones de FB, celular y computadora), publicado. Jorge dejó Advantage+ audiencia prendido (edad
  30-54 como sugerencia) y cambió intereses: Small business, House, Family, Investor, Recently moved + bienes raíces/inversión/
  turismo + Livestock, empleadores y Farmer. **El anuncio `52545260642250` quedó en borrador** (el primer publish no lo incluyó;
  el segundo lo frenó el permiso automático): hay que publicarlo con el OK de Jorge. Saldo ≈ 240 Bs (cargó 236 Bs el 12/11).
- **Lotes — una sola campaña (13/11):** Jorge: *"borrá la de 38 Bs el día. Esa no sirve"* → campaña `52545259104250` **DELETED**
  (0 Bs gastados). **La única campaña de los lotes es `52545260604850`** (13 Bs/día, 182 Bs, 14 al 27/11, solo Facebook, ubicaciones
  y segmentación de Jorge, WhatsApp "Quiero más información de los terrenos de San Ignacio."). **El anuncio `52545260642250` sigue
  en borrador: Jorge dijo "todavía no"** a publicarlo. **Pedido de Jorge:** si Advantage+ audiencia gasta más de lo normal, analizar
  si vale la pena tenerlo (comparar costo por conversación contra Calocha: 3,40 Bs en oct, 7,86 en nov).
- **Lotes — el anuncio NO se pudo publicar (13/11, madrugada):** Jorge dijo *"publicá y mergeá"*. PR #6 mergeado a `main`. El anuncio
  `52545260642250` falla al publicar: con `object_story_id` (+ `object_id`) da **"Post not owned by ad's Page"** (error 3858759) y
  con el `creative_id` del boost borrado (`1214082897934692`) da **"Page Post Can't Be Used"** (1487472). El post es una publicación
  de varias fotos (`1445747361945494_122116283907511431`). Campaña y conjunto publicados, pero sin anuncio no entrega (`no_ads`).
  Dato: el boost que hizo Jorge tenía mensaje prellenado "¿Cuál es el precio total de cada lote?". Salidas: (a) armar el anuncio
  como carrusel con las 6 imágenes del repo y el mismo texto (no es "el post", pero se ve igual y cada foto lleva botón de
  WhatsApp); (b) que Jorge use "Usar publicación existente" en el Administrador. Esperando decisión de Jorge.

### 13 de noviembre de 2026 — Anuncio de los lotes como carrusel (opción A)
- Jorge: *"Hacé la A entonces"* → anuncio = carrusel con las 6 imágenes del post en 1:1 (`fotos/lotes-san-ignacio/carrusel-anuncio-1x1/`,
  commit `da15c5a`), cada tarjeta con botón WhatsApp y mensaje prellenado "Quiero más información de los terrenos de San Ignacio."
  Texto = el del post (con créditos de Wikimedia). Títulos de tarjeta: Venta de lotes · San Ignacio · Elegí tu lote · El pueblo ·
  Tu lote · 13 $US el m².
- Imágenes subidas a la cuenta `64830109` (hashes, en orden): `73856ab57f733b6b1a6cd965f27e9955`, `5b6047f86832937a6b626264e061ef69`,
  `43db03c9b6c6f38d137b954ff307ff9c`, `a72d2a58307a094251112adee33d6ca7`, `ee88ca7326f2a583123e658d0cddf19f`,
  `8109bbf19f54f2fa30503b18588d6274`.
- **No se pudo cargar el carrusel en el anuncio `52545260642250`**: el conector de Meta Ads se cayó (timeout) a mitad de la tarea.
  Siguiente paso al volver: `ads_update_entity` del anuncio con `object_story_spec.link_data.child_attachments` (6 tarjetas,
  CTA `WHATSAPP_MESSAGE`, `multi_share_optimized:false`, `multi_share_end_card:false`, `page_welcome_message`), revisar
  `active_errors` y publicar (`ads_activate_entity`, Jorge ya dio el OK: "publicá" + "Hacé la A").
- Memoria: entradas de octubre movidas a `memoria/2026-10.md`.

- **Conector de Meta Ads borrado por Jorge (13/11)** porque fallaba. Para volver a agregarlo: claude.ai → Configuración →
  Conectores → "Agregar conector personalizado", nombre "Meta Ads", URL **`https://mcp.facebook.com/ads`** (MCP oficial de Meta,
  beta desde el 29/04/2026), iniciar sesión con Facebook y tildar la cuenta `64830109` y la página "Venta estancias" sin
  destildar las demás. Después hace falta abrir una **sesión nueva** (los conectores se cargan al empezar la sesión).
