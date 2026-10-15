from typing import Annotated
import bcrypt
from fastapi import Depends, FastAPI, HTTPException, status, APIRouter
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from datetime import datetime, timedelta
from pydantic import BaseModel

app = FastAPI()

security = HTTPBasic()

#Credentials 
username = "admin"
password = "admin123"
hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())



@app.get("/")
def secret_response(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    if credentials.username != username or not bcrypt.checkpw(credentials.password.encode('utf-8'), hash): 
       raise HTTPException(
       status_code=status.HTTP_401_UNAUTHORIZED,
       detail="Invalid credentials",
       headers={"WWW-Authenticate": "Basic"},
    )           
    return {"message": "You have access to the Website!"}





