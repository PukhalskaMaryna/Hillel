from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.sql import functions as func
from fastapi.responses import Response

app = FastAPI(
    title="ToDo API",
    description="A simple ToDo API built with FastAPI",
    version="1.0.0"
)

DATABASE_URL = "sqlite:///task.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class TaskDB(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=False)
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
Base.metadata.create_all(bind=engine)

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class TaskIn(TaskBase):
    pass

class TaskOut(TaskBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

@app.post(
    path="/tasks", 
    response_model=TaskOut, 
    status_code=status.HTTP_201_CREATED
    )
async def create_task(task: TaskIn):
    db = SessionLocal()
    try:
        db_task = TaskDB(**task.model_dump())
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        return db_task
    finally:
        db.close()

@app.get(
    path="/tasks", 
    response_model=List[TaskOut]
    )
async def task_list(completed: Optional[bool] = None):
    db = SessionLocal()
    try:
        query = db.query(TaskDB)
        if completed is not None:
            query = query.filter(TaskDB.completed == completed)
        tasks = query.all()
        return tasks
    finally:
        db.close() 
          
@app.get(     
    path="/tasks/{task_id}", 
    response_model=TaskOut
    )     
async def task_detail(task_id: int):
    db = SessionLocal()
    try:
        task = db.query(TaskDB).filter(TaskDB.id == task_id).first()
        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found"
            )
        return task
    finally:
        db.close()

@app.put(
    path="/tasks/{task_id}", 
    response_model=TaskOut
    )
async def update_task(task_id: int, task: TaskIn):
    db = SessionLocal()
    try:
        db_task = db.query(TaskDB).filter(TaskDB.id == task_id).first()
        if not db_task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found"
            )
        for key, value in task.model_dump().items():
            setattr(db_task, key, value)
        db.commit()
        db.refresh(db_task)
        return db_task
    finally:
        db.close()

@app.delete(
    path="/tasks/{task_id}", 
    status_code=status.HTTP_204_NO_CONTENT
    )
async def delete_task(task_id: int):        
    db = SessionLocal()
    try:
        db_task = db.query(TaskDB).filter(TaskDB.id == task_id).first()
        if not db_task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found"
            )
        db.delete(db_task)
        db.commit()
    finally:
        db.close()
    return Response(status_code=status.HTTP_204_NO_CONTENT)