# OrderFlow

O **OrderFlow** é um sistema de gerenciamento de pedidos desenvolvido para pequenos e médios estabelecimentos do setor alimentício, como hamburguerias, pizzarias, lanchonetes e restaurantes.

O projeto tem como objetivo digitalizar e organizar o fluxo de pedidos, reduzindo erros operacionais e facilitando o acompanhamento das solicitações, desde o registro até a finalização.

O sistema está sendo desenvolvido com foco em simplicidade, organização e facilidade de utilização, permitindo que cada estabelecimento tenha sua própria instalação independente.

## Tecnologias

### Backend

- **Python 3.13** — Linguagem de programação.
- **FastAPI** — Framework para desenvolvimento da API REST.
- **SQLAlchemy** — ORM e gerenciamento de conexões com o banco de dados.
- **asyncpg** — Driver assíncrono para PostgreSQL.
- **Pydantic Settings** — Gerenciamento das configurações da aplicação.
- **Poetry** — Gerenciamento de dependências e ambiente virtual.
- **Ruff** — Análise estática e formatação de código.
- **Pytest** — Testes automatizados.
- **Taskipy** — Automação de tarefas de desenvolvimento.

### Frontend (planejado)

- **React** — Biblioteca para construção da interface.
- **TypeScript** — Linguagem utilizada no desenvolvimento do frontend.

### Banco de dados

- **PostgreSQL 16** — Banco de dados relacional.

### Infraestrutura

- **Docker** — Containerização da API e do banco de dados.
- **Docker Compose** — Orquestração dos serviços no ambiente de desenvolvimento.
- **GitHub Actions** — Integração contínua para verificações de lint e testes automatizados.

## Estrutura do projeto

O OrderFlow utiliza uma estrutura de monorepositório, centralizando aplicações, infraestrutura e documentação.

```text
orderflow/
├── .github/
│   ├── ISSUE_TEMPLATE/    # Templates de Issues
│   ├── workflows/         # Workflows de CI
│   └── pull_request_template.md
├── apps/
│   └── api/               # Backend FastAPI
│       ├── app/           # Código-fonte da aplicação
│       ├── tests/         # Testes automatizados
│       ├── Dockerfile     # Build multi-stage da API
│       └── pyproject.toml # Dependências e ferramentas
├── docs/                  # Documentação técnica
├── .env.example           # Exemplo de variáveis de ambiente
├── compose.yml            # Serviços da API e PostgreSQL
├── CONTRIBUTING.md        # Diretrizes de contribuição
└── README.md
```

A estrutura será expandida conforme o desenvolvimento das aplicações e dos serviços de infraestrutura.

## Executando com Docker Compose

O ambiente de desenvolvimento utiliza Docker Compose para executar a API FastAPI e o PostgreSQL em contêineres separados.

### Pré-requisitos

- Docker Engine instalado.
- Docker Compose V2 disponível.

### Configuração do ambiente

Na raiz do repositório, crie o arquivo `.env` a partir do exemplo:

```bash
cp .env.example .env
```

Preencha as variáveis de ambiente necessárias:

| Variável            | Descrição                               |
| ------------------- | --------------------------------------- |
| `POSTGRES_USER`     | Usuário do PostgreSQL                   |
| `POSTGRES_PASSWORD` | Senha de acesso ao banco                |
| `POSTGRES_DB`       | Nome do banco de dados                  |
| `POSTGRES_PORT`     | Porta publicada no computador local     |
| `POSTGRES_HOST`     | Host utilizado na execução local da API |

Para execução local da API fora do Docker, utilize `POSTGRES_HOST=localhost` e a porta publicada em `POSTGRES_PORT`.

Dentro do Docker Compose, a API utiliza automaticamente o serviço `database` na porta interna `5432`, independentemente dos valores de host e porta definidos para acesso local.

**Importante:** o arquivo `.env` pode conter credenciais e não deve ser versionado.

### Inicialização dos serviços

Na raiz do repositório, execute:

```bash
docker compose up -d --build
```

O comando constrói a imagem da API e inicia os serviços em segundo plano.

O PostgreSQL possui um healthcheck, e o serviço da API aguarda o banco atingir o estado saudável antes de iniciar.

### Verificação dos serviços

Para consultar o estado dos contêineres:

```bash
docker compose ps
```

Os serviços esperados são:

| Serviço    | Contêiner       | Estado esperado        |
| ---------- | --------------- | ---------------------- |
| API        | `orderflow_api` | Em execução            |
| PostgreSQL | `orderflow_db`  | Em execução e saudável |

