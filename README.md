# 🚀 Career Pipeline API — Plataforma de Recrutamento e Carreira com IA

![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=tinalmeid_python-tinas-career-pipeline&metric=alert_status)
![Coverage](https://sonarcloud.io/api/project_badges/measure?project=tinalmeid_python-tinas-career-pipeline&metric=coverage)
![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=tinalmeid_python-tinas-career-pipeline&metric=duplicated_lines_density)
![Build Status](https://github.com/tinalmeid/python-tinas-career-pipeline/actions/workflows/ci.yml/badge.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Desenvolvimento

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/API-FastAPI-009688?style=flat&logo=fastapi&logoColor=white)
![Pytest](https://img.shields.io/badge/Testes-Pytest-0A9EDC?style=flat&logo=pytest&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/ORM-SQLAlchemy-D71F00?style=flat)
![Pydantic](https://img.shields.io/badge/Validação-Pydantic-3776AB?style=flat)
![Celery](https://img.shields.io/badge/Filas-Celery-37814A?style=flat&logo=celery&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)

## Infraestrutura

![Docker](https://img.shields.io/badge/Container-Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Neon](https://img.shields.io/badge/Serverless-Neon_PostgreSQL-00E599?style=flat&logo=neon&logoColor=white)
![Neon PGMQ](https://img.shields.io/badge/Fila-Neon_PGMQ-00E599?style=flat&logo=neon&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/BD-PostgreSQL-4169E1?style=flat&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/Cache-Redis-DC382D?style=flat&logo=redis&logoColor=white)

## Produtividade, Gestão & DevOps

![WakaTime](https://img.shields.io/badge/WakaTime-000000?style=flat&logo=wakatime&logoColor=white)
![Jira](https://img.shields.io/badge/Gestão-Jira-0052CC?style=flat&logo=jira&logoColor=white)
![Azure DevOps](https://img.shields.io/badge/Gestão-Azure_DevOps-0078D7?style=flat&logo=azuredevops&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/CI-GitHub_Actions-2088FF?style=flat&logo=githubactions&logoColor=white)
![SonarCloud](https://img.shields.io/badge/Quality-SonarCloud-F3702A?style=flat&logo=sonarcloud&logoColor=white)
![Clean Code](https://img.shields.io/badge/Prática-Clean_Code-green?style=flat)

## Observabilidade

![Grafana](https://img.shields.io/badge/Dashboard-Grafana-F46800?style=flat&logo=grafana&logoColor=white)
![Prometheus](https://img.shields.io/badge/Métricas-Prometheus-E6522C?style=flat&logo=prometheus&logoColor=white)
![Loki](https://img.shields.io/badge/Logs-Loki-FF6F00?style=flat)

---

> Sistema de microsserviços para gestão de vagas aplicadas no Linkedin.
> O usuário seleciona as vagas para busca de vagas, gerencia candidaturas e fornece métricas de desempenho para as novas oportunidades.

O projeto utiliza uma arquitetura blindada por testes automatizados, observabilidade proativa (Loki/Prometheus) e análise estática rigorosa.

## 🚀 Como Rodar (Quick Start)

### Pre-requisitos

- Python 3.12 or higher
- Docker & Docker Compose
- pip (Python package manager)

### Instalação

1.📥**Clone o repositório:**

```Bash
git clone https://github.com/tinalmeid/python-tinas-career-pipeline.git
```

2.🐍**Crie o ambiente virtual:**

```Bash
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

3.📦**Instale as dependências:**

```Bash
pip install --upgrade pip
pip install -r requirements-dev.txt
```

🔬Rode os Testes:

```Bash
pytest tests/ -v
```

## 🧪 Padrões de Qualidade (QA Engineering)

Para garantir a excelência do código, este projeto utiliza um Quality Gate rigoroso:

1. **Linting (Pylint):** O código deve seguir a PEP8.

2. **Testes (Pytest):** Cobertura mínima de 80% exigida pelo SonarCloud.

3. **Clean Code:** Funções pequenas, nomes descritivos e princípios SOLID.

4. **Code Review:** Nenhum código entra na main sem passar pela pipeline de CI (GitHub Actions).

## 📝 Development Guidelines

Para manter a qualidade e a rastreabilidade do projeto, seguimos estritamente:

1. **🌿 Branching Strategy:**

    - Toda branch deve começar com a chave do Jira: `ENG-XXX-nome-da-tarefa`.
    - Ex: `ENG-XXX-infra/python-setup`.

2. **💾 Padrão de Commit (Conventional Commits):**

    - Formato: `ENG-XXX tipo: Descrição breve`.
    - Tipos permitidos:
      - `feat`: Nova funcionalidade.
      - `fix`: Correção de bug.
      - `docs`: Documentação.
      - `test`: Testes.
      - `refactor`: Melhoria de código sem alterar funcionalidade.
      - `chore`: Configurações e manutenção.
    - Ex: `ENG-586 chore: Configura pipeline inicial`.

3. **🧪 Testes & TDD:**

    - Toda nova funcionalidade em `src/` deve ter um teste correspondente em `tests/`.
    - Rode `pytest` localmente antes de subir o código.

4. **🛡️ Quality Gate:**

    - Para aceite de Pull Requests será necessário aprovação do **Quality Gate (SonarCloud)** e conformidade com o Checklist de Engenharia **(SOLID + Clean Code)**.

    - Código sem **Docstrings** (documentação de função) será reprovado no Code Review.
    - Mantenha o **SonarCloud** feliz: Zero "Bugs", Zero "Vulnerabilities" e Cobertura aceitável.

5. **🧹 Clean Code:**
    - **Variáveis descritivas:** Proibido o uso de nomes genéricos como x, y, aux ou data.
    - **Respeito absoluto à PEP 8:** O código deve seguir as convenções oficiais do Python.

## 🏗️ Estrutura do Projeto

```Text
python-tinas-career-pipeline/
├── .github/
│   └── workflows/           # 🤖 Automação (GitHub Actions)
├── docker/                  # 🐳 Configuração de Observabilidade (Loki/Prometheus)
├── docs/                    # 📝 Templates de padrões (Git, Jira, SOLID) e documentação técnica
├── scripts/                 # ⚙️ Scripts utilitários e suporte à infraestrutura (Shell/Python)
├── src/                     # 🧠 Core da aplicação, API e processamento de dados
├── tests/                   # 🧪 Suíte de testes automatizados com Pytest
├── .gitignore
├── azure-pipeline.yaml      # 🕸️ Configuração legada de CI/CD (Mantida para referência histórica)
├── README.md
├── requirements             # 📦 Gerenciamento de dependências do projeto e de desenvolvimento
└── sonar-project.properties # 📡 Definições de Qualidade e chaves do SonarCloud
```

## 🗺️ Roadmap & Entregas (Jira)

Monitoramento de tarefas de desenvolvimento com base no fluxo de trabalho de Engenharia.

| ID Jira | Módulo / Tarefa | Branch | Status |
| --------- | ------- | --------- | ------- |
| ENG-659 | Setup do projeto e ambiente virtual | ENG-659-infra/python-setup | ✅ Concluído |
| ENG-660 | SonarCloud e GitHub Actions CI | ENG-660-infra/sonarcloud-ci | ✅ Concluído |
| ENG-661 | Docker Compose observabilidade local | ENG-661-infra/docker-observability | ✅ Concluído |
| ENG-662 | Segurança e feature toggles | ENG-662-infra/security-toggles | ✅ Concluído |
| ENG-663 | README completo e badges | ENG-663-docs/readme | ✅ Concluído |
| ENG-664 | Documentação API Swagger/OpenAPI | ENG-664-docs/api-docs | 📝 A Fazer |
| ENG-665 | Modelos de dados Pydantic | ENG-665-core/models-pydantic | 📝 A Fazer |
| ENG-666 | Schema e migrações Alembic | ENG-666-core/schema-migrations | 📝 A Fazer |
| ENG-667 | LinkedIn scraper com resiliência | ENG-667-core/linkedin-scraper | 📝 A Fazer |
| ENG-668 | Repository e persistência Neon | ENG-668-core/repository-neon | 📝 A Fazer |
| ENG-669 | Pipeline de busca (scraper + repo) | ENG-669-core/search-pipeline | 📝 A Fazer |
| ENG-670 | Health check e modo offline | ENG-670-core/health-offline | 📝 A Fazer |
| ENG-671 | API: GET Endpoints | ENG-671-api/get-endpoints | 📝 A Fazer |
| ENG-672 | API: POST/PUT Endpoints | ENG-672-api/post-put-endpoints | 📝 A Fazer |
| ENG-673 | API: Rate limit e Security Middleware | ENG-673-api/rate-limit-security | 📝 A Fazer |
| ENG-674 | CLI: Comandos básicos | ENG-674-cli/basic-commands | 📝 A Fazer |
| ENG-675 | CLI: Comandos avançados | ENG-675-cli/advanced-commands | 📝 A Fazer |
| ENG-676 | Dash: Streamlit Tema Dark | ENG-676-dash/streamlit-dark | 📝 A Fazer |
| ENG-677 | Dash: KPIs e Gráficos | ENG-677-dash/kpis-graphs | 📝 A Fazer |
| ENG-678 | Dash: Exportação e Filtros | ENG-678-dash/export-filters | 📝 A Fazer |
| ENG-679 | OBS: Métricas Prometheus | ENG-679-obs/prometheus-metrics | 🚧 Em Andamento |
| ENG-680 | OBS: Logs Loki | ENG-680-obs/loki-logs | 🚧 Em Andamento |
| ENG-681 | QA: Segurança e Cobertura 80% | ENG-681-qa/security-coverage | 📝 A Fazer |
| ENG-682 | OPS: Housekeeping anual | ENG-682-ops/housekeeping | 📝 A Fazer |
| ENG-683 | CORE: NLP - Extração de Skills | ENG-683-core/nlp-skills | 📝 A Fazer |
| ENG-684 | CORE: Deduplicação e Blacklist | ENG-684-core/dedup-logic | 📝 A Fazer |
| ENG-685 | DASH: Interface Painel Kanban | ENG-685-dash/kanban-board | 📝 A Fazer |

> **Legenda:** ✅ Concluído | 🚧 Em Andamento | 📝 A Fazer

## 📄 Licença

Este projeto faz parte de um curso de aprendizagem. Sinta-se à vontade para utilizá-lo para fins educacionais.

👩🏽‍💻 Desenvolvido por **Cristina de Almeida** como parte do plano de desenvolvimento técnico.
