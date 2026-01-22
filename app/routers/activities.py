from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.activity import Activity, ActivityCreate
from app.crud.activity import (
    create_activity,
    get_activities,
    get_activity,
    get_activity_tree,
)
from app.database import get_db

router = APIRouter(prefix="/activities", tags=["activities"])


@router.post("/", response_model=Activity)
def create_new_activity(activity: ActivityCreate, db: Session = Depends(get_db)):
    return create_activity(db, activity)


@router.get("/", response_model=list[Activity])
def read_activities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_activities(db, skip, limit)


@router.get("/{activity_id}", response_model=Activity)
def read_activity(activity_id: int, db: Session = Depends(get_db)):
    db_activity = get_activity(db, activity_id)
    if db_activity is None:
        raise HTTPException(status_code=404, detail="Activity not found")
    return db_activity


@router.get("/tree/{activity_id}", response_model=Activity)
def read_activity_tree(activity_id: int, db: Session = Depends(get_db)):
    activity_tree = get_activity_tree(db, activity_id)
    if activity_tree is None:
        raise HTTPException(status_code=404, detail="Activity not found")
    return activity_tree
