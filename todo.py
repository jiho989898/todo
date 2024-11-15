from fastapi import APIRouter, Path, HTTPException, status, Request, Depends
from fastapi.templating import Jinja2Templates
from model import Todo,TodoItem,TodoItems

todo_router = APIRouter()

# DB 없는 상태에서 딕셔너리 내에 id,item 을 저장하기 위한 리스트
todo_list = []

# 구성된 내용을 반영하기 위한 템플릿 파일은 ? 
templates = Jinja2Templates(directory="templates/")

# item 추가 (POST)
@todo_router.post("/todo",status_code=201)
async def add_todo(request: Request, todo: Todo = Depends(Todo.as_form)):
    todo.id = len(todo_list) + 1
    todo_list.append(todo)
    return templates.TemplateResponse("todo.html",
    {
        "request": request,
        "todos": todo_list
    })


# 전체 데이터 확인
@todo_router.get("/todo", response_model=TodoItems)
async def retrieve_todos(request: Request):
    return templates.TemplateResponse("todo.html", {
        "request" : request,
        "todos" : todo_list
    })


@todo_router.get("/todo/{todo_id}")
async def get_single_todo(request: Request, todo_id: int = Path(..., title="특정 todo를 확인하기 위한 ID",ge=1,le=1000)) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return templates.TemplateResponse(
                    "todo.html" , {
                    "request": request,
                    "todo": todo
                    })
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="존재하지 않는 ID 입니다"
    )


# 개별 id 의 item 수정하기(PUT)
@todo_router.put("/todo/{todo_id}")
async def update_todo(todo_data: TodoItem, todo_id: int = Path(...,title=("변경할 아이템의 ID"))) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {
                "message" : "todo 가 업데이트 되었습니다"
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="존재하지 않는 ID 입니다"
    )


# 전체 목록 삭제하기
@todo_router.delete("/todo")
async def delete_all_todo() -> dict:
    todo_list.clear()
    return {
            "message": "전체 삭제되었습니다"
    }


# 특정 item 삭제하기
@todo_router.delete("/todo/{todo_id}")
async def delete_single_todo(todo_id: int) -> dict:
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            return {
                    "message": "삭제되었습니다"
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="존재하지 않는 ID 입니다"
    )