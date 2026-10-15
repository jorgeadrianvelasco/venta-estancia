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
  estancias" (`1445747361945494`)** en el portfolio "Jorge Velasco", verificada con el MCP el 15/10/2026. Falta WhatsApp.
- **Categoría especial de vivienda:** no hace falta para un público en Bolivia (`reglas.md`, regla 5).
- **Próximo paso:** el plan de 10 pasos de `plan.md` (15/10/2026). Pasos 1, 3 y 6 hechos; 2 lo maneja Jorge en persona; 4 a medias (sin comparables). Paso 8:
  3 borradores sin aprobar. Fotos en `fotos/` (paso 5). **Texto aprobado: V1.** Paso 7: página creada; faltan contenido de la página y WhatsApp. Construir sí, lotear no. **Tono de las respuestas: camba, como habla Jorge, firmado como el dueño.**

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
