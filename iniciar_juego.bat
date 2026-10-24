@echo off
chcp 65001 > nul
title De Newton a los Qubits — Motor Python + Qiskit IBM Quantum
cd /d "%~dp0"
if exist ".venv\Scripts\python.exe" (
    ".venv\Scripts\python.exe" de_newton_a_los_qubits.py
) else (
    python de_newton_a_los_qubits.py
)
pause

