#Schemas describe the structure of the data that will be sent and received by the API endpoints. They define the expected fields, their types, and any validation rules. 
   #Schemas are used to ensure that the data being sent to and received from the API adheres to a specific format, making it easier to work with and reducing the likelihood of errors.
#FastAPI uses Pydantic models to define schemas. Pydantic is a data validation and settings management library for Python, based on Python type annotations. It allows you to define
    #data models using standard Python types, and it automatically validates the data against those models.

from pydantic import BaseModel

class Member(BaseModel):
    Full_name: str
    email: str
    password: str
    cellnumber: str
    age: int
#Compair to the adding new members part in main.py, the Member class is used to define the structure of the 
# data that will be sent when creating a new member. It includes fields for Full_name, email, password, cellnumber, and age. 
# This ensures that when a new member is created, the data adheres to this specific format.

#_____________________________  MEMBERS/USERS   ___________________
class Member_put(BaseModel):
    plan_name: str
    description: str
    price: float
    duration: int

class Member_post(BaseModel):
    plan_name: str
    description: str
    price: float
    duration: int    

class Member_get(BaseModel):
    plan_name: str
    description: str
    price: float
    duration: int

class Member_delete(BaseModel):
    plan_name: str
    description: str
    price: float
    duration: int

#_____________________________  LOGIN/JOIN NOW   ___________________
class Login(BaseModel):
    Full_name: str
    email: str
    password: str

class Login_post(BaseModel):
    Full_name: str
    email: str
    password: str    

class Login_put(BaseModel):
    Full_name: str
    email: str
    password: str  

class Login_get(BaseModel):
    Full_name: str
    email: str
    password: str

#  _____________________________  TRAINERS   ___________________

class Trainers(BaseModel):
    Full_name: str
    email: str
    password: str

class Trainers_post(BaseModel):
    Full_name: str
    email: str
    password: str

class Trainers_put(BaseModel):
    Full_name: str
    email: str
    password: str

class Trainers_get(BaseModel):
    Full_name: str
    email: str
    password: str

class Trainers_delete(BaseModel):
    Full_name: str
    email: str
    password: str

#______________________________  SESSIONS/CLASSES   ___________________
class Sessions(BaseModel):
    session_name: str
    description: str
    duration: int
    trainer_id: int
    datetime: str

class Sessions_post(BaseModel):
    session_name: str
    description: str
    duration: int
    trainer_id: int
    datetime: str       



    




   



