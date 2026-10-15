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
- **Estancia:** Calocha, a 6,6 km de Trinidad sobre la laguna Suárez. Resto de la ficha pendiente (`negocio.md`).
- **Objetivo (Jorge):** compradores serios de estancias, no curiosos. **El precio no se publica** (`decisiones.md`).
- **Aviso anterior:** boost de Marketplace del 17 al 20/10/2025 (cuenta personal `64830109`): 20,57 Bs, 6
  conversaciones, ninguna seria: "preguntan el precio y se van" (`textos-anuncios.md`).
- **Meta:** todo va en el portfolio "Jorge Velasco" (`160471911857072`), aprobado por Jorge. **Falta que Jorge cree
  ahí la página y la cuenta publicitaria** (el MCP no puede). Verificado de nuevo el 15/10/2026: todavía no están.
- **Categoría especial de vivienda:** no hace falta para un público en Bolivia (`reglas.md`, regla 5).
- **Próximo paso:** la página y la cuenta; seguir con la ficha de a 3 o 4 datos; definir cómo filtrar curiosos.

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
