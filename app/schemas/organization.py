from pydantic import BaseModel, field_validator


class OrganizationBase(BaseModel):
    name: str
    building_id: int


class OrganizationCreate(OrganizationBase):
    pass


class Organization(OrganizationBase):
    id: int
    phone_numbers: list[str] = []
    activities: list[str] = []

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

    class Config:
        from_attributes = True
