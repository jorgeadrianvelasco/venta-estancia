# Láminas de los lotes de San Ignacio de Moxos

Mismo estilo que las láminas de Calocha (`presentacion/fuente/`): azul noche, ocre y crema, Cormorant Garamond y Work Sans.
**El texto lo pone el script, no la IA** (`guias/imagenes.md`): todos los números salen de `propiedades/lotes-san-ignacio.md`.

```
python3 laminas_lotes.py <dir>            # copia antes img/terreno.jpg e img/letrero.jpg a <dir>/img/
NODE_PATH=$(npm root -g) node render_lotes.js <dir> <dir>/png
```

| Lámina | Contenido | Foto |
|---|---|---|
| 1 "Elegí tu lote" | Plano de los 10 lotes con sus m², "Desde 13 $US el m²", "Plano aprobado por la Alcaldía" | — (dibujo, geometría del diseño de Jorge) |
| 2 "Para vivir o para invertir" | 10 lotes · 642 a 1.641 m² · 13 $US el m² · plano aprobado | `img/terreno.jpg`: recorte de la foto real del letrero (y 1560→2500 de la versión 2160×3840) |
| 3 "Venta directa del dueño" | Foto real del letrero + WhatsApp | `img/letrero.jpg`: recorte 4:5 (y 300→3000) de la misma foto |

Carrusel armado (12/11/2026) en `fotos/lotes-san-ignacio/carrusel/`: 1 = diseño de Jorge (sin cambios), 2-4 = estas láminas.
