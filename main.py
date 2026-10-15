from fastapi import FastAPI, Form, Query, Path, Body,UploadFile
from pydantic import BaseModel, PydanticUserError

#________________________________________________________IMPORTS____________________________________________________________

import schemas
import database
import Auth
import app

app=FastAPI()

#________________________________________________________Home Page___________________________________________________________

@app.get("/items") #The GET method is used to retrieve information from the server. It is the most common method for fetching data.
def read_items():
    return {'message': 'Welcome to Nyakatani Fitness Center!'}

#___________________________________________________List of all Membership Plans_________________________________________________

@app.get("/Membership_plans") #The GET method is used to retrieve information from the server. It is the most common method for fetching data.
def read_membership_plans():
    return list(Membership_plans())


@app.get("/Trainers") #The GET method is used to retrieve information from the server. It is the most common method for fetching data.
def read_trainers():
    return list(Trainers())


@app.get("/members/{member_id}") #The GET method is used to retrieve information from the server. It is the most common method for fetching data.
def read_member(member_id: str):
    return {'member_id': member_id, 'message': 'Member details retrieved successfully'}

#__________________________________________________________NEW RESOURCES_____________________________________________________________

@app.post("/login") # The POST method is used to send data to the server to create new resources. It is typically used for submitting form data, creating new records in a database
def login(Full_name: str, email: str, password: str):
    return {'username': Full_name, 'email': email, 'message': 'Login successful'}


@app.post("/members") # The POST method is used to send data to the server to create new resources. It is typically used for submitting form data, creating new records in a database
def create_member(Full_name: str, email: str, password: str):
    return {'Full_name': Full_name, 'email': email, 'password': password, 'message': 'Member created successfully'}

#def create_members(member: Member):
#    return member

@app.post("/Trainers") # The POST method is used to send data to the server to create new resources. It is typically used for submitting form data, creating new records in a database
def create_trainer(Full_name: str, email: str, password: str):  
    return {'Full_name': Full_name, 'email': email, 'password': password, 'message': 'Trainer created successfully'}

@app.post("/Membership_plans") # The POST method is used to send data to the server to create new resources. It is typically used for submitting form data, creating new records in a database
def create_membership_plan(plan_name: str, description: str, price: float, duration: int):
    return {'plan_name': plan_name, 'description': description, 'price': price, 'duration': duration, 'message': 'Membership plan created successfully'}


#________________________________________________________Upload Member Profile Picture______________________________________________________________

@app.post("/uploadfile") # The POST method is used to send data to the server to create new resources. It is typically used for submitting form data, creating new records in a database
def upload_file(file: UploadFile):
    return {'filename': file.filename, 'content_type': file.content_type, 'message': 'File uploaded successfully'}

#______________________________________________________Update Exixting Member Information______________________________________________________________________

@app.put("/members/{member_id}") # The PUT method is used to update existing resources on the server. It replaces the entire resource with the new data provided in the request.
def update_member(member_id: str, Full_name: str, email: str, password: str):
    return {'member_id': member_id, 'Full_name': Full_name, 'email': email, 'password': password}


@app.put("/login/{login_id}") # The PUT method is used to update existing resources on the server. It replaces the entire resource with the new data provided in the request.
def update_login(login_id: str, Full_name: str, email: str, password: str):
    return {'login_id': login_id, 'Full_name': Full_name, 'email': email, 'password': password}

#________________________________________________________________Delete Members____________________________________________________

@app.delete("/members/{member_id}") # The DELETE method is used to remove a resource from the server. It deletes the specified resource identified by the provided identifier.
def delete_member(member_id: str):
    return {'message': f'Member deleted with ID: {member_id}'}

