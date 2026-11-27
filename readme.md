# Bibliotecas da aplicação
pip install fastapi uvicorn sqlalchemy passlib[crypt] python-jose[cryptography] python-dotenv python-multipart

# Executar a aplicação
uvicorn main:app --reload

# Módulo para migrar classes para a base de dados
pip install alembic
alembic init alembic

# Configurações alembic
No ficheiro alembic.ini, alterar o caminho da base de dados (sqlalchemy.url)
No ficheiro env.py, importar a variável Base
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

Ainda no ficheiro env.py, antes da linha target_metadata:
from models import Base
target_metadata = Base.metadata

# Criar o ficheiro de migração
alembic revision --autogenerate -m "nome_migracao"
# Executar a migração
alembic upgrade head