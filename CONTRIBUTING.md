# Guia de Contribuição — OrderFlow

Este documento estabelece as convenções e boas práticas para contribuir com o desenvolvimento do **OrderFlow**, um sistema de gerenciamento de pedidos para estabelecimentos alimentícios.

O objetivo é manter um fluxo de desenvolvimento organizado, colaborativo e rastreável, garantindo consistência entre as alterações realizadas pelos integrantes da equipe.

## 1. Organização do projeto

O OrderFlow utiliza um fluxo de desenvolvimento baseado em **Git, GitHub, Issues e Pull Requests**.

As principais tecnologias do projeto são:

- **Backend:** Python e FastAPI.
- **Frontend:** React e TypeScript.
- **Banco de dados:** PostgreSQL.
- **Infraestrutura:** Docker e Docker Compose.
- **Integração contínua:** GitHub Actions (planejado).

Cada integrante deve trabalhar em branches específicas, evitando alterações diretas na branch principal.

A branch `main` representa a versão integrada do projeto.

## 2. Convenções de branches

Toda nova branch deve ser criada a partir da `main` atualizada.

Utilize nomes curtos, descritivos e em inglês, seguindo o padrão:

`tipo/descricao-da-alteracao`

| Prefixo     | Finalidade                                 | Exemplo                      |
| ----------- | ------------------------------------------ | ---------------------------- |
| `feat/`     | Desenvolvimento de funcionalidades         | `feat/order-creation`        |
| `fix/`      | Correção de bugs                           | `fix/order-validation`       |
| `infra/`    | Alterações de infraestrutura               | `infra/postgres-healthcheck` |
| `docs/`     | Documentação                               | `docs/contributing-guide`    |
| `chore/`    | Manutenção e configuração                  | `chore/github-templates`     |
| `refactor/` | Refatoração sem alteração de comportamento | `refactor/order-service`     |
| `test/`     | Criação ou manutenção de testes            | `test/order-validation`      |

### Criando uma branch

Atualize a branch principal:

```bash
git switch main
git pull origin main
```

Crie uma branch para sua tarefa:

```bash
git switch -c feat/order-creation
```

Evite desenvolver diretamente na `main` ou reutilizar branches de tarefas já concluídas.

## 3. Convenções de commits

O projeto adota o padrão **Conventional Commits** para manter um histórico organizado.

Formato:

`tipo: descrição da alteração`

### Tipos utilizados

| Tipo       | Finalidade                                      |
| ---------- | ----------------------------------------------- |
| `feat`     | Nova funcionalidade                             |
| `fix`      | Correção de erro                                |
| `docs`     | Documentação                                    |
| `chore`    | Manutenção e configuração                       |
| `refactor` | Refatoração                                     |
| `test`     | Testes                                          |
| `build`    | Alterações no processo de build ou dependências |
| `ci`       | Integração contínua                             |
| `perf`     | Melhorias de desempenho                         |

### Exemplos

```text
feat: add order creation endpoint
fix: correct order status validation
infra: improve PostgreSQL Compose configuration
docs: add PostgreSQL backup and restore guide
chore: add GitHub issue templates
ci: add backend test workflow
```

**Observação:** `infra` é uma convenção adicional adotada pelo projeto para identificar alterações de infraestrutura.

### Boas práticas

- Utilize mensagens objetivas e descritivas.
- Prefira um commit por alteração lógica.
- Evite mensagens genéricas como `update`, `changes` ou `fix stuff`.
- Não inclua arquivos temporários, credenciais ou alterações não relacionadas à tarefa.

## 4. Gerenciamento de Issues

As Issues devem ser utilizadas para registrar problemas, propostas de funcionalidades e melhorias.

O repositório disponibiliza dois templates:

### Bug Report

Utilize quando identificar um erro ou comportamento inesperado.

O registro deve conter:

- Descrição do problema.
- Passos para reprodução.
- Comportamento esperado e comportamento atual.
- Informações do ambiente.
- Logs e evidências relevantes.

### Feature Request

Utilize para propor uma funcionalidade ou melhoria.

