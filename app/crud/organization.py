from sqlalchemy.orm import Session
from app.models.organization import Organization, PhoneNumber
from app.models.activity import Activity
from app.models.building import Building
from app.schemas.organization import OrganizationCreate
from typing import List


def create_organization(
    db: Session,
    organization: OrganizationCreate,
    phone_numbers: List[str],
    activity_ids: List[int],
):
    db_organization = Organization(**organization.model_dump())
    db.add(db_organization)
    db.commit()
    db.refresh(db_organization)

    for phone in phone_numbers:
        db_phone = PhoneNumber(number=phone, organization_id=db_organization.id)
        db.add(db_phone)

    for activity_id in activity_ids:
        activity = db.query(Activity).filter(Activity.id == activity_id).first()
        if activity:
            db_organization.activities.append(activity)

    db.commit()
    db.refresh(db_organization)
    return db_organization


def get_organizations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Organization).offset(skip).limit(limit).all()


def get_organization(db: Session, organization_id: int):
    return db.query(Organization).filter(Organization.id == organization_id).first()


def get_organizations_by_building(db: Session, building_id: int):
    return db.query(Organization).filter(Organization.building_id == building_id).all()


def get_organizations_by_activity(db: Session, activity_id: int):
    activity = db.query(Activity).filter(Activity.id == activity_id).first()
    if not activity:
        return []

    def get_all_child_activity_ids(activity: Activity):
        child_ids = []
        for child in activity.children:
            child_ids.append(child.id)
            child_ids.extend(get_all_child_activity_ids(child))
        return child_ids

    all_activity_ids = [activity.id] + get_all_child_activity_ids(activity)
    organizations = []
    for act_id in all_activity_ids:
        orgs = (
            db.query(Organization)
            .join(Organization.activities)
            .filter(Activity.id == act_id)
            .all()
        )
        organizations.extend(orgs)

    return organizations


def search_organizations_by_name(db: Session, name: str):
    return db.query(Organization).filter(Organization.name.ilike(f"%{name}%")).all()


def get_organizations_in_radius(
    db: Session, latitude: float, longitude: float, radius_km: float
):
    from math import radians, cos, sin, sqrt, atan2

    R = 6371  # Earth radius in km

    def haversine(lat1, lon1, lat2, lon2):
        lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        return R * c

    buildings = db.query(Building).all()
    result = []

    for building in buildings:
        distance = haversine(latitude, longitude, building.latitude, building.longitude)
        if distance <= radius_km:
            orgs = (
                db.query(Organization)
                .filter(Organization.building_id == building.id)
                .all()
            )
            result.extend(orgs)

    return result
