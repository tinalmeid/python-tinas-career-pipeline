# 📘 Padrões de Git e Code Review

Este documento define os padrões de qualidade, versionamento e revisão de código do projeto.

## 1.⚡Cheatsheet (Fluxo de Trabalho)

Siga esta ordem para executar suas tarefas sem erros.

### 1. Volte para a main e atualize

Sempre atualize a main antes de criar sua branch.

```Bash
git checkout main # Volte para a main
git pull origin main # Pegue as novidades (seu código mergeado)
```

### 2. Crie a branch da sua tarefa (Ex: Task CDD-586)

```Bash
git checkout -b ID-JIRA-tipo/nome-da-tarefa
git checkout -b CDD-5-chore/setup-ambiente
```

### 3. Salvar o Código (Commit)

O padrão de mensagem é: CDD-ID tipo(escopo): descrição.

```Bash
cd .. # Volta a raiz do projeto, se necessário
git status # Mostra os arquivos modificados
git add . # Adicione os arquivos modificados
git commit -m "CDD-5 chore(setup): configura ambiente e ci/cd" # Faça o commit seguindo o padrão
```

### 4. Enviar para o Repositório Remoto (Github)

Na primeira vez que subir a branch, você precisa ligar ela ao remoto (-u).

```Bash
git push -u origin CDD-5-chore/setup-ambiente
```

Próximas Vezes (Só atualizar): Como o vínculo já existe, basta rodar:

```Bash
git push
```

## 2.🛡️ Auto Code Review

*Confirme os itens abaixo no seu código antes de solicitar a revisão de outro desenvolvedor.*

- [ ] 🏗️ **Design & Padrões:** O código respeita princípios de design (ex: SRP - Ver `SOLID.md`) e possui nomes descritivos para variáveis e métodos (Ver `CLEAN_CODE.md`).
- [ ] 📖 **Docs & Tipagem:** Funções, classes e métodos possuem documentação clara no padrão do projeto e os tipos de dados (entrada/saída) estão definidos, se a linguagem suportar.
- [ ] 🧹 **Limpeza:** O código está livre de logs de debug esquecidos no console (ex: `print`, `console.log`), trechos de código comentados (código morto) e imports não utilizados.
- [ ] 🔒 **Segurança:** Garanti que **NENHUMA** credencial, senha, chave de API ou dado sensível foi commitado no repositório.
- [ ] ✅ **Qualidade:** A suíte de testes passa localmente com a cobertura mínima exigida e o Quality Gate (ex: SonarCloud) está verde.

## 3. Padrão de Merge (Squash & Merge)

*Ao finalizar um PR no GitHub, utilize a opção **"Squash and Merge"** e edite a mensagem final seguindo este padrão.*

### 1.🔀 Estrutura do Título

`[CDD-XXX] tipo(escopo): descrição curta e imperativa`

**Tipos Permitidos:**

- `chore`: Configuração, infra, CI/CD (não altera código de produção).
- `docs`: Alteração apenas em documentação.
- `feat`: Nova funcionalidade.
- `test`: Criação ou correção de testes.
- `refactor`: Melhoria de código sem alterar comportamento.
- `fix`: Correção de bug.

**Exemplos de Título:**

- `[CDD-5] feat(auth): implementa login com google`
- `[CDD-254] chore(setup): configura pipeline de ci e sonarcloud`
- `[CDD-16] fix(pandas): corrige erro de tipagem na coluna data`
- `[CDD-765] docs(readme): adiciona badges de status e cobertura`

### 2.📄 Estrutura do Corpo da Mensagem

*Liste as alterações técnicas em tópicos e vincule a tarefa do Jira no final.*

```text
Implementa a estrutura inicial do projeto e configurações de qualidade.

Alterações realizadas:
* Configura ambiente virtual e dependências (requirements.txt).
* Adiciona pipeline do GitHub Actions para testes e SonarCloud.
* Cria módulo `src/setup_inicial` com exemplos de Clean Code.
* Documenta padrões de projeto no README e docs/.

Relacionado a: [ID-JIRA]
```

## 4.♻️ Limpeza (Pós-Merge no GitHub)

Depois que seu PR for aprovado e mergeado na `main`, a branch remota será **apagada automaticamente** pelo GitHub.

No GitHub Web:

```text
Settings > General > Pull Requests > Marcar ✅ Automatically delete head branches.
```

Para manter a sua máquina local limpa e pronta para a próxima tarefa, rode os seguintes comandos:

```bash
git checkout main # Volte para a main
git pull origin main # Puxa o código atualizado (incluindo seu merge)
git branch # Exibe as branch existentes, a main deve ter um *
git branch -d ID-JIRA-tipo/nome-da-tarefa # Apague a branch local
git checkout -b ID-JIRA-tipo/nome-da-nova-tarefa # Cria a nova branch de trabalho
```
