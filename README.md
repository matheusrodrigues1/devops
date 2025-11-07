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