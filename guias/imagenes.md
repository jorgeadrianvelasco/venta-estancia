# Imágenes y láminas

Orden de trabajo decidido por Jorge el 12/11/2026, "para que hagamos mejores imágenes":

| # | Herramienta | Cuándo |
|---|---|---|
| 1 | **Higgsfield** | Siempre primero, mientras tenga créditos |
| 2 | **Moda** | Si Higgsfield no tiene créditos o no puede hacer lo que se pide |
| 3 | **Canva** | Último recurso |

Encima de este orden manda la regla 7 (`reglas.md`): **el producto que aparece en un anuncio es siempre el real.**
Las herramientas sirven para mejorar la foto real, ponerla en una escena o armar la pieza. No sirven para inventar el
producto. Lo de Higgsfield sale de leer sus flujos y precios el 12/11/2026. **Todavía no se generó ninguna imagen con
Higgsfield**: lo que no se probó dice "sin probar".

> **En la estancia:** esta guía es copia de la base y cita sus reglas, que acá tienen otra numeración. El "producto
> real" son **las fotos reales de Calocha** (`fotos/`): Higgsfield solo puede mejorarlas (resolución, encuadre, cielo,
> luz), **nunca agregar algo que el predio no tiene** (ganado, casas, agua, caminos, árboles). La "regla 7" de la base acá
> es la regla 4 de `reglas.md` (no inventar datos) y `fotos/README.md` (en anuncios, solo fotos reales del predio). La
> "regla 6" (Jorge aprueba cada imagen) acá cae en la regla 1: nada se publica sin su pedido. El script de láminas ya
> está en `presentacion/fuente/`.

## 1. Higgsfield

### Antes de generar

1. **Créditos:** `balance`. El 12/11/2026 la cuenta tenía **126 créditos, plan basic**.
2. **Precio:** cada herramienta de generación acepta `get_cost: true`, que devuelve el precio sin generar nada.
   Antes de una tanda, se le dice a Jorge cuántos créditos va a costar y se espera su sí (regla 1: nada se gasta sin
   pedido).
3. **Foto real del producto:** se sube con `media_upload`, se le hace PUT con `curl` a la `upload_url` y se confirma
   con `media_confirm`. Así queda un `media_id`. Si el archivo no se puede leer desde la sesión, se usa
   `media_upload_widget` como única herramienta de ese turno. Un link web se sube con `media_import_url`.
4. Si `balance` da 0 o una generación vuelve sin créditos: **no se compran créditos**. Se pasa a Moda y se le avisa a
   Jorge (`show_plans_and_credits` muestra los planes, solo si él lo pide).

### Qué usar para cada cosa

| Para qué | Herramienta o modelo | Créditos (precio de lista, 12/11/2026) | Estado |
|---|---|---|---|
| **Fotos del producto real en una escena, packshot, carrusel o pack de anuncios** | Flujo `product-photoshoot` (`get_workflow_instructions`). Usa `nano_banana_pro` en 2K con la foto real como `image_references` | **2 por imagen** | Sin probar |
| Avisos con texto incluido (titular, copy) | Flujo `ads-studio`: lee la página o la foto del producto, escribe el copy y hace la imagen. Cotiza con `ads_studio_quote` | Según la cotización | Sin probar |
| Imagen de producto para anuncio, en un clic | `marketing_studio_image` | 2 por imagen en 1K | Sin probar |
| Cambiar el estilo o la temporada de una foto real sin cambiar el producto | Modo `restyle` de `product-photoshoot` | 2 por imagen | Sin probar |
| Logo, portada de la página, ilustraciones sin producto | `gpt_image_2_6` (el modelo general) o el flujo `brand-asset-creation` | 0,25 por imagen | Sin probar |
| Subir de resolución una foto real | `upscale_image` (hay que pasarle el ancho y el alto en píxeles) | Costo fijo; se ve con `get_cost` | Sin probar |
| Recortar el fondo de una foto real | `remove_background` | — | Sin probar |
| Agrandar una foto real hacia los costados (por ejemplo, de horizontal a 4:5) | `flux_2_pro_outpaint` | — | Sin probar |
| Video corto para Reels | `generate_video` (`marketing_studio_video` para anuncios). Sale caro: cotizar primero | — | Sin probar |

### Gastar la menor cantidad de créditos (pedido de Jorge, 12/11/2026)

| Regla | Por qué |
|---|---|
| **`get_cost: true` antes de cada tanda**, y decirle a Jorge el total | Nada se gasta sin saber cuánto |
| **Primero 1 imagen, después las demás.** Se manda una variante, se mira, y recién si sirve se hacen las otras | Si el pedido estaba mal, se pierde 1 imagen y no 3 |
| **La calidad justa**: 2K para anuncios, nunca 4K de entrada. Si una sola imagen hace falta en 4K, se sube después con `upscale_image` | El feed muestra 1080 px |
| **El modelo barato para lo que no lleva producto** (`gpt_image_2_6`, 0,25 créditos) | Cuesta 8 veces menos que una foto de producto |
| **Pensar el pedido antes de mandarlo**: modo, escena, luz, proporción y qué evitar, escritos completos | La mayoría de las repeticiones vienen de un pedido vago |
| **Corregir, no rehacer**: la corrección usa la imagen anterior como referencia y dice qué defecto arregla. Máximo dos por imagen | Rehacer desde cero repite todo el gasto |
| **Nunca volver a mandar una generación que tarda**: se espera con `jobs_wait` y se reusa el ID | Mandarla de nuevo cobra dos veces |
| **Reusar lo que ya se hizo**: una imagen aprobada se guarda en `fotos/generadas/` con su ID y se reusa en otra campaña | Una imagen buena sirve más de una vez |
| **Las proporciones que se van a usar, y nada más** | Una versión 9:16 que nadie pidió es gasto |
| **Los "ilimitados" (`use_unlim`) solo si Jorge los pide** | Así lo indica la herramienta |
| **Sin créditos, se pasa a Moda**; no se compran créditos sin que Jorge lo pida | Es el orden que fijó él |
| **Cada gasto se anota** en `memory.md`: qué se hizo, cuántos créditos y si sirvió | Para saber qué rinde |

