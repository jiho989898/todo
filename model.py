from pydantic import BaseModel
from typing import List

class Todo(BaseModel):
    id: int
    item: str

    class Config:
        json_schema_extra = {
                "example": {
                    "id": 1,
                    "item": "Example Schema"
                }
        }

class TodoItem(BaseModel):
    item: str

    class Config:
        json_schema_extra = {
                "example": {
                    "item": "TEST TEST"
                }
        }

class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Config:
        schema_extra = {
                "example": {
                    "beomtaeks": [
                        {
                            "item": "Example schema 1"
                        },
                        {
                            "item": "Example schema 2"
                        }
                    ]
                }
        }
