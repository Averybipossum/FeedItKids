# import pytest
# from httpx import AsyncClient
# from main import app  # ajuste o caminho se necessário
# from src.database.database import get_db, Base
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# # Configuração do banco de dados para testes
# SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
# TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base.metadata.create_all(bind=engine)

# def override_get_db():
#     try:
#         db = TestingSessionLocal()
#         yield db
#     finally:
#         db.close()

# app.dependency_overrides[get_db] = override_get_db

# @pytest.fixture
# async def client():
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         yield ac

# @pytest.mark.asyncio
# async def test_create_usuario(client):
#     response = await client.post("/usuarios/", json={
#         "email": "test@example.com",
#         "senha": "password123",
#         "pontuacao_total": 0
#     })
#     assert response.status_code == 200
#     assert response.json()["email"] == "test@example.com"

# @pytest.mark.asyncio
# async def test_read_user(client):
#     # Cria o usuário primeiro
#     create_response = await client.post("/usuarios/", json={
#         "email": "test@example.com",
#         "senha": "password123",
#         "pontuacao_total": 0
#     })
#     user_id = create_response.json()["id_usuario"]

#     # Recupera o usuário
#     response = await client.get(f"/usuarios/{user_id}")
#     assert response.status_code == 200
#     assert response.json()["email"] == "test@example.com"
