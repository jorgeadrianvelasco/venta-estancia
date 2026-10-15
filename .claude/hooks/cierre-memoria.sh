#!/usr/bin/env bash
# Se ejecuta cuando Claude termina de responder.
# Avisa si la sesión avanzó sin dejar nada registrado en memory.md.
set -uo pipefail
cd "${CLAUDE_PROJECT_DIR:-$(dirname "$0")/../..}" 2>/dev/null || exit 0

hoy=$(date +%Y-%m-%d)
# ¿memory.md cambió hoy, en commits o en el árbol de trabajo?
tocado_commit=$(git log --since="$hoy 00:00" --format=%H -- memory.md 2>/dev/null | head -1)
tocado_arbol=$(git status --porcelain -- memory.md 2>/dev/null)

if [ -z "$tocado_commit" ] && [ -z "$tocado_arbol" ]; then
  python3 -c '
import json
print(json.dumps({
  "systemMessage": "memory.md no se tocó hoy. Si esta sesión dejó algo que la próxima necesite saber, usá /cerrar."
}))
'
fi
