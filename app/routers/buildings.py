from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.building import Building, BuildingCreate
from app.crud.building import create_building, get_buildings, get_building
from app.database import get_db

router = APIRouter(prefix="/buildings", tags=["buildings"])


@router.post("/", response_model=Building)
def create_new_building(building: BuildingCreate, db: Session = Depends(get_db)):
    return create_building(db, building)


@router.get("/", response_model=list[Building])
def read_buildings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_buildings(db, skip, limit)


@router.get("/{building_id}", response_model=Building)
def read_building(building_id: int, db: Session = Depends(get_db)):
    db_building = get_building(db, building_id)
    if db_building is None:
        raise HTTPException(status_code=404, detail="Building not found")
    return db_building
