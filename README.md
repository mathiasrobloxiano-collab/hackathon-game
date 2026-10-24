# ⚛️ De Newton a los Qubits (1687 — 2026)

> **"No implementamos todos los algoritmos cuánticos. Lo que construimos es la rampa que falta antes de ellos, y la validamos con hardware real en lugar de simularla."**

[![Qiskit 2.6.1](https://img.shields.io/badge/Qiskit-2.6.1-6929C4?style=for-the-badge&logo=qiskit)](https://github.com/Qiskit/qiskit)
[![IBM Quantum](https://img.shields.io/badge/QPU_Real-ibm__kingston_(156_Qubits)-00F0FF?style=for-the-badge&logo=ibm)](https://quantum.cloud.ibm.com/)
[![Demo Web](https://img.shields.io/badge/🌐_Jugar_Demo_Web_en_1_Clic-GitHub_Pages-10B981?style=for-the-badge)](https://mathiasrobloxiano-collab.github.io/hackathon-game/)

---

## 🎯 Acceso Rápido para el Jurado

1. 🌐 **Demo Web Instantánea (Sin instalar nada):**  
   👉 **[https://mathiasrobloxiano-collab.github.io/hackathon-game/](https://mathiasrobloxiano-collab.github.io/hackathon-game/)** *(o abre directamente [`index.html`](index.html) en cualquier navegador)*.
2. 📓 **Jupyter Notebook Oficial de Verificación Qiskit + Hardware Real:**  
   👉 **[`experimentos_qiskit_ibm_kingston.ipynb`](experimentos_qiskit_ibm_kingston.ipynb)** *(contiene el código Qiskit, circuitos transpilados y los Job IDs reales ejecutados en `ibm_kingston`)*.
3. 🎬 **Guion Oficial de Exposición por Escenas (`02:48`):**  
   👉 **[`GUION_VIDEO_PRESENTACION.md`](GUION_VIDEO_PRESENTACION.md)**
4. ⚡ **Ejecutables Locales en 1 Clic (Motor Python + Qiskit + IBM Quantum Platform en Vivo):**
   - **Windows:** Doble clic en **[`iniciar_juego.bat`](iniciar_juego.bat)** *(o `python de_newton_a_los_qubits.py`)*.
   - **macOS / Linux:** Ejecutar **`./iniciar_juego.sh`** *(o `python3 de_newton_a_los_qubits.py`)*.

---

## 📋 Evidencia de Ejecución en Procesador Cuántico Físico (`ibm_kingston` · 156 Qubits Heron r2)

Todos los histogramas y procesos cuánticos del proyecto están respaldados por circuitos reales ejecutados mediante `QiskitRuntimeService`, `generate_preset_pass_manager` y `SamplerV2` en la instancia `open-instance` (`us-east`):

| Job ID Oficial (IBM Quantum Platform) | Procesador QPU | Qubits Usados | Proceso / Experimento Cuántico | Estado |
| :--- | :---: | :---: | :--- | :---: |
| `dbeg6fvgdj9s73flnokg` | `ibm_kingston` | 8 Qubits | Certificación Física de No-Localidad Bell-CHSH ($S > 2$) | ✅ `COMPLETED` |
| `dbeg6fvgdj9s73flnojg` | `ibm_kingston` | 60 Qubits | Cadena Entrelazada de Gran Escala (Supera límite de RAM clásica) | ✅ `COMPLETED` |
| `dbeg6evgdj9s73flnohg` | `ibm_kingston` | 16 Qubits | Generador Cuántico QRNG en Paralelo ($H^{\otimes 16}$) para Monte Carlo $\pi$ | ✅ `COMPLETED` |
| `dbeg6dngdj9s73flnoeg` | `ibm_kingston` | 3 Qubits | Oráculo y Difusor Cuántico de Grover ($O(\sqrt{N})$) | ✅ `COMPLETED` |
| `dbeg637gdj9s73flnnmg` | `ibm_kingston` | 3 Qubits | Teletransportación Cuántica Física de Estado Continuo $|\psi\rangle$ | ✅ `COMPLETED` |
| `dbeg3hfpc3tc739lkhng` | `ibm_kingston` | 3 Qubits | Compositor Interactivo de Circuitos (Nivel 8) | ✅ `COMPLETED` |
| `dbefh5vgdj9s73flmbb0` | `ibm_kingston` | 60 Qubits | Utilidad Cuántica de 60 Qubits Entrelazados (16,384 PB RAM equiv.) | ✅ `COMPLETED` |

---

## 🚀 Arquitectura y los 10 Niveles Históricos (1687 — 2026)

1. **Modo Historia de 10 Niveles Cronológicos con Simuladores 3D:**
   - **Nivel 1 (1687 — Newton):** Balística determinista en 3D y gravitación universal.
   - **Nivel 2 (1900 — Planck):** Cuantización de la energía ($E = n \cdot h \cdot \nu$), radiación de cuerpo negro y efecto fotoeléctrico.
   - **Nivel 3 (1922 — Stern-Gerlach):** Cuantización espacial del espín en átomos de plata conectado a `ibm_kingston`.
   - **Nivel 4 (1927 — Doble Rendija, Heisenberg y Schrödinger):** Interferencia cuántica (`H-H`), colapso por medición en `ibm_kingston` y Principio de Incertidumbre.
   - **Nivel 5 (1935 — Paradoja EPR y Bell):** Entrelazamiento cuántico $(|00\rangle + |11\rangle)/\sqrt{2}$ y análisis del ruido térmico real $T_1/T_2$ a 14.8 mK.
   - **Nivel 6 (1981 — Feynman):** Explosión exponencial del espacio de Hilbert ($2^n$) y colapso de la RAM clásica frente a los 156 qubits de IBM.
   - **Nivel 7 (El Qubit — Bloch):** Esfera de Bloch interactiva en 3D y curva de rotaciones $R_y(\theta)$ medida en `ibm_kingston`.
   - **Nivel 8 (Circuitos Cuánticos):** Compositor interactivo de 3 qubits (`H`, `X`, `Y`, `Z`, `S`, `T`, `CNOT`, `SWAP`) y estados GHZ.
   - **Nivel 9 (1996 — Grover):** Búsqueda cuántica $O(\sqrt{N})$ por amplificación de amplitud en hardware real.
   - **Nivel 10 (2026 — Quantum Dart Race):** Estimación de $\pi$ por Monte Carlo en 3D enfrentando `Math.random()` contra bits cuánticos reales (`QRNG`) de `ibm_kingston`.

2. **6 Procesos Exclusivos que Sí o Sí Requieren una Computadora Cuántica Real (`motor_qiskit.py`):**
   - **1. Cadena Entrelazada de 45 a 127 Qubits:** Imposible de almacenar en memoria RAM clásica ($2^{60}$ amplitudes = 16,384 Petabytes de RAM).
   - **2. Test de No-Localidad Bell-CHSH en 8 Qubits:** Demuestra correlación cuántica $S > 2.0$ imposible para variables ocultas locales clásicas.
   - **3. QRNG Físico de 16 Qubits ($H^{\otimes 16}$):** Azar cuántico fundamental irreproducible con algoritmos pseudoaleatorios.
   - **4. Oráculo Cuántico de Grover de 3 Qubits (`CCZ`):** Interferencia constructiva sobre el estado buscado en paralelo físico.
   - **5. Teletransportación Cuántica de Estado Continuo:** Transferencia de $|\psi\rangle = R_y(\pi/3)R_z(\pi/4)|0\rangle$ mediante canal entrelazado de Bell.
   - **6. Diagnóstico Criogénico $T_1/T_2$ (Hahn Spin Echo):** Sondeo en vivo de la relajación térmica real del chip superconductor a 15 milikelvin.

---

## 🛠️ Instalación y Ejecución con Python + Qiskit + IBM Quantum Platform

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. (Opcional) Copiar plantilla de credenciales IBM Quantum Platform
cp ibm_credentials.example.json ibm_credentials.json

# 3. Iniciar servidor cuántico y abrir el juego automáticamente en http://localhost:8080/index.html
python de_newton_a_los_qubits.py
```
