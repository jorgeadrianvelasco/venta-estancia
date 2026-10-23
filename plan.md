# Plan de la venta de Calocha — 10 pasos en orden

Armado el 15/10/2026 a pedido de Jorge. **Se marca cada paso al cerrarlo, con fecha.** Si el orden cambia, se
anota por qué.

La lógica del orden: primero **qué se vende y si está en regla**, después **a quién**, después **con qué se lo
muestra**, y recién al final **se gasta**. Así ningún boliviano de publicidad sale antes de que haya con qué
responder a un comprador serio.

| # | Paso | Qué sale de este paso | Quién | Depende de | Estado |
|---|---|---|---|---|---|
| 1 | **Cerrar la ficha** | `negocio.md` completo: de quién es la franja de 10 m, corrales/brete/potreros, forma de pago y moneda, si hay comisión, equipos | Jorge responde, Claude anota | — | **hecho 15/10/2026** (solo falta la capacidad de carga, que no frena nada) |
| 2 | **Papeles y lo que se puede hacer en el predio** | Folio real, plano georreferenciado (que muestre los 800 m y el 1,3 km), impuestos al día. El abogado responde: qué restricciones pone la Ley 2604 en la orilla y qué uso de suelo urbano tiene el predio (si se puede lotear) | Jorge y su abogado | 1 | **lo maneja Jorge en persona** (15/10/2026): no se guarda ni se manda nada |
| 3 | **Definir a quién se le vende** | 1 o 2 perfiles de comprador en `comprador.md` (p. ej. desarrollador que lotea, inversionista que guarda tierra, empresa o ganadero que quiere campo pegado a la ciudad). Cambia todo el anuncio | Jorge decide, Claude propone | 1, 2 | **hecho 15/10/2026**: B, C y D (`comprador.md`) |
| 4 | **Investigar el mercado** | Agente `investigador-estancia`: precios de referencia de terrenos periurbanos y estancias cerca de Trinidad, con fuente; dónde se publican; inmobiliarias de la zona. **No se publica nada**: es para que Jorge sepa dónde está su precio | Claude | 3 | **hecho a medias 15/10/2026**: el proxy bloqueó los portales; ningún comparable directo (`investigacion/precios-y-canales-trinidad.md`). Falta que Jorge abra los avisos o aporte ventas que conozca |
| 5 | **Fotos, drone y plano** | Vuelo de drone por la orilla, la casa, el alambrado, las pozas y la entrada desde la carretera a Loreto; un plano simple con el frente marcado. Van a `fotos/` | Jorge | 2 | **hecho 15/10/2026**: 8 fotos en `fotos/` (catálogo en `fotos/README.md`). Son capturas: para la campaña, pedir originales |
| 6 | **El filtro de curiosos y las respuestas** | 3 o 4 preguntas de calificación (para qué lo quiere, en qué plazo, cómo pagaría, si puede visitar) y las respuestas de `respuestas.md` **aprobadas por Jorge** | Claude redacta, Jorge aprueba | 3 | **hecho 15/10/2026** (`respuestas.md`) |
| 7 | **WhatsApp y página de Facebook** | Número de WhatsApp de la venta (no el de Kakau) y página nueva, con fotos y datos. Se verifica con el MCP que la página aparezca para la cuenta `64830109` | Jorge crea, Claude verifica | 5, 6 | **en curso**: página **"Venta estancias"** creada y verificada (15/10/2026); logo elegido (B2). **Jorge subió logo, portada y la primera publicación con V1 (15/10/2026, dicho por Jorge)**. WhatsApp conectado (15/10/2026). Falta el link de la publicación (para usarla como anuncio) |
| 8 | **Textos de anuncio** | 2 o 3 versiones en `textos-anuncios.md`: los 800 m sobre la laguna, 530 ha tituladas, a 6,6 km de Trinidad. Sin precio y con el filtro del paso 6 | Claude redacta, Jorge aprueba | 6, 7 | **hecho 15/10/2026**: Jorge eligió V1 (`textos-anuncios.md`) |
| 9 | **Primera campaña de prueba** | **Solo cuando Jorge la pida** (`reglas.md`, regla 1): monto, público y días que él defina. Se crea pausada y se activa con su visto bueno. Decidir también si se publica fuera de Meta (portales, inmobiliarias) | Jorge decide, Claude crea | 8 | **publicada el 15/10/2026**, pero **corrió solo ~2 h** (16/10 08:00-10:00) por falta de saldo: 0,43 Bs, 38 impresiones. **Campaña nueva (`52538379010850`) del 20/10 11:30 al 22/10 23:59: terminó completa, 74,81 Bs, 22 conversaciones de WhatsApp** (13 Trinidad, 9 Santa Cruz); la vieja quedó pausada. **Falta saber cuántos son serios** (paso 10) |
| 10 | **Seguimiento de interesados** | Cada consulta calificada en `interesados.md` (skill `calificar-interesado`); a los 7 días, revisar cuántos serios y cuántas visitas, y ajustar | Claude, con Jorge | 9 | **pendiente: esperando los 22 chats de la campaña del 20 al 22/10** (23/10/2026) |

