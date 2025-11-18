import re
from datetime import datetime, time
from collections import defaultdict

# ------------------------------------------------------
# CONFIGURAÇÕES
# ------------------------------------------------------

USUARIOS_DESABILITADOS = ["guest", "teste.desativado", "old.user"]
HORARIO_MADRUGADA = (time(0, 0), time(5, 0))
BRUTE_FORCE_LIMITE = 5  # número de falhas dentro do período

# ------------------------------------------------------
# FUNÇÕES AUXILIARES
# ------------------------------------------------------

def enviar_alerta(mensagem):
    print(f"[ALERTA] {mensagem}")


def parse_log_line(linha):
    """
    Espera formato:
    2024-11-18 03:22:15 | user=jose | status=FAILED
    """
    padrao = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \| user=([a-zA-Z0-9\.\-_]+) \| status=(SUCCESS|FAILED)"
    match = re.match(padrao, linha.strip())
    if not match:
        return None

    timestamp_str, user, status = match.groups()
    timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")

    return {
        "timestamp": timestamp,
        "user": user.lower(),
        "status": status
    }


def horario_e_madrugada(timestamp):
    hora = timestamp.time()
    return HORARIO_MADRUGADA[0] <= hora <= HORARIO_MADRUGADA[1]


# ------------------------------------------------------
# DETECÇÕES
# ------------------------------------------------------

def detectar_brute_force(logs):
    falhas_por_usuario = defaultdict(list)

    for entry in logs:
        if entry["status"] == "FAILED":
            falhas_por_usuario[entry["user"]].append(entry["timestamp"])

    for user, falhas in falhas_por_usuario.items():
        if len(falhas) >= BRUTE_FORCE_LIMITE:
            enviar_alerta(f"Possível brute force detectado no usuário '{user}'. Falhas: {len(falhas)}")


def detectar_logins_madrugada(logs):
    for entry in logs:
        if entry["status"] == "SUCCESS" and horario_e_madrugada(entry["timestamp"]):
            enviar_alerta(
                f"Login de madrugada detectado. Usuário '{entry['user']}' às {entry['timestamp']}"
            )


def detectar_logins_usuarios_desabilitados(logs):
    for entry in logs:
        if entry["user"] in USUARIOS_DESABILITADOS:
            enviar_alerta(
                f"Usuário desabilitado '{entry['user']}' tentou login ({entry['status']})"
            )

# ------------------------------------------------------
# EXECUÇÃO PRINCIPAL
# ------------------------------------------------------

def processar_logs(arquivo):
    logs_processados = []
    with open(arquivo, "r") as f:
        for linha in f:
            entry = parse_log_line(linha)
            if entry:
                logs_processados.append(entry)

    detectar_brute_force(logs_processados)
    detectar_logins_madrugada(logs_processados)
    detectar_logins_usuarios_desabilitados(logs_processados)


if __name__ == "__main__":
    processar_logs("exemplo_logs.txt")
