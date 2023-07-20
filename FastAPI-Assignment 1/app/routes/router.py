from fastapi import FastAPI, HTTPException, Depends, APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from uuid import UUID
import app.models.models as models
from app.database.database import get_db
from sqlalchemy.orm import Session
from app.schemas.schemas import Task, TaskDetails, Priority
from sqlalchemy import desc
from http import HTTPStatus
from app.utils.exceptions import InvalidIDError

router = APIRouter()


# ------------------------------ Get Requests------------------------------
@router.get("/")
def get_tasks(db: Session = Depends(get_db)):
    return db.query(models.Tasks).all()


@router.get("/{task_id}")
def get_task(task_id: int, db: Session = Depends(get_db)):
    try:
        task = db.query(models.Tasks).filter(models.Tasks.id == task_id).first()
        if task is None:
            raise InvalidIDError(task_id, "task")
        return task

    except InvalidIDError as e:
        raise HTTPException(status_code=e.status, detail=str(e))


@router.get("/priority-tasks/{priority}")
def get_tasks_by_priority(priority: Priority, db: Session = Depends(get_db)):
    return db.query(models.Tasks).filter(models.Tasks.priority == priority).all()


@router.get("/check-status/{status}")
def get_tasks_by_status(status: bool, db: Session = Depends(get_db)):
    return db.query(models.Tasks).filter(models.Tasks.status == status).all()


@router.get("/sort-by-date/")
def sort_tasks_by_date(db: Session = Depends(get_db)):
    return db.query(models.Tasks).order_by(desc(models.Tasks.start_date)).all()


# ------------------------------ Post Requests------------------------------


@router.post("/", status_code=201)
async def create_task(task: Task, db: Session = Depends(get_db)):
    try:
        task_model = models.Tasks(**task.dict())
        db.add(task_model)
        db.commit()

        return JSONResponse(content="Successfully created the task")
    except ValueError:
        raise HTTPException(
            status_code=HTTPStatus.UNPROCESSABLE_ENTITY, detail="Invalid data"
        )


# ------------------------------ Put Request------------------------------


@router.put("/{task_id}", status_code=200)
async def update_task(task_id: int, task: TaskDetails, db: Session = Depends(get_db)):
    try:
        task_model = db.query(models.Tasks).filter(models.Tasks.id == task_id).first()
        if task_model is None:
            raise InvalidIDError(task_id, "task")
        task_model.name = task.name
        task_model.description = task.description
        task_model.priority = task.priority

        db.add(task_model)
        db.commit()
        return JSONResponse(content="Successfully updated the task")
    except InvalidIDError as e:
        raise HTTPException(status_code=e.status, detail=str(e))
    except ValueError:
        raise HTTPException(
            status_code=HTTPStatus.UNPROCESSABLE_ENTITY, detail="Invalid data"
        )


# ------------------------------ Delete Requests------------------------------


@router.delete("/{task_id}", status_code=200)
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    try:
        task_model = db.query(models.Tasks).filter(models.Tasks.id == task_id).first()
        if task_model is None:
            raise InvalidIDError(task_id, "task")
        db.query(models.Tasks).filter(models.Tasks.id == task_id).delete()
        db.commit()
        return JSONResponse(content="Successfully deleted the task")
    except InvalidIDError as e:
        raise HTTPException(status_code=e.status, detail=str(e))


@router.delete("/delete-all/", status_code=200)
async def delete_task(db: Session = Depends(get_db)):
    try:
        db.query(models.Tasks).delete()
        db.commit()
        return JSONResponse(content="Successfully deleted all the tasks")
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail=str(e))
