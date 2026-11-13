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
  23:59, WhatsApp "Estoy interesado en la estancia Calocha. Quiero más información." Al 11/11 17:39: 22,43 Bs, 3 conversaciones.
  Cierre programado 13/11 00:30 Bolivia. Interesados serios: 0. Falta: chats del padre, lámina 3.
- **Lotes San Ignacio de Moxos** (`propiedades/lotes-san-ignacio.md`): 10 lotes de 642 a 1.641 m², esquina Av. Circunvalación
  y Av. al Aeropuerto, **desde 13 $US el m²** (lote más chico), plano aprobado. WhatsApp: "Estoy interesado en los lotes de San
  Ignacio. Quiero más información." Fotos listas (`fotos/lotes-san-ignacio/2026-11-12-*`). **Publicación lista (Moda, 2 imágenes)**
  (`propiedades/lotes-san-ignacio-publicacion.md`); falta: Jorge la publica en la página y pasa el link → campaña con ese post. Pendiente:
  lugares del público, monto, días; agua/luz/financiamiento sin confirmar (no se prometen).
- **Meta:** cuenta personal **`64830109` prepaga** (leer `delivery`); página "Venta estancias" `1445747361945494`; WhatsApp del
  padre (compartido con tubos). Sin Instagram. Nada de Kakau. Crear o activar campañas: solo con pedido expreso de Jorge.
- **Herramientas:** Canva y Moda para diseño (permisos automáticos para Canva e imágenes de Higgsfield); Higgsfield gratis: el
  upscale inventa números → nunca sobre textos o planos. **Con Jorge, solo hora de Bolivia (Santa Cruz).**
- **Repo público:** sin nombres ni teléfonos de interesados; el plano de los lotes no se sube (tiene nombres).
- **Imágenes (12/11):** orden Higgsfield → Moda → Canva, solo mejorando fotos reales y cotizando antes (`guias/imagenes.md`,
  skill `generar-imagenes`).

## Bitácora

Las entradas del 15 al 20/10/2026 están en `memoria/2026-10.md`.

### 21 de octubre de 2026
- **05:21 (resumen pedido por Jorge):** Trinidad **13,80 Bs · 642 impresiones · 404 personas · 10 conversaciones · 1,38 Bs c/u**.
  Santa Cruz **8,77 Bs · 506 impresiones · 430 personas · 0 conversaciones**. Total 22,57 de 75 Bs. Se le propuso (sin tocar
  nada) pasar lo que le queda a Santa Cruz a Trinidad. Siguen sin aparecer los chats para calificar.
- **08:25:** Trinidad **16,94 Bs · 775 impresiones · 465 personas · 10 conversaciones (1,69 c/u)**, sin conversaciones nuevas
  desde las 05:21 (madrugada). Santa Cruz **9,12 Bs · 538 · 446 · 1 conversación (9,12 c/u)**. Total 26,06 de 75 Bs,
  11 conversaciones. Sigue en pie la propuesta de pasar lo que queda de Santa Cruz a Trinidad, y los chats sin calificar.
- **Decisión de Jorge (21/10 ~08:30):** **Santa Cruz sigue** ("los compradores más serios deben ser los de Santa Cruz").
  No se pausa ni se mueve presupuesto. Anotado en `decisiones.md`. Para juzgar Santa Cruz importan los interesados serios,
  no el costo por conversación: falta saber de qué ciudad es cada chat.
- **11:10:** Trinidad **19,35 Bs · 892 · 512 personas · 11 conversaciones (1,76 c/u)**. Santa Cruz **10,49 Bs · 604 · 473 ·
  2 conversaciones (5,25 c/u)**. Total **29,84 de 75 Bs · 13 conversaciones**. Siguen sin pasar los chats.
- **Control 2 (12:00, mitad):** Trinidad **19,84 Bs · 922 · 529 personas · 11 conversaciones (1,80 c/u)**. Santa Cruz **10,64 Bs
  · 621 · 484 · 3 conversaciones (3,55 c/u)**: su costo por conversación bajó de 9,12 (08:25) a 3,55. Total **30,48 de 75 Bs ·
  14 conversaciones**. Siguen sin pasar los chats; se le volvió a pedir a Jorge, con la ciudad de cada uno.
