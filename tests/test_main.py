import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Importe o necessário da sua aplicação
from app.main import app, get_db
from app.models import Base

# 1. Configurar Banco de Dados de Teste em Memória
# Use um banco de dados SQLite para os testes em vez do PostgreSQL
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture()
def session():
    # Cria as tabelas antes de cada teste
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        # Deleta as tabelas após cada teste
        Base.metadata.drop_all(bind=engine)

@pytest.fixture()
def client(session):
    # Sobrescreve a dependência get_db com uma versão que usa a session de teste
    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    app.dependency_overrides.clear()

# 2. Escrever Testes para as Rotas CRUD

def test_create_user(client):
    response = client.post(
        "/users/",
        json={"email": "test@example.com", "name": "Test User"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@example.com"
    assert "id" in data

def test_read_user(client):
    # Cria um usuário primeiro
    new_user = client.post(
        "/users/",
        json={"email": "read@example.com", "name": "Read User"},
    ).json()
    user_id = new_user["id"]

    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["email"] == "read@example.com"

def test_update_user(client):
    # Cria um usuário primeiro
    new_user = client.post(
        "/users/",
        json={"email": "update@example.com", "name": "Update User"},
    ).json()
    user_id = new_user["id"]

    # Atualiza o usuário
    response = client.put(
        f"/users/{user_id}",
        json={"name": "Updated Name", "is_active": False},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Name"
    assert data["is_active"] == False

def test_delete_user(client):
    # Cria um usuário primeiro
    new_user = client.post(
        "/users/",
        json={"email": "delete@example.com", "name": "Delete User"},
    ).json()
    user_id = new_user["id"]

    # Deleta o usuário
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "User deleted successfully"

    # Tenta ler o usuário deletado
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 404