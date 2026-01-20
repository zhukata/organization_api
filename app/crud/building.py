from sqlalchemy.orm import Session
from app.models.building import Building
from app.schemas.building import BuildingCreate


def create_building(db: Session, building: BuildingCreate):
    db_building = Building(**building.model_dump())
    db.add(db_building)
    db.commit()
    db.refresh(db_building)
    return db_building


def get_buildings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Building).offset(skip).limit(limit).all()


def get_building(db: Session, building_id: int):
    return db.query(Building).filter(Building.id == building_id).first()
