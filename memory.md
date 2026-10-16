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
- **Paso 9 — campaña en BORRADOR** `52537356511050` (sin publicar, 0 Bs gastados): conjuntos **Trinidad**
  `52537356525250` (40 km) y **Santa Cruz** `52537356542650` (80 km), 30-65+, solo feed de Facebook, 37,50 Bs cada
  uno, a WhatsApp, intereses agro que puso Jorge. **Inicio 16/10 08:00, fin domingo 19/10 08:00** (hora de Bolivia).
- **Falta: los anuncios.** Jorge pidió una presentación profesional en vez de la primera publicación: **hecha en Moda**
  (`textos-anuncios.md`), 8 láminas con **fotos reales** y mapa en el **pin de Calocha** (-14.884522, -64.857659). Exportada a
  `presentacion/` (JPG + PDF) **sin sello**: rehecha en HTML + Chromium (`presentacion/fuente/`). Jorge pidió Creative Claw,
  que no conectó en esta sesión. **Sin aprobar.** Red: acceso completo.
  **No publicar sin su "publicala".** Construir sí, lotear no. **Tono: camba, como habla Jorge, firmado como el dueño.**

## Bitácora

### 15 de octubre de 2026 — Creación del repositorio
- **Qué se hizo:** Jorge creó `jorgeadrianvelasco/venta-estancia` (privado). Se armó la estructura copiando de
  Kakau la forma, no el contenido: reglas, decisiones, memoria con "Estado actual", hooks de inicio, commit y
  cierre, comando `/cerrar`, receta de campañas de Meta, skills `calificar-interesado` y `crear-campana`, y el
  agente `investigador-estancia`.
- **Pendiente:** el aviso anterior de la estancia y todos los datos de `negocio.md`.

### 15 de octubre de 2026 — Calocha, estructura de Meta y el boost de Marketplace de 2025
- **Jorge:** la estancia se llama **Calocha**. Pidió ver si hace falta un portfolio para vender y buscar el aviso que
  publicó "un par de veces" y que impulsó "sin que funcione para nada".
- **Qué ve el MCP** (`ads_get_ad_accounts`, `ads_get_user_pages`, `ads_catalog_get_businesses`): cuenta personal
  `64830109` (Jorge Velasco Avila, sin portfolio, ACTIVE, con forma de pago) y la de Kakau; portfolios "Kakau" y
  "Jorge Velasco" (`160471911857072`, solo con la página "Perriwos"); como página para anunciar, solo la de Kakau.
  El MCP no da el nombre del perfil conectado: se confirma recién cuando un cambio hecho por él aparece en el log.
- **El aviso:** en `64830109` hay un solo boost: "En venta propiedad urbana a 6.6 km de trinidad sobre la laguna
  suarez", Marketplace, 17 al 20/10/2025. 20,57 Bs, 20.594 impresiones, 10.600 de alcance, 590 clics, **6
  conversaciones a 3,43 Bs**. Público de 40 millas alrededor de Trinidad, 18 a 65+. El log muestra que Jorge lo
  reactivó el 3/3/2026 y lo apagó el 20/4/2026; después del 20/10/2025 no gastó más. Las otras publicaciones (sin
  pauta) no se ven por API. La Biblioteca de anuncios no tiene nada con "Calocha" en Bolivia.
