# @file scripts/start-observability.sh
# @description Script para iniciar o stack de observabilidade (Prometheus, Grafana, Loki e Promtail) para o projeto python_tinas_career_pipeline.
# Este script verifica se o docker-compose está instalado, inicia os serviços em segundo plano e
# fornece informações de acesso aos dashboards e interfaces dos serviços.
#
# @author Tina de Almeida
# @date Abril 2026
# @version 1.0.0

# Verificar se o docker desktop está instalado e rodando: docker version
# Script para iniciar o stack de observabilidade
# Verificar se o docker desktop está instalado e rodando
# Rode no terminal: bash scripts/start-observability.sh
# Aguardar os serviços subirem corretamente
# Verificar se está rodando : docker ps
# Para para os serviços use: bash scripts/stop-observability.sh ou docker-compose down

set -e

echo "🚀 Iniciando stack de observabilidade..."

# Verificar se docker-compose está instalado
if ! command -v docker-compose &> /dev/null; then
    echo "❌ docker-compose não encontrado. Instale primeiro."
    exit 1
fi

# Iniciar os serviços
docker-compose up -d

# Aguardar serviços ficarem prontos
echo "⏳ Aguardando serviços iniciarem..."
sleep 5

echo "✅ Stack de observabilidade iniciada!"
echo ""
echo "📊 Acessos:"
echo "  - Prometheus: http://localhost:9090"
echo "  - Grafana: http://localhost:3000 (admin/admin)"
echo "  - Loki: http://localhost:3100"
echo "  - Promtail: http://localhost:9080"
echo ""
echo "Para parar: ./scripts/stop-observability.sh"
