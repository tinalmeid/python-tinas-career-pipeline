# 🧹 Clean Code & Boas Práticas

> *"Código é lido muito mais vezes do que é escrito."*

Este guia define como manter o código legível e profissional.

## 1. Nomenclatura (Naming)

Nomes devem revelar intenção. Não tenha medo de nomes grandes se eles forem claros.

| Tipo | ❌ Ruim | ✅ Bom | Por |
| ------ | ------ | ------ | ------ |
| **Variáveis** | `x`, `d`, `aux`, `lista` | `dias_restantes`, `lista_usuarios` | `d` poderia ser dia ou distância. Seja explícito. |
| **Funções** | `processar()`, `fazer()` | `calcular_imposto_renda()`, `buscar_usuario_id()` | O verbo deve dizer exatamente o que a função faz. |
| **Booleanos** | `flag`, `status`  `is_ativo`, `tem_permissao`, `user_has_access` | Deve soar como uma pergunta de Sim/Não. | Deve soar como uma pergunta de Sim/Não. |

## 2. Limpeza Geral

Antes de comitar, faça a "faxina":

💀 **Dead Code:** Apague códigos comentados. Se precisar do histórico, o Git já guardou para você.

🖨️ **Prints:** Remova todos os print("TESTE") usados para debug. Use logs se for necessário.

🍝 **Importações:** Remova imports que não estão sendo usados (o topo do arquivo deve estar limpo).

## 3. Observabilidade e Logs

* Logs são a nossa principal ferramenta de métricas e diagnóstico em produção.

* Abandone o Print: Utilize sempre a biblioteca de log padrão do projeto (logging, ILogger, etc.).

* Logue Eventos, não Código: Não logue "entrou na função". Logue marcos de negócio (Ex: "Job de ETL iniciado com 50.000 linhas").

* Níveis de Log: Use INFO para o caminho feliz, WARN para falhas recuperáveis e ERROR para falhas críticas.

* Segurança: NUNCA logue credenciais, senhas, tokens de API ou dados sensíveis (PII).

## 4. Tipagem (Type Hinting)

Em linguagens dinâmicas (como Python ou JavaScript/TypeScript), o uso de tipagem explícita em projetos profissionais é obrigatório para evitar falhas em tempo de execução e melhorar o intellisense (autocompletar) da IDE.

❌ Ruim: def soma(a, b): (O que é a? Número? Texto?)

✅ Bom: def soma(a: int, b: int) -> int: (Fica o contrato claro: entra número e sai número).
