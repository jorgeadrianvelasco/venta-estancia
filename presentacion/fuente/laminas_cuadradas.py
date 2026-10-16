"""Versión cuadrada (1080x1080) de las 8 láminas de Calocha, para el carrusel de anuncios de Facebook.

Uso: python3 laminas_cuadradas.py <dir_salida>   (las fotos van en <dir_salida>/img/)
"""
import sys, os

OUT = sys.argv[1]
NAVY, OCRE, OCRE_OSC, CREMA = "#18222F", "#C8963E", "#A87A2A", "#F2ECE1"
H = 1080


def alambrado(color, op, x0=80, x1=1000, y=1030, paso=46, alto=26, doble=True):
    p = [f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{color}" stroke-width="2" opacity="{op}"/>']
    if doble:
        p.append(f'<line x1="{x0}" y1="{y+11}" x2="{x1}" y2="{y+11}" stroke="{color}" stroke-width="1" opacity="{op*0.65:.2f}"/>')
    x = x0
    while x <= x1:
        p.append(f'<rect x="{x}" y="{y-9}" width="3" height="{alto}" fill="{color}" opacity="{op}"/>')
        x += paso
    return f'<svg class="abs" style="left:0;top:0" width="1080" height="{H}">{"".join(p)}</svg>'


CSS = f"""
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;1,500&family=Work+Sans:wght@400;600&display=swap');
html,body{{margin:0;padding:0;width:1080px;height:{H}px;overflow:hidden}}
body{{position:relative;font-family:'Work Sans',sans-serif;-webkit-font-smoothing:antialiased}}
.abs{{position:absolute;margin:0}}
.serif{{font-family:'Cormorant Garamond',serif;font-weight:600}}
.idx{{font-size:20px;font-weight:600;letter-spacing:4px}}
.etq{{font-size:22px;font-weight:600;letter-spacing:6px;text-transform:uppercase}}
.foto{{object-fit:cover;display:block}}
"""


def pagina(fondo, cuerpo):
    return f'<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{CSS}</style></head><body style="background:{fondo}">{cuerpo}</body></html>'


def velo(top, alto, paradas):
    return f'<div class="abs" style="left:0;top:{top}px;width:1080px;height:{alto}px;background:linear-gradient(180deg,{paradas})"></div>'


L = {}

L[1] = pagina(NAVY, f"""
<img class="abs foto" src="img/portada.jpg" style="left:0;top:0;width:1080px;height:1080px">
{velo(420, 660, f"rgba(24,34,47,0) 0%,rgba(24,34,47,.8) 40%,rgba(24,34,47,.96) 72%,{NAVY} 100%")}
<p class="abs idx" style="left:72px;top:64px;color:{NAVY};opacity:.85">01 / 08</p>
<p class="abs etq" style="left:72px;top:640px;color:{OCRE}">En venta · Trinidad, Beni</p>
<p class="abs serif" style="left:72px;top:678px;width:940px;font-size:92px;line-height:.98;color:{CREMA}">530 hectáreas sobre la laguna Suárez</p>
<div class="abs" style="left:72px;top:880px;width:80px;height:4px;background:{OCRE}"></div>
<p class="abs" style="left:72px;top:902px;width:920px;font-size:30px;line-height:1.35;color:{CREMA}">Propiedad urbana de gran extensión<br>a 6,6 km de Trinidad</p>
{alambrado(OCRE, .55, x0=72, x1=1008)}
""")

L[2] = pagina(CREMA, f"""
<p class="abs idx" style="left:72px;top:64px;color:{NAVY};opacity:.6">02 / 08</p>
<p class="abs etq" style="left:72px;top:116px;color:{OCRE_OSC}">Ubicación</p>
<p class="abs serif" style="left:64px;top:136px;width:600px;font-size:210px;line-height:1;color:{NAVY}">6,6<span style="font-size:84px;color:{OCRE_OSC}"> km</span></p>
<p class="abs" style="left:560px;top:250px;width:440px;font-size:32px;line-height:1.3;color:{NAVY}">de Trinidad,<br>capital del Beni</p>
<img class="abs foto" src="img/mapa.png" style="left:72px;top:380px;width:936px;height:407px;border-radius:8px">
<p class="abs" style="left:72px;top:798px;width:936px;font-size:19px;color:{NAVY};opacity:.65">Calocha, sobre la orilla de la laguna Suárez</p>
<p class="abs" style="left:72px;top:850px;width:936px;font-size:30px;line-height:1.45;color:{NAVY}"><b style="color:{OCRE_OSC};font-weight:600">01</b>&nbsp;&nbsp;Entrada a 600 m de la carretera a Loreto<br><b style="color:{OCRE_OSC};font-weight:600">02</b>&nbsp;&nbsp;Acceso todo el año</p>
{alambrado(OCRE_OSC, .6, x0=72, x1=1008)}
""")

L[3] = pagina(NAVY, f"""
<img class="abs foto" src="img/laguna.jpg" style="left:0;top:0;width:1080px;height:660px">
{velo(420, 242, f"rgba(24,34,47,0) 0%,rgba(24,34,47,.85) 75%,{NAVY} 100%")}
<p class="abs idx" style="left:72px;top:64px;color:{NAVY};opacity:.85">03 / 08</p>
<p class="abs serif" style="left:60px;top:470px;width:960px;font-size:240px;line-height:1;color:{OCRE}">800<span style="font-size:92px;color:{CREMA}"> metros</span></p>
<p class="abs etq" style="left:72px;top:752px;color:{OCRE}">La laguna</p>
<p class="abs serif" style="left:72px;top:790px;width:940px;font-size:54px;line-height:1.05;color:{CREMA}">de frente propio sobre la laguna Suárez</p>
<p class="abs" style="left:72px;top:870px;width:940px;font-size:28px;line-height:1.4;color:{CREMA};opacity:.8">Uno de los lugares más conocidos de Trinidad y del Beni</p>
{alambrado(OCRE, .55, x0=72, x1=1008)}
""")

D = f"font-size:120px;line-height:1;color:{NAVY}"
U = f"font-size:46px;color:{OCRE_OSC}"
T = f"font-size:26px;line-height:1.3;color:{NAVY};opacity:.85"
L[4] = pagina(CREMA, f"""
<img class="abs foto" src="img/pampa.jpg" style="left:0;top:0;width:1080px;height:340px">
<p class="abs idx" style="left:72px;top:64px;color:{NAVY};opacity:.85">04 / 08</p>
<p class="abs etq" style="left:72px;top:380px;color:{OCRE_OSC}">El campo</p>
<p class="abs serif" style="left:72px;top:414px;width:936px;font-size:64px;line-height:1;color:{NAVY}">El campo, en números</p>
<div class="abs" style="left:72px;top:752px;width:936px;height:1px;background:{OCRE_OSC};opacity:.5"></div>
<div class="abs" style="left:540px;top:526px;width:1px;height:460px;background:{OCRE_OSC};opacity:.5"></div>
<p class="abs serif" style="left:72px;top:520px;{D}">530<span style="{U}"> ha</span></p>
<p class="abs" style="left:76px;top:650px;width:440px;{T}">tituladas</p>
<p class="abs serif" style="left:580px;top:520px;{D}">500<span style="{U}"> ha</span></p>
<p class="abs" style="left:584px;top:650px;width:440px;{T}">de pasto natural (arrocillo)</p>
<p class="abs serif" style="left:72px;top:780px;{D}">30<span style="{U}"> ha</span></p>
<p class="abs" style="left:76px;top:910px;width:440px;{T}">de monte</p>
<p class="abs serif" style="left:580px;top:780px;{D}">4<span style="{U}"> pozas</span></p>
<p class="abs" style="left:584px;top:910px;width:440px;{T}">de agua, más la laguna</p>
{alambrado(OCRE_OSC, .6, x0=72, x1=1008)}
""")

N = f"font-family:'Cormorant Garamond',serif;font-size:38px;color:{OCRE};font-weight:600"
L[5] = pagina(NAVY, f"""
<p class="abs idx" style="left:72px;top:64px;color:{CREMA};opacity:.75">05 / 08</p>
<p class="abs etq" style="left:72px;top:112px;color:{OCRE}">Infraestructura</p>
<p class="abs serif" style="left:72px;top:144px;width:940px;font-size:84px;line-height:1;color:{CREMA}">Lista para trabajar</p>
<div class="abs" style="left:88px;top:276px;width:932px;height:376px;border:2px solid {OCRE};opacity:.7"></div>
<img class="abs foto" src="img/casa.jpg" style="left:72px;top:260px;width:936px;height:380px">
<div class="abs" style="left:72px;top:684px;width:936px;font-size:30px;line-height:1.3;color:{CREMA}">
  <p style="margin:0 0 12px"><span style="{N}">01</span>&nbsp;&nbsp;Casa</p>
  <p style="margin:0 0 12px"><span style="{N}">02</span>&nbsp;&nbsp;Alambrado perimetral en buen estado</p>
  <p style="margin:0"><span style="{N}">03</span>&nbsp;&nbsp;Corral con brete y corralón</p>
</div>
<p class="abs" style="left:72px;top:944px;width:936px;font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:500;font-size:34px;line-height:1.2;color:{OCRE}">Se vende sin ganado: todo lo demás queda con el predio.</p>
{alambrado(OCRE, .55, x0=72, x1=1008, y=1040)}
""")

L[6] = pagina(NAVY, f"""
<img class="abs foto" src="img/alambrado.jpg" style="left:0;top:0;width:1080px;height:560px">
<p class="abs idx" style="left:72px;top:64px;color:{NAVY};opacity:.85">06 / 08</p>
<img class="abs foto" src="img/camino.jpg" style="left:0;top:575px;width:600px;height:505px">
<p class="abs" style="left:640px;top:620px;width:390px;font-size:20px;font-weight:600;letter-spacing:5px;color:{OCRE}">ASÍ ES CALOCHA</p>
<p class="abs serif" style="left:640px;top:656px;width:400px;font-size:54px;line-height:1.04;color:{CREMA}">Pampa abierta, monte y laguna</p>
<div class="abs" style="left:640px;top:850px;width:72px;height:4px;background:{OCRE}"></div>
<p class="abs" style="left:640px;top:872px;width:390px;font-size:24px;line-height:1.4;color:{CREMA};opacity:.8">Fotos reales del predio, tomadas con drone</p>
""")


def uso(n, y, titulo, desc):
    return f"""
<div class="abs" style="left:72px;top:{y-24}px;width:936px;height:1px;background:{OCRE_OSC};opacity:.5"></div>
<p class="abs serif" style="left:72px;top:{y}px;width:160px;font-size:108px;line-height:1;color:{OCRE_OSC}">{n}</p>
<p class="abs" style="left:250px;top:{y+10}px;width:760px;font-size:36px;font-weight:600;color:{NAVY}">{titulo}</p>
<p class="abs" style="left:250px;top:{y+60}px;width:760px;font-size:28px;line-height:1.35;color:{NAVY};opacity:.8">{desc}</p>"""


L[7] = pagina(CREMA, f"""
<p class="abs idx" style="left:72px;top:64px;color:{NAVY};opacity:.6">07 / 08</p>
<p class="abs etq" style="left:72px;top:112px;color:{OCRE_OSC}">Usos</p>
<p class="abs serif" style="left:72px;top:144px;width:936px;font-size:84px;line-height:1;color:{NAVY}">¿Qué se puede hacer en Calocha?</p>
{uso('01', 384, 'Producir', 'Ganadería en un campo listo, pegado a la ciudad')}
{uso('02', 564, 'Vivir o descansar', 'Tu casa de campo sobre la laguna Suárez')}
{uso('03', 744, 'Invertir', 'Tierra titulada a minutos de Trinidad')}
<div class="abs" style="left:72px;top:900px;width:936px;height:1px;background:{OCRE_OSC};opacity:.5"></div>
{alambrado(OCRE_OSC, .6, x0=72, x1=1008)}
""")

L[8] = pagina(NAVY, f"""
<img class="abs foto" src="img/cierre.jpg" style="left:0;top:0;width:1080px;height:1080px">
{velo(360, 720, f"rgba(24,34,47,0) 0%,rgba(24,34,47,.82) 35%,rgba(24,34,47,.97) 62%,{NAVY} 100%")}
<p class="abs idx" style="left:72px;top:64px;color:{NAVY};opacity:.85">08 / 08</p>
<p class="abs etq" style="left:72px;top:592px;color:{OCRE}">Visitas con cita</p>
<p class="abs serif" style="left:72px;top:628px;width:940px;font-size:88px;line-height:1;color:{CREMA}">Venta directa del dueño</p>
<p class="abs" style="left:72px;top:748px;width:920px;font-size:29px;line-height:1.4;color:{CREMA};opacity:.88">Atendemos a interesados en invertir, en producir o en tener su casa de campo sobre la laguna.</p>
<div class="abs" style="left:72px;top:868px;width:520px;height:76px;border-radius:38px;background:{OCRE};color:{NAVY};font-size:30px;font-weight:600;display:flex;align-items:center;justify-content:center">Escribinos por WhatsApp</div>
<p class="abs" style="left:72px;top:996px;width:600px;font-size:20px;font-weight:600;letter-spacing:6px;color:{CREMA};opacity:.7">VENTA ESTANCIAS · CALOCHA</p>
{alambrado(OCRE, .55, x0=680, x1=1008, y=1012, paso=41, alto=24, doble=False)}
""")

os.makedirs(OUT, exist_ok=True)
for n, html in L.items():
    open(os.path.join(OUT, f"lamina-{n}.html"), "w", encoding="utf-8").write(html)
print("ok", len(L))
