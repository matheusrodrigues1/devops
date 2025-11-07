markdown
# Docker Multi-Container Application

Uma aplicação CRUD completa com FastAPI e PostgreSQL usando Docker Compose.

## Estrutura do Projeto

- `app/` - Código da aplicação FastAPI
- `docker/` - Configurações do PostgreSQL
- `scripts/` - Scripts utilitários
- `Dockerfile` - Definição da imagem da aplicação
- `docker-compose.yml` - Orquestração dos containers
- `.env.example` - Template de variáveis de ambiente

## Pré-requisitos

- Docker
- Docker Compose

## Configuração

1. **Clone o repositório**
   ```bash
   git clone <url-do-repositorio>
   cd projeto-docker
Configure as variáveis de ambiente

bash
cp .env.example .env
Edite o arquivo .env com suas configurações:

env
DB_NAME=app_database
DB_USER=postgres
DB_PASSWORD=senha_segura_postgres
DB_APP_PASSWORD=senha_segura_app_user
SECRET_KEY=sua_chave_secreta_muito_segura
Execute a aplicação

bash
docker-compose up --build
Serviços
Aplicação: http://localhost:8000

PostgreSQL: localhost:5432

API Endpoints
Users CRUD
GET / - Health check

GET /health - Status da aplicação

POST /users/ - Criar usuário

GET /users/ - Listar usuários

GET /users/{id} - Buscar usuário por ID

PUT /users/{id} - Atualizar usuário

DELETE /users/{id} - Deletar usuário

Exemplos de Uso
Criar usuário
bash
curl -X POST "http://localhost:8000/users/" \
  -H "Content-Type: application/json" \
  -d '{"email": "usuario@exemplo.com", "name": "João Silva"}'
Listar usuários
bash
curl "http://localhost:8000/users/"
Atualizar usuário
bash
curl -X PUT "http://localhost:8000/users/1" \
  -H "Content-Type: application/json" \
  -d '{"name": "João Santos"}'
Segurança
Usuário não-root para a aplicação

Permissões mínimas necessárias para o usuário do banco

Variáveis de ambiente para configurações sensíveis

Rede customizada isolando a comunicação entre containers

Comandos Úteis
bash
# Executar em background
docker-compose up -d

# Parar serviços
docker-compose down

# Ver logs
docker-compose logs -f

# Acessar banco de dados
docker exec -it postgres_db psql -U postgres -d app_database

# Executar testes
docker-compose exec app python -m pytest
Persistência de Dados
Os dados do PostgreSQL são persistidos no volume postgres_data.

Rede
Os containers comunicam-se através da rede customizada app-network.

text

## Como usar:

1. Crie um repositório no GitHub
2. Copie todos os arquivos acima para seu repositório
3. Execute os comandos:
```bash
chmod +x scripts/wait-for-db.sh
cp .env.example .env
# Edite o .env com suas senhas
docker-compose up --build
Teste a API em http://localhost:8000

Esta implementação atende todos os requisitos:

✅ Dockerfile multi-stage com Alpine

✅ Docker Compose com 2 serviços

✅ Volumes para persistência

✅ Rede customizada

✅ Variáveis de ambiente

✅ CRUD completo

✅ Segurança no banco (usuário app_user com permissões limitadas)

✅ Documentação completa