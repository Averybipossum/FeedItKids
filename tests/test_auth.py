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
# async def test_login_for_access_token(client):
#     # Primeiro, cria um usuário para autenticar
#     await client.post("/usuarios/", json={
#         "email": "test@example.com",
#         "senha": "password123",
#         "pontuacao_total": 0
#     })
    
#     # Em seguida, autentica o usuário
#     response = await client.post("/token", data={
#         "username": "test@example.com",
#         "password": "password123"
#     })
#     assert response.status_code == 200
#     assert "acess_token" in response.json()

# @pytest.mark.asyncio
# async def test_read_users_me(client):
#     # Primeiro, cria e autentica um usuário
#     await client.post("/usuarios/", json={
#         "email": "test@example.com",
#         "senha": "password123",
#         "pontuacao_total": 0
#     })
#     login_response = await client.post("/token", data={
#         "username": "test@example.com",
#         "password": "password123"
#     })
#     token = login_response.json()["acess_token"]
    
#     # Em seguida, obtém os dados do usuário autenticado
#     response = await client.get("/me", headers={
#         "Authorization": f"Bearer {token}"
#     })
#     assert response.status_code == 200
#     assert response.json()["email"] == "test@example.com"