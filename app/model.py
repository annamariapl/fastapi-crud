from pydantic import BaseModel, Field
from typing import Optional, List

class PersonSchema(BaseModel):
    name: str = Field(...)
    noGoPlaces: List[str] = Field(...)
    noGoTags: List[str] = Field(...)
    mustTags: List[str] = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "Daniel",
                "noGoTags": ["asian"],
                "noGoPlaces": ["Taka Fish House | Kotti"],
                "mustTags":["has-sitting-places"]
            }
        }

class UpdatePersonSchema(BaseModel):
    name: Optional[str]
    noGoPlaces: Optional[List[str]]
    noGoTags: Optional[List[str]]
    mustTags: Optional[List[str]]

    class Config:
        schema_extra = {
           "example": {
                "name": "Axel",
                "noGoTags": ["asian"],
                "noGoPlaces": ["Taka Fish House | Kotti"],
                "mustTags":["has-sitting-places"]
            }
        }