### Cómo se pide una foto de producto

Esto es lo que dice el flujo `product-photoshoot`:

- Primero se elige un **modo**: packshot de estudio, escena de uso, primer plano con manos, carrusel, pack de
  anuncios, restyle, etc. Después se arma el pedido por secciones (sujeto, escena, luz, paleta, qué evitar).
- **La foto real va como referencia en todas las variantes**, para que el producto sea el mismo en todas.
- Hacer **3 variantes distintas** (cambia la escena, la luz o la cámara; el producto no), no 3 copias.
- Para avisos, cada variante con un **gancho** distinto: aspiración, detalle del producto, transformación, prueba
  social, curiosidad.
- **Proporciones:** feed **4:5**, Facebook y carrusel **1:1**, historias **9:16**. En Ads Studio no existe 4:5: se usa
  3:4.
- Máximo **dos correcciones por imagen**, y cada una dice qué defecto arregla.
- Si una generación tarda, se espera con `jobs_wait`. **No se vuelve a mandar**: se gastaría dos veces.

### Lo que no se hace con Higgsfield

| No | Por qué |
|---|---|
| Generar el producto solo con texto, sin la foto real | Regla 7. Higgsfield lo permite; nosotros no |
| Cambiarle al producto la forma, el color, la etiqueta o el tamaño | Es mostrar algo que el cliente no va a recibir |
| Escribir con Higgsfield datos que tienen que ser exactos (precio, teléfono, hectáreas) | La IA deforma letras y números. Ese texto se pone en el Administrador de Meta o con el script de láminas |
| Usar los "créditos ilimitados" (`use_unlim`) sin que Jorge lo pida | Así lo indica la herramienta |
| Mostrarle a Jorge una imagen sin haberla mirado | Ver abajo |

### Antes de mostrarle una imagen a Jorge

1. **Mirarla** (bajarla y abrirla) y compararla con la foto real: forma, color, etiqueta, tamaño, cantidad.
2. Si el producto cambió en algo, **se descarta**, aunque la imagen sea linda.
3. Decirle qué herramienta se usó y cuántos créditos costó.
4. Se la mandan las imágenes con `SendUserFile`. **Jorge aprueba antes de que vaya a un anuncio** (regla 6).
5. Anotar en `memory.md` qué se pidió, cuánto costó y qué le pareció a Jorge. Lo que sirva para todas las líneas va
   también a la base.

## 2. Moda (si Higgsfield no tiene créditos)

| Sirve | Cuidado |
|---|---|
| Lienzo editable, láminas, presentaciones | El plan gratis pone un sello "moda.app" en lo que se exporta |
| **Mapa real** (Mapbox) | El marcador va siempre al centro; `satellite` y `marker` se ignoran |
| Editar una imagen adentro de un diseño (`canvas_edit_image`) | No genera imágenes sueltas |

Para subir fotos: PUT a la URL de `upload` y después `upload(storage_key=…)`. Hace falta la red completa
(`agents.moda.app`). Se empieza con `moda_bootstrap`. Probado en la estancia (16/10/2026).

## 3. Canva (último recurso)

| Sirve | No sirve |
|---|---|
| `generate-image` para un logo o una portada, eligiendo entre varias rondas | `create-design` mete **fotos de stock que no son del producto**: Jorge las rechazó ("es falsa") |
| | Pasar un diseño a vertical lo desarmó y gastó una prueba Pro |

## Láminas con texto exacto: HTML → PNG

Cuando la pieza lleva números o datos que no pueden salir mal (precio, superficie, teléfono), el texto se pone con el
script de láminas, no con IA. El modelo está en la base, en `modelos/laminas/`, probado el 12/11/2026. Se copia a
`presentacion/fuente/` del repo de la línea y se le cambian textos, fotos y colores. La foto de fondo puede salir de
Higgsfield (la foto real mejorada); el texto lo pone el script.

## Formatos

| Uso | Proporción | Tamaño |
|---|---|---|
| Imagen única en el feed | 4:5 | 1080×1350 |
| Carrusel | 1:1 | 1080×1080 |
| Historias y Reels | 9:16 | 1080×1920 |

## Fotos reales

- Pedirle a Jorge los **archivos originales**: las capturas del celular pierden calidad y traen bordes negros.
- Cada foto va a `fotos/` con su fila en `fotos/README.md`: qué muestra y para qué se usa.
- **Mirar la foto antes de decir qué muestra.** En Kakau se identificaron mal productos en las fotos.
- Una foto que salió de Higgsfield va a `fotos/generadas/`, con la foto real de la que salió y la herramienta.

## Logo e identidad

Lo que funcionó para el logo de la estancia: un agente investiga la identidad visual de la competencia y arma los
prompts; se generan varias opciones; Jorge elige y pide cambios (fueron cuatro rondas). Lo que rechazó: "se nota
muchísimo que es IA", "muy básicas y feas". Lo que eligió: un símbolo simple del rubro, dos colores y poco texto.
Con Higgsfield, el flujo para esto es `brand-asset-creation` (sin probar).

## Vista previa del anuncio

El link de `ads_get_ad_preview` no le abre a Jorge (viene con `&amp;` y vence en minutos). Se abre con Chromium, se
expande "Ver más", se recorre el carrusel y se le mandan las capturas.
