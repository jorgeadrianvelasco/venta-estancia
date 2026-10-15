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
| 7 | **WhatsApp y página de Facebook** | Número de WhatsApp de la venta (no el de Kakau) y página nueva, con fotos y datos. Se verifica con el MCP que la página aparezca para la cuenta `64830109` | Jorge crea, Claude verifica | 5, 6 | **en curso 15/10/2026**: guía paso a paso dada; falta que Jorge cree la página y conecte el WhatsApp |
| 8 | **Textos de anuncio** | 2 o 3 versiones en `textos-anuncios.md`: los 800 m sobre la laguna, 530 ha tituladas, a 6,6 km de Trinidad. Sin precio y con el filtro del paso 6 | Claude redacta, Jorge aprueba | 6, 7 | **hecho 15/10/2026**: Jorge eligió V1 (`textos-anuncios.md`) |
| 9 | **Primera campaña de prueba** | **Solo cuando Jorge la pida** (`reglas.md`, regla 1): monto, público y días que él defina. Se crea pausada y se activa con su visto bueno. Decidir también si se publica fuera de Meta (portales, inmobiliarias) | Jorge decide, Claude crea | 8 | pendiente |
| 10 | **Seguimiento de interesados** | Cada consulta calificada en `interesados.md` (skill `calificar-interesado`); a los 7 días, revisar cuántos serios y cuántas visitas, y ajustar | Claude, con Jorge | 9 | pendiente |
