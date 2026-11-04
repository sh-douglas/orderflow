# PostgreSQL — Backup e Restauração

Este documento descreve os procedimentos para realizar backups e restaurar bancos de dados PostgreSQL do **OrderFlow**, utilizando Docker Compose e as ferramentas nativas `pg_dump` e `pg_restore`.

O objetivo é permitir a recuperação de dados e a reprodução do procedimento em diferentes ambientes de desenvolvimento.

> **Importante:** este guia é destinado ao ambiente de desenvolvimento. Ambientes de produção exigem políticas adicionais de segurança, armazenamento e retenção de backups.

## 1. Pré-requisitos

Antes de iniciar, certifique-se de que:

- Docker Engine e Docker Compose V2 estejam instalados.
- O PostgreSQL esteja configurado e em execução.
- O arquivo `.env` esteja configurado corretamente.
- O usuário PostgreSQL possua as permissões necessárias.

Para verificar o estado do serviço:

```bash
docker compose ps
```

O container `orderflow_db` deverá apresentar o estado `healthy`.

Para configurar o ambiente pela primeira vez, consulte a [documentação do PostgreSQL](database.md).

## 2. Diretório de backups

Na raiz do projeto, crie um diretório para armazenar os arquivos de backup:

```bash
mkdir -p backups
```

A estrutura esperada é:

```text
orderflow/
├── backups/
├── docs/
│   ├── backup.md
│   └── database.md
├── .env.example
├── .gitignore
├── compose.yml
└── README.md
```

Adicione o diretório ao `.gitignore`:

```gitignore
backups/
```

**Atenção:** arquivos de backup podem conter informações sensíveis e não devem ser versionados no Git.

## 3. Criando um backup

O PostgreSQL disponibiliza a ferramenta `pg_dump` para exportar a estrutura e os dados de um banco.

Neste exemplo, utilizaremos o banco `orderflow_backup_lab`, criado exclusivamente para testes.

Execute na raiz do projeto:

```bash
docker compose exec -T database pg_dump \
  -U root \
  -d orderflow_backup_lab \
  -Fc > backups/orderflow_backup_lab.dump
```

### Parâmetros utilizados

| Parâmetro             | Descrição                                               |
| --------------------- | ------------------------------------------------------- |
| `docker compose exec` | Executa um comando dentro do container                  |
| `-T`                  | Desabilita a alocação de terminal interativo            |
| `database`            | Nome do serviço PostgreSQL no Compose                   |
| `pg_dump`             | Ferramenta de exportação do PostgreSQL                  |
| `-U root`             | Usuário utilizado na conexão                            |
| `-d`                  | Banco de dados de origem                                |
| `-Fc`                 | Gera um backup no formato customizado                   |
| `>`                   | Redireciona a saída para um arquivo no computador local |

O formato customizado permite utilizar o `pg_restore` para restaurar objetos e dados do banco.

**Observação:** substitua `root` pelo usuário configurado no ambiente e `orderflow_backup_lab` pelo banco que deseja exportar.

## 4. Verificando o backup

Após executar o comando, verifique se o arquivo foi criado:

```bash
ls -lh backups/
```

Para inspecionar o conteúdo do arquivo:

```bash
docker compose exec -T database pg_restore -l \
  < backups/orderflow_backup_lab.dump
```

O comando deverá apresentar informações como:

- Versão do PostgreSQL utilizada.
- Formato do arquivo.
- Tabelas incluídas.
- Sequências.
- Restrições.
- Entradas de dados das tabelas.

A listagem confirma que o arquivo pode ser interpretado pelo `pg_restore`, mas não garante que todos os dados possam ser recuperados corretamente.

Para validar a recuperação, é necessário realizar uma restauração de teste.

## 5. Criando um banco para restauração

Para evitar alterações no banco original, a restauração será realizada em um banco separado.

Acesse o PostgreSQL:

```bash
docker compose exec database psql -U root -d postgres
```

Crie o banco de destino:

```sql
CREATE DATABASE orderflow_restored_lab;
```

Saia do terminal interativo:

```sql
\q
```

O banco de destino deverá estar vazio antes da restauração.

## 6. Restaurando o backup

Com o banco de destino criado, execute:

```bash
docker compose exec -T database pg_restore \
  -U root \
  -d orderflow_restored_lab \
  --no-owner \
  --exit-on-error \
  < backups/orderflow_backup_lab.dump
```

### Parâmetros utilizados

| Parâmetro         | Descrição                                           |
| ----------------- | --------------------------------------------------- |
| `pg_restore`      | Ferramenta de restauração                           |
| `-U root`         | Usuário utilizado na conexão                        |
| `-d`              | Banco de destino                                    |
| `--no-owner`      | Não restaura os proprietários originais dos objetos |
| `--exit-on-error` | Interrompe a restauração ao encontrar um erro       |
| `<`               | Envia o conteúdo do arquivo local para o comando    |

O processo deverá recriar os objetos e restaurar os dados presentes no backup.

Se o comando apresentar erros, investigue a causa antes de considerar a restauração concluída.

**Atenção:** não execute uma restauração sobre um banco que contenha dados importantes sem antes avaliar os possíveis conflitos e os riscos de sobrescrita ou duplicação.

## 7. Validando os dados restaurados

Após a restauração, conecte-se ao banco de destino:

```bash
docker compose exec database psql -U root -d orderflow_restored_lab
```

Consulte os registros:

```sql
SELECT * FROM backup_test;
```

No exercício realizado, o resultado esperado contém três registros:

| id  | description        |
| --- | ------------------ |
| 1   | First backup test  |
| 2   | Second backup test |
| 3   | Third backup test  |

Além das descrições, os identificadores e os valores de `created_at` devem corresponder aos registros originais.

A restauração será considerada validada quando os dados e objetos esperados estiverem presentes e consistentes.

## 8. Boas práticas

- Não versionar arquivos `.dump` ou credenciais.
- Armazenar backups importantes fora do servidor de origem.
- Restringir o acesso aos arquivos de backup.
- Utilizar criptografia quando houver dados sensíveis.
- Verificar o código de saída dos comandos de backup.
- Testar periodicamente a restauração.
- Definir políticas de retenção para evitar armazenamento desnecessário.
- Utilizar bancos isolados para testes de recuperação.

> Um backup só deve ser considerado confiável depois que sua restauração tiver sido testada com sucesso.

## 9. Limitações

O procedimento apresentado utiliza `pg_dump`, que realiza backups lógicos de um banco de dados.

Esse método não substitui estratégias de recuperação contínua, backups físicos ou mecanismos de recuperação para um ponto específico no tempo (PITR).

Além disso, `pg_dump` não exporta automaticamente todos os objetos globais do cluster PostgreSQL, como usuários e permissões globais.

Para ambientes de produção, a estratégia deverá ser definida considerando volume de dados, frequência de backup, retenção, segurança e requisitos de recuperação.

---

## Status da validação

O procedimento foi testado no ambiente local de desenvolvimento do OrderFlow utilizando PostgreSQL 16.

Foram realizadas as seguintes operações:

- [x] Criação de banco e tabela de testes.
- [x] Inserção de três registros.
- [x] Exportação utilizando `pg_dump -Fc`.
- [x] Inspeção utilizando `pg_restore -l`.
- [x] Criação de um banco separado para recuperação.
- [x] Restauração utilizando `pg_restore`.
- [x] Verificação dos três registros restaurados.

**Resultado:** backup e restauração concluídos com sucesso no ambiente de testes.
