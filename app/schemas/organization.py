from pydantic import BaseModel
from typing import List


class OrganizationBase(BaseModel):
    name: str
    building_id: int


class OrganizationCreate(OrganizationBase):
    pass


class Organization(OrganizationBase):
    id: int
    phone_numbers: List[str] = []
    activities: List[str] = []

    class Config:
        from_attributes = True
