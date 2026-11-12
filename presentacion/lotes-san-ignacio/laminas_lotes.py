"""Láminas premium (1080x1350) de los lotes de San Ignacio de Moxos, con texto exacto (sin IA).

Uso: python3 laminas_lotes.py <dir_salida>    (las fotos van en <dir_salida>/img/)
Fotos que usa: img/terreno.jpg (foto real del terreno, 4:5) e img/letrero.jpg (foto real del letrero, 4:5).
Render: NODE_PATH=$(npm root -g) node ../fuente/render.js <dir_salida> <dir_png>  (renderiza lamina-1..N existentes)

Datos (propiedades/lotes-san-ignacio.md, plano 2/5 y diseño de Jorge): 10 lotes de 642 a 1.641 m², esquina Av.
Circunvalación y Av. al Aeropuerto, desde 13 $US el m² (lote más chico), plano aprobado por la Alcaldía.
"""
import sys, os

OUT = sys.argv[1]
NAVY, OCRE, OCRE_OSC, CREMA = "#18222F", "#C8963E", "#A87A2A", "#F2ECE1"
W, H = 1080, 1350

CSS = f"""
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;1,500&family=Work+Sans:wght@400;600&display=swap');
html,body{{margin:0;padding:0;width:{W}px;height:{H}px;overflow:hidden}}
body{{position:relative;font-family:'Work Sans',sans-serif;-webkit-font-smoothing:antialiased}}
.abs{{position:absolute;margin:0}}
.serif{{font-family:'Cormorant Garamond',serif;font-weight:600;font-variant-numeric:lining-nums}}
text{{font-variant-numeric:lining-nums}}
.idx{{font-size:22px;font-weight:600;letter-spacing:4px}}
.etq{{font-size:24px;font-weight:600;letter-spacing:6px;text-transform:uppercase}}
.foto{{object-fit:cover;display:block}}
"""


def pagina(fondo, cuerpo):
    return f'<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{CSS}</style></head><body style="background:{fondo}">{cuerpo}</body></html>'


def velo(top, alto, paradas):
    return f'<div class="abs" style="left:0;top:{top}px;width:{W}px;height:{alto}px;background:linear-gradient(180deg,{paradas})"></div>'


def alambrado(color, op, x0=72, x1=1008, y=1296, paso=46, alto=30):
    p = [f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{color}" stroke-width="2" opacity="{op}"/>',
         f'<line x1="{x0}" y1="{y+12}" x2="{x1}" y2="{y+12}" stroke="{color}" stroke-width="1" opacity="{op*0.65:.2f}"/>']
    x = x0
    while x <= x1:
        p.append(f'<rect x="{x}" y="{y-10}" width="3" height="{alto}" fill="{color}" opacity="{op}"/>')
        x += paso
    return f'<svg class="abs" style="left:0;top:0" width="{W}" height="{H}">{"".join(p)}</svg>'


