from pydantic import BaseModel, Field


class BuildingBase(BaseModel):
    address: str = Field(..., description="Адрес здания")
    latitude: float = Field(..., description="Широта здания")
    longitude: float = Field(..., description="Долгота здания")


class BuildingCreate(BuildingBase):
    pass


class Building(BuildingBase):
    id: int = Field(..., description="Уникальный идентификатор здания")

    class Config:
        from_attributes = True
