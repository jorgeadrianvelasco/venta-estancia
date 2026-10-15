# Identidad visual de inmobiliarias rurales (Bolivia, Brasil, Argentina) y prompts para la marca de "Venta estancias"

Investigación del 15/10/2026 hecha por el agente `investigador-estancia`, pedida por Jorge para la imagen de marca de la
página "Venta estancias" (`1445747361945494`). Contexto: las 3 imágenes de Canva (badge con amanecer, líneas con palmera,
monograma "VE") le parecieron "muy básicas y feas" y "se nota mucho que es IA" (`fotos/README.md`).
**No toca Meta Ads ni la página.** El precio de Calocha no aparece acá (`decisiones.md`).

## Límite grande: no se vio ninguna página de verdad

| Qué se intentó | Resultado |
|---|---|
| `WebFetch` a 18 dominios (sitios de las firmas, portales, Wikipedia, example.com, fonts.google.com) | `getaddrinfo ENOTFOUND` en **todos**, incluso en sitios que no son competidores |
| `curl` a Wikipedia desde la consola | El proxy lo rechazó (403, `connect_rejected`) |
| Instagram y Facebook de las firmas | No se abrieron. Solo aparecen como resultado de buscador (título y a veces una línea de la bio) |
| `WebSearch` | Funcionó, pero devuelve **resúmenes redactados por un modelo**: dicen quién es la firma y cómo se presenta, **no dicen colores, tipografías ni qué se ve en la foto de perfil o la portada** |

Consecuencia: **ningún logo, color, tipografía, foto de perfil ni portada de ninguna firma fue visto.** Todo lo de abajo
está marcado `[DATO de resumen — URL]` (lo dice un resumen, no lo vi) o `[ESTIMACIÓN]`. La palabra **"no visto"** en una
celda es literal. Los patrones de paleta y tipografía son por eso **hipótesis razonadas**, no un relevamiento de los
competidores (ver "Qué quedó sin verificar" para cómo confirmarlos en 10 minutos desde una conexión sin bloqueo).

## 1. Quién vende campos y cómo se presenta (según resúmenes)

### 1a. Bolivia (Santa Cruz y Beni)

| Firma | Qué es | Señales de confianza que usa | Lo visual | Fuente |
|---|---|---|---|---|
| Kmpo ("Campos en Bolivia") | Asesor en compra y venta de propiedades ganaderas y agrícolas en Santa Cruz y Beni. Listados por zona (Chaco, Chiquitania, San Julián, Portachuelo) con precio por ha | Explica el proceso: informes legales, análisis de suelo y revisión previa antes de fijar precio y forma de pago. Muestra al menos un aviso marcado "vendido" | **No visto.** El resumen advierte precios distintos entre versiones guardadas de la misma ficha (10.000 vs 24.000 USD/ha en una de lácteo) | `[DATO de resumen — https://kmpo.bo/en/]`, `[DATO de resumen — https://kmpo.bo/venta-de-campos/]` |
| Century 21 Amazonía (red Century 21) | Publica 2 terrenos de Cercado, Beni, en un portal de la red (100 ha cerca de Trinidad; ~6 ha sobre la carretera a Santa Cruz). Century 21 Bolivia: desde 2017, 65 oficinas en 8 departamentos (2024) | Red grande y marca conocida; no es especialista rural | **No visto.** Marca de la red descrita como **negro y dorado** (ver sección 2). Los avisos de Beni traen datos inconsistentes (un terreno con "2 dormitorios") | `[DATO de resumen — https://c21global.immobel.com/property/s-n-municipio-de-san-javier-cercado-beni-bolivia-C21136439329-USD]`, `[DATO de resumen — https://eju.tv/?p=4085541]` |
| RE/MAX Bolivia | Red inmobiliaria; un estudio dice que 58% de quienes usaron agente eligieron RE/MAX. **No se hallaron avisos de campos en Beni** | Cuota de mercado | **No visto** | `[DATO de resumen — https://eju.tv/?p=3556114]` |
| SIRIA Bienes y Raíces | Aparece en un directorio como experta en avalúos de quintas y estancias ganaderas. Solo texto del directorio | Avalúo como servicio | **No visto** | `[DATO de resumen — https://bolivia.gugadir.com/empresas-ganaderas-de-bolivia/]` |
| Portales (InfoCasas, Inmobiliaria.com, BienesOnline, Evisos) | Mezclan avisos de particulares e inmobiliarias | Ninguna uniforme | No visto. Resúmenes: avisos con ha y m² mezclados, precio 0, vendidos que siguen publicados | ver `investigacion/precios-y-canales-trinidad.md` |

Lectura **[ESTIMACIÓN]**: en Bolivia **no encontré una inmobiliaria rural con identidad visual descrita en ninguna fuente**.
Lo que hay son portales de avisos mezclados y una red internacional. Una identidad prolija y consistente no tendría un
competidor local evidente, pero eso es ausencia de evidencia en un buscador bloqueado, no una comprobación.

