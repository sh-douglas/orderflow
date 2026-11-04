# PostgreSQL — Ambiente de Desenvolvimento

Este documento descreve como configurar e executar o banco de dados PostgreSQL do **OrderFlow** utilizando Docker Compose.

## 1. Pré-requisitos

Antes de iniciar, certifique-se de possuir as seguintes ferramentas instaladas:

- Docker Engine
- Docker Compose V2

Verifique as instalações executando:

```bash
docker --version
docker compose version
```

## 2. Configuração do ambiente

Na raiz do projeto, crie um arquivo `.env` a partir do `.env.example`:

```bash
cp .env.example .env
```

Configure as seguintes variáveis:

| Variável            | Descrição                           |
| ------------------- | ----------------------------------- |
| `POSTGRES_USER`     | Usuário do PostgreSQL               |
| `POSTGRES_PASSWORD` | Senha de acesso ao banco            |
| `POSTGRES_DB`       | Nome do banco de dados              |
| `POSTGRES_PORT`     | Porta utilizada no computador local |

Exemplo de configuração:

```dotenv
POSTGRES_USER=orderflow
POSTGRES_PASSWORD=change_me
POSTGRES_DB=orderflow
POSTGRES_PORT=5434
```

**Importante:** o arquivo `.env` contém credenciais e não deve ser versionado. Utilize uma senha própria no ambiente local.

## 3. Inicialização do PostgreSQL

Na raiz do projeto, execute:

```bash
docker compose up -d
```

O Docker realizará o download da imagem, caso necessário, criará o volume persistente e iniciará o container.

Para verificar o estado do serviço:

```bash
docker compose ps
```

O container deverá apresentar o estado `healthy` após a inicialização.

## 4. Conexão com o banco de dados

Para conectar utilizando ferramentas como DBeaver, utilize os dados definidos no `.env`.

| Propriedade | Valor                        |
| ----------- | ---------------------------- |
| Host        | `localhost`                  |
| Porta       | `5434` (ou `POSTGRES_PORT`)  |
| Database    | Valor de `POSTGRES_DB`       |
| Username    | Valor de `POSTGRES_USER`     |
| Password    | Valor de `POSTGRES_PASSWORD` |

Quando a API estiver executando diretamente no computador, deverá utilizar `localhost` e a porta configurada.

Quando a API estiver em outro container na mesma rede do Docker Compose, deverá utilizar:

- Host: `database`
- Porta: `5432`

## 5. Comandos úteis

### Verificar os containers

```bash
docker compose ps
```

### Visualizar os logs

```bash
docker compose logs -f database
```

### Reiniciar o PostgreSQL

```bash
docker compose restart database
```

### Parar os containers

```bash
docker compose down
```

O volume persistente será preservado.

### Remover containers e volumes

```bash
docker compose down -v
```

**Atenção:** este comando remove os volumes declarados pelo projeto, incluindo os dados persistidos do PostgreSQL.

## 6. Persistência dos dados

O OrderFlow utiliza um volume Docker nomeado:

`orderflow_postgres_data`

Esse volume mantém os dados do PostgreSQL mesmo após a remoção ou recriação do container.

A persistência é mantida enquanto o volume não for excluído.

## 7. Verificação de integridade

O serviço possui um `healthcheck` baseado no utilitário `pg_isready`.

Ele verifica periodicamente se o PostgreSQL está aceitando conexões.

Para consultar o estado do container:

```bash
docker inspect --format='{{.State.Health.Status}}' orderflow_db
```

O resultado esperado é:

```text
healthy
```

Esse estado indica que o servidor está aceitando conexões, mas não substitui um teste de autenticação da aplicação.

---

**Observação:** o PostgreSQL é executado de forma independente da API, permitindo que o desenvolvimento do backend seja realizado localmente sem a necessidade de containerizar a aplicação.
