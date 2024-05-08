import enum
from sqlalchemy import Column, String, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType, PasswordType
from back_end.src.database.db_setup import Base



class Papel(enum.Enum):
    admin = 1
    usuario = 2

class Usuario(Base):
    __tablename__ = "Usuarios"

    id_usuario = Column(EmailType, primary_key=True)
    nome = Column(String(64), nullable=False)
    senha = Column(PasswordType(
        shemes = [
            'pbkdf2_sha512',
            'md5_crypt'
        ],
        deprecated = ['md5_crypt']
    ))
    papel = Column(Enum(Papel))
    id_animal = Column(Integer, ForeignKey("animal.id_animal"))

    animal = relationship("Animal", back_populates="usuario")

    ObejtivoCompleto= relationship("ObejtivoCompleto", secondary="usuario")
    
    
class Obejtivos(Base):
    __tablename__ = "objetivos"

    id_objetivo = Column(Integer, primary_key=True)
    descricao = Column(String(255), nullable=False)
    pontuacao = Column(Integer, nullable=False)

class ObejtivoCompleto(Base):
    __tablename__ = "ObejtivoCompleto"

    id_user = Column(EmailType, ForeignKey("usuarios.id_usuario"), primary_key=True)

    id_task = Column(Integer, ForeignKey("objetivos.id_objetivos"), primary_key=True)

    usuario = relationship("Usuario", back_populates="objetivo_completo")

    objetivo = relationship("Objetivos")
