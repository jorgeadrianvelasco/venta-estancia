# Memoria del agente — venta de la estancia

Claude Code no recuerda nada entre sesiones: solo sabe lo que está escrito en el repositorio.
Este archivo tiene dos partes:

1. **Estado actual**: máximo 20 líneas. **Se reescribe** cada vez que algo cambia. Es lo primero que ve
   una sesión nueva (lo muestra el hook de inicio).
2. **Bitácora**: entradas con fecha, la más nueva al final. **No se reescribe**, se agrega.

Cuando el archivo pase de ~300 líneas, las entradas viejas se mueven a `memoria/AAAA-MM.md` y acá queda
una línea que diga dónde están. (En Kakau el archivo llegó a 3.151 líneas y ninguna sesión lo leía entero.)

## Estado actual
<!-- máximo 20 líneas; se reescribe -->
- **Estancia:** Calocha, 530 ha tituladas (500 de arrocillo, 30 de monte), predio urbano en Cercado sobre la laguna Suárez
  (**frente propio: 800 m**), a 6,6 km de Trinidad, acceso todo el año. Se vende sin ganado; pago negociable, sin intermediario.
  Dueño y precio: **Jorge**. **El precio no se publica.** Ficha completa en `negocio.md`.
- **Meta:** cuenta **personal `64830109`, prepaga** (leer el campo `delivery`); página "Venta estancias" `1445747361945494`;
  WhatsApp del padre de Jorge, compartido con tubos. Sin Instagram. Nada de Kakau.
