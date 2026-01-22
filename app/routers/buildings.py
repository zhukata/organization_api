from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.building import Building, BuildingCreate
from app.crud.building import create_building, get_buildings, get_building
from app.database import get_db

router = APIRouter(prefix="/buildings", tags=["buildings"])


@router.post("/", response_model=Building)
def create_new_building(building: BuildingCreate, db: Session = Depends(get_db)):
    """
    Создать новое здание.

    - **building**: Данные для создания здания, включая адрес, широту и долготу.
    Возвращает созданное здание с присвоенным ID.
    """
    return create_building(db, building)


@router.get("/", response_model=list[Building])
def read_buildings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Получить список всех зданий с пагинацией.

    - **skip**: Количество записей для пропуска (по умолчанию 0).
    - **limit**: Максимальное количество записей для возврата (по умолчанию 100).
    Возвращает список зданий.
    """
    return get_buildings(db, skip, limit)


@router.get("/{building_id}", response_model=Building)
def read_building(building_id: int, db: Session = Depends(get_db)):
    """
    Получить здание по ID.

    - **building_id**: Уникальный идентификатор здания.
    Возвращает здание или 404, если не найдено.
    """
    db_building = get_building(db, building_id)
    if db_building is None:
        raise HTTPException(status_code=404, detail="Building not found")
    return db_building
