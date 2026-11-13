---
name: fotos-premium
description: Hacer o mejorar fotos con aspecto premium en Higgsfield, como las del pueblo de San Ignacio de Moxos del 13/11/2026 que Jorge aprobó ("quedó perfecto"). Usar cuando Jorge mande una foto y diga "editala", "mejorala", "ponele mejor luz", o pida fotos nuevas de un lugar, un terreno, un producto o una escena para un anuncio. Sirve para cualquier línea, no solo terrenos.
---

# Fotos premium con Higgsfield

**Probado el 13/11/2026** con tres fotos de San Ignacio de Moxos (`propiedades/lotes-san-ignacio-prompts-higgsfield.md`):
las tres salieron bien a la primera, 2 créditos cada una, y Jorge dijo *"ahora sí me gusta... quedó perfecto, las ideas y
demás"*. Esta skill es esa forma de trabajar. Las reglas de fondo están en `guias/imagenes.md` y la skill `generar-imagenes`.

**App:** Higgsfield. **Modelo:** `nano_banana_pro` (el job figura como `nano_banana_2`). **Flujo:** `product-photoshoot`
(modo `restyle` para mejorar una foto; escena nueva cuando se pide una imagen que no existe).

## 1. Entender antes de generar (gratis)
1. ¿Qué se vende, a quién y dónde va la imagen (post, carrusel, anuncio)? Leé la ficha del producto (`propiedades/`,
   `negocio.md`). La imagen tiene que tener **sentido y coherencia con lo que se vende** (Jorge: nada de "imágenes vacías").
2. **Investigá el lugar o el producto**: Wikipedia (curl a la API) para saber qué lo hace reconocible (en San Ignacio: las
   letras MOXOS de la plaza, la iglesia jesuita, la laguna Isireri, techos de teja, calles de tierra roja).
3. **Siempre una foto real de referencia**:
   - la que manda Jorge: `media_upload` → PUT con `curl` → `media_confirm`;
   - o una foto real con licencia libre de **Wikimedia Commons** (API `generator=categorymembers` +
     `iiextmetadatafilter=LicenseShortName|Artist`). Sirven CC BY, CC BY-SA y dominio público. Se importa con
     `media_import_url`. **Anotá autor y licencia**: el post tiene que nombrarlos.
   - Antes de elegir, bajá miniaturas (`Special:FilePath/<archivo>?width=1000`) y miralas.

## 2. El pedido (en inglés, por secciones)
Una imagen por pedido, completo y pensado (la mayoría de las repeticiones vienen de un pedido vago):

```
[SOURCE] (mejorar una foto) Restyle the referenced real photo of <qué y dónde>. PRESERVE exactly: <lista concreta de lo
         que no puede cambiar: letras y su orden/colores, edificios, techos, calles, árboles, el producto, su etiqueta>.
  o
[SUBJECT] (escena nueva) Photorealistic premium <tipo de foto> of <escena>. Match the <arquitectura/paisaje> of the
          referenced real photo of <lugar>: <rasgos reales>.
[SCENE] (solo escena nueva) <qué hay, qué se ve, el sentimiento: "your future home starts here">
[TRANSFORMATION] Premium <travel-editorial / real-estate drone / product> photograph at golden hour.
[COMPOSITION] Vertical 4:5 frame, <ángulo>, <lente: 24mm/35mm>, <qué va en cada tercio>, generous sky.
[LIGHTING] Warm late-afternoon sun, long soft shadows, warm glow on <superficie>, rich but natural color.
[STYLE] High-end <tourism / real-estate / product> campaign photography, crisp natural detail, natural color grading.
[AVOID] no change to <lo que se preserva>, no extra letters or words, no people, no cars, no added buildings,
        no AI artifacts, no warped or smeared text, no plastic look, no oversaturated HDR, no HDR halos,
        no oversharpened look, no stale stock-photo aesthetic, no watermarks.

resolution: 2k
```

Parámetros: `model: nano_banana_pro`, `resolution: 2k`, `aspect_ratio: 4:5` (feed; 1:1 para carrusel de anuncio, 9:16
historias), `count: 1`, `medias: [{value: <media_id>, role: image_references}]`, `use_unlim: false`.

## 3. Gastar poco
1. `balance` y `get_cost: true` (2 créditos por imagen el 13/11/2026). Decile a Jorge el total si él no lo pidió ya.
2. **Primero una sola imagen** con `generate_image_batch` (un pedido) y `jobs_wait`. **Nunca reenviar** una que tarda.
3. Bajala, mirala y comparala con la foto real. Si sirve, recién ahí las demás en un solo `generate_image_batch`.
4. Una corrección dice qué defecto arregla y usa la imagen anterior como referencia. Máximo dos por imagen.

## 4. Revisar antes de mostrar
- Lo que había que preservar está igual (letras, edificios, producto). Textos chicos: ampliar y leerlos.
- **Escena inventada (no es el producto ni el lugar real exacto): va con "Imagen referencial"** en la pieza.
- La IA no escribe datos que tienen que ser exactos (precio, medidas, teléfono): van con el script de láminas o en Canva.
- `upscale_image` inventa números y letras: nunca sobre planos o carteles (probado el 12/11/2026).

## 5. Entregar y dejar escrito
- Guardar en `fotos/<producto>/opciones-higgsfield/AAAA-MM-DD-opcion-N-<qué>.jpg`.
- Anotar en un archivo de prompts (`propiedades/<producto>-prompts-higgsfield.md`): prompt, foto de referencia (autor y
  licencia), job ID, créditos y qué dijo Jorge. Y una línea en `memory.md`.
- Mandarlas con `SendUserFile`, diciendo app, modelo y créditos. **Jorge elige** cuáles entran y dónde.
- Para armar la pieza final (carrusel, textos encima): **Canva**. Moda gratis pone un sello "moda.app" en lo que exporta.
