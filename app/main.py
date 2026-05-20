from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel
import model, database
import redis, os

model.Base.metadata.create_all(bind=database.engine)
# tuesday update
app = FastAPI(title="TaskFlow API")

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=6379, decode_responses=True
)

# --- Schemas ---
class UserCreate(BaseModel):
    email: str
    password: str

class TaskCreate(BaseModel):
    title: str
    description: str = None

class TaskUpdate(BaseModel):
    title: str = None
    completed: bool = None

# --- Routes ---
@app.get("/health")
def health():
    return {"status": "ok", "service": "taskflow-api bind storage","version": "2.0"}
   

@app.post("/users", status_code=201)
def create_user(user: UserCreate, db: Session = Depends(database.get_db)):
    from passlib.context import CryptContext
    pwd = CryptContext(schemes=["bcrypt"])
    db_user = model.User(email=user.email, hashed_password=pwd.hash(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"id": db_user.id, "email": db_user.email}

@app.get("/tasks")
def get_tasks(db: Session = Depends(database.get_db)):
    return db.query(model.Task).all()

@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate, db: Session = Depends(database.get_db)):
    db_task = model.Task(**task.dict(), owner_id=1)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    redis_client.incr("tasks_created")
    return db_task

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskUpdate, db: Session = Depends(database.get_db)):
    db_task = db.query(model.Task).filter(model.Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    for k, v in task.dict(exclude_none=True).items():
        setattr(db_task, k, v)
    db.commit()
    return db_task

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int, db: Session = Depends(database.get_db)):
    db_task = db.query(model.Task).filter(model.Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(db_task)
    db.commit()

@app.get("/stats")
def stats():
    count = redis_client.get("tasks_created") or 0
    return {"total_tasks_created": int(count)}