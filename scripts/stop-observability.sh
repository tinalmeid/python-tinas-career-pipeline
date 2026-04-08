# @file scripts/stop-observability.sh
# @description Script para parar o stack de observabilidade (Prometheus, Grafana, Loki e Promtail) para o projeto python_tinas_career_pipeline.
# Este script verifica se o docker-compose está instalado e para os serviços em execução.
#
# @author Tina de Almeida
# @date Abril 2026
# @version 1.0.0

# Script para parar o stack de observabilidade
# Rode no terminal: bash scripts/stop-observability.sh
# Verificar se está rodando : docker ps
# Se os serviços não pararem, use: docker-compose down --rmi all --volumes --remove-orphans
# Pra iniciar novamente use: bash scripts/start-observability.sh ou docker-compose up -d


set -e

echo "🛑 Parando stack de observabilidade..."

# Verificar se docker-compose está instalado
if ! command -v docker-compose &> /dev/null; then
    echo "❌ docker-compose não encontrado. Instale primeiro."
    exit 1
fi

# Parar os serviços
docker-compose down

echo "✅ Stack de observabilidade parado!"
