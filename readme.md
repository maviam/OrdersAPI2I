# Bibliotecas da aplicação
pip install fastapi uvicorn sqlalchemy passlib[crypt] python-jose[cryptography] python-dotenv python-multipart

# Executar a aplicação
uvicorn main:app --reload