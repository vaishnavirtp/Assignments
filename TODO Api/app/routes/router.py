from fastapi import FastAPI, HTTPException, Depends, APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from uuid import UUID
import app.models.models as models
from app.database.database import get_db
from sqlalchemy.orm import Session
from app.schemas.schemas import Task, TaskDetails, Priority
from sqlalchemy import desc

router = APIRouter()


# ------------------------------ Get Requests------------------------------
@router.get("/")
def get_tasks(db: Session = Depends(get_db)):
    return db.query(models.Tasks).all()


@router.get("/priority-tasks/{priority}")
def get_tasks(priority: Priority, db: Session = Depends(get_db)):
    return db.query(models.Tasks).filter(models.Tasks.priority == priority).all()


@router.get("/check-status/{status}")
def get_tasks(status: bool, db: Session = Depends(get_db)):
    return db.query(models.Tasks).filter(models.Tasks.status == status).all()


@router.get("/sort-by-date/")
def get_tasks(db: Session = Depends(get_db)):
    return db.query(models.Tasks).order_by(desc(models.Tasks.start_date)).all()


# ------------------------------ Post Requests------------------------------


@router.post("/", status_code=201)
async def create_task(task: Task, db: Session = Depends(get_db)):
    try:
        task_model = models.Tasks(**task.dict())

        db.add(task_model)
        db.commit()
        return JSONResponse(content="Successfully created the task")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=f"Some error occured.")


# ------------------------------ Put Requests------------------------------


@router.put("/{task_id}", status_code=200)
async def update_task(task_id: int, task: TaskDetails, db: Session = Depends(get_db)):
    try:
        task_model = db.query(models.Tasks).filter(models.Tasks.id == task_id).first()
        if task_model is None:
            raise HTTPException(status_code=404, detail="ID doesn't exist")
        task_model.name = task.name
        task_model.description = task.description
        task_model.priority = task.priority

        db.add(task_model)
        db.commit()
        return JSONResponse(content="Successfully updated the task")
    except:
        return HTTPException(status_code=404, detail=f"Task Not found.")


# ------------------------------ Delete Requests------------------------------


@router.delete("/{task_id}", status_code=200)
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    try:
        task_model = db.query(models.Tasks).filter(models.Tasks.id == task_id).first()
        if task_model is None:
            raise HTTPException(status_code=404, detail="ID doesn't exist")
        db.query(models.Tasks).filter(models.Tasks.id == task_id).delete()
        db.commit()
        return JSONResponse(content="Successfully deleted the task")
    except:
        return HTTPException(status_code=404, detail=f"Task Not found.")


@router.delete("/delete-all/", status_code=200)
async def delete_task(db: Session = Depends(get_db)):
    try:
        db.query(models.Tasks).delete()
        db.commit()
        return JSONResponse(content="Successfully deleted all the tasks")
    except:
        return HTTPException(status_code=400, detail=f"Some error occured.")
