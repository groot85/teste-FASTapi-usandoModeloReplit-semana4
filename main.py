from fastapi import FastAPI
from uuid import UUID
from typing import List
from models import UserBase, UserCreate, UserUpdate,Role

app = FastAPI()

db: List[UserBase] = [
    UserCreate(
        id = UUID('1'),
        first_name = "Laura",
        last_name = "Avila",
        email = "queiroz.analaura@gmail.com",
        role = [Role.role_1]    
    ),
    UserCreate(
        id = UUID('2'),
        first_name = "Cesar",
        last_name = "Pedroso",
        email = "cesar.pedroso@gmail.com",
        role = [Role.role_2]
    ),
    UserCreate(
        id = UUID('3'),
        first_name = "Jose",
        last_name = "Ferreira",
        email = "jose.ferreira@gmail.com",
    )
]


@app.get("/api/users")
async def get_users():
    return db;

@app.get("/api/users/{id}")
async def get_user(id: UUID):
    for user in db:
        if user.id == id:
            return user
    return {"message": "Usuário não encontrado"}

@app.put("/api/users/{id}")
async def get_user(id: UUID, user_update: UserUpdate):
    for index, user in enumerate(db):
        if user.id == id:
            db[index] = user_update
            return user_update
    return {"message": "Usuário não encontrado"}

@app.post("/api/users")
async def create_user(user: UserCreate):
    db.append(user)
    return user

@app.delete("/api/users/{id}")
async def delete_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return {"message": "Usuário deletado"}
    return {"message": "Usuário não encontrado"}  