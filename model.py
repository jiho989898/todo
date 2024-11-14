from pydantic import BaseModel
from typing import List

class Todo(BaseModel):
    id: int
    item: str

    class Config:
        json_schema_extra = {
                "example": {
                    "id": 1,
                    "item": "첫번째 아이템"
                }
        }


#todo의 item을 변경하기 위한 모델

class todoItem(BaseModel):
    item: str
    class Config:
        json_schema_extra = {
                "example": {
                    "item": "변경할 아이템 작성"
                }
        }

#todo_list의 item만 리턴하기 위한 모델
class TodoItems(BaseModel):
    todos: List[todoItem]
    class Config:
        json_schema_extra = {
            "example": {
                "todos": [
                    {
                        "item": "첫번재 아이템"
                    },
                    {
                        "item": "두번재 아이템"
                    }
                ]
            }
        }