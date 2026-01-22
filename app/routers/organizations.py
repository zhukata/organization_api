from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.organization import Organization, OrganizationCreate
from app.crud.organization import (
    create_organization,
    get_organizations,
    get_organization,
    get_organizations_by_building,
    get_organizations_by_activity,
    search_organizations_by_name,
    get_organizations_in_radius,
)
from app.database import get_db
from typing import List

router = APIRouter(prefix="/organizations", tags=["organizations"])


@router.post("/", response_model=Organization)
def create_new_organization(
    organization: OrganizationCreate,
    phone_numbers: List[str],
    activity_ids: List[int],
    db: Session = Depends(get_db),
):
    """
    Создать новую организацию.

    - **organization**: Данные для создания организации, включая имя и ID здания.
    - **phone_numbers**: Список номеров телефонов.
    - **activity_ids**: Список ID активностей, связанных с организацией.
    Возвращает созданную организацию с присвоенным ID.
    """
    return create_organization(db, organization, phone_numbers, activity_ids)


@router.get("/", response_model=list[Organization])
def read_organizations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Получить список всех организаций с пагинацией.

    - **skip**: Количество записей для пропуска (по умолчанию 0).
    - **limit**: Максимальное количество записей для возврата (по умолчанию 100).
    Возвращает список организаций.
    """
    return get_organizations(db, skip, limit)


@router.get("/{organization_id}", response_model=Organization)
def read_organization(organization_id: int, db: Session = Depends(get_db)):
    """
    Получить организацию по ID.

    - **organization_id**: Уникальный идентификатор организации.
    Возвращает организацию или 404, если не найдена.
    """
    db_organization = get_organization(db, organization_id)
    if db_organization is None:
        raise HTTPException(status_code=404, detail="Organization not found")
    return db_organization


@router.get("/by_building/{building_id}", response_model=list[Organization])
def read_organizations_by_building(building_id: int, db: Session = Depends(get_db)):
    """
    Получить список организаций по ID здания.

    - **building_id**: Уникальный идентификатор здания.
    Возвращает список организаций, расположенных в данном здании.
    """
    return get_organizations_by_building(db, building_id)


@router.get("/by_activity/{activity_id}", response_model=list[Organization])
def read_organizations_by_activity(activity_id: int, db: Session = Depends(get_db)):
    """
    Получить список организаций по ID активности.

    - **activity_id**: Уникальный идентификатор активности.
    Возвращает список организаций, связанных с данной активностью.
    """
    return get_organizations_by_activity(db, activity_id)


@router.get("/by_name/{name}", response_model=list[Organization])
def search_organizations(name: str, db: Session = Depends(get_db)):
    """
    Поиск организаций по имени.

    - **name**: Часть имени организации для поиска.
    Возвращает список организаций, чьи имена содержат указанную строку.
    """
    return search_organizations_by_name(db, name)


@router.get("/in_radius/", response_model=list[Organization])
def get_organizations_in_radius_endpoint(
    latitude: float, longitude: float, radius_km: float, db: Session = Depends(get_db)
):
    """
    Получить организации в заданном радиусе от точки.

    - **latitude**: Широта центральной точки.
    - **longitude**: Долгота центральной точки.
    - **radius_km**: Радиус поиска в километрах.
    Возвращает список организаций, находящихся в указанном радиусе.
    """
    return get_organizations_in_radius(db, latitude, longitude, radius_km)