## Propuesta para la primera campaña (paso 9) — **borrador del 15/10/2026, sin aprobar, no se crea nada**

Se arma solo cuando Jorge la pida (`reglas.md`, regla 1). Lo que está acá es para que decida.

| Qué | Propuesta | Por qué | Decide Jorge |
|---|---|---|---|
| Anuncio | La primera publicación de la página (V1 + fotos reales) | Sin Instagram, el anuncio sale de un post de Facebook | — |
| Destino del mensaje | **WhatsApp del padre** (Jorge, 15/10/2026). Hay que conectarlo antes de crear la campaña | Responde el padre | ✅ decidido |
| Ubicaciones | Solo Facebook, **sin Marketplace** (Jorge, 15/10/2026: "probemos esta campaña sin Marketplace") | Sin Instagram; Marketplace trajo curiosos en 2025 (hipótesis) | ✅ decidido |
| Público | **Dos conjuntos, 50 % y 50 %** (Jorge, 15/10/2026): **Trinidad** (radio 40 km, centro aprox. -14.833, -64.900) y **Santa Cruz de la Sierra** (radio 30 km, centro aprox. -17.783, -63.182), con `custom_locations` (el MCP no busca IDs de ciudad). **30 a 65+** años → `advantage_audience: 0` (Advantage+ no respeta un mínimo mayor a 25). Intereses elegidos: ganadería, bienes raíces e inversión, agricultura y agro, turismo rural | Perfiles B, C y D. **Ojo:** el MCP no tiene buscador de intereses y no se inventan IDs: Jorge los agrega en el Administrador de anuncios sobre los conjuntos pausados | ✅ decidido |
| Categoría de vivienda | No | Público solo en Bolivia (`reglas.md`, regla 5) | — |
| Duración | **3 días** (Jorge, 15/10/2026) | — | ✅ decidido |
| Presupuesto | **75 Bs en total** (25 Bs/día × 3 días; Jorge, 15/10/2026): **37,50 Bs por conjunto** (12,50 Bs/día, arriba del mínimo de 11,95) | — | ✅ decidido |
| Cómo se mide | Interesados serios y visitas (`interesados.md`), no conversaciones | `decisiones.md` | — |
| Ubicación dentro de Facebook | Solo **feed** (inicio) de Facebook | Sin Marketplace ni Instagram; el post es de fotos | a confirmar |
| Objetivo técnico | `OUTCOME_ENGAGEMENT`, conjuntos `CONVERSATIONS` → `WHATSAPP` (receta de Kakau) | — | — |

**Estado al 16/10/2026:** campaña y conjuntos creados en **borrador** (`52537356511050`); WhatsApp conectado; fin de los
dos conjuntos el **domingo 19/10 08:00**. **Falta solo el anuncio**: el link de la publicación (A) o la foto 4:5 subida a la
biblioteca de la cuenta (B). El MCP no puede subir imágenes en esta cuenta todavía (`memory.md`, 16/10/2026).
