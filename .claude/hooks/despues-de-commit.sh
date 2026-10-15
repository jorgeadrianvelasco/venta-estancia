#!/usr/bin/env bash
# Se ejecuta después de cada comando Bash, pero SOLO avisa cuando hubo un commit nuevo.
#
# La verificación está acá y no en un filtro de settings.json porque en Kakau (8/9/2026) se comprobó
# que ese filtro dejaba pasar cualquier comando Bash. Comparar el SHA de HEAD no depende del filtro.
set -uo pipefail
cd "${CLAUDE_PROJECT_DIR:-$(dirname "$0")/../..}" 2>/dev/null || exit 0

marca=".git/estancia-ultimo-commit-avisado"
head_actual=$(git rev-parse HEAD 2>/dev/null) || exit 0

# Primera ejecución en este repositorio: se guarda la marca sin avisar.
if [ ! -f "$marca" ]; then
  echo "$head_actual" > "$marca"
  exit 0
fi

# Si HEAD no cambió, el comando no fue un commit: silencio.
[ "$head_actual" = "$(cat "$marca" 2>/dev/null)" ] && exit 0

echo "$head_actual" > "$marca"
ultimo=$(git log -1 --format='%s' 2>/dev/null || echo '')
python3 -c '
import sys, json
ultimo = sys.argv[1] if len(sys.argv) > 1 else ""
aviso = (
  "Acabás de commitear: \"" + ultimo + "\".\n"
  "Antes de seguir, decidí si esto deja un aprendizaje que una sesión futura necesite: "
  "un dato de la estancia, un interesado, algo que se probó y falló, una regla nueva, un ID de Meta. "
  "Si es así, actualizá el Estado actual y agregá la entrada fechada a memory.md ahora."
)
print(json.dumps({
  "systemMessage": "Recordatorio: ¿esto va a memory.md?",
  "hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": aviso}
}))
' "$ultimo"