- **Etapa:** paso 9 del plan hecho (dos campañas); paso 10 sin datos. **Interesados serios: 0** (Jorge, 24/10: "ningún
  interesado muy interesado"). Nadie anotado en `interesados.md`.
- **Última campaña:** `52538379010850`, del 20/10 11:30 al 22/10 23:59, Trinidad 40 km + Santa Cruz 80 km, carrusel V1 a
  WhatsApp. **74,81 Bs, 22 conversaciones** (13 Trinidad a 2,88 Bs; 9 Santa Cruz a 4,16). Trinidad se agotó el primer día;
  Santa Cruz mejoró cada día y sus charlas fueron más largas. Análisis: `analisis/campana-20-22-oct-2026.md`.
- **No repetir:** anuncio sin mensaje prellenado (al padre le llegaba "Hola, quiero más información"); públicos distintos por
  ciudad y solo agro; 4 días perdidos por falta de saldo. Todo anotado en `como-crear-campana.md`.
- **Próxima campaña (Jorge, 25/10; NO creada):** 30 a 54 años; + bienes raíces, inversión, turismo y agronomía; sin leche,
  lácteos ni zona rural; mismos intereses en las dos ciudades; prellenado que diga anuncio y ciudad; 60/40 para Santa Cruz.
  Detalle en `decisiones.md`. Los intereses nuevos los carga Jorge. **Se crea solo cuando Jorge la pida.**
- **Saldo:** ~75 Bs (150 cargados − 74,81), **sin verificar**. Ninguna campaña activa ni control programado.
- **Pendiente de Jorge:** los chats (o su Excel con ciudad, qué preguntó y si es serio); si la lámina 3 es del tramo propio
  de 800 m; InfoCasas y Evisos (opcional).
- **Repo público:** sin nombres ni teléfonos de interesados. Todo en `main` (PR #3, 25/10). Tono camba, firmado como el dueño.

## Bitácora

Las entradas del 15 al 20/10/2026 están en `memoria/2026-10.md`.

### 21 de octubre de 2026
- **05:21 (resumen pedido por Jorge):** Trinidad **13,80 Bs · 642 impresiones · 404 personas · 10 conversaciones · 1,38 Bs c/u**.
  Santa Cruz **8,77 Bs · 506 impresiones · 430 personas · 0 conversaciones**. Total 22,57 de 75 Bs. Se le propuso (sin tocar
  nada) pasar lo que le queda a Santa Cruz a Trinidad. Siguen sin aparecer los chats para calificar.
- **08:25:** Trinidad **16,94 Bs · 775 impresiones · 465 personas · 10 conversaciones (1,69 c/u)**, sin conversaciones nuevas
  desde las 05:21 (madrugada). Santa Cruz **9,12 Bs · 538 · 446 · 1 conversación (9,12 c/u)**. Total 26,06 de 75 Bs,
  11 conversaciones. Sigue en pie la propuesta de pasar lo que queda de Santa Cruz a Trinidad, y los chats sin calificar.
- **Decisión de Jorge (21/10 ~08:30):** **Santa Cruz sigue** ("los compradores más serios deben ser los de Santa Cruz").
  No se pausa ni se mueve presupuesto. Anotado en `decisiones.md`. Para juzgar Santa Cruz importan los interesados serios,
  no el costo por conversación: falta saber de qué ciudad es cada chat.
- **11:10:** Trinidad **19,35 Bs · 892 · 512 personas · 11 conversaciones (1,76 c/u)**. Santa Cruz **10,49 Bs · 604 · 473 ·
  2 conversaciones (5,25 c/u)**. Total **29,84 de 75 Bs · 13 conversaciones**. Siguen sin pasar los chats.
- **Control 2 (12:00, mitad):** Trinidad **19,84 Bs · 922 · 529 personas · 11 conversaciones (1,80 c/u)**. Santa Cruz **10,64 Bs
  · 621 · 484 · 3 conversaciones (3,55 c/u)**: su costo por conversación bajó de 9,12 (08:25) a 3,55. Total **30,48 de 75 Bs ·
  14 conversaciones**. Siguen sin pasar los chats; se le volvió a pedir a Jorge, con la ciudad de cada uno.
- **15:35:** Trinidad **22,57 Bs · 1.067 · 593 personas · 12 conversaciones (1,88 c/u)**. Santa Cruz **12,93 Bs · 751 · 567 ·
  3 conversaciones (4,31 c/u)**. Total **35,50 de 75 Bs · 15 conversaciones**. Chats sin pasar.

### 22 de octubre de 2026

- **06:02:** Trinidad **27,93 Bs · 1.424 · 749 personas · 12 conversaciones (2,33 c/u)**: gastó 5,36 Bs desde las 15:35 del 21
  sin conversaciones nuevas. Santa Cruz **19,32 Bs · 1.164 · 841 · 4 conversaciones (4,83 c/u)**: una nueva. Total **47,25 de
  75 Bs · 16 conversaciones (2,95 c/u)**. Quedan 27,75 Bs hasta las 23:59 de hoy (Trinidad 9,57, Santa Cruz 18,18). Chats sin pasar.
- **17:43:** Trinidad **33,66 Bs · 1.858 · 906 personas · 13 conversaciones (2,59 c/u)**: +1 desde las 06:02. Santa Cruz
  **32,35 Bs · 1.648 · 1.124 · 7 conversaciones (4,62 c/u)**: +3; hoy aceleró (13,03 Bs en el día, más que Trinidad). Total
  **66,01 de 75 Bs · 20 conversaciones (3,30 c/u)**. Quedan 8,99 Bs hasta las 23:59 (Trinidad 3,84, Santa Cruz 5,15). Chats sin pasar.
- **Cierre (23/10 00:30, control automático):** la campaña terminó a las 23:59 del 22/10 (`completed`). Totales del 20 al 22/10:
  Trinidad **37,40 Bs · 2.322 · 1.133 personas · 13 conversaciones (2,88 c/u)**; Santa Cruz **37,39 Bs · 1.994 · 1.345 · 9
  conversaciones (4,15 c/u)**: +2 desde las 17:43. Total **74,79 de 75 Bs · 4.316 impresiones · 22 conversaciones (3,40 c/u)**.
  Contra el boost de 2025 (20,57 Bs, 6 conversaciones, 3,43 c/u, 0 serios): 3,6 veces más conversaciones con el mismo costo
  por conversación. Contra la primera campaña (0,43 Bs, 38 impresiones): esa no se pudo medir. Serios y visitas: **pendiente**,
  se le pidió a Jorge. Anotado en `negocio.md`, `textos-anuncios.md` y `plan.md`. No se creó ni se activó nada.

### 23 de octubre de 2026

- **09:22 (Jorge: "dame resumen, decime cuándo acaba"):** la campaña ya había terminado (jueves 22/10 23:59). Meta ajustó un poco
  las cifras desde las 00:30: Santa Cruz **37,41 Bs · 2.003 impresiones** (antes 37,39 · 1.994), Trinidad **2.327 impresiones**
  (antes 2.322). Conversaciones sin cambio: **22 (13 + 9)**. Total final **74,81 Bs, 3,40 c/u**. No hay nada corriendo en la
  cuenta: la campaña vieja sigue pausada. Se actualizaron `negocio.md`, `textos-anuncios.md` y `plan.md`. Los chats siguen sin pasar.

### 24 de octubre de 2026 — Balance de la campaña y el problema del WhatsApp

- **Jorge:** al padre le llega solo "Hola, quiero más información", sin la imagen ni saber qué preguntan; y **"no hubo ningún
  interesado muy interesado"**. Pregunta si el público no fue el ideal o si faltó encontrar a la persona.
- **Causa del mensaje genérico (verificado en lo que se creó):** los anuncios se armaron con CTA `WHATSAPP_MESSAGE` y link
  `api.whatsapp.com/send`, **sin mensaje prellenado propio**, así que salió el texto por defecto de Meta. `decisiones.md` pedía
  uno que diga "Calocha" y se pasó por alto. No se pudo confirmar con fuente oficial si la app WhatsApp Business muestra la
  tarjeta del anuncio en el chat. Arreglo: prellenado por conjunto (producto + ciudad), anotado en `como-crear-campana.md` y
  `receta-repo-nuevo.md`.
- **Público que corrió (leído en `targeting`):** 30-65, feed de Facebook, Trinidad 40 km y Santa Cruz 80 km, `home`, `recent`
  y `frequently_in`; intereses **solo agro**: Agribusiness, Milk, Dairy, Cattle, Livestock, Farm, Agriculture, Agronomy, Rural
  area, Cattle feeding + empleador Agriculture. **Faltaron bienes raíces, inversión y turismo rural** (perfiles B y D del plan).
- **Lo bueno:** el sistema funciona de punta a punta (anuncio aprobado, las dos ciudades entregaron, el WhatsApp recibió); 22
  conversaciones a 3,40 Bs, 3,6 veces más que en 2025 por el mismo costo; el carrusel y el texto V1 quedan para reusar.
- **Lo malo:** sin prellenado no se sabe de qué ciudad ni qué preguntó cada uno; público solo agro (llega a quien trabaja con
  ganado, no a quien tiene capital para comprar); el objetivo "conversaciones" busca a quien escribe, no a quien compra; los
  chats no se calificaron, así que no hubo forma de ajustar durante la campaña; se perdieron 4 días (16-20/10) por el saldo.
- **Propuesto a Jorge (no creado):** prellenado por conjunto; público con bienes raíces e inversión además de agro; probar
  un formulario de "mayor intención" con preguntas de filtro o volver a mostrarle el anuncio a quien ya interactuó;
  anotar cada chat en Excel (ciudad, qué preguntó, perfil). Esperando su decisión.
- **Análisis a fondo (24/10, agente pedido por Jorge; `analisis/campana-20-22-oct-2026.md`):** 5 hallazgos. (1) **Trinidad se agotó
  el primer día:** 10 de 13 conversaciones el mar 20 (13,78 Bs, 1,38 c/u); mié y jue, 23,62 Bs por 3 (7,87 c/u). (2) **Santa Cruz
  mejoró cada día** (0 → 4 → 5) y sus charlas fueron más largas: 2.º mensaje en 5 de 9 (Trinidad, 4 de 13). (3) **Horas:** la tarde,
  de 12 a 18, dio 12 de 22 conversaciones a 2,71 c/u; la noche, de 18 a 24, 25,26 Bs por 5 (5,05 c/u, muchos clics sin mensaje);
  la madrugada casi no gastó (3,18 Bs de 00 a 07). 21,03 Bs (28 %) cayeron en horas sin ninguna conversación. (4) **Los públicos
  no eran iguales:** Santa Cruz tenía cargos "Farmer" y "Farm Owner Operator" y Ganado de carne; Trinidad, Leche, Lácteos y Zona
  rural. Ninguno tenía bienes raíces ni inversión. (5) **Puja automática** ("mayor volumen", se paga por impresión): CPM de 16,05 Bs
  en Trinidad y 18,65 en Santa Cruz; contra 2025, 18,6 % de los clics al botón terminó en conversación (2025: 1,9 %). Cifras finales:
  74,83 Bs. No disponible: clics por lámina, rankings de calidad y comparación con otros anunciantes.

### 25 de octubre de 2026

- **Jorge aprobó el análisis y anotó cambios para la próxima campaña:** *"aumentar bienes raíces e inversión, también turismo,
  agronomía y otras cosas más. Saca a los de 55 años. Quiero que el mensaje de WhatsApp diga sobre qué anuncio están hablando.
  Está bien lo otro que investigaste."* Anotado en `decisiones.md`, `analisis/` (sección 10), `comprador.md` y `plan.md`. No se
  creó nada. Pidió PR y merge de todo a `main`.

### 28 de octubre de 2026 — Cierre de la etapa de octubre
- **Qué se probó:** la campaña del 20 al 22/10 hasta el final (lecturas cada vez que Jorge pidió "dame resumen" y control de
  cierre automático); balance; análisis a fondo con un agente (horas, días, edad, sexo, celular, puja, públicos); PR y merge.
- **Resultado:** 74,81 Bs, 22 conversaciones, ningún interesado "muy interesado". Jorge aprobó los ajustes para la próxima
  (`decisiones.md`, 25/10). PR #3 mergeado a `main` el 25/10; la rama se reinició desde `main` para seguir.
- **Qué aprendimos / qué cambiar la próxima vez:** mensaje prellenado obligatorio; leer el `targeting` de cada conjunto antes
  de publicar; Trinidad se agota rápido (rondas cortas), Santa Cruz rinde con días; sin los chats calificados no se sabe qué
  trae compradores: pedirle a Jorge el Excel **antes** de gastar de nuevo. Las entradas del 16 al 20/10 se archivaron en
  `memoria/2026-10.md` (memory.md llegaba a 300 líneas).