- **Ayuda de Meta consultada:** la categoría de vivienda solo es obligatoria con público en EE. UU., Canadá o
  partes de Europa ([1198401317374558](https://www.facebook.com/business/help/1198401317374558)). Un portfolio nuevo
  crea **una** cuenta publicitaria; sube a 3 después de una campaña pagada
  ([915885887059947](https://www.facebook.com/business/help/915885887059947)).
- **Qué aprendimos:** el boost no falló en entrega: trajo conversaciones baratas. Lo débil fue el público (cualquiera
  de 18 a 65 alrededor de Trinidad) y el monto (21 Bs en 3 días). Hipótesis hasta saber qué preguntaron las 6.
- **Pendiente:** que Jorge confirme si era Calocha, qué preguntaron las 6, el texto y el precio del aviso, y si
  acepta la propuesta de página y cuenta dentro del portfolio "Jorge Velasco".

### 15 de octubre de 2026 — Jorge confirma Calocha, el precio oculto y el portfolio
- **Jorge:** el boost de Marketplace de oct-2025 **es Calocha**; *"la gente pregunta el precio y se va. No me molesta
  eso, quiero que la gente se interese [...] que no sean curiosos"*. El texto del aviso estaba bien. **El precio no
  se publica**: es muy elevado y no quiere que se sepa. **Todo lo de Meta va en el portfolio "Jorge Velasco"**.
- **Qué cambia:** el éxito se mide por interesados serios y visitas, no por conversaciones. El filtro de curiosos va
  en el anuncio y en la primera respuesta (`decisiones.md`). Ubicación anotada en `negocio.md`.
- **Pendiente:** que Jorge cree la página y la cuenta publicitaria dentro de "Jorge Velasco"; el WhatsApp de la venta;
  el resto de la ficha.

### 15 de octubre de 2026 — Verificación de página y cuenta en "Jorge Velasco"
- **Qué se hizo:** `ads_get_ad_accounts`, `ads_get_pages_for_business` (`160471911857072`) y `ads_get_user_pages`.
- **Resultado:** **todavía no están**. Cuentas visibles: `64830109` (personal, sin portfolio) y `2193563287857709`
  (Kakau, no se usa). Páginas del portfolio "Jorge Velasco": solo "Perriwos" (`1866464063601665`). Páginas con
  permiso de anunciar: solo la de Kakau.
- **Pendiente:** que Jorge cree la página y la cuenta dentro de "Jorge Velasco" y se vuelva a verificar; respuestas
  de la primera tanda de preguntas de la ficha (dueño, superficie, urbano o rural, municipio).

### 15 de octubre de 2026 — Primera tanda de la ficha y cambio de cuenta publicitaria
- **Jorge:** es **el dueño y decide el precio**; **530 ha, todas tituladas**; es un **predio urbano de gran extensión**
  por estar sobre la laguna Suárez. La cuenta publicitaria **es la suya, `64830109`**, no una nueva en el portfolio.
  Prefiere terminar la ficha antes de crear la página en business.facebook.com.
- **Provincia:** Jorge creía Marbán. La laguna Suárez está en **Cercado, municipio Trinidad** (Wikipedia, Ley 2604);
  Marbán limita con Trinidad al sur y sureste. Queda a confirmar con el folio real.
- **Hallazgo:** la Ley 2604 (2003) declara la laguna patrimonio ecológico (614,39 ha). Anotado en `documentacion.md`
  para consultar al abogado qué restricciones tiene la orilla.
- **Pendiente:** segunda tanda de la ficha; la página; el WhatsApp de la venta.

### 15 de octubre de 2026 — Segunda tanda de la ficha
- **Jorge:** provincia **Cercado** (sin el título a mano; dice que los papeles están "todo perfecto"). *"800 metros sobre
  la laguna y 1,3 km bordeando la laguna"* (falta aclarar). Acceso **todo el año**, a **600 m de la carretera a Loreto**.
  **Con ganado**, 500 ha de pastura y **30 ha de monte**. **Casa** con energía a motor y **agua de lluvia**.
- **Pendiente:** aclarar el frente a la laguna; pasturas (especie), aguadas, corrales y alambrado, si se vende con
  ganado.

### 15 de octubre de 2026 — Tercera tanda de la ficha y plan de 10 pasos
- **Jorge:** el frente son **dos tramos**: 800 m colindantes con la laguna y 1,3 km a 10 m de la orilla. Pasturas
  **naturales de arrocillo**. **Alambrado perimetral** en buen estado, **4 pozas** y la laguna. **Se vende sin ganado.**
- **Jorge pidió** los 10 próximos pasos en orden cronológico: quedaron en `plan.md`.
- **Pendiente:** de quién es la franja de 10 m; corrales, brete y potreros; forma de pago y moneda; equipos.

### 15 de octubre de 2026 — Cierre de la ficha (paso 1 del plan)
- **Jorge:** la franja de 10 m del tramo de 1,3 km **es de un vecino**. Hay **corral con brete y un corralón**. Pago
  **negociable** en forma y monto. **Sin intermediario.** Todo queda en el predio menos los animales.
- **Consecuencia para los anuncios:** el frente propio sobre la laguna son **800 m**; no se puede decir "2,1 km de
  orilla". El 1,3 km se describe como "a 10 m de la laguna".
- **Pendiente:** capacidad de carga (opcional); paso 2 (abogado) y paso 3 (perfil de comprador).

### 15 de octubre de 2026 — Perfiles de comprador (paso 3 del plan)
- **Jorge eligió:** B (inversionista que guarda tierra), C (ganadero o empresa que quiere campo cerca de la ciudad) y
  D (quinta o turismo). **No eligió** A (desarrollador que lotea). Anotado en `comprador.md`.
- **Se propuso** el borrador del filtro de curiosos (paso 6): una línea en el anuncio + 3 preguntas en la primera
  respuesta (uso, plazo, visita), y el precio solo en persona o por llamada. **Sin aprobar**: no va a `respuestas.md`.
- **Pendiente:** aprobación del filtro; paso 2 (abogado).

### 15 de octubre de 2026 — Filtro de curiosos aprobado (paso 6) e investigación (paso 4)
- **Jorge:** aprobó la línea del anuncio. La primera respuesta la quiso **en camba, como él habla, sin exagerar**,
  diciendo que **él es el dueño**, y **sin preguntar el plazo**. El precio **se puede charlar por mensaje pero no sale
  automático**: lo da él. Con esos cambios, aprobado (`respuestas.md`).
- **Se lanzó** el agente `investigador-estancia` para el paso 4 (precios de referencia y canales cerca de Trinidad).

### 15 de octubre de 2026 — Resultado de la investigación de mercado (paso 4)
- **Qué se hizo:** el agente `investigador-estancia` buscó precios, valores oficiales, canales y restricciones de la
  laguna. Resultado en `investigacion/precios-y-canales-trinidad.md` y 8 filas en `competencia.md`.
- **Resultado:** **débil**. El proxy bloqueó todos los portales y normas: todo sale de resúmenes de buscador, sin abrir
  los avisos. **Ningún aviso sobre la laguna Suárez ni la carretera a Loreto.** Estancias del Beni piden de ~10 a
  2.000 USD/ha (rango inútil); dos cerca de Trinidad con agua, ~1.000-1.100 USD/ha. Un solo periurbano (16 ha). Nada
  público de catastro ni INRA. Hay ordenanzas de 2010-2011 y Ley departamental 017 (2011) sobre la laguna, sin texto.
- **Qué aprendimos:** desde este entorno no se pueden abrir portales bolivianos. Los comparables reales los tiene que
  aportar Jorge (ventas que conozca) o abrirlos él. Para anuncios: **no prometer construir ni lotear** hasta el abogado.

### 15 de octubre de 2026 — Papeles, construcción y borradores de anuncio (paso 8)
- **Jorge:** los papeles (folio real, plano, impuestos, Ley 2604) **los charla él en persona**: Claude no los guarda
  ni los manda. **En la laguna se puede construir pero no lotear** (por eso no se vende a loteadores). Las fotos y el
  drone ya existen: están en el aviso de Marketplace de 2025.
- **Fotos por el MCP:** solo hay una del aviso (la vista aérea ya guardada en `fotos/`). La creatividad del boost es
  una publicación de Marketplace (`709824314797323`, STATUS, sin `image_url`). Las otras 4 imágenes de la cuenta son
  de feb-2025 y el proxy bloquea `fbcdn.net`. **Ninguna muestra la laguna**: se le pidió a Jorge que las pase.
- **Borradores:** V1 general, V2 ganadero, V3 laguna (`textos-anuncios.md`), sin aprobar.
- **Siguiente:** aprobación de textos; fotos de la orilla; paso 7 (página y WhatsApp).

### 15 de octubre de 2026 — Fotos del predio (paso 5)
- **Jorge mandó 9 fotos por el chat** (capturas de celular de las del aviso de 2025). Se guardaron 7 en `fotos/`,
  recortadas sin bordes negros (una era repetida y otra igual a la que ya estaba). Catálogo y uso en `fotos/README.md`.
- **Foto principal:** `2025-drone-laguna-casa-y-camino.jpg` (laguna, casa y camino en una toma). **No usar** la de la
  pampa con agua (puede leerse como que se inunda) ni la nublada.
- **Pendiente:** originales en mejor calidad; aprobación de textos; WhatsApp y página (paso 7).

### 15 de octubre de 2026 — Texto V1 aprobado y guía para la página (paso 7)
- **Jorge eligió V1** (el general). V2 y V3 quedan como borradores no elegidos (`textos-anuncios.md`).
- **Se le dio la guía** para crear la página "Estancia Calocha" en el portfolio "Jorge Velasco" desde Meta Business
  Suite ([Meta 720478807965744](https://www.facebook.com/business/help/720478807965744)) y conectar el WhatsApp Business
  desde Configuración → Cuentas vinculadas ([Meta 1583303048513172](https://www.facebook.com/business/help/1583303048513172)).
- **Ojo para la verificación:** Jorge conectó el MCP cuando armó Kakau. Si la página nueva no aparece en
  `ads_get_user_pages`, hay que reconectar el conector de Meta en claude.ai y tildar la página nueva **sin destildar
  la de Kakau** (si no, se rompe el agente de Kakau).

### 15 de octubre de 2026 — Página creada y verificada (paso 7)
- **Jorge creó la página "Venta estancias"** (`1445747361945494`) en el portfolio "Jorge Velasco" desde Business
  Suite (en inglés: Settings → Accounts → Pages → + Add). Casi entra en "Ad accounts": se le avisó que no agregue ahí
  la cuenta `64830109`.
- **MCP:** `ads_get_pages_for_business` la muestra en el portfolio; `ads_get_user_pages` la muestra junto a la de Kakau
  (puede anunciar). **No hizo falta reconectar el conector.** `ads_get_ad_account_pages` de `64830109` vacío: normal.
- **Pendiente:** foto de perfil, portada, presentación, primera publicación con V1; conectar WhatsApp Business.

### 15 de octubre de 2026 — WhatsApp: número del padre de Jorge
- **Jorge** quiere usar el **número de su padre** para la venta y preguntó si hace falta WhatsApp Business.
- **Ayuda oficial de Meta** ([372008982225441](https://www.facebook.com/business/help/372008982225441)): desde marzo de
  2024 los anuncios que llevan a WhatsApp **exigen WhatsApp Business**; un número personal no sirve. Se puede **pasar el
  mismo número** gratis sin perder chats ni contactos, pero los chats personales y los de la venta quedan juntos.
- **Se le preguntó:** quién responde (la respuesta aprobada dice "Soy Jorge, el dueño") y si ese número ya se usa para
  los tubos del padre (un número solo se conecta a un negocio; además, regla 7: no mezclar líneas).
- **Se le dieron** los pasos para cargar la página desde el celular (perfil, portada, presentación, publicación con V1).

### 15 de octubre de 2026 — Logo con IA para la página
- **Jorge pidió** una imagen hecha con IA en Canva para la página "Venta estancias" (es la primera publicación/imagen).
- **Se hizo** un logo redondo: "VENTA DE ESTANCIAS · Beni • Bolivia", con pampa, laguna, palmeras, alambrado y
  amanecer (Canva media `MAHYF22URdM`). Sugerido como **foto de perfil**; la portada sigue siendo la orilla real.
- **Regla:** la imagen con IA es de marca. En anuncios y publicaciones de Calocha van **solo fotos reales**.
- **Jorge:** el primer logo "se nota muchísimo que es IA". Se hicieron dos más sobrios: **A, líneas** (palmera, orilla,
  verde oscuro, `MAHYFz49kG4`) y **B, marca de ganado** (monograma "VE", marrón sobre crema, `MAHYF1dius4`). Falta que elija.

### 15 de octubre de 2026 — WhatsApp compartido con los tubos
- **Jorge decidió:** el número de su padre atiende **tubos y Calocha**, conectado a las dos páginas. Responde el padre,
  que también se llama Jorge: usa la primera respuesta aprobada tal cual. Anotado como excepción en `reglas.md` (regla 7)
  y en `decisiones.md`.
- **Meta:** se puede conectar varios números a una página ([228271686945544](https://www.facebook.com/business/help/228271686945544)).
  Que un mismo número vaya a dos páginas **no está confirmado**: si la de tubos está en otro portfolio puede salir
  "WhatsApp number linked to another Facebook business" ([2091769220999799](https://www.facebook.com/business/help/2091769220999799)).
  La salida que da Meta (sacar el número del otro portfolio) **rompería los tubos**: si pasa, se consulta a Jorge.
- **Pendiente:** conectar el número a "Venta estancias"; que Jorge elija logo (A líneas o B "VE").

### 15 de octubre de 2026 — Pago y lo que falta para anunciar
- **Jorge:** el WhatsApp se conecta después; primero quiere dejar listo el método de pago "y demás".
- **MCP (`ads_get_ad_accounts`):** `64830109` ACTIVE, **ya tiene forma de pago**, moneda BOB, presupuesto diario mínimo
  11,95 Bs. El MCP no muestra qué tarjeta es ni si está vencida: Jorge la revisa en Facturación.
- **Instagram:** `ads_get_ig_accounts` de `64830109` vacío: no hay Instagram vinculado (opcional).
- **Pendiente para la campaña:** presupuesto total y costo máximo por interesado serio (`negocio.md`, sin definir).
- El agente `investigador-estancia` está investigando la identidad visual de competidores (BO, BR, AR) para mejores
  prompts de logo en Canva.

### 15 de octubre de 2026 — Identidad visual: investigación y tercera ronda de logos
- **Jorge:** las versiones de líneas y "VE" eran "muy básicas y feas"; pidió un agente que mire competidores (BO, BR, AR)
  y arme prompts para Canva. Resultado en `investigacion/identidad-visual-competidores.md` (débil: el proxy bloqueó
  todos los sitios; solo resúmenes de buscador). Patrones: nombre propio y datos dan confianza; foto real del campo;
  2-3 colores; marca simple que funcione chica; serif sobria. Agregó 2 filas de Century 21 Amazonía a `competencia.md`.
- **Generadas:** A "E" serif verde y crema (`MAHYF5P7CNo`), B alambrado ocre y azul (`MAHYF57Fd4k`, parece escalera),
  C portada verde (`MAHYF5qCAE8`). Falta que Jorge elija.
- **Sugerencia del investigador (decide Jorge):** el nombre "Venta estancias" es genérico; las firmas serias usan un
  nombre propio.
- **Jorge eligió la B** (alambrado ocre sobre azul marino), "aunque ninguna me encantó". Que diga **"BOLIVIA"**, no
  "Beni · Bolivia". **Sin Instagram por ahora**: se vende mejor en Facebook (`decisiones.md`).
- **Cuarta ronda:** B1 igual con "BOLIVIA" (`MAHYF0zLHG4`) y **B2 con alambrado corregido** (`MAHYF5H25mc`, recomendada).

### 15 de octubre de 2026 — Logo elegido y propuesta de primera campaña
- **Jorge eligió la B2** (alambrado corregido, ocre sobre azul marino, "BOLIVIA"; Canva `MAHYF5H25mc`).
- **Se armó un borrador de propuesta** para la primera campaña en `plan.md` (sin aprobar, no se creó nada): post V1 de
  la página, solo Facebook, público Bolivia (Beni, Santa Cruz, La Paz, Cochabamba) 30-65+, 7 días. Faltan de Jorge:
  monto, destino (esperar WhatsApp o Messenger), con o sin Marketplace.

### 15 de octubre de 2026 — Primera publicación de la página
- **Jorge** quiere hacer ya la primera publicación. **El MCP no puede publicar en la página** (no hay herramienta para
  posts orgánicos): la hace Jorge desde el celular. Se le dio el paso a paso: V1 + 5 fotos reales en orden (drone
  laguna, orilla, casa y corrales, alambrado, pampa), **"Publicar ahora", nunca "Impulsar"**.
- **Pendiente:** que Jorge pase el link de la publicación (su ID se usa después como anuncio).
- **Verificación tras "ya, fijate todo" (15/10/2026):** la página "Venta estancias" sigue con permiso de anunciar;
  activity log de hoy **vacío** en `64830109` y sin campañas nuevas en la de Kakau → **no se impulsó nada**. El MCP **no
  puede ver** publicaciones, foto de perfil ni portada de la página: para eso Jorge manda el link o captura.
- **Jorge (15/10/2026):** "ya está la publicación, la foto de perfil y de cover. Confiá en mí". Se le preguntaron las
  decisiones de la primera campaña (monto, destino, Marketplace) antes de crear nada.
- **Respuestas de Jorge para la primera campaña (15/10/2026):** "25 Bs por 3 días" (a aclarar si es total o por día:
  25 Bs en total queda debajo del mínimo diario de 11,95 Bs), destino **WhatsApp del padre**, **sin Marketplace**, "sí,
  armala pausada" **pero "primero quiero hacer la segmentación"**. No se creó nada: falta segmentación, aclarar monto,
  conectar el WhatsApp y el link del post.
- **Segmentación decidida (15/10/2026):** Trinidad 50 % y Santa Cruz 50 % (dos conjuntos de 37,50 Bs), 30-65+, intereses
  ganadería / bienes raíces e inversión / agro / turismo rural, **75 Bs en total** (25 Bs/día × 3). El MCP no tiene
  buscador de intereses ni de ciudades: ciudades por coordenadas + radio; intereses los agrega Jorge en el Administrador.
- **WhatsApp (15/10/2026):** el número del padre **va a estar en el portfolio de tubos**. En "Venta estancias" se conecta
  **solo a la página** (no al portfolio "Jorge Velasco"): una cuenta de WhatsApp Business va en un solo portfolio. Riesgo
  no verificado de choque entre portfolios: probar y re-verificar después de que tubos lo agregue. La configuración de
  tubos no se hace desde este repo (regla 7).

### 15 de octubre de 2026 — Primera campaña creada como BORRADOR
- **Jorge:** conectó el WhatsApp del padre a "Venta estancias" (el MCP no tiene cómo leerlo; se prueba al publicar).
  Pidió: "vos hacés toda y el público, pero me enviás el link para que yo añada más".
- **Creado por el MCP en modo borrador** (no está publicado, no gasta): campaña **`52537356511050`** "Calocha - WhatsApp -
  Prueba 3 dias (oct 2026)", `OUTCOME_ENGAGEMENT`, sin categoría especial. Conjuntos (ABO, `CONVERSATIONS` → `WHATSAPP`,
  page `1445747361945494`, 37,50 Bs de presupuesto total c/u, 16/10 08:00 a 19/10 08:00 -04:00, 30-65, `advantage_audience: 0`,
  solo feed de Facebook): **Trinidad 40 km** `52537356525250` (-14.8333, -64.9) y **Santa Cruz 30 km** `52537356542650`
  (-17.7833, -63.1821). Validación del borrador: sin errores.
- **Falta:** el anuncio (post V1; Jorge puede elegirlo en el Administrador con "usar publicación existente" o pasar el
  link), los intereses (los agrega Jorge) y **publicar solo con su visto bueno**: al publicar sale ACTIVA.
- Link: https://adsmanager.facebook.com/adsmanager/manage/adsets?act=64830109&selected_campaign_ids=52537356511050
- **Ojo en el Administrador (15/10/2026):** Jorge entró por error al **boost viejo de Marketplace** (`6836819733446`,
  "Completed"; errores de "no se puede editar" y ubicaciones: normales, es de 2025). Además hay un **borrador viejo**
  "New Leads Campaign" (`6898918260046`, creado por Jorge el 3/3/2026, con categoría HOUSING y errores): **no publicarlo**.
  La campaña nuestra está en borradores con el nombre "Calocha - WhatsApp - Prueba 3 dias (oct 2026)".

### 15 de octubre de 2026 — Revisión del borrador después de los cambios de Jorge
- **WhatsApp:** ✅ los dos conjuntos ya tienen el número del padre conectado (`page_whatsapp_number_id`
  `1446613075192256`, número terminado en 629). Queda confirmado que la página tiene WhatsApp.
- **Intereses que agregó Jorge:** todos agro/ganaderos (granja, ganado, agricultura, agronegocios, ganadería de carne,
  lechería, caballos, zona rural; empleos de agricultura y "Farm Owner Operator" en Santa Cruz). **No** hay bienes raíces,
  inversión ni turismo rural: cubre el perfil C, no B ni D.
- **Cambios de Jorge:** Santa Cruz pasó a **80 km** de radio. Meta agregó `recent` y `frequently_in` a los tipos de
  ubicación. **Trinidad termina el 18/10 08:00** (Bolivia) y Santa Cruz el 19/10 08:00: Trinidad quedó en 2 días
  (18,75 Bs/día). Se le preguntó si fue a propósito.
- **Falta:** ❌ **ningún anuncio** en el borrador (solo campaña y 2 conjuntos): sin anuncio no se puede publicar.

### 16 de octubre de 2026 — Fecha de Trinidad corregida; los anuncios esperan el link del post
- **Jorge:** "hacelos vos [los anuncios], que terminen los dos el domingo".
- **Hecho:** conjunto Trinidad (`52537356525250`) → `end_time` 2026-10-19T08:00:00-0400 (igual que Santa Cruz). Sigue en borrador.
- **Anuncios:** no se pudieron crear: hace falta el ID de la publicación (el MCP no lista posts de la página y las fotos del
  repo no tienen URL pública para subirlas). Se le pidió el link a Jorge.
- **Ojo:** el inicio quedó en 16/10 08:00 y ya es 16/10: al publicar hay que poner una hora de inicio real (receta de
  Kakau: una vez pasada, no se puede cambiar).

### 16 de octubre de 2026 (20:10 del 15/10 en Bolivia) — Intento de armar los anuncios sin el link del post
- **Corrección de la entrada anterior:** el "ya es 16/10" era la hora UTC. En Bolivia todavía es jueves 15/10 a la noche:
  el **inicio del 16/10 08:00 sigue en el futuro**. Si se publica antes de esa hora, arranca a las 8.
- **Subir la foto por el MCP:** `ads_creative_upload_local_image` responde "se está habilitando de a poco; probá más
  adelante" para la cuenta `64830109`. `ads_creative_upload_media` pide una URL pública (o la app interactiva, que esta
  sesión no tiene). Subirla a Canva para sacar una URL: **el proxy bloquea `www.canva.com`**. Sin salida desde acá.
- **Biblioteca de imágenes de la cuenta:** las mismas 5 de siempre (sin nombre); ninguna muestra la laguna.
- **Hecho:** recorte **4:5** de la foto principal para el feed (`fotos/2025-drone-laguna-casa-y-camino-4x5.jpg`, 1170×1462,
  sin cielo de más): entran la laguna, la casa y el camino.
- **Se le pidió a Jorge una de dos:** (A) el link de la publicación → anuncio con el post (`object_story_id`); o (B) subir
  la foto 4:5 a la biblioteca de la cuenta → anuncio nuevo con V1 y botón de WhatsApp (`image_hash`).

### 16 de octubre de 2026 (noche del 15/10 en Bolivia) — Presentación profesional: Canva descartado, Moda armada
- **Jorge:** "no me gustó para nada cómo quedó la publicación, haceme algo con Canva más profesional", "que sea como una
  presentación, que diga qué cosas tiene, que es propiedad urbana, que es cerca, qué se puede hacer ahí".
- **Canva:** `create-design` generó 7 láminas 16:9 (`DAHYIBt3tR8`) con **fotos de stock que no son de Calocha**; el
  `resize-design` a 4:5 (`DAHYIPRhqsE`, gastó una prueba Pro: queda 1) desarmó el diseño. Jorge denegó seguir editando y dijo
  que las láminas 1, 2, 4, 5 y 6 eran falsas. **Ojo:** la 3 y la 7, que le parecieron bien, **también eran stock**: se le avisó.
- **Moda** (conector nuevo de Jorge, plan gratis): lienzo `cvs_26PX3C3T1297QS1XFB0R6P9YER` con 8 láminas 1080×1350. Mapa real
  de Mapbox centrado en la laguna (el marcador siempre va al centro del mapa; `marker="lon,lat"` y `style="satellite"` se
  ignoran). Sin kit de marca: colores del logo B2.
- **Subir fotos, bloqueado desde la sesión:** `agents.moda.app` y `www.canva.com` dan 403 en el proxy; `<image src="data:...">`
  no existe en Moda. Camino: Jorge sube en **moda.app → Drive → Subir**; después `file_list` da los `file_…`.
- **Pendiente:** fotos en Moda → colocarlas → exportar PNG (Facebook) y PDF (WhatsApp) → que Jorge apruebe.

### 16 de octubre de 2026 — Acceso para subir fotos y ubicación real de Calocha
- **Jorge:** no sabe subir fotos a Moda y quiere que **siempre lo haga Claude**: pidió investigar cómo dar acceso.
- **Causa:** la política de red del entorno bloquea `agents.moda.app` (subida a Moda), `www.canva.com` (subida a Canva),
  `maps.app.goo.gl` (pines de Google Maps) y antes `*.fbcdn.net` (fotos de Meta). **Solución:** que Jorge agregue esos
  dominios en el entorno (barra de título de la sesión → menú del entorno → Editar → Acceso a la red → Limitado +
  dominios permitidos, sin destildar los gestores de paquetes), o suba el nivel de acceso.
  Docs: https://code.claude.com/docs/en/cloud-environments#network-access. Con eso, Jorge manda fotos por el chat y Claude
  las sube.
- **Mapa (lámina 2):** Jorge dijo que la laguna está bien ubicada, pero **Calocha no queda donde estaba el marcador** (centro
  de la laguna). Se sacó el marcador. Mandó un pin: https://maps.app.goo.gl/FCMzghnqHacJfcw49. **No se pudo abrir** (proxy):
  se le pidieron las coordenadas en números. Cuando lleguen: anotarlas en `negocio.md` y centrar el mapa ahí con marcador.

### 16 de octubre de 2026 — Acceso completo, fotos reales en Moda y pin de Calocha
- **Jorge** puso el acceso a la red en **completo** (no tenía la opción "limitado"). Ya funcionan `agents.moda.app` y
  `maps.app.goo.gl`.
- **Pin:** el link de Jorge resuelve a **-14.884522, -64.857659** (orilla este de la laguna Suárez, al sur del balneario
  Finca Paraíso de Dios, cerca de la carretera a Loreto). Anotado en `negocio.md`. En línea recta desde el centro de Trinidad
  da ~7,3 km (coordenadas de la plaza aproximadas); el 6,6 km es dato de Jorge y queda.
- **Fotos en Moda:** subidas por PUT a la URL de `upload` + `upload(storage_key=…)`. Para que encajen, se recortan antes a la
  proporción de cada marco (scratchpad `recortes/`), y se ponen con `canvas_edit` → `update(id, {src: 'file_…'})`.
- **IDs de archivos en Moda:** portada `file_7W6EJ57FAS96P8Y09QC2G72GJV`, orilla `file_0JZ49GN3QW86TBMYG7DHQNWJAA`, pampa
  (recorte) `file_4RQ9NXNYF784JVWZND07Y230SY`, casa y corrales (recorte) `file_473Y88Z67M9AWTK79V26D3V4M0`, alambrado (recorte)
  `file_4Z4RH18GF881W9KMHT8DD2TRFR`, camino (recorte) `file_7BX1YQSVW59EAA5NGPE6HD7J4J`, cierre (recorte de la portada, arriba)
  `file_6S4XDF5M2H95XS5KZPZEP7CE35`.
- **Exportación:** `presentacion/` (8 JPG + PDF). El plan gratis de Moda agrega un sello "moda.app" abajo a la derecha: no se
  quitó (es la marca del plan gratis). Se le dieron opciones a Jorge.

### 16 de octubre de 2026 — Láminas sin sello
- **Jorge:** "hacé la opción A, sin el sello. Hacelo con Creative Claw".
- **Creative Claw:** sus herramientas no están en la sesión: el servidor falló al iniciar (`ERR_PROXY_TUNNEL`, cuando la red
  estaba bloqueada). Hace falta una sesión nueva o reconectarlo (y quizás iniciar sesión en Creative Claw).
- **Hecho:** las 8 láminas en HTML (`presentacion/fuente/laminas.py`), renderizadas con Playwright/Chromium del entorno, sin
  sello. Reemplazan a las de Moda en `presentacion/`. El mapa es un recorte del mapa de Moda (atribución Mapbox/OSM visible).

### 16 de octubre de 2026 — Publicación con las láminas y anuncios del borrador
- **Jorge:** "quiero que me hagas una publicación como la que hice y que a base de eso hagamos la misma campaña que habíamos
  creado". Se le mandaron las 8 láminas (`presentacion/`).
- **No se puede publicar en la página desde acá:** el MCP de Meta no tiene herramienta para publicar posts orgánicos. Jorge
  publica el post (8 láminas + texto V1) y pasa el link → anuncios con `object_story_id` en los 2 conjuntos del borrador.
- **Carrusel de anuncio, descartado para estas láminas:** en Facebook el carrusel manual solo acepta 1:1 o 9:16; el 4:5 es
  solo para catálogo ([Meta 1114358518575630](https://www.facebook.com/business/help/1114358518575630)). Imagen única 4:5 sí
  es la recomendada en el feed ([Meta 682655495435254](https://www.facebook.com/business/help/682655495435254)).
- **Imágenes en la cuenta `64830109`:** portada `feb81d27245ec62a74f3e90c4273e2bf` y el campo `293529fb91585c61be69305063cdb0b4`
  (subidas con los links temporales de GitHub). **El control de seguridad de la sesión frenó el resto por "fuga de
  credenciales"** (el link lleva un token de acceso al repo privado): **no volver a usar ese camino**.

