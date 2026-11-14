#!/usr/bin/env bash
# Se ejecuta ANTES de crear una campaña, un conjunto o un anuncio en Meta Ads.
# Frena la llamada si lo que se crea nace ACTIVO: en Meta todo se crea en pausa (reglas.md, regla 1).
# No frena activar: eso se hace con ads_activate_entity, cuando Jorge lo aprueba.
# Si no puede leer la entrada, deja pasar: un hook roto no tiene que trabar el trabajo.
# Idea tomada de YSY-99/meta-ads-api-field-guide (MIT); el código es propio.
python3 -c '
import sys, json, re
try:
    d = json.load(sys.stdin)
except Exception:
    sys.exit(0)
if not re.search(r"ads_create_(campaign|ad_set|ad)$", str(d.get("tool_name", ""))):
    sys.exit(0)
def activos(x, ruta=""):
    out = []
    if isinstance(x, dict):
        for k, v in x.items():
            r = (ruta + "." + str(k)) if ruta else str(k)
            if str(k).lower() in ("status", "configured_status") and isinstance(v, str) and v.strip().upper() == "ACTIVE":
                out.append(r)
            out += activos(v, r)
    elif isinstance(x, list):
        for i, v in enumerate(x):
            out += activos(v, ruta + "[" + str(i) + "]")
    elif isinstance(x, str) and x.strip().startswith("{"):
        try:
            out += activos(json.loads(x), ruta)
        except Exception:
            pass
    return out
hallados = activos(d.get("tool_input", {}))
if hallados:
    sys.stderr.write("Regla 1: en Meta todo se crea en pausa. Esta llamada trae estado ACTIVE en: " + ", ".join(hallados) + ". Creala en PAUSED y activala con ads_activate_entity cuando Jorge lo apruebe.")
    sys.exit(2)
sys.exit(0)
'
