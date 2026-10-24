# -*- coding: utf-8 -*-
import json
import os
import subprocess
import urllib.request
import urllib.error
import webbrowser
import sys

def abrir_en_chrome(url: str):
    """Abre una URL directamente en Google Chrome (o navegador predeterminado)."""
    rutas_chrome = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe")
    ]
    for ruta in rutas_chrome:
        if os.path.exists(ruta):
            subprocess.Popen([ruta, url])
            return
    webbrowser.open(url)

def obtener_credenciales_github():
    print("[GitHub] Abriendo Google Chrome directamente para autorizar con GitHub...", flush=True)
    env = os.environ.copy()
    env["GCM_GUI_PROMPT"] = "false"
    env["GCM_GITHUB_AUTHMODES"] = "browser"
    env["GCM_INTERACTIVE"] = "always"

    gcm_exe = r"C:\Program Files\Git\mingw64\bin\git-credential-manager.exe"
    cmd = [gcm_exe, "get"] if os.path.exists(gcm_exe) else ["git", "credential", "fill"]

    proc = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        env=env
    )
    entrada = "protocol=https\nhost=github.com\n\n"
    out, err = proc.communicate(input=entrada, timeout=240)
    if err:
        print(err, flush=True)
    creds = {}
    for line in out.splitlines():
        if "=" in line:
            k, v = line.split("=", 1)
            creds[k.strip()] = v.strip()

    # Guardar la credencial en Git Credential Manager para que no vuelva a pedirla
    if creds.get("password"):
        try:
            store_cmd = [gcm_exe, "store"] if os.path.exists(gcm_exe) else ["git", "credential", "approve"]
            p_store = subprocess.Popen(store_cmd, stdin=subprocess.PIPE, text=True, env=env)
            p_store.communicate(
                input=f"protocol=https\nhost=github.com\nusername={creds.get('username','oauth2')}\npassword={creds['password']}\n\n",
                timeout=10
            )
        except Exception:
            pass
    return creds

def crear_y_subir_repo(nombre_repo="de-newton-a-los-qubits"):
    creds = obtener_credenciales_github()
    token = creds.get("password")
    if not token:
        print("[Error] No se obtuvo token de GitHub.", flush=True)
        sys.exit(1)

    req_user = urllib.request.Request(
        "https://api.github.com/user",
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "User-Agent": "DeNewtonALosQubits-Uploader"
        }
    )
    with urllib.request.urlopen(req_user) as resp:
        user_data = json.loads(resp.read().decode("utf-8"))
        login = user_data["login"]
        print(f"[GitHub] Conectado a la cuenta de GitHub: @{login}", flush=True)

    payload = json.dumps({
        "name": nombre_repo,
        "description": "De Newton a los Qubits — Juego educativo de fisica cuantica conectado en tiempo real a Python, Qiskit 2.x e IBM Quantum Platform (ibm_kingston 156 qubits)",
        "private": False,
        "auto_init": False
    }).encode("utf-8")

    req_repo = urllib.request.Request(
        "https://api.github.com/user/repos",
        data=payload,
        method="POST",
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "Content-Type": "application/json",
            "User-Agent": "DeNewtonALosQubits-Uploader"
        }
    )
    try:
        with urllib.request.urlopen(req_repo) as resp:
            repo_data = json.loads(resp.read().decode("utf-8"))
            html_url = repo_data["html_url"]
            clone_url = repo_data["clone_url"]
            print(f"[GitHub] Repositorio creado exitosamente: {html_url}", flush=True)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="ignore")
        if e.code == 422:
            html_url = f"https://github.com/{login}/{nombre_repo}"
            clone_url = f"https://github.com/{login}/{nombre_repo}.git"
            print(f"[GitHub] El repositorio ya existe: {html_url}", flush=True)
        else:
            print(f"[Error API GitHub {e.code}] {body}", flush=True)
            sys.exit(1)

    subprocess.run(["git", "remote", "remove", "origin"], stderr=subprocess.DEVNULL)
    subprocess.run(["git", "remote", "add", "origin", clone_url], check=True)
    subprocess.run(["git", "branch", "-M", "main"], check=True)
    print(f"[GitHub] Subiendo archivos a {html_url} ...", flush=True)
    subprocess.run(["git", "push", "-u", "origin", "main", "--force"], check=True)
    print(f"[EXITO] Todo el proyecto ya esta publicado en: {html_url}", flush=True)
    abrir_en_chrome(html_url)

if __name__ == "__main__":
    crear_y_subir_repo("de-newton-a-los-qubits")
