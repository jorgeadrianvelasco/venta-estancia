# Fuente de la presentación de Calocha

`laminas.py` genera las 8 láminas en HTML (1080×1350) y `render.js` las pasa a PNG con Chromium (Playwright):

```
python3 laminas.py <dir_html> img/        # vista previa local (fotos en <dir_html>/img/)
python3 laminas.py <dir_html> "{{"        # con tokens {{portada}}, {{mapa}}… para Creative Claw (render_html_image)
NODE_PATH=$(npm root -g) node render.js <dir_html> <dir_png>
```

Fotos en `img/` (todas de `fotos/`, recortadas a la proporción de cada marco, ancho completo):

| Archivo | Origen | Recorte (y desde arriba, en px del original) |
|---|---|---|
| `portada.jpg` | `2025-drone-laguna-casa-y-camino.jpg` | 309 → 1771 (4:5) |
| `laguna.jpg` | `2025-orilla-pasto-y-laguna.jpg` | entera |
| `pampa.jpg` | `2025-drone-pampa.jpg` | 330, proporción 1080:500 |
| `casa.jpg` | `2025-10-17-boost-marketplace-vista-aerea.jpg` | 220, proporción 920:540 |
| `alambrado.jpg` | `2025-drone-alambrado-hacia-la-laguna.jpg` | 120, proporción 1080:760 |
| `camino.jpg` | `2025-drone-camino-interno-y-pampa.jpg` | 700, proporción 600:570 |
| `cierre.jpg` | `2025-drone-laguna-casa-y-camino.jpg` | 0, proporción 4:5 |
| `mapa.png` | Mapa de Moda (Mapbox/OpenStreetMap) centrado en el pin -14.884522, -64.857659, zoom 11.3 | 920×500 |
