from typing import List, Optional 
from uuid import UUID, uuid4
from pydantic import BaseModel 
from enum import Enum

class Genero(str, Enum):
    masculino = "Masculino"
    femenino = "Femenino"
    otro = "otro"
class Roles(str, Enum):
    admin = "admin"
    user = "user"
    bad = "Bad_Bitch"
class User (BaseModel):
    id: Optional [UUID] = uuid4()
    nombre: str 
    apellidos: str 
    genero: Genero 
    roles: List[Roles] 