- **15:35:** Trinidad **22,57 Bs · 1.067 · 593 personas · 12 conversaciones (1,88 c/u)**. Santa Cruz **12,93 Bs · 751 · 567 ·
  3 conversaciones (4,31 c/u)**. Total **35,50 de 75 Bs · 15 conversaciones**. Chats sin pasar.

### 22 de octubre de 2026

- **06:02:** Trinidad **27,93 Bs · 1.424 · 749 personas · 12 conversaciones (2,33 c/u)**: gastó 5,36 Bs desde las 15:35 del 21
  sin conversaciones nuevas. Santa Cruz **19,32 Bs · 1.164 · 841 · 4 conversaciones (4,83 c/u)**: una nueva. Total **47,25 de
  75 Bs · 16 conversaciones (2,95 c/u)**. Quedan 27,75 Bs hasta las 23:59 de hoy (Trinidad 9,57, Santa Cruz 18,18). Chats sin pasar.
- **17:43:** Trinidad **33,66 Bs · 1.858 · 906 personas · 13 conversaciones (2,59 c/u)**: +1 desde las 06:02. Santa Cruz
  **32,35 Bs · 1.648 · 1.124 · 7 conversaciones (4,62 c/u)**: +3; hoy aceleró (13,03 Bs en el día, más que Trinidad). Total
  **66,01 de 75 Bs · 20 conversaciones (3,30 c/u)**. Quedan 8,99 Bs hasta las 23:59 (Trinidad 3,84, Santa Cruz 5,15). Chats sin pasar.
- **Cierre (23/10 00:30, control automático):** la campaña terminó a las 23:59 del 22/10 (`completed`). Totales del 20 al 22/10:
  Trinidad **37,40 Bs · 2.322 · 1.133 personas · 13 conversaciones (2,88 c/u)**; Santa Cruz **37,39 Bs · 1.994 · 1.345 · 9
  conversaciones (4,15 c/u)**: +2 desde las 17:43. Total **74,79 de 75 Bs · 4.316 impresiones · 22 conversaciones (3,40 c/u)**.
  Contra el boost de 2025 (20,57 Bs, 6 conversaciones, 3,43 c/u, 0 serios): 3,6 veces más conversaciones con el mismo costo
  por conversación. Contra la primera campaña (0,43 Bs, 38 impresiones): esa no se pudo medir. Serios y visitas: **pendiente**,
  se le pidió a Jorge. Anotado en `negocio.md`, `textos-anuncios.md` y `plan.md`. No se creó ni se activó nada.

### 23 de octubre de 2026

- **09:22 (Jorge: "dame resumen, decime cuándo acaba"):** la campaña ya había terminado (jueves 22/10 23:59). Meta ajustó un poco
  las cifras desde las 00:30: Santa Cruz **37,41 Bs · 2.003 impresiones** (antes 37,39 · 1.994), Trinidad **2.327 impresiones**
  (antes 2.322). Conversaciones sin cambio: **22 (13 + 9)**. Total final **74,81 Bs, 3,40 c/u**. No hay nada corriendo en la
  cuenta: la campaña vieja sigue pausada. Se actualizaron `negocio.md`, `textos-anuncios.md` y `plan.md`. Los chats siguen sin pasar.

### 24 de octubre de 2026 — Balance de la campaña y el problema del WhatsApp

- **Jorge:** al padre le llega solo "Hola, quiero más información", sin la imagen ni saber qué preguntan; y **"no hubo ningún
  interesado muy interesado"**. Pregunta si el público no fue el ideal o si faltó encontrar a la persona.
- **Causa del mensaje genérico (verificado en lo que se creó):** los anuncios se armaron con CTA `WHATSAPP_MESSAGE` y link
  `api.whatsapp.com/send`, **sin mensaje prellenado propio**, así que salió el texto por defecto de Meta. `decisiones.md` pedía
  uno que diga "Calocha" y se pasó por alto. No se pudo confirmar con fuente oficial si la app WhatsApp Business muestra la
  tarjeta del anuncio en el chat. Arreglo: prellenado por conjunto (producto + ciudad), anotado en `como-crear-campana.md` y
  `receta-repo-nuevo.md`.
- **Público que corrió (leído en `targeting`):** 30-65, feed de Facebook, Trinidad 40 km y Santa Cruz 80 km, `home`, `recent`
  y `frequently_in`; intereses **solo agro**: Agribusiness, Milk, Dairy, Cattle, Livestock, Farm, Agriculture, Agronomy, Rural
  area, Cattle feeding + empleador Agriculture. **Faltaron bienes raíces, inversión y turismo rural** (perfiles B y D del plan).