### 1b. Brasil (MS, MT, GO)

| Firma | Qué es | Señales de confianza que usa | Lo visual | Fuente |
|---|---|---|---|---|
| Beto Invest | Imobiliária de Campo Grande (MS) enfocada en venta y arrendamiento de fazendas para agricultura y pecuaria | No visto más allá del texto | **No visto** | `[DATO de resumen — https://www.investfazendas.com.br/]` |
| Riccoagro / Grupo Ricco Agronegócio | "Imobiliária rural em Goiânia e região" (GO) | Muestra su **registro CRECI** en los portales | **No visto** (el buscador no devolvió nada de logo ni Instagram) | `[DATO de resumen — https://www.riccoagro.com.br/]`, `[DATO de resumen — https://www.zapimoveis.com.br/imobiliaria/823972/]` |
| Agroinvest Imóveis Rurais | Imobiliária rural de Goiânia; fazendas en GO y MT (una de ~7.500 ha en Água Boa, MT, "con venta fraccionada") | En su página de Facebook se presenta como una "relación segura entre vendedores y compradores" | **No visto** (la página de Facebook no se abrió) | `[DATO de resumen — https://www.agroinvestimoveis.com.br/]`, `[DATO de resumen — https://www.facebook.com/agroinvestimoveis/]` |
| JR Imóveis Goiás | Fazendas en GO; una de sus fichas se titula "avaliador de fazendas e chácaras" | Avalúo como servicio | **No visto** | `[DATO de resumen — https://www.jrimoveisgoias.com.br/629/imoveis/venda-fazenda-zona-rural-goiania-go]` |
| IBR Imóveis; Inédita Fazendas; Mil Fazendas; Fazendas Mato Grosso | Existen como sitios con fazendas en venta (Campo Grande, Goiânia, GO, MT) | **No verificado** | **No visto.** Solo se vieron títulos y listados. En Inédita el resumen marca un aviso con "9 m²" a R$ 12 millones | `[DATO de resumen — https://www.ibrimoveis.com.br/imoveis/a-venda/fazenda+sitio+terreno+area/campo-grande]`, `[DATO de resumen — https://www.ineditafazendas.com.br/imoveis/a-venda/fazenda+terreno/goiania]`, `[DATO de resumen — https://milfazendas.com.br/]`, `[DATO de resumen — https://fazendasmatogrosso.com.br/]` |
| Beto Imóveis Fazendas | Aparece solo como título de una página de MS. **No se pudo confirmar** qué es ni si es la misma que Beto Invest | — | No visto | `[DATO de resumen — https://betoimoveisfazendas.com.br/property-state/mato-grosso-do-sul/]` |
| BrasilAgro | Empresa que **vende** fazendas grandes: vendió Alto Taquari (MT) por R$ 589 millones, "el mayor negocio de su historia" | Comunica como empresa, con prensa | **No visto** | `[DATO de resumen — https://forbes.com.br/forbes-agro/2021/10/brasilagro-vende-fazenda-em-mato-grosso-por-r-589-milhoes-maior-negocio-ja-realizado-pela-empresa/]` |
| Portales (Imovelweb, Wimoveis, ZAP, MF Rural, OLX) | Agregan avisos de muchas imobiliárias | — | No visto | ver `investigacion/precios-y-canales-trinidad.md` (no repite acá) |

Los resúmenes de Brasil repiten una advertencia: avisos con área en m² donde va hectárea, precios imposibles (50.000 ha por
R$ 5.000 millones) y áreas distintas entre el título y el texto `[DATO de resumen — https://www.imovelweb.com.br/rurais-mato-grosso-do-sul.html]`.

### 1c. Argentina (inmobiliarias de campos y consignatarias)

