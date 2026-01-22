from sqlalchemy.orm import Session
from app.models.activity import Activity
from app.schemas.activity import ActivityCreate


def create_activity(db: Session, activity: ActivityCreate):
    db_activity = Activity(**activity.model_dump())
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    return db_activity


def get_activities(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Activity).offset(skip).limit(limit).all()


def get_activity(db: Session, activity_id: int):
    return db.query(Activity).filter(Activity.id == activity_id).first()


def get_activity_by_name(db: Session, name: str):
    return db.query(Activity).filter(Activity.name == name).first()


def get_activity_tree(db: Session, activity_id: int):
    activity = db.query(Activity).filter(Activity.id == activity_id).first()
    if not activity:
        return []

    def get_children(activity):
        children = db.query(Activity).filter(Activity.parent_id == activity.id).all()
        for child in children:
            child.children = get_children(child)
        return children

    activity.children = get_children(activity)
    return activity