- **Lo bueno:** el sistema funciona de punta a punta (anuncio aprobado, las dos ciudades entregaron, el WhatsApp recibió); 22
  conversaciones a 3,40 Bs, 3,6 veces más que en 2025 por el mismo costo; el carrusel y el texto V1 quedan para reusar.
- **Lo malo:** sin prellenado no se sabe de qué ciudad ni qué preguntó cada uno; público solo agro (llega a quien trabaja con
  ganado, no a quien tiene capital para comprar); el objetivo "conversaciones" busca a quien escribe, no a quien compra; los
  chats no se calificaron, así que no hubo forma de ajustar durante la campaña; se perdieron 4 días (16-20/10) por el saldo.
- **Propuesto a Jorge (no creado):** prellenado por conjunto; público con bienes raíces e inversión además de agro; probar
  un formulario de "mayor intención" con preguntas de filtro o volver a mostrarle el anuncio a quien ya interactuó;
  anotar cada chat en Excel (ciudad, qué preguntó, perfil). Esperando su decisión.
- **Análisis a fondo (24/10, agente pedido por Jorge; `analisis/campana-20-22-oct-2026.md`):** 5 hallazgos. (1) **Trinidad se agotó
  el primer día:** 10 de 13 conversaciones el mar 20 (13,78 Bs, 1,38 c/u); mié y jue, 23,62 Bs por 3 (7,87 c/u). (2) **Santa Cruz
  mejoró cada día** (0 → 4 → 5) y sus charlas fueron más largas: 2.º mensaje en 5 de 9 (Trinidad, 4 de 13). (3) **Horas:** la tarde,
  de 12 a 18, dio 12 de 22 conversaciones a 2,71 c/u; la noche, de 18 a 24, 25,26 Bs por 5 (5,05 c/u, muchos clics sin mensaje);
  la madrugada casi no gastó (3,18 Bs de 00 a 07). 21,03 Bs (28 %) cayeron en horas sin ninguna conversación. (4) **Los públicos
  no eran iguales:** Santa Cruz tenía cargos "Farmer" y "Farm Owner Operator" y Ganado de carne; Trinidad, Leche, Lácteos y Zona
  rural. Ninguno tenía bienes raíces ni inversión. (5) **Puja automática** ("mayor volumen", se paga por impresión): CPM de 16,05 Bs
  en Trinidad y 18,65 en Santa Cruz; contra 2025, 18,6 % de los clics al botón terminó en conversación (2025: 1,9 %). Cifras finales:
  74,83 Bs. No disponible: clics por lámina, rankings de calidad y comparación con otros anunciantes.

### 25 de octubre de 2026

- **Jorge aprobó el análisis y anotó cambios para la próxima campaña:** *"aumentar bienes raíces e inversión, también turismo,
  agronomía y otras cosas más. Saca a los de 55 años. Quiero que el mensaje de WhatsApp diga sobre qué anuncio están hablando.
  Está bien lo otro que investigaste."* Anotado en `decisiones.md`, `analisis/` (sección 10), `comprador.md` y `plan.md`. No se
  creó nada. Pidió PR y merge de todo a `main`.

### 28 de octubre de 2026 — Cierre de la etapa de octubre
- **Qué se probó:** la campaña del 20 al 22/10 hasta el final (lecturas cada vez que Jorge pidió "dame resumen" y control de
  cierre automático); balance; análisis a fondo con un agente (horas, días, edad, sexo, celular, puja, públicos); PR y merge.
- **Resultado:** 74,81 Bs, 22 conversaciones, ningún interesado "muy interesado". Jorge aprobó los ajustes para la próxima
  (`decisiones.md`, 25/10). PR #3 mergeado a `main` el 25/10; la rama se reinició desde `main` para seguir.
- **Qué aprendimos / qué cambiar la próxima vez:** mensaje prellenado obligatorio; leer el `targeting` de cada conjunto antes
  de publicar; Trinidad se agota rápido (rondas cortas), Santa Cruz rinde con días; sin los chats calificados no se sabe qué
  trae compradores: pedirle a Jorge el Excel **antes** de gastar de nuevo. Las entradas del 16 al 20/10 se archivaron en
  `memoria/2026-10.md` (memory.md llegaba a 300 líneas).

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