| Firma | Qué es | Señales de confianza que usa | Lo visual | Fuente |
|---|---|---|---|---|
| Nordheimer Campos y Estancias | Fundada en 1976 por Pedro Nordheimer, hoy la conducen sus tres hijos; más de 25 agentes. Según su propio sitio (resumen), con oficinas en Uruguay, Paraguay, **Bolivia** y EE. UU. Un resumen dice "seis países"; el título de LinkedIn lista Argentina, EE. UU., Uruguay y Paraguay (**contradicción, no resuelta**) | **Apellido familiar, año de fundación, tamaño**, tasación de campos. Instagram `@nordheimercamposyestancias`: la bio se describe como empresa familiar dedicada a la venta de campos y estancias; ~18 mil seguidores y 930 publicaciones (dato del resumen, puede estar viejo). Canal de YouTube y página de Facebook "Nordheimer Campos y Estancias - En todo el Territorio" | **No visto** | `[DATO de resumen — https://nordheimer.com/]`, `[DATO de resumen — https://nordheimer.com/quienes-somos/]`, `[DATO de resumen — https://www.instagram.com/nordheimercamposyestancias/]`, `[DATO de resumen — https://www.facebook.com/Nordheimer.Campos/]`, `[DATO de resumen — https://ar.linkedin.com/company/nordheimer-campos-y-estancias]` |
| Botta Campos (Osvaldo Botta Campos) | Fundada por Osvaldo Botta hace 36 años (nota de diciembre de 2025), nacida en Mercedes (Buenos Aires), **más de 1.000 operaciones**; "de familia de ganaderos". Avisos con precio "consultar" y pago en cuotas | **Apellido del fundador, años, cantidad de operaciones** | **No visto** | `[DATO de resumen — https://news.agrofy.com.ar/noticia/214844/formula-experto-quintuplicar-hectareas-y-duplicar-vacas-misma-inversion-oportunidad]`, `[DATO de resumen — https://www.bottacampos.com.ar/]` |
| Bullrich Campos | Descendiente de la Casa Bullrich (fundada, según una nota, en 1867). Su representante fue el primer presidente de la CAIR | **Linaje y apellido** | **No visto** (no se encontró ni historia propia ni listados) | `[DATO de resumen — https://news.agrofy.com.ar/noticia/196857/familia-bullrich-casa-patio-historia-ganadera-detras-primer-shopping-argentina]`, `[DATO de resumen — https://news.agrofy.com.ar/noticia/107864/null]` |
| Gustavo Novella Campos Propiedades | Socio de la CAIR; "más de tres décadas" (otro pasaje dice 35 años: **no coincide**). Al recibir un campo evalúa potreros y mejoras, usa **drones**, genera informes detallados y vistas satelitales | **Apellido del dueño, años, cámara, informe técnico** | **No visto** | `[DATO de resumen — https://news.agrofy.com.ar/noticia/214216/se-vende-estancia-emblematica-125-hectareas-uso-mixto-ejemplo-que-invertir-campos-es]` |
| CAIR (Cámara Argentina de Inmobiliarias Rurales) | Formada en 2011; ~200 socios (nota de 2021); publica un índice mensual de actividad | La **pertenencia a la cámara** funciona como sello | **No visto** | `[DATO de resumen — https://caircampos.org/oferta-de-campos-agricolas/]`, `[DATO de resumen — https://bichosdecampo.com/el-mercado-de-tierras-segun-juan-jose-madero-todos-buscan-alquilar-campos-pero-pocos-los-venden-salvo-quienes-deciden-dejar-el-pais/]` (el resumen no dice cuál de dos notas trae "~200 socios") |
| Sotheby's International Realty (Patagonia) y JamesEdition | Segmento **alto**: listan campos y estancias patagónicas (algunos con precio "a consultar"). La sección de Sotheby's de Patagonia se centra más en casas | Marca global, fichas con hectáreas, agua, accesos y mejoras | **No visto** el sitio. De la marca madre: Pentagram rediseñó Sotheby's en 2014 con un logotipo en **serif Mercury** (ver sección 2) | `[DATO de resumen — https://www.sothebysrealty.com/spu/venta/patagonia-arg]`, `[DATO de resumen — https://www.jamesedition.com/real_estate/farm_ranch-argentina]` |
| Consignatarias (Colombo y Magliano, Jáuregui Lorda, Otermin y Massini) | Aparecen **rematando hacienda (ganado)**, en Expoagro y por TV | — | **No visto.** **No pude confirmar que vendan campos**: los resúmenes hablan solo de remates de ganado | `[DATO de resumen — https://bichosdecampo.com/el-remate-de-la-confianza-mas-igualdad-y-transparencia-que-esta-no-hay-destacan-desde-la-consignataria-otermin-y-massini-que-se-llevo-la-chapa-de-ser-la-primera-en-vender-hacienda/]`, `[DATO de resumen — https://www.lanacion.com.ar/economia/campo/ganaderia-el-congreso-de-aapresid-tendra-su-primer-remate-de-hacienda-nid28072025]` |

Hallazgo que no se buscaba: según el resumen de su propio sitio, **Nordheimer declara oficina en Bolivia**. No verificado,
pero si es cierto es un competidor (o un canal) para Calocha.

## 2. Referencias de identidad visual que sí están descritas (casi todas fuera de los tres países)

Son casos de diseño o marcas conocidas. **No son prueba de lo que usan las firmas de la sección 1.** Se incluyen porque
son lo único con paleta, tipografía o foto descritas.

