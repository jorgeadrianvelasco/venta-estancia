---
name: generar-imagenes
description: Hacer imágenes para anuncios, la página o una presentación de esta línea, gastando la menor cantidad de créditos. Usar cuando Jorge pida una imagen, una foto, una lámina, un carrusel, un logo, una portada o "mejorá esta foto". Sigue el orden Higgsfield, después Moda, después Canva, usa siempre la foto real del producto y cotiza antes de gastar.
---

# Generar imágenes

El detalle (modelos, precios, flujos, trampas) está en `guias/imagenes.md`. Esta skill es el orden y los controles
que no se saltean. Orden decidido por Jorge el 12/11/2026: **Higgsfield → Moda → Canva**.

## 0. Antes de tocar nada
1. **El producto es siempre el real.** En la estancia, "el producto real" son **las fotos reales de Calocha**
   (`fotos/`, catálogo en `fotos/README.md`). Higgsfield **solo puede mejorarlas**: resolución, encuadre, cielo y luz.
   **Nunca agregar cosas que el predio no tiene** (ganado, casas, corrales, agua, caminos, árboles, gente) ni sacar lo
   que sí tiene. Si la imagen muestra algo distinto de la foto, se descarta. Sin foto real no se hace imagen del
   predio: se le pide a Jorge. Logo o portada sin el predio no necesitan foto (`reglas.md`, regla 4; `fotos/README.md`).
2. **Texto que tiene que ser exacto** (precio, teléfono, medidas) no lo escribe la IA: va en el Administrador de Meta
   o con el script de láminas (`presentacion/fuente/`).
3. Leé en `memory.md` si ya hay una imagen aprobada que sirva (`fotos/generadas/`). **Reusar no cuesta nada.**

## 1. Higgsfield
1. `balance`. Si da 0, pasá al paso 2 y avisale a Jorge. No compres créditos.
2. Elegí la herramienta (tabla de `guias/imagenes.md`):
   - foto de producto, escena, carrusel o pack de avisos: flujo `product-photoshoot`, con la foto real como referencia;
   - aviso con copy: flujo `ads-studio`;
   - logo o portada: `gpt_image_2_6` o el flujo `brand-asset-creation`;
   - mejorar una foto real: `upscale_image`, `remove_background` o `flux_2_pro_outpaint`.
3. Subí la foto real (`media_upload` → PUT con `curl` → `media_confirm`).
4. Escribí el pedido completo: modo, escena, luz, paleta, proporción y qué evitar, incluyendo "no cambiar la forma, el
   color ni la etiqueta del producto".
5. **Cotizá** con `get_cost: true` el total de la tanda. Decile a Jorge cuántos créditos son y cuántos quedan, y
   esperá su sí.
6. **Primero 1 imagen.** Esperala con `jobs_wait` (sin volver a mandarla), bajala y mirala junto a la foto real.
   - Si el producto cambió en algo: descartala y corregí el pedido. Máximo dos correcciones por imagen.
   - Si sirve: recién ahí las demás variantes.
7. 2K para anuncios. 4K solo para una imagen aprobada que lo necesite, con `upscale_image`.

## 2. Moda (si Higgsfield no tiene créditos o no puede)
`moda_bootstrap` y la skill que corresponda. Ojo: el plan gratis pone un sello "moda.app" en lo exportado. Sirve
sobre todo para láminas, presentaciones y el mapa.

## 3. Canva (último recurso)
Solo `generate-image` para logo o portada. **Nunca `create-design` para piezas con producto**: mete fotos de stock.

## 4. Mostrar y dejarlo escrito
- Mandale a Jorge las imágenes con `SendUserFile`, diciendo qué herramienta se usó y cuántos créditos costó.
  **No va a ningún anuncio sin su aprobación.**
- Las aprobadas van a `fotos/generadas/` con una fila en `fotos/README.md`: de qué foto real salió, herramienta, ID de
  Higgsfield y fecha.
- `memory.md`: qué se pidió, cuántos créditos, qué dijo Jorge. Si aprendiste algo que sirve para todas las líneas,
  avisale para llevarlo a la base.
