from pydantic import BaseModel, Field
from typing import Optional


class ActivityBase(BaseModel):
    name: str = Field(..., description="Название активности")
    parent_id: Optional[int] = Field(
        None, description="ID родительской активности (опционально)"
    )


class ActivityCreate(ActivityBase):
    pass


class Activity(ActivityBase):
    id: int = Field(..., description="Уникальный идентификатор активности")

    class Config:
        from_attributes = True
