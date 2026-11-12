# Higgsfield: cómo hacer las imágenes premium del carrusel de los lotes gastando pocos créditos

Consulta: 12/11/2026, alrededor de las 17:00 a 17:30 UTC. **No se generó nada y no se gastó ningún crédito**: el saldo era de 126
antes y después de la consulta (`balance`). Tampoco se cambiaron preferencias ni se crearon proyectos, carpetas ni marcas.

Pieza: carrusel vertical 4:5 (1080×1350) para la página y después como anuncio. La primera imagen es el diseño "VENTA DE LOTES" y la
última es la foto real del letrero. En el medio van 2 o 3 imágenes nuevas hechas con Higgsfield.

Marcas: `[DATO — fuente]` es lo visto en una herramienta o una página. `[ESTIMACIÓN]` es una cuenta o recomendación mía.

## Cómo se hizo

- Herramientas MCP de Higgsfield, todas de solo lectura: `balance`, `transactions`, `show_plans_and_credits`,
  `models_explore` (list, recommend y get), `get_workflow_instructions` y `get_workflow_bundle_file` (flujos `ads-studio`,
  `product-photoshoot` y `thumbnail-generation`), `get_presets` (marketing_studio / product-shot) y `show_medias`.
  También `generate_image`, `upscale_image` y `outpaint_image`, **siempre con `get_cost: true`**: devuelven el precio sin crear
  ningún trabajo. Y `ads_studio_quote`, que solo cotiza.
- Web: `WebFetch` no llega a higgsfield.ai (ENOTFOUND). **Con `curl` sí**: bajé los términos de uso, el centro de ayuda y
  docs.higgsfield.ai. La página de precios se arma con JavaScript y no trae los planes en el HTML. Para los planes uso el
  widget del MCP y fuentes de terceros.
- Miré el diseño y la foto del letrero que están en `fotos/lotes-san-ignacio/`.

## 1. Plan y créditos de la cuenta

