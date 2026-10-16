"""Genera las 8 láminas del carrusel de Calocha como HTML (1080x1350).

Uso: python3 laminas.py <dir_salida> [prefijo_img]
  prefijo_img: "img/" para la vista previa local, o "{{" para tokens de Creative Claw.
"""
import sys, os

OUT = sys.argv[1]
MODO = sys.argv[2] if len(sys.argv) > 2 else "img/"

NAVY, OCRE, OCRE_OSC, CREMA = "#18222F", "#C8963E", "#A87A2A", "#F2ECE1"


def src(nombre):
    base = nombre.split(".")[0]
    return "{{%s}}" % base if MODO == "{{" else MODO + nombre


def alambrado(color, op, x0=80, x1=1000, y=1296, paso=46, alto=30, doble=True):
    partes = [f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{color}" stroke-width="2" opacity="{op}"/>']
    if doble:
        partes.append(f'<line x1="{x0}" y1="{y+12}" x2="{x1}" y2="{y+12}" stroke="{color}" stroke-width="1" opacity="{op*0.65:.2f}"/>')
    x = x0
    while x <= x1:
        partes.append(f'<rect x="{x}" y="{y-10}" width="3" height="{alto}" fill="{color}" opacity="{op}"/>')
        x += paso
    return f'<svg class="abs" style="left:0;top:0" width="1080" height="1350">{"".join(partes)}</svg>'


BASE_CSS = f"""
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;1,500&family=Work+Sans:wght@400;600&display=swap');
html,body{{margin:0;padding:0;width:1080px;height:1350px;overflow:hidden}}
body{{position:relative;font-family:'Work Sans',sans-serif;-webkit-font-smoothing:antialiased}}
.abs{{position:absolute;margin:0}}
.serif{{font-family:'Cormorant Garamond',serif;font-weight:600}}
.idx{{font-size:22px;font-weight:600;letter-spacing:4px}}
.etq{{font-size:24px;font-weight:600;letter-spacing:6px;text-transform:uppercase}}
.foto{{object-fit:cover;display:block}}
"""


def pagina(fondo, cuerpo):
    return f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<style>{BASE_CSS}</style></head>
<body style="background:{fondo}">{cuerpo}</body></html>"""


L = {}

L[1] = pagina(NAVY, f"""
<img class="abs foto" src="{src('portada.jpg')}" style="left:0;top:0;width:1080px;height:1350px">
<div class="abs" style="left:0;top:560px;width:1080px;height:790px;background:linear-gradient(180deg,rgba(24,34,47,0) 0%,rgba(24,34,47,.78) 38%,rgba(24,34,47,.96) 70%,{NAVY} 100%)"></div>
<p class="abs idx" style="left:80px;top:80px;color:{NAVY};opacity:.85">01 / 08</p>
<p class="abs etq" style="left:80px;top:874px;color:{OCRE}">En venta · Trinidad, Beni</p>
<p class="abs serif" style="left:80px;top:918px;width:930px;font-size:108px;line-height:.98;color:{CREMA}">530 hectáreas sobre la laguna Suárez</p>
<div class="abs" style="left:80px;top:1158px;width:88px;height:4px;background:{OCRE}"></div>
<p class="abs" style="left:80px;top:1184px;width:920px;font-size:34px;line-height:1.35;color:{CREMA}">Propiedad urbana de gran extensión<br>a 6,6 km de Trinidad</p>
{alambrado(OCRE, .55)}
""")

L[2] = pagina(CREMA, f"""
<p class="abs idx" style="left:80px;top:80px;color:{NAVY};opacity:.6">02 / 08</p>
<p class="abs etq" style="left:80px;top:150px;color:{OCRE_OSC}">Ubicación</p>
<p class="abs serif" style="left:70px;top:170px;width:940px;font-size:290px;line-height:1;color:{NAVY}">6,6<span style="font-size:110px;color:{OCRE_OSC}"> km</span></p>
<p class="abs" style="left:80px;top:470px;width:920px;font-size:36px;line-height:1.3;color:{NAVY}">de Trinidad, capital del Beni</p>
<img class="abs foto" src="{src('mapa.png')}" style="left:80px;top:560px;width:920px;height:500px;border-radius:8px">
<p class="abs" style="left:80px;top:1072px;width:920px;font-size:20px;color:{NAVY};opacity:.65">Calocha, sobre la orilla de la laguna Suárez</p>
<p class="abs" style="left:80px;top:1120px;width:920px;font-size:32px;line-height:1.45;color:{NAVY}"><b style="color:{OCRE_OSC};font-weight:600">01</b>&nbsp;&nbsp;Entrada a 600 m de la carretera a Loreto<br><b style="color:{OCRE_OSC};font-weight:600">02</b>&nbsp;&nbsp;Acceso todo el año</p>
{alambrado(OCRE_OSC, .6)}
""")

L[3] = pagina(NAVY, f"""
<img class="abs foto" src="{src('laguna.jpg')}" style="left:0;top:0;width:1080px;height:820px">
<div class="abs" style="left:0;top:560px;width:1080px;height:262px;background:linear-gradient(180deg,rgba(24,34,47,0) 0%,rgba(24,34,47,.85) 75%,{NAVY} 100%)"></div>
<p class="abs idx" style="left:80px;top:80px;color:{NAVY};opacity:.85">03 / 08</p>
<p class="abs serif" style="left:66px;top:640px;width:950px;font-size:270px;line-height:1;color:{OCRE}">800<span style="font-size:104px;color:{CREMA}"> metros</span></p>
<p class="abs etq" style="left:80px;top:940px;color:{OCRE}">La laguna</p>
<p class="abs serif" style="left:80px;top:980px;width:920px;font-size:58px;line-height:1.05;color:{CREMA}">de frente propio sobre la laguna Suárez</p>
<p class="abs" style="left:80px;top:1072px;width:920px;font-size:30px;line-height:1.4;color:{CREMA};opacity:.8">Uno de los lugares más conocidos de Trinidad y del Beni</p>
{alambrado(OCRE, .55)}
""")

DATO = "font-size:150px;line-height:1;color:%s" % NAVY
UNI = "font-size:56px;color:%s" % OCRE_OSC
TXT = "font-size:28px;line-height:1.3;color:%s;opacity:.85" % NAVY
L[4] = pagina(CREMA, f"""
<img class="abs foto" src="{src('pampa.jpg')}" style="left:0;top:0;width:1080px;height:500px">
<p class="abs idx" style="left:80px;top:80px;color:{NAVY};opacity:.85">04 / 08</p>
<p class="abs etq" style="left:80px;top:550px;color:{OCRE_OSC}">El campo</p>
<p class="abs serif" style="left:80px;top:588px;width:920px;font-size:76px;line-height:1;color:{NAVY}">El campo, en números</p>
<div class="abs" style="left:80px;top:960px;width:920px;height:1px;background:{OCRE_OSC};opacity:.5"></div>
<div class="abs" style="left:540px;top:710px;width:1px;height:510px;background:{OCRE_OSC};opacity:.5"></div>
<p class="abs serif" style="left:80px;top:700px;{DATO}">530<span style="{UNI}"> ha</span></p>
<p class="abs" style="left:84px;top:862px;width:420px;{TXT}">tituladas</p>
<p class="abs serif" style="left:580px;top:700px;{DATO}">500<span style="{UNI}"> ha</span></p>
<p class="abs" style="left:584px;top:862px;width:420px;{TXT}">de pasto natural (arrocillo)</p>
<p class="abs serif" style="left:80px;top:990px;{DATO}">30<span style="{UNI}"> ha</span></p>
<p class="abs" style="left:84px;top:1152px;width:420px;{TXT}">de monte</p>
<p class="abs serif" style="left:580px;top:990px;{DATO}">4<span style="{UNI}"> pozas</span></p>
<p class="abs" style="left:584px;top:1152px;width:420px;{TXT}">de agua, más la laguna</p>
{alambrado(OCRE_OSC, .6)}
""")

NUM = "font-family:'Cormorant Garamond',serif;font-size:42px;color:%s;font-weight:600" % OCRE
L[5] = pagina(NAVY, f"""
<p class="abs idx" style="left:80px;top:80px;color:{CREMA};opacity:.75">05 / 08</p>
<p class="abs etq" style="left:80px;top:150px;color:{OCRE}">Infraestructura</p>
<p class="abs serif" style="left:80px;top:186px;width:940px;font-size:100px;line-height:1;color:{CREMA}">Lista para trabajar</p>
<div class="abs" style="left:96px;top:346px;width:916px;height:536px;border:2px solid {OCRE};opacity:.7"></div>
<img class="abs foto" src="{src('casa.jpg')}" style="left:80px;top:330px;width:920px;height:540px">
<div class="abs" style="left:80px;top:918px;width:920px;font-size:34px;line-height:1.3;color:{CREMA}">
  <p style="margin:0 0 20px"><span style="{NUM}">01</span>&nbsp;&nbsp;Casa</p>
  <p style="margin:0 0 20px"><span style="{NUM}">02</span>&nbsp;&nbsp;Alambrado perimetral en buen estado</p>
  <p style="margin:0"><span style="{NUM}">03</span>&nbsp;&nbsp;Corral con brete y corralón</p>
</div>
<p class="abs" style="left:80px;top:1196px;width:920px;font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:500;font-size:38px;line-height:1.2;color:{OCRE}">Se vende sin ganado: todo lo demás queda con el predio.</p>
{alambrado(OCRE, .55)}
""")

L[6] = pagina(NAVY, f"""
<img class="abs foto" src="{src('alambrado.jpg')}" style="left:0;top:0;width:1080px;height:760px">
<p class="abs idx" style="left:80px;top:80px;color:{NAVY};opacity:.85">06 / 08</p>
<img class="abs foto" src="{src('camino.jpg')}" style="left:0;top:780px;width:600px;height:570px">
<p class="abs" style="left:644px;top:832px;width:380px;font-size:22px;font-weight:600;letter-spacing:5px;color:{OCRE}">ASÍ ES CALOCHA</p>
<p class="abs serif" style="left:644px;top:872px;width:390px;font-size:60px;line-height:1.04;color:{CREMA}">Pampa abierta, monte y laguna</p>
<div class="abs" style="left:644px;top:1040px;width:72px;height:4px;background:{OCRE}"></div>
<p class="abs" style="left:644px;top:1064px;width:380px;font-size:26px;line-height:1.4;color:{CREMA};opacity:.8">Fotos reales del predio, tomadas con drone</p>
""")

def uso(n, y, titulo, desc):
    return f"""
<div class="abs" style="left:80px;top:{y-30}px;width:920px;height:1px;background:{OCRE_OSC};opacity:.5"></div>
<p class="abs serif" style="left:80px;top:{y}px;width:170px;font-size:130px;line-height:1;color:{OCRE_OSC}">{n}</p>
<p class="abs" style="left:270px;top:{y+14}px;width:730px;font-size:40px;font-weight:600;color:{NAVY}">{titulo}</p>
<p class="abs" style="left:270px;top:{y+70}px;width:730px;font-size:30px;line-height:1.35;color:{NAVY};opacity:.8">{desc}</p>"""

L[7] = pagina(CREMA, f"""
<p class="abs idx" style="left:80px;top:80px;color:{NAVY};opacity:.6">07 / 08</p>
<p class="abs etq" style="left:80px;top:150px;color:{OCRE_OSC}">Usos</p>
<p class="abs serif" style="left:80px;top:186px;width:920px;font-size:100px;line-height:1;color:{NAVY}">¿Qué se puede hacer en Calocha?</p>
{uso('01', 500, 'Producir', 'Ganadería en un campo listo, pegado a la ciudad')}
{uso('02', 730, 'Vivir o descansar', 'Tu casa de campo sobre la laguna Suárez')}
{uso('03', 960, 'Invertir', 'Tierra titulada a minutos de Trinidad')}
<div class="abs" style="left:80px;top:1160px;width:920px;height:1px;background:{OCRE_OSC};opacity:.5"></div>
{alambrado(OCRE_OSC, .6)}
""")

L[8] = pagina(NAVY, f"""
<img class="abs foto" src="{src('cierre.jpg')}" style="left:0;top:0;width:1080px;height:1350px">
<div class="abs" style="left:0;top:500px;width:1080px;height:850px;background:linear-gradient(180deg,rgba(24,34,47,0) 0%,rgba(24,34,47,.82) 35%,rgba(24,34,47,.97) 65%,{NAVY} 100%)"></div>
<p class="abs idx" style="left:80px;top:80px;color:{NAVY};opacity:.85">08 / 08</p>
<p class="abs etq" style="left:80px;top:762px;color:{OCRE}">Visitas con cita</p>
<p class="abs serif" style="left:80px;top:800px;width:920px;font-size:100px;line-height:1;color:{CREMA}">Venta directa del dueño</p>
<p class="abs" style="left:80px;top:1020px;width:900px;font-size:32px;line-height:1.4;color:{CREMA};opacity:.88">Atendemos a interesados en invertir, en producir o en tener su casa de campo sobre la laguna.</p>
<div class="abs" style="left:80px;top:1150px;width:560px;height:84px;border-radius:42px;background:{OCRE};color:{NAVY};font-size:32px;font-weight:600;display:flex;align-items:center;justify-content:center">Escribinos por WhatsApp</div>
<p class="abs" style="left:80px;top:1270px;width:600px;font-size:22px;font-weight:600;letter-spacing:6px;color:{CREMA};opacity:.7">VENTA ESTANCIAS · CALOCHA</p>
{alambrado(OCRE, .55, x0=680, x1=1000, y=1288, paso=40, alto=26, doble=False)}
""")

os.makedirs(OUT, exist_ok=True)
for n, html in L.items():
    with open(os.path.join(OUT, f"lamina-{n}.html"), "w", encoding="utf-8") as f:
        f.write(html)
print("ok", len(L))
