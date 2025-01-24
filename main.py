'''Operación CRUD en FastApi.'''
from fastapi import FastAPI
from uuid import UUID, uuid4
from models import Genero, Roles, User
from typing import List 


app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(), 
        nombre="Yayo", 
        apellidos="Lopez", 
        genero=Genero.femenino, 
        roles=[Roles.admin]
    ), 
        User(
        id=uuid4(), 
        nombre="Jazziel", 
        apellidos="Ortiz", 
        genero=Genero.masculino,  
        roles=[Roles.admin]
    ),
        User(
        id=uuid4(), 
        nombre="Irving", 
        apellidos="Morales", 
        genero=Genero.masculino, 
        roles=[Roles.admin]
    )
]

@app.get('/') 

async def root(): 
    return{"message": "Saludo"}
@app.get("/api/users")
async def get_users(): 
    return db

@app.post("/api/users")
async def create_user(user: User): 
    db.append(user)
    return{"id":user.id}

@app.delete("/api/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"message": "Deleted"}
    return {"error": f"User with id {user_id} not found"}

@app.put("/api/users/{user_id}")
async def update_user(user_id: UUID, updated_user: User):
    for user in db:
        if user.id == user_id:
            user.nombre = updated_user.nombre
            user.apellidos = updated_user.apellidos
            user.genero = updated_user.genero
            user.roles = updated_user.roles
            return {"message": f"User with id {user_id} has been updated", "user": user}
    return {"error": f"User with id {user_id} not found"}
