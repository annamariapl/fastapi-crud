from pymongo import MongoClient
from bson import ObjectId
from decouple import config

connection_details = config("DB_HOST")

client = MongoClient(connection_details)

database = client.persons

person_collection = database.get_collection('persons_collection')

def parse_person_data(person) -> dict:
    return {
        "id": str(person["_id"]),
        "name": person["name"],
        "noGoTags": person["noGoTags"],
        "mustTags": person["mustTags"],
        "noGoPlaces": person["noGoPlaces"]
    }

def save_person(person_data: dict) -> dict:
    person = person_collection.insert_one(person_data).inserted_id
    return {
        "id": str(person)
    }

def get_single_person(id: str) -> dict:
    person = person_collection.find_one({"_id": ObjectId(id)})
    if person:
        return parse_person_data(person)

def get_all_persons() -> list:
    persons = []
    for person in person_collection.find():
        persons.append(parse_person_data(person))

    return persons

def update_person_data(id: str, data: dict):
    person = person_collection.find_one({"_id": ObjectId(id)})
    if person:
        person_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        return True

def remove_person(id: str):
    person = person_collection.find_one({"_id": ObjectId(id)})
    if person:
        person_collection.delete_one({"_id": ObjectId(id)})
        return True