| Referencia | Qué dice el resumen | Fuente |
|---|---|---|
| Boerenwijs (inmobiliaria rural, Países Bajos; caso de agencia) | Paleta dominada por **azul marino con crema** ("confiabilidad y experiencia"); **dos tipografías** de carácter opuesto (una humanista y otra técnica); símbolo con motivo de techo rural; **fotos auténticas del paisaje rural** en web, vallas e impresos. En un resumen la firma no aparece nombrada: el nombre sale de otros dos | `[DATO de resumen — https://worldbranddesign.com/?p=399534]` |
| Roger Parry (inmobiliaria rural, Reino Unido; caso de agencia) | Marca construida sobre **azul y amarillo**, reconocida localmente; el rediseño conservó esa reconocibilidad | `[DATO de resumen — https://source-design.co.uk/projects/roger-parry/]` |
| Raizar (agencia de comunicación para el sector rural, Brasil; **no vende campos**) | Verde (vegetación), **marrón y ocre** (tierra, tradición) y azul (cielo y agua); mezcla **serif y sans**; grafismos de hoja, semilla y sol | `[DATO de resumen — https://worldbranddesign.com/?p=360827]` |
| Century 21 (red; en Bolivia con avisos rurales de Beni) | Esquema **negro y dorado**, conservado en el rediseño de 2018; marca de techo geométrico. Sus normas digitales piden **minúscula de oración** para titulares y botones largos y desaconsejan mayúsculas "por usabilidad" | `[DATO de resumen — https://eliteagent.com/century-21-australasian-operations-announces-local-rebrand/]`, `[DATO de resumen — https://branding.alpha.century21.com/digital/typography.html]` |
| Sotheby's (marca madre) | Rediseño de Pentagram (2014) con logotipo en serif Mercury; una guía de tipografía lo cita como ejemplo de **serif de alto contraste** para lujo inmobiliario (blog, fuente secundaria) | `[DATO de resumen — https://www.designweek.co.uk/issues/april-2014/pentagrams-abbott-miller-leads-sothebys-overhaul/]`, `[DATO de resumen — https://fontalternatives.com/blog/typography-real-estate-luxury-branding/]` |
| Barron Legacy Ranch (rancho de EE. UU.; caso de agencia) | Marca que combina las letras B y R y **funciona como marca de ganado real** | `[DATO de resumen — https://www.whiteboard.is/case-study/real-brand-barron-legacy-ranch]` |
| Guías de logo agro | Los símbolos clásicos son casa de campo, granero y silueta de finca; los **monogramas e iniciales** dan una marca más pulida y "premium"; el logo debe ser simple, funcionar en varios tamaños y en blanco y negro; 3 a 5 tonos en total (el resumen no dice cuál de las dos guías trae cada cosa) | `[DATO de resumen — https://www.zenind.com/help/post/agriculture-logo-design-20-ideas-symbols-and-practical-tips]`, `[DATO de resumen — https://www.wix.com/blog/how-to-make-a-farm-logo]` |

## 3. Estilo de fotos que usan

| Qué | Evidencia | Fuente |
|---|---|---|
| **Foto real, aérea con dron**, como herramienta de venta | Novella usa drones para registrar imágenes e informes; una imobiliária brasileña dice que las fotos aéreas hacen ganar su aviso frente a otras que publican el mismo inmueble; artículo de Agrofy sobre drones para relevar campos | `[DATO de resumen — https://news.agrofy.com.ar/noticia/214216/se-vende-estancia-emblematica-125-hectareas-uso-mixto-ejemplo-que-invertir-campos-es]`, `[DATO de resumen — https://startupi.com.br/imobiliaria-usa-drones-e-3d-para-atrair-novos-clientes/]`, `[DATO de resumen — https://news.agrofy.com.ar/noticia/181603/drones-y-su-uso-inmobiliarias-rurales-como-relevar-campos-minutos]` |
| Qué mostrar y en qué orden | Guías de video aéreo de campos: acceso y perímetro, después recursos (aguadas, monte, mangas, instalaciones), cierre con panorámicas; tomas bajas para detalles; mostrar escala y linderos; ojo con mostrar demasiado techo | `[DATO de resumen — https://www.hopgrove.com/?p=7807]`, `[DATO de resumen — https://globalvideohq.com/aerial-video-showcases-north-texas-farm-ranch-land-sale/]`, `[DATO de resumen — https://www.theportugalnews.com/news/algarve-aerial-videos/36407]` |
| **Paisaje auténtico**, no ilustración | Caso Boerenwijs: fotos auténticas del campo en todos los soportes | `[DATO de resumen — https://worldbranddesign.com/?p=399534]` |
| Ilustración como imagen principal | **No apareció en ninguna fuente.** Que no haya ilustración entre los vendedores es **[ESTIMACIÓN]**: no pude ver sus perfiles | — |

Calocha ya tiene este material (drone de la laguna, casa y camino, `fotos/README.md`). El logo no tiene que competir con eso.

## 4. Patrones

Confianza: "respaldado" = lo dice al menos un resumen con fuente; **[ESTIMACIÓN]** = lo razoné yo.

