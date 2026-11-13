# Cómo gastar menos tokens — manual de trabajo

Para Claude (Opus 5.5 o el modelo que toque) y para Jorge. Escrito el 13/11/2026, a pedido de Jorge, con la medición
de una sesión real y la [guía oficial de costos de Claude Code](https://code.claude.com/docs/en/costs).

## Qué se midió

La sesión que armó la base y El Arca (11 al 13/11/2026), leída de su propia transcripción. Son datos, no estimaciones.

| Dato | Valor |
|---|---|
| Mensajes de Jorge | 13 |
| Llamadas al modelo | 92 |
| Tamaño de la conversación **al abrir**, antes de la primera palabra | 108.114 tokens |
| …de eso, fijo del programa (no se puede tocar) | 65.877 |
| …de eso, propio de la cuenta y del repo (plugins, conectores, skills, `CLAUDE.md`, hook) | 42.237 |
| Tamaño de la conversación al final | 607.382 tokens |
| Tokens leídos de la conversación guardada (caché) | 33,3 millones |
| Tokens **escritos** a la conversación guardada | 1,98 millones |
| Tokens de respuesta | 133.000 |
| El agente que hizo los 4 PR (aparte) | 166.811 tokens, 37 llamadas |

Jorge paga una suscripción, no por token. Para comparar, a
[precio de lista](https://platform.claude.com/docs/en/about-claude/pricing) esa sesión equivale a unos **34 dólares**
(cálculo: tokens medidos × precio de lista). No verifiqué cómo pondera el plan cada tipo de token: el cálculo sirve
para ver proporciones, no para saber cuánto del plan se gastó.

| En qué se fue | Parte |
|---|---|
| Escribir la conversación a la caché | 67 % |
| Releer la conversación en cada llamada | 20 % |
| Las respuestas | 13 % |

**El dato que manda: el 45 % se fue en cuatro momentos** en que hubo que volver a escribir la conversación entera
(entre 308.000 y 467.000 tokens cada vez): dos veces por **cambiar de modelo** en la mitad, y tres por **retomar la
sesión después de horas** (5, 13 y 25 horas; la última coincidió con un cambio de modelo).

## Por qué pasa

1. En cada llamada, el modelo recibe **toda** la conversación: lo que se habló, cada archivo leído y cada resultado.
2. Lo que ya está guardado se relee barato. Lo nuevo se escribe una vez, caro.
3. La conversación guardada **vence**: en la sesión medida duró una hora (puede bajar a 5 minutos si la cuenta entra
   en uso extra). Pasado ese tiempo, el próximo mensaje vuelve a escribir todo.
4. La conversación guardada es **por modelo**: cambiar de modelo la escribe entera otra vez.
5. Cada herramienta que se usa es otra llamada. Con la conversación en 600.000 tokens, cada llamada relee 600.000.

Por eso lo que más pesa no es cuánto escribe Claude, sino **cuán grande es la conversación, cuántas llamadas se hacen
sobre ella y cuántas veces se la retoma en frío**.

## Reglas para Jorge, por orden de peso

| # | Regla | Por qué |
|---|---|---|
| 1 | **Una tarea, una sesión, un repo.** Terminó la tarea: `/cerrar` y sesión nueva para la siguiente | Una sesión nueva pesa ~108.000 tokens; una de dos días, 600.000 |
| 2 | **Si pasó más de una hora, abrí una sesión nueva en vez de retomar la vieja** | Retomar reescribe toda la conversación. El estado está en `memory.md`: la sesión nueva lo lee en 2.000 tokens |
| 3 | **Elegí el modelo al abrir y no lo cambies en el medio** | Cada cambio reescribe todo |
| 4 | **Un mensaje completo en vez de cinco cortos**: qué querés, de qué repo, con qué datos | Cada mensaje es al menos una llamada sobre toda la conversación |
| 5 | **Una sesión por campaña**, abierta para crearla y recibir sus controles, y nada más | Los controles programados despiertan la sesión y le mandan la conversación entera |
| 6 | **Agentes, solo para trabajo grande** | El de los 4 PR gastó 167.000 tokens |
| 7 | **Apagar los plugins y conectores que no se usan** (lista abajo) | Bajan los 42.000 del arranque. Es la palanca más chica |

## Reglas para Claude

**Leer**
- Antes de abrir un archivo, mirá cuánto pesa (`wc -c`). Más de 20 KB: `grep` y el tramo que haga falta, nunca entero.
- `memoria/`, `investigacion/` y `analisis/` no se leen enteros: se buscan.
- No releas lo que acabás de escribir o editar, ni lo que ya está en la conversación.
- Una imagen cuesta tokens: abrí la que hace falta, una vez.

**Llamar**
- Juntá los comandos en una sola llamada de Bash, y las lecturas independientes en un mismo mensaje.
- Recortá la salida (`head`, `cut`, `tail`): un resultado largo queda en la conversación hasta el final.
- A Meta, pedile los campos que vas a usar, en el nivel y el rango de fechas que hacen falta. La identidad
  (`ads_get_ad_accounts`) se verifica una vez por sesión, no en cada lectura.
- Las instrucciones de un flujo de Higgsfield pesan miles de tokens: cargá solo el que vas a usar, una vez.
- Con `ToolSearch`, pedí las herramientas por nombre exacto.

**Delegar**
- Un agente conviene cuando hay que leer mucho y solo importa la conclusión. Para algo que se resuelve con dos
  archivos, sale más caro.
- El agente va con modelo Sonnet (o Haiku para ordenar y extraer), escribe su archivo y devuelve diez líneas.

**Responder y anotar**
- Respuesta corta: la conclusión, una tabla y lo pendiente. Sin repetir lo que Jorge ya sabe ni el contenido de los archivos.
- Entradas de `memory.md` cortas. "Estado actual" de 20 líneas como máximo. Arriba de 300 líneas, lo viejo va a `memoria/`.
- `CLAUDE.md` apunta, no contiene: todo lo que está ahí se carga en cada sesión.

**Avisar**
- Si la sesión ya hizo otra tarea grande, o Jorge vuelve después de más de una hora con una tarea nueva, decíselo en
  una línea: conviene `/cerrar` y abrir otra. La decisión es suya.
- Si te pide cambiar de modelo en la mitad de una sesión larga, avisale que conviene hacerlo en una sesión nueva.

## Qué modelo para qué

Precios de lista por millón de tokens (página oficial, leída el 13/11/2026):

| Modelo | Entrada | Escritura (1 h) | Lectura guardada | Respuesta |
|---|---|---|---|---|
| Fable 5.2 | 8 | 16 | 0,20 | 40 |
| **Opus 5.5** | 4 | 8 | 0,20 | 20 |
| Sonnet 5.5 | 2 | 4 | 0,10 | 10 |
| Haiku 5.5 (hasta 100.000 tokens) | 0,10 | 0,20 | 0,01 | 0,50 |

Recomendación (criterio propio, no medición):

| Trabajo | Modelo |
|---|---|
| Controles de campaña, "dame resumen", anotar, PR, copiar archivos | Sonnet 5.5 |
| Crear una campaña, proponer, analizar un cierre, escribir textos, armar un repo | **Opus 5.5** |
| Un problema que Opus no pudo resolver | Fable 5.2, en una sesión nueva |
| Agente investigador | Sonnet (ya está en su archivo) |

En Opus 5.5 el esfuerzo por defecto es medio. Subirlo solo para un análisis difícil.

## Qué apagar en la cuenta (lo hace Jorge en claude.ai)

Cada plugin y cada conector prendido suma su lista de skills y herramientas a **todas** las sesiones, se usen o no.

| Dejar | Apagar si no se usan |
|---|---|
| Conectores: Meta Ads, GitHub, Higgsfield, Moda, Canva | Conectores: QuickBooks, Shopify, Gmail, Google Calendar, Windsor, Google Drive |
| Skills de la cuenta: xlsx, pdf, pptx, docx, skill-creator | Plugins: Small Business, Sales, Finance, Data, Design, Customer Support, Enterprise Search, Bigdata, ActiveCampaign (además falla al conectar), Marketing, Postiz, Obsidian Notes, Memory Bank, Token Shield, Creative Claw |

Cuánto baja: **sin medir**. Mi estimación es entre 8.000 y 12.000 de los 42.000 tokens del arranque. Se mide solo:
abrir una sesión antes y otra después, y comparar el primer número.

## ¿Hace falta otra app?

**No.** Lo que más pesa se resuelve con hábitos (reglas 1 a 5) y con los archivos del repo.

| Opción | Veredicto |
|---|---|
| Hábitos + repos ordenados | Es la mayor parte del ahorro (el 45 % medido se fue en retomar y cambiar de modelo). Ya está escrito en los repos |
| Apagar plugins y conectores | Gratis, cinco minutos |
| `/usage` y `/context` adentro de la sesión | Muestran el uso del plan y qué ocupa la conversación. **Sin probar en la app de la nube** |
| claude.ai → Settings → Usage | Para ver cuánto del plan va gastado |
| Plugin Token Shield (ya instalado en la cuenta) | No lo probé. Mide lo mismo que se midió acá, y él también ocupa lugar en cada sesión |
| Otra app externa | No hace falta |

## Sin probar

| Idea | Por qué podría servir |
|---|---|
| Que cada control programado abra una **sesión nueva** (`create_trigger` con `create_new_session_on_fire`) en vez de despertar la sesión de la campaña | Un control pagaría ~108.000 tokens en vez de toda la conversación. Falta ver si la sesión nueva arranca con el repo y los conectores |
| `/compact` antes de una pausa larga | Achica la conversación, pero resumirla también es una llamada grande. Para empezar de cero, la sesión nueva no cuesta nada |

## Cómo volver a medir

La transcripción de la sesión está en `/root/.claude/projects/<carpeta>/<id>.jsonl`. Cada respuesta del modelo trae
`usage` con `input_tokens`, `cache_creation_input_tokens`, `cache_read_input_tokens` y `output_tokens`. Sumando por
llamada (una vez por `message.id`) salen las tablas de arriba. La primera llamada dice cuánto pesa el arranque.
