from fastapi import APIRouter, Path, HTTPException,status
from model import Todo, todoItem, TodoItems

todo_router = APIRouter()
todo_list = []

@todo_router.post("/todo", status_code=201)
async def add_todo(todo:Todo) -> dict:
    todo_list.append(todo)
    return {
        "message ": "todo added successfully"
    }



@todo_router.get("/todo")
async def retrieve_todos() -> dict:
    return {
        "todo" : todo_list
    }

@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int = Path(..., title="특정 todo를 확인하기 위한 ID",ge=1,le=1000)) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {
                "todo": todo
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="존재하지 않는 ID 입니다."
    )

# 개별 ip의 item을 수정하기(put)
@todo_router.put("/todo/{todo_id}")
async def update_todo(todo_data: todoItem, todo_id: int = Path(..., title="변경할 아이템의 ID")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {
                "message": "todo가 업데이트 되었습니다."
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="존재하지 않는 ID 입니다."
    )

@todo_router.delete("/todo")
async def delete_todo() -> dict:
    todo_list.clear()
    if not todo_list:
        return{
            "message": "모든 todo가 성공적으로 삭제 완료"
        }
    

@todo_router.delete("/todo/{todo_id}")
async def delete_single_todo(todo_id: int) -> dict:
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            return { "message": "삭제되었습니다"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="존재하지 않는 ID 입니다."
    )
