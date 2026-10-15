#!/usr/bin/env bash
# Se ejecuta al abrir cada sesión de Claude Code en este repositorio.
# Inyecta el estado actual de la venta para que la sesión no arranque a ciegas.
set -uo pipefail
cd "${CLAUDE_PROJECT_DIR:-$(dirname "$0")/../..}" 2>/dev/null || exit 0

{
  echo "=== ESTADO DE LA VENTA DE LA ESTANCIA AL INICIAR LA SESIÓN ==="
  echo
  echo "Rama: $(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo '?')"
  echo "Último commit: $(git log -1 --format='%h %s' 2>/dev/null || echo '?')"
  echo
  echo "--- Estado actual (memory.md) ---"
  # Bloque entre "## Estado actual" y el siguiente título "## ".
  awk '/^## Estado actual/{f=1; next} f && /^## /{exit} f' memory.md 2>/dev/null || echo "(sin memory.md)"
  echo
  echo "--- Últimas líneas de la bitácora ---"
  awk '/^## Bitácora/{f=1; next} f' memory.md 2>/dev/null | tail -n 15
  lineas=$(wc -l < memory.md 2>/dev/null || echo 0)
  if [ "$lineas" -gt 300 ]; then
    echo
    echo "AVISO: memory.md tiene $lineas líneas. Mové las entradas viejas a memoria/AAAA-MM.md."
  fi
  echo
  echo "--- Recordatorio ---"
  echo "Leé reglas.md antes de actuar: son las reglas que no se negocian."
  echo "La ficha de la estancia está en negocio.md; el porqué de cada decisión, en decisiones.md."
  echo "Cómo trabaja Jorge está en como-trabaja-jorge.md."
} | python3 -c '
import sys, json
ctx = sys.stdin.read()
print(json.dumps({"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": ctx}}))
'
