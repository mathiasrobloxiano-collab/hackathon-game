#!/usr/bin/env bash
# Lanzador en 1 clic para macOS y Linux — De Newton a los Qubits
set -e
cd "$(dirname "$0")"
if [ -x ".venv/bin/python" ]; then
    .venv/bin/python de_newton_a_los_qubits.py
else
    python3 de_newton_a_los_qubits.py
fi
