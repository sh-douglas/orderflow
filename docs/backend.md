# OrderFlow API

Backend da plataforma **OrderFlow**, desenvolvido em Python com FastAPI, seguindo uma abordagem assíncrona.

Este documento apresenta a estrutura da aplicação, as tecnologias utilizadas e os procedimentos para configuração, execução e testes do ambiente de desenvolvimento.

## Tecnologias

| Tecnologia     | Finalidade                                       |
| -------------- | ------------------------------------------------ |
| Python 3.13+   | Linguagem principal                              |
| FastAPI        | Framework para desenvolvimento da API            |
| Poetry         | Gerenciamento de dependências e ambiente virtual |
| Ruff           | Análise estática e formatação do código          |
| Taskipy        | Automação de tarefas de desenvolvimento          |
| Pytest         | Framework de testes automatizados                |
| pytest-asyncio | Suporte à execução de testes assíncronos         |
| HTTPX          | Cliente HTTP para testes da aplicação            |
| pytest-cov     | Análise de cobertura de código                   |
| PostgreSQL | Banco de dados relacional |
| SQLAlchemy Async | ORM e gerenciamento de conexões e sessões assíncronas |
| asyncpg | Driver assíncrono para PostgreSQL |
| Alembic | Gerenciamento e versionamento de migrations |
| Pydantic Settings | Gerenciamento das configurações da aplicação |
## Estrutura do backend

```text
apps/api/
├── alembic/
│   ├── versions/
│   └── env.py
├── app/
│   ├── __init__.py
│   ├── core/
│   │   └── config.py
│   ├── db/
│   │   ├── base.py
│   │   └── database.py
│   └── main.py
├── tests/
│   ├── conftest.py
│   ├── test_database_connection.py
│   ├── test_database_session.py
│   └── test_health.py
├── alembic.ini
├── pyproject.toml
└── poetry.lockml
└── poetry.lock
```

**Responsabilidades:**

- `app/`: contém o código-fonte da aplicação.
- `app/main.py`: ponto de entrada do FastAPI.
- `tests/`: contém os testes automatizados.
- `tests/conftest.py`: centraliza as fixtures compartilhadas.
- `pyproject.toml`: define dependências e configurações das ferramentas.
- `poetry.lock`: registra as versões resolvidas das dependências.
- `app/core/config.py`: centraliza as configurações da aplicação.
- `app/db/base.py`: define a base declarativa dos modelos ORM.
- `app/db/database.py`: configura a engine e as sessões assíncronas do SQLAlchemy.
- `alembic/`: contém a configuração e o histórico de migrations do banco de dados.
- `alembic.ini`: arquivo de configuração do Alembic.

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

| Recurso        | Endereço                           |
| -------------- | ---------------------------------- |
| API            | http://127.0.0.1:8000              |
| Swagger UI     | http://127.0.0.1:8000/docs         |
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

## Persistência de dados

O backend utiliza PostgreSQL com SQLAlchemy Async e o driver `asyncpg` para comunicação assíncrona com o banco de dados.

As configurações de conexão são centralizadas em `app/core/config.py`, utilizando Pydantic Settings.

O módulo `app/db/database.py` disponibiliza a engine assíncrona, a fábrica de sessões `AsyncSessionLocal` e a dependência `get_db`.

A base declarativa dos futuros modelos ORM é definida em `app/db/base.py`.

### Migrations com Alembic

O Alembic é responsável pelo versionamento das alterações na estrutura do banco de dados.

A configuração utiliza SQLAlchemy Async e possui uma migration inicial, que estabelece o histórico de revisões do projeto.

Para aplicar as migrations:

```bash
poetry run alembic upgrade head
```

Para verificar a revisão atual:

```bash
poetry run alembic current
```

Para consultar o histórico:

```bash
poetry run alembic history
```

As futuras migrations serão adicionadas conforme a implementação dos modelos ORM.

## Comandos de desenvolvimento

Os comandos de desenvolvimento são centralizados pelo Taskipy e configurados no `pyproject.toml`.

| Comando                  | Descrição                                        |
| ------------------------ | ------------------------------------------------ |
| `poetry run task run`    | Inicia a API sem recarregamento automático       |
| `poetry run task lint`   | Verifica problemas de lint e formatação          |
| `poetry run task format` | Aplica correções automáticas e formatação        |
| `poetry run task test`   | Executa os testes e gera relatórios de cobertura |

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

### Testes de integração

O backend possui testes de integração para validar a conexão com PostgreSQL e o funcionamento das sessões assíncronas do SQLAlchemy.

Os testes são identificados pelo marcador `integration` do Pytest.

Para executar somente os testes de integração:

```bash
poetry run pytest -m integration -v
```

Os testes utilizam um banco PostgreSQL separado do banco de desenvolvimento, configurado por meio das variáveis de ambiente.

O arquivo `tests/conftest.py` também contém uma fixture para liberar as conexões da engine entre os testes, evitando problemas de reutilização de conexões entre diferentes event loops.

A limpeza transacional automática dos dados ainda não foi implementada.

### Executar testes

```bash
poetry run task test
```

O Taskipy executa automaticamente a tarefa `pre_test` antes dos testes, realizando as verificações de qualidade configuradas.

### Cobertura de código

O projeto utiliza **pytest-cov** para medir quais instruções da aplicação foram executadas durante os testes.

A execução gera dois formatos de relatório:

| Relatório                 | Descrição                                                   |
| ------------------------- | ----------------------------------------------------------- |
| Terminal (`term-missing`) | Exibe a porcentagem de cobertura e as linhas não executadas |
| HTML (`html`)             | Permite visualizar a cobertura detalhada por arquivo        |

O relatório HTML é gerado em:

```text
apps/api/htmlcov/index.html
```

Para consultar o relatório, abra o arquivo `index.html` no navegador.

Os relatórios são atualizados a cada execução que conclui a geração da cobertura e não devem ser versionados no Git.

> **Nota:** 100% de cobertura não garante ausência de erros nem que todos os comportamentos da aplicação tenham sido testados. A cobertura é uma métrica complementar à qualidade dos testes.

## Estado da implementação

O backend encontra-se em fase inicial de desenvolvimento, com a estrutura FastAPI, endpoint de verificação de saúde, ferramentas de qualidade de código, testes automatizados e infraestrutura inicial de persistência com PostgreSQL, SQLAlchemy Async e Alembic.

A configuração assíncrona do banco de dados, a migration inicial e os testes de integração estão implementados. Os modelos de negócio e as integrações externas serão incorporados conforme a evolução da plataforma.