def plano(x0, y0, esc):
    """Plano de los 10 lotes. Geometría tomada del diseño de Jorge (misma posición relativa de cada lote).
    Coordenadas base: borde izquierdo 0, base 445, hipotenusa de (147,0) a (540,445)."""
    def hx(y):  # x de la hipotenusa a la altura y
        return 147 + (540 - 147) * y / 445
    lotes = [  # (n, m2, polígono en coordenadas base)
        (1, "1021", [(0, 0), (147, 0), (hx(52), 52), (0, 52)]),
        (2, "1050", [(0, 52), (hx(52), 52), (hx(104), 104), (0, 104)]),
        (3, "1245", [(0, 104), (hx(104), 104), (hx(170), 170), (0, 170)]),
        (10, "1489", [(0, 170), (80, 170), (80, 445), (0, 445)]),
        (9, "1139", [(80, 170), (161, 170), (161, 445), (80, 445)]),
        (4, "1122", [(161, 170), (hx(170), 170), (hx(242), 242), (161, 242)]),
        (5, "970", [(161, 242), (hx(242), 242), (hx(312), 312), (161, 312)]),
        (8, "642", [(161, 312), (243, 312), (243, 445), (161, 445)]),
        (7, "648", [(243, 312), (325, 312), (325, 445), (243, 445)]),
        (6, "1641", [(325, 312), (hx(312), 312), (540, 445), (325, 445)]),
    ]
    sv = []
    for n, m2, pts in lotes:
        P = [(x0 + x * esc, y0 + y * esc) for x, y in pts]
        d = " ".join(f"{x:.1f},{y:.1f}" for x, y in P)
        sv.append(f'<polygon points="{d}" fill="{CREMA}" fill-opacity="0.06" stroke="{OCRE}" stroke-width="2"/>')
        # centro aproximado (promedio de vértices), un poco a la izquierda en los que tocan la hipotenusa
        cx = sum(x for x, _ in P) / len(P)
        cy = sum(y for _, y in P) / len(P)
        if n in (1, 2, 3):
            cx = x0 + 0.38 * (hx((pts[0][1] + pts[2][1]) / 2)) * esc
        if n in (4, 5):
            cx = x0 + (161 + (hx((pts[0][1] + pts[2][1]) / 2) - 161) * 0.45) * esc
        if n == 6:
            cx = x0 + 395 * esc
        sv.append(f'<text x="{cx:.1f}" y="{cy - 4:.1f}" text-anchor="middle" font-family="Work Sans" font-weight="600" font-size="{int(15*esc)}" letter-spacing="2" fill="{OCRE}">LOTE {n}</text>')
        sv.append(f'<text x="{cx:.1f}" y="{cy + 20*esc:.1f}" text-anchor="middle" font-family="Cormorant Garamond" font-weight="600" font-size="{int(23*esc)}" fill="{CREMA}">{m2} m²</text>')
    # calles
    sv.append(f'<text x="{x0 + 270*esc:.1f}" y="{y0 + 475*esc:.1f}" text-anchor="middle" font-family="Work Sans" font-weight="600" font-size="{int(14*esc)}" letter-spacing="5" fill="{CREMA}" opacity=".7">AV. AL AEROPUERTO</text>')
    ang = 48.6
    sx, sy = x0 + 372 * esc, y0 + 205 * esc
    sv.append(f'<text x="{sx:.1f}" y="{sy:.1f}" transform="rotate({ang} {sx:.1f} {sy:.1f})" text-anchor="middle" font-family="Work Sans" font-weight="600" font-size="{int(14*esc)}" letter-spacing="5" fill="{CREMA}" opacity=".7">AV. CIRCUNVALACIÓN</text>')
    # pin en la esquina
    px, py = x0 + 540 * esc, y0 + 445 * esc
    sv.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{14*esc:.1f}" fill="{OCRE}"/><circle cx="{px:.1f}" cy="{py:.1f}" r="{5.5*esc:.1f}" fill="{NAVY}"/>')
    return f'<svg class="abs" style="left:0;top:0" width="{W}" height="{H}">{"".join(sv)}</svg>'


L = {}

# Lámina "Elegí tu lote": el plano con los 10 lotes, el precio y la aprobación.
L[1] = pagina(NAVY, f"""
<p class="abs etq" style="left:72px;top:72px;color:{OCRE}">San Ignacio de Moxos · Beni</p>
<p class="abs serif" style="left:72px;top:110px;width:940px;font-size:96px;line-height:1;color:{CREMA}">Elegí tu lote</p>
<p class="abs" style="left:74px;top:226px;width:940px;font-size:28px;line-height:1.35;color:{CREMA};opacity:.85">10 lotes en la esquina de Av. Circunvalación y Av. al Aeropuerto</p>
{plano(130, 330, 1.52)}
<div class="abs" style="left:72px;top:1060px;width:936px;height:1px;background:{OCRE};opacity:.5"></div>
<p class="abs etq" style="left:72px;top:1090px;color:{OCRE};font-size:20px">Desde</p>
<p class="abs serif" style="left:68px;top:1112px;font-size:118px;line-height:1;color:{OCRE}">13<span style="font-size:44px;color:{CREMA}"> $US el m²</span></p>
<div class="abs" style="left:640px;top:1104px;width:368px;height:126px;border:2px solid {OCRE};border-radius:6px"></div>
<p class="abs" style="left:640px;top:1124px;width:368px;text-align:center;font-size:20px;font-weight:600;letter-spacing:5px;color:{OCRE}">PLANO APROBADO</p>
<p class="abs serif" style="left:640px;top:1156px;width:368px;text-align:center;font-size:40px;line-height:1.1;color:{CREMA}">por la Alcaldía</p>
{alambrado(OCRE, .5)}
""")

