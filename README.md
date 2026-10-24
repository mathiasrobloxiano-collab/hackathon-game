# ⚛️ De Newton a los Qubits (1687 — 2026)

> **"No implementamos todos los algoritmos cuánticos. Lo que construimos es la rampa que falta antes de ellos, y la validamos con hardware real en lugar de simularla."**

Juego educativo interactivo en 3D y laboratorio cuántico conectado en vivo con **Python + Qiskit 2.x + IBM Quantum Platform** (`ibm_kingston`, `ibm_fez`, `ibm_marrakesh` · 156 qubits Heron r2). Diseñado para que estudiantes de 13 a 15 años experimenten los **10 momentos históricos en que la física se rompió**, desde el determinismo de Isaac Newton en 1687 hasta la ejecución de circuitos reales en procesadores cuánticos superconductores de IBM hoy.

---

## 🚀 Características Principales

1. **Modo Historia de 10 Niveles Cronológicos con Bloqueo Progresivo (1687 – 2026):**
   - **Nivel 1 (1687 — Newton):** Balística determinista en 3D y gravitación universal.
   - **Nivel 2 (1900 — Planck):** Cuantización de la energía ($E = n \cdot h \cdot \nu$), radiación de cuerpo negro y efecto fotoeléctrico.
   - **Nivel 3 (1922 — Stern-Gerlach):** Cuantización espacial del espín en átomos de plata y precesión de Larmor en 3D.
   - **Nivel 4 (1927 — Doble Rendija, Heisenberg y Schrödinger):** Interferencia cuántica, colapso por medición, Principio de Incertidumbre ($\Delta x \cdot \Delta p \ge \hbar/2$) y pozo de potencial 3D.
   - **Nivel 5 (1935 — Paradoja EPR y Bell):** Entrelazamiento cuántico $(|00\rangle + |11\rangle)/\sqrt{2}$, violación de la desigualdad CHSH y teletransportación cuántica.
   - **Nivel 6 (1981 — Feynman):** Explosión exponencial del espacio de Hilbert ($2^n$) y límite de memoria RAM clásica.
   - **Nivel 7 (El Qubit — Bloch):** Esfera de Bloch interactiva en 3D para 3 qubits y curva de rotaciones $R_y(\theta)$ medidas en `ibm_kingston`.
   - **Nivel 8 (Circuitos Cuánticos):** Compositor interactivo de 3 qubits (`H`, `X`, `Y`, `Z`, `S`, `T`, `CNOT`, `SWAP`) y estados GHZ.
   - **Nivel 9 (1996 — Grover):** Búsqueda cuántica $O(\sqrt{N})$ por amplificación de amplitud vs búsqueda clásica.
   - **Nivel 10 (2026 — Quantum Dart Race):** Estimación de $\pi$ por Monte Carlo en 3D enfrentando `Math.random()` contra bits cuánticos reales medidos en `ibm_kingston`.

2. **Conexión en Vivo con IBM Quantum Platform (`qiskit-ibm-runtime`) y 6 Procesos Exclusivos de QPU:**
   - Sincronización en tiempo real con la tabla **My recent workloads** (`service.jobs()`) de IBM Quantum Platform.
   - **6 Procesos que Sí o Sí Requieren una Computadora Cuántica Real (156 Qubits):**
     1. **Utilidad Cuántica de Gran Escala (45 a 127 Qubits Entrelazados):** Supera la barrera de RAM clásica ($2^{60}$ amplitudes = 16,384 Petabytes de RAM) ejecutándose directamente en `ibm_kingston`.
     2. **Certificación Física de No-Localidad Bell-CHSH ($S > 2$):** Mide 4 pares de Bell simultáneamente en 8 qubits físicos.
     3. **QRNG Físico de 16 Qubits en Paralelo ($H^{\otimes 16}$):** Genera azar cuántico fundamental en la QPU para alimentar el Nivel 10.
     4. **Oráculo Cuántico de Grover de 3 Qubits en Hardware Real:** Ejecuta el difusor de Grover con compuerta `CCZ` en la QPU.
     5. **Teletransportación Cuántica Física de Estado Continuo $|\psi\rangle$:** Transfiere un estado entre qubits físicos usando un canal de Bell real.
     6. **Sondeo Físico de Decoherencia $T_1/T_2$ (Hahn Spin Echo):** Mide la relajación térmica real del criostato de IBM a 15 mK.

---

## 🛠️ Instalación y Ejecución

### Opción 1: Con Motor Python + Qiskit + IBM Quantum Platform (Recomendado)
1. Instala las dependencias en tu entorno virtual:
   ```bash
   pip install -r requirements.txt
   ```
2. (Opcional) Configura tus credenciales de IBM Quantum Platform creando un archivo `ibm_credentials.json` en la raíz (o ingresando tu API Token desde la interfaz del juego):
   ```json
   {
     "channel": "ibm_quantum_platform",
     "token": "TU_API_TOKEN_DE_IBM_QUANTUM",
     "instance": "TU_CRN_DE_INSTANCIA"
   }
   ```
3. Inicia el servidor y abre el juego automáticamente:
   ```bash
   python de_newton_a_los_qubits.py
   ```
   *(En Windows también puedes hacer doble clic en `iniciar_juego.bat`).*

### Opción 2: Modo Web Autónomo (Sin dependencias externas)
Abre directamente `index.html` en cualquier navegador moderno. Incluye todos los simuladores 3D y la telemetría certificada medida en `ibm_kingston` (Jobs `#dbeg3hfpc3tc739lkhng` y `#dbefh5vgdj9s73flmbb0`).
