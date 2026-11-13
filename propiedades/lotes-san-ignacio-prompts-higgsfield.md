# Lotes de San Ignacio — 3 prompts para Higgsfield (13/11/2026)

Pedido de Jorge (13/11): *"imágenes generadas de lotes, de terrenos, pero que tenga sentido y coherencia con lo que estamos
vendiendo, que son terrenos en áreas urbanas en un pueblo boliviano... alguna foto de San Ignacio de Mojos, que es la
segunda foto... y la tercera sea referente a terrenos urbanos, pero a la vez rurales... Haceme esas 3 opciones"*.

**Cómo:** flujo `product-photoshoot` de Higgsfield (`guias/imagenes.md`), modelo `nano_banana_pro`, 2K, 4:5, 2 créditos por
imagen, una sola imagen por opción. Cada opción parte de una **foto real de San Ignacio de Moxos** de Wikimedia Commons como
referencia, para que el pueblo, las casas y las calles sean los de verdad.

| Opción | Para | Foto real de referencia (Wikimedia Commons, licencia) |
|---|---|---|
| 1 · El pueblo | 2.ª imagen | "Letras turísticas de Moxos", de Puya Raimondi (CC BY-SA 4.0) |
| 2 · Lotes en el pueblo, desde el aire | 3.ª imagen | "San Ignacio de Moxos vista aérea", de Gabvia (CC BY-SA 4.0) |
| 3 · Un lote urbano-rural, a nivel de calle | 3.ª imagen (alternativa) | "Calle en San Ignacio de Moxos-2022", de Carlillasa (CC BY-SA 4.0) |

**Créditos de las fotos:** la licencia CC BY-SA 4.0 permite uso comercial si se nombra al autor y la licencia. En el texto del
post va: *"Fotos base: Puya Raimondi, Gabvia y Carlillasa / Wikimedia Commons, CC BY-SA 4.0."*
**La opción 3 no es el lote real**: si se usa, lleva "Imagen referencial".

## Prompt 1 · El pueblo (San Ignacio de Moxos)

```
[SOURCE]
Restyle the referenced real photo of the main square of San Ignacio de Moxos, Beni, Bolivia. PRESERVE exactly: the large
colorful tourist letters spelling "MOXOS" (yellow M, yellow O, red X with the painted red-and-yellow feather fan above it,
green O, green S), the small "SAN IGNACIO" lettering on the yellow base, the long two-story colonial building behind with
white walls, dark wooden balcony and clay-tile roof, the palm fronds at the top right and the paved square.
[TRANSFORMATION]
Premium travel-editorial photograph of the town at golden hour.
[COMPOSITION]
Vertical 4:5 frame, eye level, 35mm. The MOXOS letters sit in the lower third, the colonial building across the middle,
generous deep-blue sky with soft scattered clouds above.
[LIGHTING]
Warm late-afternoon sun from the left, long soft shadows on the square, warm glow on the white walls, rich but natural color.
[STYLE]
High-end tourism and real-estate campaign photography, crisp natural detail, clean natural color grading, calm and inviting.
[AVOID]
no change to the spelling, shape, order or colors of the letters, no extra letters or words, no new signs, no people, no cars,
no added buildings, no AI artifacts, no warped or smeared text, no plastic look, no oversaturated HDR, no HDR halos, no
oversharpened look, no stale stock-photo aesthetic, no watermarks.
resolution: 2k
```

## Prompt 2 · Lotes en el pueblo, desde el aire

```
[SOURCE]
Restyle the referenced real aerial drone photo of San Ignacio de Moxos, a small town in the Beni lowlands of Bolivia.
PRESERVE: the town's grid of streets, the low houses with red clay-tile roofs, the many green open lots between the houses,
the trees, and the flat green savanna and forest on the horizon.
[TRANSFORMATION]
Premium golden-hour drone photograph for a residential land-sale campaign.
[COMPOSITION]
Vertical 4:5 frame, high oblique drone angle. The town grid fills the middle; the foreground shows the green open lots and a
straight street at the edge of town, so the viewer reads "lots inside a living town, with countryside around".
[LIGHTING]
Warm low sun, long shadows from trees and houses, lush natural greens, soft golden haze on the horizon, clear sky with a few
light clouds.
[STYLE]
High-end real-estate drone photography, crisp detail, natural color grading.
[AVOID]
no added buildings, no added roads, no skyscrapers, no swimming pools, no text, no labels, no lot numbers, no people, no AI
artifacts, no plastic look, no oversaturated HDR, no HDR halos, no oversharpened look, no stale stock-photo aesthetic,
no watermarks.
resolution: 2k
```

## Prompt 3 · Un lote urbano-rural, a nivel de calle

```
[SUBJECT]
Photorealistic premium real-estate photograph of an empty residential lot on the edge of a small town in the Bolivian
Amazon lowlands (Beni). Match the local architecture of the referenced real street photo of San Ignacio de Moxos: low
brick houses with red clay-tile roofs, a reddish earth street, a few tall palms and flowering trees.
[SCENE]
The lot is flat, freshly cleared, with short mowed green grass. Its corners are marked with short wooden stakes and a
taut white string boundary. A neighbor's low brick house with tile roof stands at one side; the street runs in front;
open green countryside and trees beyond. The feeling: "your future home starts here", town and countryside together.
[COMPOSITION]
Vertical 4:5 frame, eye level slightly elevated, 24mm, the lot in the foreground and center, street and neighbor house as
context, generous sky.
[LIGHTING]
Golden hour, warm low sun, long soft shadows across the grass, warm glow on the brick.
[STYLE]
High-end residential real-estate photography, natural color grading, crisp detail, calm and inviting.
[AVOID]
no house or construction inside the lot, no swimming pool, no fences other than the string, no people, no cars, no text,
no signs, no logos, no AI artifacts, no plastic look, no oversaturated HDR, no HDR halos, no oversharpened look, no stale
stock-photo aesthetic, no obviously composited background, no watermarks.
resolution: 2k
```

## Resultados

| Opción | Job de Higgsfield | Créditos | Revisión | Qué dijo Jorge |
|---|---|---|---|---|
| 1 | `2e7328fd-684d-475e-bc3b-739225b63896` | 2 | Letras "MOXOS", "SAN IGNACIO" y el edificio colonial iguales a la foto real; luz de atardecer | pendiente |
| 2 | `e21ef4c1-02f1-46da-833a-fe4e75534650` | 2 | Pueblo desde el aire: cuadrícula, techos de teja, lotes verdes, calles de tierra; atardecer. Es la foto real retocada: los detalles pueden no ser exactos | pendiente |
| 3 | `dc2c66b5-91a2-426b-9c00-89962ea5ac1c` | 2 | Lote con estacas e hilo, casa de ladrillo al lado, calle de tierra, palmeras y pampa; atardecer. **No es el lote real: va con "Imagen referencial"** | pendiente |

Total: **6 créditos** (126 → 120). Archivos: `fotos/lotes-san-ignacio/opciones-higgsfield/`. Modelo que figura en el job:
`nano_banana_2` (pedido como `nano_banana_pro`).
