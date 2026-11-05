# Overflow API

Backend da plataforma **Overflow**, desenvolvido em Python com FastAPI, seguindo uma abordagem assíncrona.

Este documento apresenta a estrutura da aplicação, as tecnologias utilizadas e os procedimentos para configuração, execução e testes do ambiente de desenvolvimento.

## Tecnologias

| Tecnologia | Finalidade |
|---|---|
| Python 3.13+ | Linguagem principal |
| FastAPI | Framework para desenvolvimento da API |
| Poetry | Gerenciamento de dependências e ambiente virtual |
| Ruff | Análise estática e formatação do código |
| Taskipy | Automação de tarefas de desenvolvimento |
| Pytest | Framework de testes automatizados |
| pytest-asyncio | Suporte à execução de testes assíncronos |
| HTTPX | Cliente HTTP para testes da aplicação |
| pytest-cov | Análise de cobertura de código |

## Estrutura do backend

```text
apps/api/
├── app/
│   ├── __init__.py
│   └── main.py
├── tests/
│   ├── conftest.py
│   └── test_health.py
├── pyproject.toml
└── poetry.lock
```

**Responsabilidades:**

- `app/`: contém o código-fonte da aplicação.
- `app/main.py`: ponto de entrada do FastAPI.
- `tests/`: contém os testes automatizados.
- `tests/conftest.py`: centraliza as fixtures compartilhadas.
- `pyproject.toml`: define dependências e configurações das ferramentas.
- `poetry.lock`: registra as versões resolvidas das dependências.

A estrutura será expandida conforme novos módulos e funcionalidades forem implementados.

## Ambiente de desenvolvimento

### Pré-requisitos

- Python compatível com a versão declarada no `pyproject.toml`.
- Poetry instalado.

### Instalação

A partir da raiz do monorepo:

```bash
cd apps/api
poetry install
```

O Poetry instalará as dependências declaradas no projeto, incluindo as ferramentas do grupo de desenvolvimento.

### Executar a aplicação

O Taskipy centraliza os comandos de execução definidos no `pyproject.toml`.

Para iniciar a aplicação:

```bash
poetry run task run
```

O comando executa a tarefa `run`, configurada para iniciar o FastAPI sem recarregamento automático.

Para executar diretamente em modo de desenvolvimento, com recarregamento automático:

```bash
poetry run fastapi dev app/main.py
```

Após iniciar o servidor, os seguintes endereços estarão disponíveis:

| Recurso | Endereço |
|---|---|
| API | http://127.0.0.1:8000 |
| Swagger UI | http://127.0.0.1:8000/docs |
| OpenAPI Schema | http://127.0.0.1:8000/openapi.json |

## Endpoints

### GET /health

Verifica a disponibilidade básica da aplicação.

**Resposta esperada — HTTP 200**

```json
{
  "status": "ok"
}
```

Esse endpoint confirma que a aplicação está respondendo às requisições HTTP.

Ele não verifica conexões com banco de dados ou a disponibilidade de serviços externos.

## Comandos de desenvolvimento

Os comandos de desenvolvimento são centralizados pelo Taskipy e configurados no `pyproject.toml`.

| Comando | Descrição |
|---|---|
| `poetry run task run` | Inicia a API sem recarregamento automático |
| `poetry run task lint` | Verifica problemas de lint e formatação |
| `poetry run task format` | Aplica correções automáticas e formatação |
| `poetry run task test` | Executa os testes e gera relatórios de cobertura |

### Qualidade de código

O Ruff é utilizado para análise estática e padronização do código.

Para verificar possíveis problemas sem modificar arquivos:

```bash
poetry run task lint
```

Para aplicar correções automáticas e formatar o código:

```bash
poetry run task format
```

As regras de lint e formatação podem ser configuradas no `pyproject.toml`.

## Testes automatizados

O backend utiliza Pytest com suporte a testes assíncronos por meio do pytest-asyncio.

O HTTPX permite realizar requisições diretamente à aplicação FastAPI utilizando `AsyncClient` e `ASGITransport`, sem necessidade de iniciar um servidor HTTP externo.

As fixtures compartilhadas são definidas em `tests/conftest.py`, permitindo reutilizar recursos entre os testes.

### Executar testes

```bash
poetry run task test
```

O Taskipy executa automaticamente a tarefa `pre_test` antes dos testes, realizando as verificações de qualidade configuradas.

### Cobertura de código

O projeto utiliza **pytest-cov** para medir quais instruções da aplicação foram executadas durante os testes.

A execução gera dois formatos de relatório:

| Relatório | Descrição |
|---|---|
| Terminal (`term-missing`) | Exibe a porcentagem de cobertura e as linhas não executadas |
| HTML (`html`) | Permite visualizar a cobertura detalhada por arquivo |

O relatório HTML é gerado em:

```text
apps/api/htmlcov/index.html
```

Para consultar o relatório, abra o arquivo `index.html` no navegador.

Os relatórios são atualizados a cada execução que conclui a geração da cobertura e não devem ser versionados no Git.

> **Nota:** 100% de cobertura não garante ausência de erros nem que todos os comportamentos da aplicação tenham sido testados. A cobertura é uma métrica complementar à qualidade dos testes.

## Estado da implementação

O backend encontra-se em fase inicial de desenvolvimento, com a estrutura FastAPI, um endpoint de verificação de saúde, ferramentas de qualidade de código e testes automatizados assíncronos.

A persistência de dados, os módulos de negócio e as integrações externas serão incorporados conforme a evolução da plataforma.