| Qué | Valor | Fuente |
|---|---|---|
| Plan actual | **`basic`** | [DATO — `balance` y `show_plans_and_credits` (`current_plan: "basic"`)] |
| Créditos disponibles | **126** | [DATO — `balance`] |
| Movimientos | +10 (registro, 20/10) · +2 (reinicio diario, 20/10) · −2 y −2 (upscale bytedance, 12/11 a las 13:40 y 13:42) · **+120 "Subscription Credits" (12/11 a las 17:00 UTC)** | [DATO — `transactions`] |
| Planes por encima del de la cuenta | PLUS: 1.000 créditos/mes, 39 €/mes (29 €/mes pagando el año). ULTRA: 3.000 créditos/mes, 79 €/mes (65 €/mes anual). El widget dice *"Best upgrade from Basic"* | [DATO — `show_plans_and_credits`] |
| Precio del Basic | Las fuentes de terceros dicen **9 $US/mes con 120 créditos**, lo que coincide con la concesión de 120 que se ve en la cuenta. No lo pude ver en la página oficial | [DATO de terceros — búsqueda web; ver Fuentes] |
| Recargas sueltas | 500 créditos por 29,41 €, 1.000 por 55,56 €, 2.000 por 105,26 € y 4.000 por 210,53 €. **Vencen a los 90 días** | [DATO — `show_plans_and_credits`; [ayuda: vencimiento](https://higgsfield.ai/creator-hub/help-center/credits/top-up-credits-expire)] |
| Vencimiento de los créditos del plan | Se renuevan con cada ciclo y **los que no se usan se pierden** (no se acumulan) | [DATO — [ayuda: cómo funcionan los créditos](https://higgsfield.ai/creator-hub/help-center/credits/how-credits-work)] |
| Ilimitados / generaciones gratis | Para esta cuenta, `unlim.available: false`. Además, el centro de ayuda dice que los ilimitados y las generaciones gratis **solo valen en la web higgsfield.ai**: todo lo que se genera por MCP (o sea, desde acá) **siempre descuenta créditos** | [DATO — `models_explore` y [ayuda](https://higgsfield.ai/creator-hub/help-center/credits/how-credits-work)] |
| Marca de agua | Con cualquier plan pago **no hay marca de agua visible**. Higgsfield puede meter marcas invisibles de "hecho con IA" (C2PA) | [DATO — [ayuda: marca de agua](https://higgsfield.ai/creator-hub/help-center/credits/watermark-and-how-to-remove)] |

**Ojo:** El dueño entendió que contrató "el mejor modelo", pero la cuenta muestra el plan **Basic**, el de entrada. Según la
[ayuda de planes](https://higgsfield.ai/creator-hub/help-center/plans/how-do-higgsfield-plans-work), *"Entry-level plans include
core generation models. Higher plans unlock every model"*. `get_cost` da precio para todos los modelos, pero **eso no prueba que el
Basic pueda usarlos** (ver "Qué quedó sin verificar"). Para este trabajo alcanza con los 126 créditos (sección 5): no hace falta
comprar más.

## 2. Modelos de imagen, precios y para qué sirven

Precios con `get_cost`, para **1 imagen en 4:5**, salvo donde se aclara otra relación. El MCP devuelve dos números, `credits` y
`credits_exact`. Casi siempre coinciden; cuando no, van los dos.

### Precios verificados

| Modelo (id) | 1k | 2k | 4k | ¿4:5? | Referencias | Notas |
|---|---|---|---|---|---|---|
| **GPT Image 2.6** (`gpt_image_2_6`), calidad low | **0,25** | 0,5 | — | Sí | Sí (`image_references`, sin máximo en el esquema) | Modelo por defecto del MCP *"for ordinary generation, photorealistic images, typography, and reference-based editing"* |
| ídem, calidad medium | 0,5 | 1 | — | | | |
| ídem, calidad high | 1,5 | **2,75** | 4,25 | | | |
| ídem, calidad xhigh / max | — | 4,5 / 9 | — | | | |
| ídem, `batch_size` 4 (low, 1k) | **1** en total | | | | | Cada salida se cobra aparte (0,25 × 4) |
| ídem, con imagen de referencia (high 2k / medium 1k) | 0,5 | 2,75 | | | | **La referencia no cambia el precio** |
| GPT Image 2.6 Flare / GPT Image 2.5 (high) | | 2,75 | | Sí | Sí | Igual precio que 2.6 |
| GPT Image 2 (`gpt_image_2`), high | | 6 / 6,5 | | **No** (3:4) | Sí | Más caro y sin 4:5 |
| **Nano Banana Pro** (`nano_banana_pro`) | 2 | **2** | 4 | **Sí** (nativo) | Hasta 14 | **El 1k y el 2k cuestan lo mismo.** Con referencia, también 2 |
| Nano Banana 2 (`nano_banana_2`) | 1,5 | 2 | 3 | Sí | Hasta 14 + **máscara** (`is_inpaint`) | Puede editar solo la zona enmascarada |
| Nano Banana 2.1 (`nano_banana_2_1`) | 1,5 | 2 | 3 | Sí | Hasta 14 + máscara | **Tiene `seed`** |
| Nano Banana 2 Lite | 1 | — | — | Sí | Hasta 14 | Solo 1k |
| Nano Banana | 1 | | | Sí | Hasta 8 | Edición por instrucción |
| Cinema Studio Image 2.5 (`cinematic_studio_2_5`) | 2 | 2 | 4 | Sí | Sí | Estilo cine |
| FLUX 3 (`flux_3_image`) | 2 | 3 | **19** | Sí | Hasta 10 | El 4k es carísimo |
| FLUX.2 max | | 6 (3:4) | | No | Sí | |
| Seedream 5.0 Pro / 5.5 | | 2,5 / 3,5 (3:4) | | **No** | Sí | Edición por instrucción |
| Ideogram 4.5 | 1 (low) | 2 (medium) · 6,25 (high) | | Sí | Hasta 5 + máscara | **Tiene `seed`**; especialista en tipografía |
| Recraft V4.1 | 1,25 | **8** | | Sí | No acepta | |
| OpenAI Hazel (high) | 6 (2:3) | | | No | Sí | *"best text rendering"*, pero sin 4:5 |
| Marketing Studio Image (`marketing_studio_image`) | 2 | 2 | | Sí | Sí | Pensado para fotos de producto |
| Soul Location / Soul 2.0 / Soul Cinema | 1 / 0,12 exacto (3:4) | | | No | Soul Location: no | Paisajes y lugares. Precio ambiguo |
| Kling O1 Image | | 0,5 (3:4) | | No | Sí | |
| `upscale_image` (bytedance) | | | 2 | — | — | Es el que **inventó números y letras** el 12/11 |
| `outpaint_image` a 4:5 | 2 | | | Sí | — | Agranda el lienzo sin tocar lo que ya hay |
| Topaz (`topaz_image`) | no se pudo cotizar | | | | | Error 422: no admite estimación de costo |
| Ads Studio | no se pudo cotizar | | | **No** (solo 1:1, 9:16, 16:9 y 3:4) | | Para cotizar hay que crear antes una "marca" en Higgsfield, y no la creé |

[DATO — `models_explore` y `get_cost`, 12/11/2026. Lo de "hasta 14" y "hasta 8" referencias es de la
[ayuda de Nano Banana](https://higgsfield.ai/creator-hub/help-center/ai-models/how-do-i-use-nano-banana)]

### Cuál conviene para cada cosa

| Necesidad | Recomendación | Por qué |
|---|---|---|
| (a) Fotos premium fotorrealistas (paisaje, atardecer, casa de ejemplo, detalle del terreno) | **Final: Nano Banana Pro, 2k, 4:5 → 2 créditos.** Borrador: GPT Image 2.6 low 1k → 0,25 | Los flujos de Higgsfield para fotos terminadas fijan este modelo: *"Model is always `nano_banana_pro`"* (product-photoshoot) y *"Main thumbnail render: nano_banana_pro"* (thumbnail-generation). Tiene 4:5 nativo y su 2k cuesta igual que su 1k [DATO]. **Esta elección es mía** [ESTIMACIÓN] |
| (b) Texto en español dentro de la imagen | **Mejor no pedirle texto a la IA:** el texto se pone en Moda o Canva. Si igual se quiere, conviene Nano Banana Pro o GPT Image 2.6 con el texto corto entre comillas, y revisar letra por letra | La ayuda de Higgsfield dice que *"GPT Image handles text rendering and precise color better than most"* y que Nano Banana Pro y 2 *"render accurate typography"*. Pero el propio flujo de miniaturas de Higgsfield indica *"Default: NO text in the image — … headline text belongs in a crisp typographic overlay … (zero generation credits, always legible)"*. Y el upscale ya inventó números en esta cuenta |
| (c) Mejorar la foto real del letrero sin cambiarle el contenido | **No pasarla por IA generativa:** recortar a 4:5 en Moda o Canva (0 créditos). Si se quiere un cielo mejor: Nano Banana 2 con **máscara solo sobre el cielo** (2 créditos, 2k) y después pegar encima el cartel original | Cualquier modelo que redibuja toda la imagen puede cambiar letras del cartel. La máscara (`is_inpaint`) limita la edición a la zona marcada, pero eso no lo probé [ESTIMACIÓN]. `outpaint_image` (2 créditos) solo hace falta si se quiere agrandar el lienzo; el recorte alcanza |

## 3. Cómo gastar menos

Datos (de herramientas y ayuda):
- **Borradores casi gratis:** GPT Image 2.6 low 1k cuesta **0,25**, y 4 variantes con `batch_size: 4` cuestan **1 crédito** en total.
  Cada salida se cobra aparte, también con `count` [DATO — `get_cost`; [ayuda: qué gasta créditos](https://higgsfield.ai/creator-hub/help-center/credits/what-uses-my-credits)].
- **En Nano Banana Pro no conviene borrador en 1k**, porque cuesta lo mismo que 2k (2 créditos). El borrador barato tiene que hacerse
  con otro modelo [DATO].
- **La resolución 4k no sirve para Facebook** (la pieza es 1080×1350) y duplica el costo: 4 créditos en Nano Banana Pro, 19 en FLUX 3.
  El flujo de miniaturas da 4:5 en 4K = 3712×4608, así que en 2K queda cerca de 1856×2304, de sobra para 1080×1350
  [DATO del tamaño 4K — flujo `thumbnail-generation`; lo del 2K es ESTIMACIÓN].
- **`seed`:** por MCP solo la tienen Nano Banana 2.1 e Ideogram 4.5. GPT Image 2.6 y Nano Banana Pro no la tienen. Para repetir o
  ajustar una imagen se pasa **el id del trabajo terminado como imagen de referencia**, algo que el MCP acepta: *"job_id from a prior
  generation"* [DATO — esquemas de `generate_image` y `models_explore`].
- **Batch:** `generate_image_batch` manda hasta 12 pedidos distintos de una vez, pero no permite `get_cost` adentro. Antes hay que
  cotizar cada uno con `generate_image` y `get_cost` [DATO — esquema].
- **`use_unlim` y generaciones gratis: no aplican.** La cuenta no tiene ilimitados (`available: false`), y por MCP siempre se cobra
  [DATO]. La promo "11.11" (hasta el 15/11/2026, 00:00 UTC) da ilimitados de Nano Banana Pro y GPT Image 2.5 **al pasarse a un plan
  mayor** y **solo en la web**. Para gastar unos 15 créditos no hace falta [DATO de la promo — `show_plans_and_credits`; la
  conclusión es mía].
- Lo que más gasta o conviene evitar: FLUX 3 en 4k (19), GPT Image 2.6 max (9), Recraft en 2k (8), GPT Image 2 (6,5 y sin 4:5),
  Ideogram high 2k (6,25), OpenAI Hazel (6 y sin 4:5), **cualquier upscale o regeneración sobre imágenes con números**, y pedir
  muchas variantes del final [DATO de precios; la selección es mía].
- Los créditos del plan **vencen en la renovación** y no se acumulan: no sirve guardarlos [DATO — ayuda].

Recomendación [ESTIMACIÓN]:
1. Explorar barato: **GPT Image 2.6, low, 1k, 4:5, `batch_size: 4`**, una llamada por concepto (1 crédito cada una).
2. Elegir con el dueño **una** variante por concepto.
3. Hacer el final en **Nano Banana Pro 2k 4:5**, con el borrador elegido como `image_references` y el prompt completo (2 créditos).
4. Corregir **una sola cosa por vez** y como máximo 2 veces por imagen. El flujo de Higgsfield fija *"max 3 generations per final
   output"*. Si algo sale mal, cambiar el prompt **o** la referencia, no los dos a la vez (ayuda de Nano Banana).

## 4. Cómo escribir los prompts para una publicidad premium

Lo que dicen las fuentes:

- **Estructura.** Según Google: *"[Subject] + [Action] + [Location/context] + [Composition] + [Style]"*; con referencias,
  *"[Reference images] + [Relationship instruction] + [New scenario]"*. Según Higgsfield: sujeto, composición, acción, lugar y estilo,
  con la relación de aspecto escrita en números [DATO — [guía de Google](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana) y [guía de prompts de Higgsfield](https://higgsfield.ai/nano-banana-pro-prompt-guide)].
- **Escribir en inglés.** Los textos que van impresos en la imagen quedan en español, tal cual: *"Assemble prompts in English …
  Preserve exact user-requested on-image strings in their original language"* [DATO — flujo `product-photoshoot`].
- **Vocabulario de fotografía, nunca palabras vagas.** Para la luz: dirección y calidad, más la temperatura en Kelvin (por ejemplo
  *"golden hour backlight", "3500K"*). Para la lente: distancia focal y apertura (*"24mm wide", "f/8"*). Para la profundidad de
  campo y las sombras, términos concretos. Hay que evitar *"good lighting", "high quality", "realistic", "professional photo"*
  [DATO — `references/photography-vocabulary.md` del flujo `product-photoshoot`].
- **Carrusel coherente.** Antes de generar se fija un "sistema visual" (paleta, luz, altura de cámara, regla de composición) y se
  copia igual en el prompt de cada imagen. Para Instagram y Facebook se usa 4:5 [DATO — `references/social-carousel.md`].
- **"Negative".** Ningún modelo del MCP tiene un parámetro `negative_prompt` (ver los esquemas). Los flujos de Higgsfield agregan al
  final del prompt un bloque de texto `[AVOID]` (*"no AI artifacts, no warped or smeared text, no fake words baked into the image,
  … no watermarks"*). Google, en cambio, recomienda decir lo que se quiere (*"empty street" instead of "no cars"*). Conviene usar
  las dos cosas [DATO — `references/negative-prompts.md`; guía de Google].
- **Respetar una imagen de referencia.** Decir qué se mantiene y qué cambia: *"Keep the exact same … Change only …"*. En una
  corrección: *"Keep composition, subject, framing, and overall scene IDENTICAL. Only change: …"*. Con 2 o más imágenes, empezar
  con *"IMAGE REFERENCES: image 1 = …; image 2 = …"* [DATO — [ayuda: cómo escribir un buen prompt](https://higgsfield.ai/creator-hub/help-center/getting-started/how-do-i-write-a-good-prompt), `references/refinement-pass.md` y flujo `thumbnail-generation`].
- **Texto exacto, si hace falta.** Ponerlo entre comillas, describir el tipo de letra, el tamaño y la ubicación, y agregar *"No
  other text"*. Después, verificar letra por letra; si falla, generar la imagen limpia y poner el texto encima con una herramienta
  común [DATO — ayuda de Nano Banana, guía de Google y flujo `thumbnail-generation`].
- **No reservar "espacio vacío" para el texto.** Si se pide *"clean negative space"*, el modelo dibuja una franja plana que queda fea.
  Lo que sí funciona es *"one area of the frame visually calm and tonally uniform … sky, blurred background"* [DATO — `references/typography.md`].

**Marketing Studio y Ads Studio: no convienen para este caso** [DATO de lo visto; la conclusión es mía]:
- Marketing Studio, en `get_presets` / product-shot, tiene 418 plantillas de **producto físico** (latas, envases, hielo). `marketing_studio_image`
  cuesta 2 créditos y tiene 4:5, pero está hecho para *"product image ads"*.
- Ads Studio arma anuncios de Meta completos, con textos que **escribe él mismo**. **No tiene 4:5** (*"4:5 is not available"*) y
  para cotizar pide crear una "marca". Hay riesgo de que invente atributos, como servicios, y eso choca con la regla 4 de `reglas.md`.

### Prompts propuestos para los 3 conceptos [ESTIMACIÓN: borradores para revisar con el dueño]

Sistema visual, copiado igual en los tres:
`[VISUAL SYSTEM] Warm late-afternoon golden hour, sun low behind camera-left, ~3500K warm key with long soft shadows; palette of deep
grass greens, warm ochre and straw, soft cream-blue sky; natural filmic grade, gentle contrast, no HDR; eye-level or slightly elevated
camera; rule of thirds. Photorealistic editorial real-estate photography, tack-sharp, true-to-life textures.`

1. **"La región"** (llevará la leyenda "Imagen referencial de la región"):
   `Wide landscape of the Beni lowland savanna in Bolivia: flat open grassland with tall green and golden grass in the foreground,
   scattered motacú palms and tropical trees along a low horizon, huge sky with a few cumulus clouds. 24mm wide, f/8, deep depth of field.
   4:5 vertical. No text, no signs, no people, no buildings, no roads.`
2. **"Tu casa"** (llevará "Imagen ilustrativa: ejemplo de vivienda"):
   `A modern single-story tropical house with a wide covered veranda, cream walls and clay-tile roof, set back on a spacious lawn with a
   large mango tree, at blue hour with warm interior lights glowing; calm, aspirational but realistic for a small lowland town. 35mm, f/5.6.
   4:5 vertical. No text, no house numbers, no people.`
3. **"Tu inversión"** (llevará "Imagen ilustrativa"):
   `Close detail of a wooden survey stake with a bright red ribbon standing in tall green grass, wire fence posts softly blurred behind,
   open field at golden hour, shallow depth of field. 85mm, f/2.8. 4:5 vertical. No text, no numbers.`

Cierre común: `[AVOID] no AI artifacts, no text or letters anywhere, no fake signs, no logos or brand names, no watermarks, no paved
avenues, no streetlights, no landmarks, no plastic look, no oversaturated HDR.` y al final `resolution: 2k`.

Así se llama a la herramienta:
- Borrador: `{"model":"gpt_image_2_6","aspect_ratio":"4:5","resolution":"1k","quality":"low","batch_size":4,"prompt":"…"}`.
  Cuesta 1 crédito [DATO — get_cost].
- Final: `{"model":"nano_banana_pro","aspect_ratio":"4:5","resolution":"2k","prompt":"IMAGE REFERENCES: image 1 = composition draft — keep
  its framing and layout, re-render with full photographic detail. …","medias":[{"value":"<job_id del borrador elegido>","role":"image_references"}]}`.
  Cuesta 2 créditos [DATO — get_cost].

## 5. Recomendación para nuestro caso [ESTIMACIÓN]

| Paso | Qué | Modelo y ajustes | Créditos |
|---|---|---|---|
| 0 | El dueño aprueba los 3 conceptos y los prompts (sección 4) | — | 0 |
| 1 | Borradores: 4 variantes por concepto | GPT Image 2.6 · low · 1k · 4:5 · `batch_size` 4 | 3 × 1 = **3** |
| 2 | El dueño elige 1 variante por concepto | — | 0 |
| 3 | Finales, con el borrador elegido como referencia | Nano Banana Pro · 2k · 4:5 | 3 × 2 = **6** |
| 4 | Una corrección puntual por imagen, si hace falta | Nano Banana Pro · 2k · referencia = el final anterior | hasta 3 × 2 = **6** |
| 5 | Letrero: recortar a 4:5 de modo que el cartel quede arriba y se pierda la franja de abajo con "Meta AI" y la fecha | Moda o Canva, sin IA | **0** |
| 6 | Textos, leyendas "Imagen referencial/ilustrativa", logo y WhatsApp | Moda (donde ya está la publicación) o Canva | **0** |
| | **Total** | | **9 como mínimo, ~15 lo probable, 20 como techo**, de 126 |

- Si Nano Banana Pro no anda con el plan Basic: hacer el final con **GPT Image 2.6, high, 2k (2,75 créditos)** o Nano Banana 2 en 2k
  (2 créditos). El paso 1 sirve además como prueba barata de acceso (0,25 créditos por imagen).
- **Para que la IA no invente datos:** las imágenes de Higgsfield van **sin texto ni números**. Precio, metros, número de lote,
  avenidas y WhatsApp se ponen en Moda o Canva, copiados de `propiedades/lotes-san-ignacio.md`. Antes de publicar, alguien lee cada
  número contra esa ficha. **Nada de upscale de IA** sobre el diseño, el plano o el letrero.
- Para Moda o Canva conviene bajar la imagen apenas termina. Para la API, Higgsfield guarda los archivos 7 días; no verifiqué si en la
  web es igual ([docs: facturación y retención](https://docs.higgsfield.ai/docs/concepts/billing-and-retention.md)).

## 6. Riesgos

| Riesgo | Qué hacer | Base |
|---|---|---|
| **Una "vista aérea" generada puede parecer el terreno real** sin serlo: se vería una avenida asfaltada, arbolada o con servicios que no existen | **No generar vistas aéreas "de nuestros lotes".** Las imágenes de IA muestran la región, un ejemplo de casa o un detalle simbólico, y llevan una leyenda chica pero legible: "Imagen referencial" o "Imagen ilustrativa". Nada de infraestructura no confirmada (asfalto, alumbrado, agua, luz) ni edificios conocidos de San Ignacio | Ley 453 de Bolivia, art. 5: *"Publicidad Engañosa. Es cualquier modalidad de publicidad … total o parcialmente falsa que induzca a error respecto a las características … del producto"* [DATO — [Lexivox](https://www.lexivox.org/norms/BO-L-N453.html)]. Los términos de Higgsfield (5.1) prohíben lo *"deceptive"* |
| **El fondo aéreo del diseño ya hecho (imagen 1) parece ilustrativo:** muestra una avenida asfaltada con árboles y en la foto del letrero se ve campo abierto con un camino de tierra | Preguntarle al dueño si esa vista es del lugar. Si no lo es, agregar también ahí "imagen referencial" | [DATO — vi las dos imágenes; si es o no el lugar real es **pendiente**] |
| **La IA inventa texto y números** | Ningún texto ni número generado por IA. Revisar todo a mano antes de publicar | Pasó con el upscale el 12/11 (`memory.md`) |
| **La foto del letrero tiene una marca "Meta AI" y la fecha "11/11/26" abajo a la derecha**, y el cartel impreso tiene palabras mal escritas ("PLOSVALIN", "CHRSTIATI", "DESSOROLLO") | El recorte a 4:5 elimina la marca y la fecha. Las palabras mal escritas son del cartel real: con IA no se corrigen sin riesgo. Que el dueño decida si lo deja así o achica el cartel en el encuadre | [DATO — vi `2026-11-12-letrero-mejorado-13-usd-m2.jpg`. No tiene marca de agua de Higgsfield. La ficha ya anota las faltas] |
| **Meta puede marcar el anuncio como "Información de IA"** | Es esperable. Los términos de Higgsfield (5.5) piden no borrar las marcas de origen | Higgsfield puede meter marcas C2PA (términos 6.4) y Meta detecta herramientas de terceros por *"industry-standard signals"* [DATO — [Meta](https://www.meta.com/en-gb/help/artificial-intelligence/355108217670024/) y [términos](https://higgsfield.ai/terms)] |
| **Derechos de uso** | El uso comercial está permitido. No pedir marcas comerciales, logos ni caras de personas reales | Términos 4.4: *"does not claim ownership of any of your Inputs or Outputs, nor does it restrict your commercial use of Outputs"*. La protección legal (indemnización) es solo del plan Enterprise [DATO — [ayuda: uso comercial](https://higgsfield.ai/creator-hub/help-center/account/who-owns-my-generations-and-can-i-use-them-commercially)] |
| **Datos personales:** lo que se sube puede usarse para entrenar modelos | En la cuenta hay **2 imágenes subidas el 12/11**. Según `memory.md` eran el plano (que tiene nombres y firmas) y el cartel. Que el dueño decida si las borra desde la web; el MCP no tiene una herramienta para borrar medias. No subir más documentos con nombres | Términos 4.4: *"Your Content, Inputs, and Outputs may be used by Company to train"*; se corta borrando el contenido [DATO — `show_medias` y términos] |
| **El plan Basic puede no incluir todos los modelos** | Probar primero lo más barato y tener la alternativa del paso 5 | [DATO — ayuda de planes] |

## Qué quedó sin verificar

- **Si el plan Basic puede usar Nano Banana Pro y GPT Image 2.6.** `get_cost` da el precio, pero no comprueba si el plan tiene
  acceso. Con el plan gratis, GPT Image 2.6 pedía plan pago; con el Basic no se probó, porque probarlo es generar.
- **El precio y la lista de modelos del Basic en la página oficial.** La página de precios no trae los planes en el HTML. El "9 $US /
  120 créditos" sale de terceros; solo los 120 créditos coinciden con la cuenta.
- **Qué número se cobra cuando `credits` y `credits_exact` no coinciden** (Soul: 1 contra 0,12; GPT Image 2: 6 contra 6,5).
- **Cuántas imágenes en paralelo** permite el Basic.
- **El costo de Ads Studio**, porque pide crear una marca, y **el de Topaz**, porque la estimación da error 422.
- **La calidad real de cada modelo** con estos prompts: no se generó nada. La elección de Nano Banana Pro para el final se apoya en
  los flujos de Higgsfield, no en una prueba.
- **Si la máscara de Nano Banana 2 deja intacto el cartel** al cambiar solo el cielo.
- **Si el fondo aéreo del diseño es el lugar real.**
- Si en la web (no en la API) los archivos generados también se borran a los 7 días.

## Fuentes (consultadas el 12/11/2026)

Herramientas MCP de Higgsfield, 12/11/2026, ~17:00 a 17:30 UTC: `balance`, `transactions`, `show_plans_and_credits`,
`models_explore` (list, recommend y get de `gpt_image_2_6` y `nano_banana_pro`), `generate_image`, `upscale_image` y `outpaint_image`
con `get_cost: true`, `ads_studio_quote`, `get_presets` (marketing_studio / product-shot), `show_medias`, y `get_workflow_instructions`
y `get_workflow_bundle_file` (flujos `ads-studio`, `product-photoshoot` con `typography.md`, `negative-prompts.md`,
`social-carousel.md`, `restyle.md`, `photography-vocabulary.md`, `refinement-pass.md` y `ad-creative-pack.md`, y
`thumbnail-generation` con `thumbnail-frameworks.md`).

Web:
- Higgsfield, términos de uso (última actualización: 23/10/2026): https://higgsfield.ai/terms
- Ayuda: uso comercial: https://higgsfield.ai/creator-hub/help-center/account/who-owns-my-generations-and-can-i-use-them-commercially
- Ayuda: cómo funcionan los créditos: https://higgsfield.ai/creator-hub/help-center/credits/how-credits-work
- Ayuda: qué gasta créditos: https://higgsfield.ai/creator-hub/help-center/credits/what-uses-my-credits
- Ayuda: vencimiento de recargas: https://higgsfield.ai/creator-hub/help-center/credits/top-up-credits-expire
- Ayuda: modelos ilimitados: https://higgsfield.ai/creator-hub/help-center/credits/what-are-unlimited-models-and-which-plans-include-them
- Ayuda: marca de agua: https://higgsfield.ai/creator-hub/help-center/credits/watermark-and-how-to-remove
- Ayuda: cómo funcionan los planes: https://higgsfield.ai/creator-hub/help-center/plans/how-do-higgsfield-plans-work
- Ayuda: cómo escribir un buen prompt: https://higgsfield.ai/creator-hub/help-center/getting-started/how-do-i-write-a-good-prompt
- Ayuda: Nano Banana: https://higgsfield.ai/creator-hub/help-center/ai-models/how-do-i-use-nano-banana
- Ayuda: qué modelo usar: https://higgsfield.ai/creator-hub/help-center/ai-models/which-ai-model-should-i-use
- Guía de prompts de Nano Banana Pro (Higgsfield): https://higgsfield.ai/nano-banana-pro-prompt-guide
- Docs de la API, facturación y retención: https://docs.higgsfield.ai/docs/concepts/billing-and-retention.md
- Google Cloud, "The ultimate Nano Banana prompting guide" (06/03/2026): https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana
- Meta, cómo se identifican y etiquetan las imágenes de IA en los anuncios: https://www.meta.com/en-gb/help/artificial-intelligence/355108217670024/
- Meta, "Expanding GenAI Transparency for Meta's Ads Products": https://about.fb.com/news/2025/02/gen-ai-transparency-metas-ads-products/
- Ley 453 de Bolivia (derechos de usuarios y consumidores): https://www.lexivox.org/norms/BO-L-N453.html
- Precio del Basic, fuentes de terceros sin verificar en la web oficial: https://www.imagine.art/blogs/higgsfield-ai-pricing ·
  https://blog.segmind.com/higgsfield-credits-explained-expiry-rules-and-real-cost/ · https://www.g2.com/products/higgsfield/pricing
