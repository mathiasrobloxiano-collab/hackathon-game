# -*- coding: utf-8 -*-
"""
de_newton_a_los_qubits.py — Lanzador Principal en Python + Qiskit IBM Quantum
=============================================================================
Ejecuta el servidor interactivo del proyecto "De Newton a los Qubits"
conectado con Qiskit 2.x, Qiskit Aer y QiskitRuntimeService (ibm_kingston).

Uso:
    python de_newton_a_los_qubits.py
"""

from app import iniciar_servidor

if __name__ == "__main__":
    iniciar_servidor(abrir_navegador=True)

