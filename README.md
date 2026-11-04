# OrderFlow

O **OrderFlow** é um sistema de gerenciamento de pedidos desenvolvido para pequenos e médios estabelecimentos do setor alimentício, como hamburguerias, pizzarias, lanchonetes e restaurantes.

O projeto tem como objetivo digitalizar e organizar o fluxo de pedidos, reduzindo erros operacionais e facilitando o acompanhamento das solicitações, desde o registro até a finalização.

O sistema está sendo desenvolvido com foco em simplicidade, organização e facilidade de utilização, permitindo que cada estabelecimento tenha sua própria instalação independente.

## Tecnologias

O projeto utiliza as seguintes tecnologias:

### Backend

- **Python** — Linguagem de programação.
- **FastAPI** — Framework para desenvolvimento da API REST.

### Frontend

- **React** — Biblioteca para construção da interface.
- **TypeScript** — Linguagem utilizada no desenvolvimento do frontend.

### Banco de dados

- **PostgreSQL** — Banco de dados relacional.

### Infraestrutura

- **Docker** — Containerização dos serviços.
- **Docker Compose** — Orquestração dos containers no ambiente de desenvolvimento.
- **GitHub Actions** — Integração contínua e automação de verificações (planejado).

## Documentação

| Documento                                                    | Descrição                                                                                                |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| [PostgreSQL — Ambiente de Desenvolvimento](docs/database.md) | Instruções para configuração, inicialização e gerenciamento do banco de dados utilizando Docker Compose. |
| [PostgreSQL — Ambiente de Desenvolvimento](docs/backup.md)   | Instruções para realizar backups e restaurar bancos de dados PostgreSQL do **OrderFlow**.                |

## Status do projeto

**Em desenvolvimento.**

Atualmente, o projeto está em sua fase inicial, com a infraestrutura do banco de dados configurada e documentada. As aplicações backend e frontend serão desenvolvidas progressivamente.