# Lámina "En números": los datos grandes, con la foto real del terreno arriba.
D = f"font-size:124px;line-height:1;color:{NAVY}"
U = f"font-size:46px;color:{OCRE_OSC}"
T = f"font-size:27px;line-height:1.3;color:{NAVY};opacity:.85"
L[2] = pagina(CREMA, f"""
<img class="abs foto" src="img/terreno.jpg" style="left:0;top:0;width:1080px;height:470px">
<p class="abs etq" style="left:72px;top:520px;color:{OCRE_OSC}">Los lotes</p>
<p class="abs serif" style="left:72px;top:556px;width:936px;font-size:70px;line-height:1;color:{NAVY}">Para vivir o para invertir</p>
<div class="abs" style="left:72px;top:960px;width:936px;height:1px;background:{OCRE_OSC};opacity:.5"></div>
<div class="abs" style="left:540px;top:690px;width:1px;height:520px;background:{OCRE_OSC};opacity:.5"></div>
<p class="abs serif" style="left:72px;top:690px;{D}">10<span style="{U}"> lotes</span></p>
<p class="abs" style="left:76px;top:824px;width:440px;{T}">en una esquina sobre dos avenidas</p>
<p class="abs serif" style="left:580px;top:690px;font-size:92px;line-height:1.2;color:{NAVY}">642<span style="{U}"> a </span>1.641</p>
<p class="abs" style="left:584px;top:824px;width:440px;{T}">metros cuadrados cada uno</p>
<p class="abs serif" style="left:72px;top:990px;{D}">13<span style="{U}"> $US el m²</span></p>
<p class="abs" style="left:76px;top:1124px;width:440px;{T}">desde, el lote más chico</p>
<p class="abs serif" style="left:580px;top:1004px;font-size:76px;line-height:1.05;color:{NAVY}">Plano<br>aprobado</p>
<p class="abs" style="left:584px;top:1180px;width:440px;{T}">por la Alcaldía de San Ignacio</p>
{alambrado(OCRE_OSC, .6)}
""")

# Lámina final: la foto real del letrero, con el cierre.
L[3] = pagina(NAVY, f"""
<img class="abs foto" src="img/letrero.jpg" style="left:0;top:0;width:1080px;height:1350px">
{velo(900, 450, f"rgba(24,34,47,0) 0%,rgba(24,34,47,.85) 45%,{NAVY} 100%")}
<p class="abs etq" style="left:72px;top:1050px;color:{OCRE}">Así está hoy el terreno</p>
<p class="abs serif" style="left:72px;top:1088px;width:940px;font-size:72px;line-height:1;color:{CREMA}">Venta directa del dueño</p>
<div class="abs" style="left:72px;top:1196px;width:520px;height:72px;border-radius:36px;background:{OCRE};color:{NAVY};font-size:29px;font-weight:600;display:flex;align-items:center;justify-content:center">Escribinos por WhatsApp</div>
""")

os.makedirs(OUT, exist_ok=True)
for n, html in L.items():
    open(os.path.join(OUT, f"lamina-{n}.html"), "w", encoding="utf-8").write(html)
print("ok", len(L))
