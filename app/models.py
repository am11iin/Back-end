from sqlmodel import SQLModel, Field
from typing import Optional
from enum import Enum

# role definie proprement par enum 
class Role(str , Enum):
    admin = "admin"
    proffesseur = "proffesseur"
    etudiant = "etudiant"


# modele d'etulisaateur 
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    email: str
    password: str
    role: Role = Role.admin


from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    file = Column(String, nullable=True)
    teacher_id = Column(Integer, ForeignKey("users.id"))

    
