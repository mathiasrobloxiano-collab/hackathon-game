# -*- coding: utf-8 -*-
"""
app.py — Aplicación Principal y Servidor Cuántico en Python + IBM Quantum Platform
==================================================================================
Proyecto: "De Newton a los Qubits"
Conecta la interfaz 3D del juego educativo con Qiskit 2.x e IBM Quantum Platform.
"""

import json
import os
import sys
import threading
import webbrowser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from motor_qiskit import motor_cuantico

DIRECTORIO_BASE = Path(__file__).parent.resolve()
ARCHIVO_PROGRESO = DIRECTORIO_BASE / "progreso_jugador.json"
PUERTO_SERVIDOR = 8080


def cargar_progreso_disco():
    if ARCHIVO_PROGRESO.exists():
        try:
            return json.loads(ARCHIVO_PROGRESO.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {
        "jugador": {
            "nombre": "Mathias",
            "institucion": "Laboratorio Qiskit IBM",
            "avatar": "bohr",
            "modo_juego": "historia",
            "sesion_iniciada": False
        },
        "nivelActual": 1,
        "nivelMaximoDesbloqueado": 1,
        "xp": 0,
        "nivelesCompletados": [],
        "tarjetasDesbloqueadas": [],
        "quizzesResueltos": {},
        "medallasDesbloqueadas": []
    }


def guardar_progreso_disco(datos: dict):
    try:
        ARCHIVO_PROGRESO.write_text(
            json.dumps(datos, indent=2, ensure_ascii=False),
            encoding="utf-8"
        )
        return True
    except Exception as e:
        print(f"[Aviso] No se pudo guardar progreso en disco: {e}")
        return False


class ManejadorJuegoCuantico(SimpleHTTPRequestHandler):
    """Manejador HTTP en Python que sirve la aplicación y la API de Qiskit + IBM Quantum Platform."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIRECTORIO_BASE), **kwargs)

    def log_message(self, format, *args):
        # Silenciar logs estáticos innecesarios para mantener limpia la consola
        pass

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        super().end_headers()

    def _enviar_json(self, datos: dict, status_code: int = 200):
        cuerpo = json.dumps(datos, ensure_ascii=False).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(cuerpo)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
        self.wfile.write(cuerpo)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        parsed = urlparse(self.path)
        ruta = parsed.path
        qs = parse_qs(parsed.query)

        if ruta == "/api/status":
            estado_qiskit = motor_cuantico.obtener_estado()
            self._enviar_json(estado_qiskit)
            return

        elif ruta == "/api/workloads":
            limite = int(qs.get("limite", [10])[0])
            forzar = str(qs.get("forzar", ["0"])[0]) in ("1", "true", "True")
            datos_wl = motor_cuantico.obtener_workloads_ibm(limite=limite, forzar_cloud=forzar)
            self._enviar_json(datos_wl)
            return

        elif ruta == "/api/workload_detalle":
            job_id = qs.get("job_id", [""])[0]
            if not job_id:
                self._enviar_json({"ok": False, "mensaje": "Falta job_id"}, status_code=400)
                return
            detalle = motor_cuantico.consultar_workload_por_id(job_id)
            self._enviar_json(detalle)
            return

        elif ruta == "/api/progreso":
            progreso = cargar_progreso_disco()
            self._enviar_json({"ok": True, "progreso": progreso})
            return

        return super().do_GET()

    def do_POST(self):
        ruta = urlparse(self.path).path
        longitud = int(self.headers.get("Content-Length", 0))
        cuerpo_raw = self.rfile.read(longitud).decode("utf-8") if longitud > 0 else "{}"

        try:
            payload = json.loads(cuerpo_raw)
        except Exception:
            payload = {}

        if ruta == "/api/ejecutar":
            nivel = int(payload.get("nivel", 1))
            parametros = payload.get("parametros", {})
            print(f"[Qiskit + IBM Quantum] Ejecutando Nivel {nivel} | Params: {parametros}", flush=True)
            resultado = motor_cuantico.ejecutar_experimento(nivel, parametros)
            self._enviar_json(resultado)
            return

        elif ruta == "/api/proceso_qpu":
            tipo_proceso = payload.get("tipo_proceso", "supremacia_gran_escala")
            parametros = payload.get("parametros", {})
            print(f"[IBM Quantum Platform QPU] Ejecutando proceso exclusivo: {tipo_proceso} | Params: {parametros}", flush=True)
            resultado = motor_cuantico.ejecutar_proceso_exclusivo_qpu(tipo_proceso, parametros)
            self._enviar_json(resultado)
            return

        elif ruta == "/api/conectar_ibm":
            token = payload.get("token", "")
            instance = payload.get("instance", "")
            channel = payload.get("channel", "ibm_quantum_platform")
            print("[IBM Quantum Platform] Conectando QiskitRuntimeService...")
            res = motor_cuantico.configurar_cuenta_ibm(token=token, instance=instance, channel=channel)
            self._enviar_json(res)
            return

        elif ruta == "/api/modo":
            modo = payload.get("modo", "simulador_ruido_kingston")
            backend = payload.get("backend", None)
            estado_actual = motor_cuantico.cambiar_modo_ejecucion(modo, backend)
            self._enviar_json({"ok": True, "estado": estado_actual})
            return

        elif ruta == "/api/progreso":
            guardar_progreso_disco(payload)
            self._enviar_json({"ok": True, "mensaje": "Progreso guardado en Python correctamente."})
            return

        self._enviar_json({"ok": False, "mensaje": "Ruta API no encontrada"}, status_code=404)


def _limpiar_servidores_previos():
    """Termina cualquier proceso python.exe anterior que haya quedado escuchando en el puerto 8080."""
    try:
        import psutil
        mi_pid = os.getpid()
        pids_excluidos = {mi_pid, os.getppid()}
        try:
            proc_actual = psutil.Process(mi_pid)
            for parent in proc_actual.parents():
                pids_excluidos.add(parent.pid)
        except Exception:
            pass
        pids_a_cerrar = set()

        # 1. Buscar por conexiones de red en el puerto 8080
        try:
            for conn in psutil.net_connections(kind="inet"):
                if conn.laddr and conn.laddr.port == PUERTO_SERVIDOR and conn.pid and conn.pid not in pids_excluidos:
                    pids_a_cerrar.add(conn.pid)
        except Exception:
            pass

        # 2. Buscar por nombre/línea de comandos de Python
        for proc in psutil.process_iter(["pid", "name", "cmdline"]):
            try:
                pid = proc.info["pid"]
                if pid in pids_excluidos:
                    continue
                nombre = (proc.info["name"] or "").lower()
                cmd = " ".join(proc.info["cmdline"] or []).lower()
                if "python" in nombre and ("de_newton_a_los_qubits" in cmd or "app.py" in cmd):
                    pids_a_cerrar.add(pid)
            except Exception:
                pass

        for pid in pids_a_cerrar:
            try:
                p = psutil.Process(pid)
                print(f"[Sistema] Cerrando servidor antiguo en puerto {PUERTO_SERVIDOR} (PID {pid})...", flush=True)
                p.kill()
                p.wait(timeout=3)
            except Exception:
                pass
    except Exception:
        pass


def iniciar_servidor(abrir_navegador: bool = True):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    _limpiar_servidores_previos()
    estado = motor_cuantico.obtener_estado()
    print("=" * 74)
    print(" [QISKIT + IBM QUANTUM] DE NEWTON A LOS QUBITS - SERVIDOR PYTHON ACTIVO")
    print("=" * 74)
    print(f" * Qiskit Version         : {estado['qiskit_version']}")
    print(f" * Qiskit Aer Simulator   : {'ACTIVO' if estado['aer_disponible'] else 'Statevector Nativo'}")
    print(f" * IBM Quantum Platform   : {'CONECTADO (ONLINE)' if estado['ibm_conectado'] else 'Desconectado (' + str(estado['ultimo_error_ibm']) + ')'}")
    if estado["backends_disponibles"]:
        print(f" * QPUs de IBM Detectadas : {', '.join(estado['backends_disponibles'])}")
    print(f" * QPU Seleccionada       : {estado['backend_activo']}")
    print("-" * 74)
    url = f"http://localhost:{PUERTO_SERVIDOR}/index.html"
    print(f" -> Juego corriendo en    : {url}", flush=True)
    print("=" * 74, flush=True)

    servidor = ThreadingHTTPServer(("127.0.0.1", PUERTO_SERVIDOR), ManejadorJuegoCuantico)

    def _verificar_y_crear_workload_inicial():
        try:
            if motor_cuantico.workloads_cache:
                ids = ", ".join(w["job_id"] for w in motor_cuantico.workloads_cache[:5])
                print(f"[IBM Quantum Platform] Workloads reales sincronizados ({len(motor_cuantico.workloads_cache)}): {ids}", flush=True)
                return
            print("[IBM Quantum Platform] Enviando circuito inicial de 3 Qubits a QPU fisica ibm_kingston...", flush=True)
            res = motor_cuantico.ejecutar_experimento(8, {
                "usar_qpu_real": True,
                "shots": 1024,
                "circuito": {
                    "q0": ["H", None, "SWAP", None],
                    "q1": [None, "CNOT_CTRL", "SWAP", None],
                    "q2": [None, "CNOT_TGT", None, None]
                }
            })
            print(f"[IBM Quantum Platform] Workload Nivel 8 completado en QPU -> Job ID: {res.get('job_id')} | Estado: {res.get('estado_job')}", flush=True)
        except Exception as e:
            print(f"[IBM Quantum Platform] Aviso al verificar workloads iniciales: {e}", flush=True)

    threading.Timer(0.5, _verificar_y_crear_workload_inicial).start()

    if abrir_navegador:
        threading.Timer(0.6, lambda: webbrowser.open(url)).start()

    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        print("\n[Python] Cerrando servidor cuántico...")
        servidor.server_close()


if __name__ == "__main__":
    iniciar_servidor(abrir_navegador=True)
