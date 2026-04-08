# 📝 Descrição

 **Pull Request:** ENG-XXX | Nome da Task

 **Relacionado a:**

- [ ] 🏗️ Setup de ambiente: Configuração/Infra (`chore`)
- [ ] 🐍 Nova Feature (`feat`)
- [ ] 🐛 Correção de Bug (`fix`)

## 🎯 Contexto

> *Explique de forma simples o que mudou*

## 🏷️ Tipo de Mudança e Escopo Técnico (Onde foi alterado)

- [ ] ✨ **Nova Funcionalidade:** (`feat`) Adição de um novo endpoint, criação de um novo modelo de dados, nova métrica ou gráfico no dashboard.
  - [ ] 🐍 **Código Core:** Lógica de negócio, funções ou classes principais.
  - [ ] 🌐 **API/Serviços:** Novos endpoints, contratos de API (Swagger), integrações.
  - [ ] 📊 **Dados/Banco de Dados:** Migrations, tabelas, scripts de processamento.
  - [ ] 🎨 **Front-End/UX:** Alterações em componentes, fluxos de navegação, estilos.
- [ ] 🧪 **Testes** (`test`) Adição ou alteração de testes unitários/integrados.
- [ ] 🐛 **Correção de Bug:** (`fix`) Tratamento de falhas (ex: NullPointer), ajuste em query SQL que duplicava dados, correção de erro em produção.
- [ ] ♻️ **Refatoração:** (`refactor`) Aplicação de SOLID, otimização de performance, reescrita de código para Clean Code sem mudar a regra de negócio.
- [ ] 💥 **Breaking Change:** (`feat!` ou `refactor!`) Mudança de contrato em uma API, remoção de tabela/coluna no banco, alteração que exige atualização dos clientes.
- [ ] 📚/🔧 **Outros:** (`chore`) (`docs`) Adição de docstrings, atualização de README, ajustes em Docker ou pipeline de CI/CD.
  - [ ] 🏗️ **Infra/Configuração:** Docker, dependências, arquivos de CI/CD.

## 📸 Evidências & Testes

> *Cole aqui print visual caso exista neste momento do projeto*

**📊 Cobertura de Testes (Unitários/Integrados):**

- [ ] 🌑 Não iniciado a implementação (0%)
- [ ] 🔴 Abaixo de 50% (Atenção necessária)
- [ ] 🟡 Entre 50% e 80% (Aceitável, mas com pontos de melhoria)
- [ ] 🟢 Acima de 80% (Padrão ideal)

**🛡️ Qualidade e Padrões de Engenharia:**

- [ ] ☁️ **Quality Gate:** Passou no SonarCloud com sucesso.
- [ ] 📖 **Clean Code & Docstrings:** Todos os arquivos (novos ou alterados) possuem docstrings claras e respeitam os princípios de Clean Code e SOLID.

**🖼️ Prints / Logs:**

> *Adicione aqui o print do terminal mostrando os testes passando, o link do SonarCloud ou a evidência visual da pipeline de CI/CD.*
> Recortar e colar no comentário do PR, antes de realizar o Squash Merge, confirmando todos os itens'

**Checklist obrigatório:**

Confirmação de execução local:

- [ ] `pytest` passa localmente com `--cov-fail-under=80`
- [ ] SonarCloud Quality Gate verde (sem new code smells)
- [ ] Docstrings em todas as funções novas ou alteradas
- [ ] SOLID aplicado (especialmente SRP — funções com uma responsabilidade)
- [ ] Sem `print()` de debug, sem imports não usados
- [ ] Nenhuma credencial ou secret no código
- [ ] `requirements.txt` atualizado (se instalou nova lib)
- [ ] `README.md` atualizado (se adicionou nova feature ou endpoint)
