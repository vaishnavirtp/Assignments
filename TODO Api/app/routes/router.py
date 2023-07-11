from fastapi import FastAPI, HTTPException, Depends, APIRouter
from uuid import UUID
import app.models.models as models
from app.database.database import engine, Sessionlocal
from sqlalchemy.orm import Session
from app.schemas.schemas import Task, TaskDetails
from sqlalchemy import desc


models.Base.metadata.create_all(bind=engine)

router = APIRouter()


def get_db():
    try:
        db = Sessionlocal()
        yield db
    finally:
        db.close()


# ------------------------------ Get Requests------------------------------
@router.get("/")
def get_tasks(db: Session = Depends(get_db)):
    return db.query(models.Tasks).all()


@router.get("/priority-tasks/{priority}")
def get_tasks(priority: str, db: Session = Depends(get_db)):
    return db.query(models.Tasks).filter(models.Tasks.priority == priority).all()


@router.get("/check-status/{status}")
def get_tasks(status: bool, db: Session = Depends(get_db)):
    return db.query(models.Tasks).filter(models.Tasks.status == status).all()


@router.get("/sort-by-date/")
def get_tasks(db: Session = Depends(get_db)):
    return db.query(models.Tasks).order_by(desc(models.Tasks.start_date)).all()


# ------------------------------ Post Requests------------------------------


@router.post("/")
def create_task(task: Task, db: Session = Depends(get_db)):
    task_model = models.Tasks()
    task_model.name = task.name
    task_model.description = task.description
    task_model.priority = task.priority
    task_model.start_date = task.start_date
    task_model.end_date = task.end_date
    task_model.status = task.status

    db.add(task_model)
    db.commit()
    return HTTPException(status_code=201, detail=f"Successfully created the task")


# ------------------------------ Put Requests------------------------------


@router.put("/{task_id}")
def update_task(task_id: int, task: Task, db: Session = Depends(get_db)):
    task_model = db.query(models.Tasks).filter(models.Tasks.id == task_id).first()
    if task_model is None:
        raise HTTPException(status_code=404, detail="ID doesn't exist")
    task_model.name = task.name
    task_model.description = task.description
    task_model.priority = task.priority
    task_model.start_date = task.start_date
    task_model.end_date = task.end_date
    task_model.status = task.status

    db.add(task_model)
    db.commit()
    return HTTPException(status_code=200, detail="Successfully updated the task")


# ------------------------------ Delete Requests------------------------------


@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task_model = db.query(models.Tasks).filter(models.Tasks.id == task_id).first()
    if task_model is None:
        raise HTTPException(status_code=404, detail="ID doesn't exist")
    db.query(models.Tasks).filter(models.Tasks.id == task_id).delete()
    db.commit()
    return HTTPException(status_code=200, detail="Successfully deleted the task")


@router.delete("/delete-all/")
def delete_task(db: Session = Depends(get_db)):
    db.query(models.Tasks).delete()
    db.commit()
    return HTTPException(status_code=200, detail="Successfully deleted all the task")
