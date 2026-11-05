# OrderFlow

O **OrderFlow** é um sistema de gerenciamento de pedidos desenvolvido para pequenos e médios estabelecimentos do setor alimentício, como hamburguerias, pizzarias, lanchonetes e restaurantes.

O projeto tem como objetivo digitalizar e organizar o fluxo de pedidos, reduzindo erros operacionais e facilitando o acompanhamento das solicitações, desde o registro até a finalização.

O sistema está sendo desenvolvido com foco em simplicidade, organização e facilidade de utilização, permitindo que cada estabelecimento tenha sua própria instalação independente.

## Tecnologias

### Backend

- **Python** — Linguagem de programação.
- **FastAPI** — Framework para desenvolvimento da API REST.
- **Poetry** — Gerenciamento de dependências e ambiente virtual.
- **Ruff** — Análise estática e formatação de código.
- **Pytest** — Testes automatizados.
- **Taskipy** — Automação de tarefas de desenvolvimento.

### Frontend (planejado)

- **React** — Biblioteca para construção da interface.
- **TypeScript** — Linguagem utilizada no desenvolvimento do frontend.

### Banco de dados

- **PostgreSQL** — Banco de dados relacional.

### Infraestrutura

- **Docker** — Containerização dos serviços.
- **Docker Compose** — Gerenciamento dos containers no ambiente de desenvolvimento.
- **GitHub Actions** — Integração contínua e automação de verificações (planejado).

## Estrutura do projeto

O OrderFlow utiliza uma estrutura de monorepositório, centralizando aplicações, infraestrutura e documentação.

```text
orderflow/
├── .github/          # Templates de Issues e Pull Requests
├── apps/
│   └── api/          # Backend FastAPI
├── docs/             # Documentação técnica
├── .env.example      # Exemplo de variáveis de ambiente
├── compose.yml       # Ambiente PostgreSQL
├── CONTRIBUTING.md   # Diretrizes de contribuição
└── README.md
```

A estrutura será expandida conforme o desenvolvimento das aplicações e dos serviços de infraestrutura.

## Documentação

| Documento                                                    | Descrição                                                                              |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------- |
| [PostgreSQL — Ambiente de Desenvolvimento](docs/database.md) | Configuração, inicialização e gerenciamento do PostgreSQL com Docker Compose.          |
| [PostgreSQL — Backup e Restauração](docs/backup.md)          | Procedimentos para backup, verificação e restauração de bancos de dados PostgreSQL.    |
| [Backend — FastAPI](docs/backend.md)                         | Configuração, execução, ferramentas de desenvolvimento e testes automatizados da API.  |
| [Guia de Contribuição](CONTRIBUTING.md)                      | Convenções de branches, commits, Issues, Pull Requests e boas práticas de colaboração. |

## Status do projeto

**Em desenvolvimento.**

O OrderFlow encontra-se em fase inicial, com a infraestrutura do banco de dados configurada e o backend em desenvolvimento.

| Componente           | Estado atual                                                               |
| -------------------- | -------------------------------------------------------------------------- |
| PostgreSQL           | Configurado com Docker Compose, persistência de dados e healthcheck.       |
| Backup e restauração | Procedimentos manuais documentados e validados.                            |
| Backend FastAPI      | Estrutura inicial implementada, endpoint `/health` e testes automatizados. |
| Frontend React       | Planejado.                                                                 |
| GitHub Actions       | Planejado.                                                                 |
| Documentação         | Guias técnicos e diretrizes de contribuição disponíveis.                   |

### Próximas etapas

- Implementação dos módulos de negócio e integração do backend com PostgreSQL.
- Containerização da API FastAPI.
- Configuração de integração contínua com GitHub Actions.
- Desenvolvimento do frontend React.
- Preparação dos ambientes de implantação.

O desenvolvimento seguirá de forma incremental, priorizando organização, qualidade de código e facilidade de manutenção.
