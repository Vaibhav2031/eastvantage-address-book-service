# address_dto.py
# Data Transfer Object for Address

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class AddressDTO(BaseModel):
    id: int
    street: str
    city: str
    state: str
    zip_code: str

    class Config:
        orm_mode = True

class AddressCreateDTO(BaseModel):
    name: str
    street: str
    city: str
    latitude: float = Field(..., ge=-90, le=90, description="Latitude must be between -90 and 90")
    longitude: float = Field(..., ge=-180, le=180, description="Longitude must be between -180 and 180")

class AddressUpdateDTO(BaseModel):
    id: int
    name: Optional[str] = None
    street: Optional[str] = None
    city: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

class AddressResponseDTO(BaseModel):
    id: int
    name: str
    street: str
    city: str
    latitude: float
    longitude: float
    created_at: datetime

    class Config:
        orm_mode = True