### Acessando a API

Com os serviços em execução:

| Recurso     | Endereço                           |
| ----------- | ---------------------------------- |
| API         | http://localhost:8000              |
| Healthcheck | http://localhost:8000/health       |
| Swagger UI  | http://localhost:8000/docs         |
| OpenAPI     | http://localhost:8000/openapi.json |

Para verificar a disponibilidade básica da API:

```bash
curl -i http://localhost:8000/health
```

Resposta esperada:

```json
{
  "status": "ok"
}
```

O endpoint `/health` verifica a disponibilidade HTTP da aplicação, mas não realiza uma consulta ao banco de dados.

### Logs e encerramento

Para acompanhar os logs dos serviços:

```bash
docker compose logs -f
```

Para encerrar os contêineres:

```bash
docker compose down
```

O comando preserva os volumes persistentes do PostgreSQL.

**Atenção:** `docker compose down -v` também remove os volumes declarados pelo projeto, podendo apagar permanentemente os dados armazenados no banco.

## Desenvolvimento local da API

O backend também pode ser executado diretamente no computador, utilizando Python e Poetry.

A partir da raiz do repositório:

```bash
cd apps/api
poetry install --no-root
```

Para iniciar a aplicação:

```bash
poetry run task run
```

Para executar as verificações de qualidade:

```bash
poetry run task lint
```

Para executar os testes automatizados:

```bash
poetry run task test
```

Os testes marcados como `integration`, que dependem de um banco de dados em execução, não fazem parte da execução padrão do Pytest.

As instruções detalhadas estão disponíveis em [Backend — FastAPI](docs/backend.md).

## Integração contínua

O projeto utiliza GitHub Actions para executar verificações automatizadas da API.

O workflow `API CI` executa:

1. Configuração do ambiente Python 3.13.
2. Instalação das dependências utilizando Poetry.
3. Verificação de lint e formatação com Ruff.
4. Execução dos testes automatizados com Pytest.

As verificações são executadas em Pull Requests direcionados à branch `main` e em pushes para `main` que alterem arquivos da API ou do próprio workflow.

O job **Lint and Tests** é uma verificação obrigatória para integração na branch principal.

A construção da imagem Docker ainda não faz parte desse workflow e poderá ser automatizada posteriormente.

## Documentação

| Documento                                                    | Descrição                                                                          |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------- |
| [PostgreSQL — Ambiente de Desenvolvimento](docs/database.md) | Configuração, execução e gerenciamento do PostgreSQL.                              |
| [PostgreSQL — Backup e Restauração](docs/backup.md)          | Procedimentos de backup, verificação e restauração do banco de dados.              |
| [Backend — FastAPI](docs/backend.md)                         | Estrutura da API, ambiente de desenvolvimento, ferramentas e testes automatizados. |
| [Guia de Contribuição](CONTRIBUTING.md)                      | Convenções de branches, commits, Issues, Pull Requests e colaboração.              |

## Status do projeto

**Em desenvolvimento.**

O OrderFlow encontra-se na fase de construção da infraestrutura e da base técnica necessária para implementação dos módulos de negócio.

| Componente             | Estado atual                                                                                |
| ---------------------- | ------------------------------------------------------------------------------------------- |
| PostgreSQL             | Configurado com Docker Compose, volume persistente e healthcheck.                           |
| Backup e restauração   | Procedimentos manuais documentados e validados.                                             |
| Backend FastAPI        | Estrutura inicial, endpoint `/health` e testes automatizados.                               |
| Integração com banco   | Configuração assíncrona com SQLAlchemy e asyncpg; conectividade validada no Docker Compose. |
| Containerização da API | Dockerfile multi-stage com dependências de produção e execução sem root.                    |
| Docker Compose         | Inicialização conjunta da API e PostgreSQL implementada na etapa atual.                     |
| GitHub Actions         | CI configurada com lint e testes obrigatórios.                                              |
| Frontend React         | Planejado.                                                                                  |
| Documentação           | Guias técnicos e diretrizes de contribuição disponíveis.                                    |

### Próximas etapas

- Implementação dos modelos e módulos de negócio.
- Configuração e gerenciamento de migrações do banco de dados.
- Ampliação dos testes automatizados e de integração.
- Desenvolvimento do frontend React com TypeScript.
- Evolução da CI, incluindo validação do build Docker.
- Preparação dos ambientes de implantação.

O desenvolvimento seguirá de forma incremental, priorizando organização, qualidade de código e facilidade de manutenção.
