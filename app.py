from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Defining your route structure
# Users
@app.get("/api/v1/users")
async def get_users():
    pass


class UserCreate(BaseModel):
    fullname: str
    email: str
    password: str
    cellnumber: str
    age: int


@app.post("/api/v1/users")
async def create_user(user: UserCreate):
    pass
