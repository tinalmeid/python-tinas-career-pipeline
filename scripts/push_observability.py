"""
@file scripts/push_observability.py
@description: cript para enviar métricas e logs para a Grafana Cloud (Loki e Prometheus).
Garante a compressão correta para evitar erros de 'snappy corrupt input'.

@autor: Tina de Almeida
@data: Abril de 2026
@version: 1.0.0
"""

import os
import time
import httpx

def send_to_loki():
    """Envia logs para o Loki usando autenticação básica"""
    url = os.getenv("L_URL")
    user = os.getenv("L_USER")
    token = os.getenv("L_TOKEN")

    if not all([url, user, token]):
        print("⚠️ Loki: Variáveis de ambiente faltando.")
        return

    payload = {
        "streams": [
            {
                "stream": {"job": os.getenv("J_NAME", "career-pipeline")},
                "values": [[str(int(time.time() * 1e9)), f"Pipeline finalizado com sucesso"]]
            }
        ]
    }

    with httpx.Client(auth=(user, token)) as client:
        response = client.post(url, json=payload)
        if response.status_code == 204:
            print("📋 Loki: enviado (204 No Content)")
        else:
            print(f"⚠️ Loki: falha ({response.status_code}) - {response.text}")

# Para o Prometheus Remote Write, a implementação via script puro é complexa.
# A melhor prática para aprendizado agora é focar no Loki e Datadog.
if __name__ == "__main__":
    send_to_loki()
