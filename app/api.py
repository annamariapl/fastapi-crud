from fastapi import FastAPI, Body
from fastapi.encoders import jsonable_encoder

from app.model import PersonSchema, UpdatePersonSchema
from app.database import save_person, get_all_persons, get_single_person, update_person_data, remove_person

app = FastAPI()

@app.get("/", tags=["Root"])
def get_root() -> dict:
    return {
        "message": "Tutaj Ania! This will be backend"
    }

@app.get("/person", tags=["Person"])
def get_persons() -> dict:
    persons = get_all_persons()
    return {
        "data": persons
    }

@app.get("/person/{id}", tags=["Person"])
def get_person(id: str) -> dict:
    person = get_single_person(id)
    if person:
        return {
            "data": person
        }
    return {
        "error": "No such person with ID {} exist".format(id)
    }

@app.post("/person", tags=["Person"])
def add_person(person: PersonSchema = Body(...)) -> dict:
    new_person = save_person(person.dict())
    return new_person
    return {
        "message": "Person added successfully."
    }
  
@app.put("/person", tags=["Person"])
def update_person(id: str, person_data: UpdatePersonSchema)  -> dict:
    if not get_single_person(id):
        return {
            "error": "No such person exist"
        }

    update_person_data(id, person_data.dict())

    return {
        "message": "Person updated successfully."
    }

@app.delete("/person/{id}", tags=["Person"])
def delete_person(id: str) -> dict:
    if not get_single_person(id):
        return {
            "error": "Invalid ID passed"
        }


    remove_person(id)
    return {
        "message": "Person deleted successfully."
    }