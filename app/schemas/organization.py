from pydantic import BaseModel, field_validator, Field, ConfigDict


class OrganizationBase(BaseModel):
    name: str = Field(description="Название организации")
    building_id: int = Field(description="ID здания, где расположена организация")


class OrganizationCreate(OrganizationBase):
    pass


class Organization(OrganizationBase):
    id: int = Field(description="Уникальный идентификатор организации")
    phone_numbers: list[str] = Field(
        default_factory=list, description="Список номеров телефонов организации"
    )
    activities: list[str] = Field(
        default_factory=list, description="Список названий активностей организации"
    )

    @field_validator("phone_numbers", mode="before")
    @classmethod
    def validate_phone_numbers(cls, v):
        if isinstance(v, list):
            return [
                phone.number if hasattr(phone, "number") else str(phone) for phone in v
            ]
        return v

    @field_validator("activities", mode="before")
    @classmethod
    def validate_activities(cls, v):
        if isinstance(v, list):
            return [
                activity.name if hasattr(activity, "name") else str(activity)
                for activity in v
            ]
        return v

    model_config = ConfigDict(from_attributes=True)