| # | Patrón | Evidencia | Confianza |
|---|---|---|---|
| 1 | **La confianza viene de hechos y de un nombre real, no de decoración.** Las firmas argentinas llevan el apellido del fundador o de la familia (Nordheimer, Botta, Bullrich, Novella) y muestran años (desde 1976, 36 años, 1867), cantidad de operaciones (+1.000), cámara (CAIR), registro (CRECI) o informes (legal, de suelo, avalúo) | Sección 1 | Respaldado (resúmenes). Ninguna se vio |
| 2 | **Foto real y aérea para el campo; la marca queda en segundo plano.** Nada de escena inventada | Secciones 1 y 3 | Respaldado para dron y foto auténtica. "No usan ilustración" es **[ESTIMACIÓN]** |
| 3 | **Paleta corta (2 o 3 colores)**, de tierra o sobria: azul marino con crema, negro con dorado, azul con amarillo, verde con marrón y ocre. Verde y tierra = rural; marino = confiabilidad | Sección 2 | Respaldado como casos sueltos. Que sea **la paleta típica** de las firmas de BO, BR y AR: **[ESTIMACIÓN]**, no verificado |
| 4 | **Tipografía: serif sobria (alto contraste) para el nombre, sans limpia para el resto**, o dos familias de carácter distinto. Nada de scripts ni decorativas. Textos largos en minúscula de oración | Sección 2 (Boerenwijs, Raizar, Sotheby's, Century 21) | Respaldado en casos de fuera de los tres países. En los competidores locales: no visto |
| 5 | **Marca simple y chica**: una sola forma o monograma, legible en 1 color y a tamaño de avatar. Las marcas de ganado reales (letra como hierro) existen en ranchos | Sección 2 (guías agro, Barron) y guías de logo con IA (abajo) | Respaldado en guías. **[ESTIMACIÓN]** que aplica a un círculo chico de Facebook |
| 6 | **Los datos prolijos son parte de la identidad.** Los portales de Beni, Brasil y Argentina muestran avisos con ha y m² mezclados, precios distintos según la versión, "2 dormitorios" en un terreno. Quien muestra superficie exacta y ficha limpia se distingue | Secciones 1a, 1b y `precios-y-canales-trinidad.md` | Respaldado (varios resúmenes) |

## 5. Qué evitar

| Evitar | Por qué | Fuente |
|---|---|---|
| Degradés, sombras, brillos y colores saturados | Son la marca típica de logo hecho con IA; un logo que depende de degradé o de línea fina para entenderse se descarta | `[DATO de resumen — https://www.creativeainews.com/articles/how-to-design-a-logo-with-ai-2026/]`, `[DATO de resumen — https://m.fightcancer.org/article-307]` |
| Línea fina y mucho detalle | Se vuelve mancha a 16 px; se prueba achicando o entrecerrando los ojos | `[DATO de resumen — https://www.creativeainews.com/articles/how-to-design-a-logo-with-ai-2026/]` |
| Simetría de plantilla, formas "de moda" | Los logos con IA tienden a la simetría y al degradé, y quedan homogéneos; letras deformadas son un defecto frecuente | `[DATO de resumen — https://www.phable.io/phable-labs/ai-logo-design-benefits-risks]` |
| Prompt cargado con muchos motivos | Da resultados complejos e inutilizables: **un motivo**, estilo plano, 2 colores, fondo liso | `[DATO de resumen — https://stockimg.ai/blog/logo-design/5-common-mistakes-to-avoid-when-using-an-ai-logo-generator]` |
| Dejar que la IA escriba el texto | Los generadores deforman letras; el consejo habitual es generar el ícono y poner el nombre con una tipografía real. Hay una herramienta de Canva ("Grab Text") que dice arreglar texto roto; **no verificado** que esté en el plan de Jorge | `[DATO de resumen — https://www.creativeainews.com/articles/how-to-design-a-logo-with-ai-2026/]`, `[DATO de resumen — https://sites.libsyn.com/242546/website/how-to-fix-misspelled-text-in-ai-generated-images-using-canva-grabtext]` |
| Amontonar clichés (amanecer + palmera + laguna + alambrado) | **[ESTIMACIÓN]**: cada uno por separado es común; juntos es el sello de "IA" que Jorge ya rechazó | — |
| Una estancia inventada en la portada | Contradice `fotos/README.md`: en los anuncios y publicaciones de Calocha van solo fotos reales | `fotos/README.md` |
| Precio, "papeles en regla" o superficie en la imagen de marca | El precio no se publica (`decisiones.md`) y los papeles se charlan en persona | `decisiones.md` |

## 6. Qué explica el rechazo de las 3 versiones de Canva

**[ESTIMACIÓN]**, a partir de lo que Jorge describió; **no vi las imágenes** (el MCP solo devuelve una vista previa de 200 px).

| Versión | Contra qué patrón choca |
|---|---|
| 1. Badge con amanecer, palmeras y laguna, colores saturados | Patrones 3 y 5 y "evitar": 4 motivos juntos, saturación, detalle que no sobrevive a un círculo chico |
| 2. Líneas finas verde oscuro, palmera y orilla, texto serif | Patrón 5: línea fina. Paleta y serif sí cuadran con los patrones 3 y 4; lo que falla es el grosor del trazo y la escena |
| 3. Monograma "VE" marrón sobre crema | Es la más cercana a los patrones 3, 4 y 5. Si "se nota que es IA", lo más probable es la forma de las letras o el aspecto de plantilla; el monograma de dos letras no dice "estancias" |

## 7. Datos útiles para usar las imágenes

| Dato | Fuente |
|---|---|
| Foto de perfil de página: se recorta a círculo; las guías de terceros dan 170, 176 o 128 px de visualización (**no coinciden**). Portada: 820 × 312 px en computadora y 640 × 360 en celular; una guía dice que Facebook recomienda subir **851 × 315**; la foto de perfil tapa la esquina inferior izquierda de la portada. **No encontré la página de ayuda de Meta**: son guías de terceros | `[DATO de resumen — https://www.linearity.io/templates/facebook-size-guide]`, `[DATO de resumen — https://postfa.st/sizes/facebook/cover]` |
| Generar 8 a 12 variantes y elegir 3 es la regla práctica que dan las guías de logo con IA (regla de dedo, no estudio) | `[DATO de resumen — https://www.creativeainews.com/articles/how-to-design-a-logo-with-ai-2026/]` |

## Qué quedó sin verificar

| Qué | Motivo |
|---|---|
| **Logo, colores, tipografía, foto de perfil y portada de TODAS las firmas** de las secciones 1a, 1b y 1c | `WebFetch` falló en los 18 dominios probados (`ENOTFOUND`), `curl` recibió 403 del proxy, Instagram y Facebook bloqueados; los resúmenes de buscador no describen lo visual |
| Cuál es la **paleta y tipografía típica** de las firmas de Bolivia, Brasil y Argentina | Sin ver sus páginas. Los patrones 3 y 4 salen de 6 casos sueltos (casi todos fuera de la región) |
| Que las consignatarias argentinas vendan campos | Los resúmenes solo mencionan remates de hacienda |
| Que Nordheimer tenga oficina en Bolivia | Un resumen lo dice, otro lista otros países |
| Cantidad de seguidores y fecha de las bios de Instagram y Facebook | Solo una línea de resumen, sin fecha |
| Si Kmpo, Beto Invest, Riccoagro, Agroinvest, Mil Fazendas, Inédita, IBR y Fazendas Mato Grosso son firmas activas y confiables | Solo se vieron títulos y listados; sin CRECI, reseñas ni historial verificados |
| Si "Beto Invest" y "Beto Imóveis Fazendas" son la misma firma | El buscador no lo aclaró |
| Largo máximo del campo de prompt de Canva y qué modelo usa su generador | No hallé la ayuda oficial; si el campo corta el texto, borrar primero la línea "Avoid" |
| Medidas oficiales de Meta para perfil y portada | No hallé la página de ayuda; solo guías de terceros que no coinciden entre sí |

**Cómo cerrarlo en 10 minutos, desde una conexión sin bloqueo** (mirar: forma de la foto de perfil, colores, si la
portada es foto o gráfico, tipografía del nombre): `https://www.instagram.com/nordheimercamposyestancias/`,
`https://www.facebook.com/Nordheimer.Campos/`, `https://www.facebook.com/agroinvestimoveis/`, `https://kmpo.bo/en/`,
`https://www.riccoagro.com.br/`, `https://www.bottacampos.com.ar/`. Con eso se confirman o corrigen los patrones 3 y 4.

## Fuentes

- https://kmpo.bo/en/
- https://kmpo.bo/venta-de-campos/
- https://c21global.immobel.com/property/s-n-municipio-de-san-javier-cercado-beni-bolivia-C21136439329-USD
- https://c21global.immobel.com/property/s-n-carretera-tdd-scz-cercado-beni-bolivia-C21136438477-USD
- https://eju.tv/?p=4085541
- https://eju.tv/?p=3556114
- https://bolivia.gugadir.com/empresas-ganaderas-de-bolivia/
- https://www.investfazendas.com.br/
- https://www.riccoagro.com.br/
- https://www.zapimoveis.com.br/imobiliaria/823972/
- https://www.agroinvestimoveis.com.br/
- https://www.facebook.com/agroinvestimoveis/
- https://www.jrimoveisgoias.com.br/629/imoveis/venda-fazenda-zona-rural-goiania-go
- https://www.ibrimoveis.com.br/imoveis/a-venda/fazenda+sitio+terreno+area/campo-grande
- https://www.ineditafazendas.com.br/imoveis/a-venda/fazenda+terreno/goiania
- https://milfazendas.com.br/
- https://fazendasmatogrosso.com.br/
- https://betoimoveisfazendas.com.br/property-state/mato-grosso-do-sul/
- https://forbes.com.br/forbes-agro/2021/10/brasilagro-vende-fazenda-em-mato-grosso-por-r-589-milhoes-maior-negocio-ja-realizado-pela-empresa/
- https://www.imovelweb.com.br/rurais-mato-grosso-do-sul.html
- https://startupi.com.br/imobiliaria-usa-drones-e-3d-para-atrair-novos-clientes/
- https://nordheimer.com/
- https://nordheimer.com/quienes-somos/
- https://www.instagram.com/nordheimercamposyestancias/
- https://www.facebook.com/Nordheimer.Campos/
- https://ar.linkedin.com/company/nordheimer-campos-y-estancias
- https://www.bottacampos.com.ar/
- https://news.agrofy.com.ar/noticia/214844/formula-experto-quintuplicar-hectareas-y-duplicar-vacas-misma-inversion-oportunidad
- https://news.agrofy.com.ar/noticia/196857/familia-bullrich-casa-patio-historia-ganadera-detras-primer-shopping-argentina
- https://news.agrofy.com.ar/noticia/107864/null
- https://news.agrofy.com.ar/noticia/214216/se-vende-estancia-emblematica-125-hectareas-uso-mixto-ejemplo-que-invertir-campos-es
- https://news.agrofy.com.ar/noticia/181603/drones-y-su-uso-inmobiliarias-rurales-como-relevar-campos-minutos
- https://caircampos.org/oferta-de-campos-agricolas/
- https://bichosdecampo.com/el-mercado-de-tierras-segun-juan-jose-madero-todos-buscan-alquilar-campos-pero-pocos-los-venden-salvo-quienes-deciden-dejar-el-pais/
- https://www.sothebysrealty.com/spu/venta/patagonia-arg
- https://www.jamesedition.com/real_estate/farm_ranch-argentina
- https://bichosdecampo.com/el-remate-de-la-confianza-mas-igualdad-y-transparencia-que-esta-no-hay-destacan-desde-la-consignataria-otermin-y-massini-que-se-llevo-la-chapa-de-ser-la-primera-en-vender-hacienda/
- https://www.lanacion.com.ar/economia/campo/ganaderia-el-congreso-de-aapresid-tendra-su-primer-remate-de-hacienda-nid28072025
- https://worldbranddesign.com/?p=399534
- https://worldbranddesign.com/?p=360827
- https://source-design.co.uk/projects/roger-parry/
- https://eliteagent.com/century-21-australasian-operations-announces-local-rebrand/
- https://branding.alpha.century21.com/digital/typography.html
- https://www.designweek.co.uk/issues/april-2014/pentagrams-abbott-miller-leads-sothebys-overhaul/
- https://fontalternatives.com/blog/typography-real-estate-luxury-branding/
- https://www.whiteboard.is/case-study/real-brand-barron-legacy-ranch
- https://www.zenind.com/help/post/agriculture-logo-design-20-ideas-symbols-and-practical-tips
- https://www.wix.com/blog/how-to-make-a-farm-logo
- https://www.hopgrove.com/?p=7807
- https://globalvideohq.com/aerial-video-showcases-north-texas-farm-ranch-land-sale/
- https://www.theportugalnews.com/news/algarve-aerial-videos/36407
- https://www.creativeainews.com/articles/how-to-design-a-logo-with-ai-2026/
- https://stockimg.ai/blog/logo-design/5-common-mistakes-to-avoid-when-using-an-ai-logo-generator
- https://www.phable.io/phable-labs/ai-logo-design-benefits-risks
- https://m.fightcancer.org/article-307
- https://sites.libsyn.com/242546/website/how-to-fix-misspelled-text-in-ai-generated-images-using-canva-grabtext
- https://www.linearity.io/templates/facebook-size-guide
- https://postfa.st/sizes/facebook/cover
- Archivos del repo: `investigacion/precios-y-canales-trinidad.md`, `fotos/README.md`, `decisiones.md`, `negocio.md`, `comprador.md`

---

## Prompts para Canva (Magic Media / texto a imagen)

**Cómo usarlos.** Todo en **[ESTIMACIÓN]**: son hipótesis hechas con los patrones de arriba, sin haber visto a los competidores.
Los colores (los códigos hex son una propuesta mía) se eligieron para no copiar ninguna marca: **no se usa negro con dorado**
(la combinación de Century 21) y ningún prompt nombra firmas.

1. Generá varias variantes de cada uno (las guías hablan de 8 a 12) y elegí la más simple.
2. **Probá el círculo:** achicá la imagen a ~40 px. Si no se reconoce la forma principal, descartala.
3. **Revisá cada letra.** Si el texto sale con errores, pedí la versión sin texto (borrá las líneas de "Spanish text") y escribilo
   en Canva con una tipografía real: una serif de contraste moderado para A y C (por ejemplo Playfair Display, **no verificado**
   que esté en su plan) y una sans geométrica y gruesa para B.
4. **Ninguna de estas imágenes se usa como si fuera Calocha.** La portada con foto real del predio (drone de laguna, casa y camino)
   sigue siendo una opción: foto de `fotos/` con una banda de color de la marca y el nombre armados en Canva, sin IA.
5. Portada: recortar en Canva a **851 × 315 px** (o el doble) y dejar libre el tercio izquierdo para la foto de perfil.
6. Si elige B para el perfil, en el prompt C reemplazá "deep forest green (#1F3D2B)" por "deep navy (#14283F)" (el ocre y el crema ya
   son los mismos) para que perfil y portada hagan juego.

### Prompt A — Logo / foto de perfil: monograma serif sobrio

**Patrón que aplica:** nombre/inicial como marca, sin escena (patrón 1 y 5), paleta corta verde y crema de tierra (patrón 3), serif de alto contraste (patrón 4).

```
Minimal flat vector logo for a rural land sales brand, square 1:1 format. One single large capital letter "E" in a classic high-contrast serif typeface, thick and confident, centered and filling about 55% of the square, in warm cream (#F2EBDD) on a solid deep forest green background (#1F3D2B). Below the letter, small and well spaced, the Spanish text "VENTA DE ESTANCIAS" and under it, smaller, "BENI · BOLIVIA", in clean uppercase serif, cream, wide letter-spacing; the text block no wider than 55% of the square. Keep at least 15% empty margin on every side so a circular crop cuts nothing. Two colors only. Calm, institutional, designed by a professional typographer. Spell the text exactly: VENTA DE ESTANCIAS / BENI · BOLIVIA. Avoid: gradients, shadows, glow, 3D, textures, thin lines, illustration, photo, landscape, sun, palm trees, animals, ornaments, extra words, watermark.
```

### Prompt B — Otra dirección: símbolo geométrico de alambrado, azul marino y ocre

**Patrón que aplica:** símbolo simple atado a algo real de los campos (el alambrado perimetral), azul marino con crema como señal de confiabilidad (patrón 3), sans geométrica distinta de la serif de A (patrón 4), legible a 40 px (patrón 5).

```
Flat vector emblem for a rural land brokerage, square 1:1 format. Centered symbol built only from thick solid rectangles: two vertical fence posts, slightly taller than the three horizontal rails between them, evenly spaced, like a ranch fence seen from the front, in warm ochre (#C98A2B), on a solid deep navy blue background (#14283F). Below the symbol, the Spanish text "VENTA DE ESTANCIAS" in a bold geometric sans-serif, uppercase, wide letter-spacing, in sand cream (#EDE3CF), and underneath, smaller, "BENI · BOLIVIA". The whole composition sits inside an imaginary centered circle with at least 15% margin, so a round crop cuts nothing; the symbol is large and reads clearly when shrunk to 40 pixels. Strictly flat: ochre, navy and cream only. Looks like a real corporate identity, simple and solid. Spell the text exactly: VENTA DE ESTANCIAS / BENI · BOLIVIA. Avoid: gradients, shadows, outlines, thin lines, glow, 3D, textures, sun, sunrise, palm trees, cows, water, landscape, illustration, photo, extra words, watermark.
```

### Prompt C — Portada horizontal de marca (sin estancia)

**Patrón que aplica:** el campo se muestra con foto real en las publicaciones (patrón 2), así que la portada de marca es un gráfico plano y sobrio, con la misma paleta corta y la serif del perfil A (patrones 3 y 4), y sin ningún dato que se pueda desmentir (patrón 6).

```
Very wide horizontal brand banner for a Facebook page, aspect ratio about 2.7:1 (wide and short). Flat graphic design, not a photograph and not a landscape. Solid deep forest green background (#1F3D2B) with a very subtle texture of fine topographic contour lines in a slightly lighter green, low contrast, flowing horizontally across the whole banner like a survey map, a little denser toward the right. Keep the left 30% of the banner nearly empty (a profile picture will cover it). In the center-right area, the Spanish text "VENTA DE ESTANCIAS" in a refined uppercase serif typeface, warm cream (#F2EBDD); under it a short thin ochre rule (#C98A2B); under the rule, smaller, "BENI · BOLIVIA" in cream with wide letter-spacing. All text and graphics stay inside the central 80% of the width and the central 70% of the height so phone and desktop crops cut nothing. Calm, premium, institutional. Spell the text exactly: VENTA DE ESTANCIAS / BENI · BOLIVIA. Avoid: photo realism, sky, sunset, trees, water, buildings, animals, people, gradients, glow, 3D, bright colors, slogans, price, extra words, watermark.
```
