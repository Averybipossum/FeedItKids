from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Agora você pode acessar suas variáveis de ambiente como variáveis normais
senha = os.getenv("SENHA_BANCO")
chave_api = os.getenv("CHAVE_API")