O registro deve conter:

- Descrição da proposta.
- Problema que será resolvido.
- Solução sugerida.
- Critérios de aceitação verificáveis.
- Impactos e dependências.

Antes de criar uma Issue, verifique se já existe outra relatando o mesmo problema ou propondo a mesma funcionalidade.

Sempre que possível, relacione o Pull Request à Issue correspondente.

## 5. Fluxo de Pull Requests

Todas as alterações destinadas à branch `main` devem passar por um Pull Request.

### 5.1. Desenvolvimento

1. Atualize a branch `main`.
2. Crie uma branch específica para a tarefa.
3. Implemente as alterações necessárias.
4. Execute as verificações disponíveis.
5. Revise o diff antes de realizar o commit.
6. Faça o commit e envie a branch ao GitHub.

Exemplo:

```bash
git add .
git commit -m "feat: add order creation endpoint"
git push -u origin feat/order-creation
```

### 5.2. Abertura do Pull Request

Ao abrir um PR:

- Utilize um título objetivo.
- Preencha o template disponibilizado pelo repositório.
- Explique o problema e as alterações realizadas.
- Registre os testes e verificações executados.
- Informe possíveis impactos e dependências.
- Relacione a Issue correspondente, quando houver.
- Solicite a revisão do outro integrante.

O template de PR contém as seguintes seções:

- O que muda e por quê?
- Como foi validado?
- Impactos e implantação.
- Checklist.

### 5.3. Revisão

O responsável pela revisão deverá verificar:

- Se as alterações atendem ao objetivo da tarefa.
- Se existem problemas de implementação ou configuração.
- Se os testes e verificações são suficientes.
- Se foram introduzidos riscos de segurança.
- Se a documentação foi atualizada quando necessário.

Caso sejam identificados problemas, o autor deverá realizar as correções na mesma branch.

Novos commits enviados para essa branch atualizarão automaticamente o PR existente.

### 5.4. Merge

O merge deverá ocorrer após:

- Conclusão da revisão por outro integrante.
- Resolução dos comentários e problemas identificados.
- Execução bem-sucedida das verificações aplicáveis.
- Confirmação de que não existem alterações não relacionadas.

Após o merge:

1. Atualize sua branch `main` local.
2. Exclua a branch de trabalho local.
3. Exclua a branch remota, quando não for mais necessária.

## 6. Boas práticas de desenvolvimento

### Alterações pequenas

Prefira Pull Requests com escopo bem definido.

Evite misturar funcionalidades, refatorações e alterações de infraestrutura sem necessidade.

### Validação local

Antes de abrir um PR:

- Execute os testes disponíveis e relevantes.
- Verifique erros de lint e formatação, quando as ferramentas estiverem configuradas.
- Confirme que as alterações não comprometem funcionalidades existentes.
- Documente limitações ou verificações que não puderam ser realizadas.

### Segurança

Nunca versione:

- Arquivos `.env` contendo credenciais reais.
- Senhas, tokens ou chaves privadas.
- Backups de bancos de dados.
- Dados pessoais reais.
- Arquivos com informações sensíveis de clientes.

Utilize arquivos `.env.example` para documentar as variáveis necessárias, sem incluir valores secretos.

### Documentação

Atualize a documentação sempre que uma alteração modificar:

- Procedimentos de instalação ou configuração.
- Variáveis de ambiente.
- Comandos de desenvolvimento.
- Requisitos ou dependências.
- Procedimentos operacionais.

### Comunicação

Mantenha as discussões técnicas relacionadas às tarefas registradas nas Issues ou nos Pull Requests sempre que possível.

Decisões que afetem a arquitetura, a infraestrutura ou o funcionamento do sistema devem ser comunicadas aos integrantes envolvidos.

---

## Considerações finais

O fluxo de contribuição do OrderFlow foi definido para uma equipe pequena, priorizando clareza, colaboração e qualidade.

As convenções poderão evoluir conforme o projeto crescer e novas necessidades surgirem.

O objetivo não é aumentar a burocracia, mas garantir que cada alteração seja compreensível, verificável e rastreável.
