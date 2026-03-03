# address_controller.py
# Controller for Address endpoints

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.service.address_service import AddressService
from app.dto.address_dto import AddressCreateDTO, AddressUpdateDTO, AddressResponseDTO
from app.service.distance_service import DistanceService

router = APIRouter(prefix="/api/v1/addresses")

@router.post("/", response_model=AddressResponseDTO)
def create_address(dto: AddressCreateDTO, db: Session = Depends(get_db)):
    service = AddressService(AddressRepository(db), DistanceService())
    return service.create_address(dto)

@router.get("/", response_model=list[AddressResponseDTO])
def get_all_addresses(db: Session = Depends(get_db)):
    service = AddressService(AddressRepository(db), DistanceService())
    return service.get_all_addresses()

@router.get("/{id}", response_model=AddressResponseDTO)
def get_address_by_id(id: int, db: Session = Depends(get_db)):
    service = AddressService(AddressRepository(db), DistanceService())
    return service.get_address_by_id(id)

@router.put("/{id}", response_model=AddressResponseDTO)
def update_address(id: int, dto: AddressUpdateDTO, db: Session = Depends(get_db)):
    service = AddressService(AddressRepository(db), DistanceService())
    return service.update_address(id, dto)

@router.delete("/{id}")
def delete_address(id: int, db: Session = Depends(get_db)):
    service = AddressService(AddressRepository(db), DistanceService())
    service.delete_address(id)
    return {"message": "Address deleted successfully."}

@router.get("/nearby", response_model=list[AddressResponseDTO])
def get_nearby_addresses(center_lat: float, center_lon: float, max_km: float, db: Session = Depends(get_db)):
    service = AddressService(AddressRepository(db), DistanceService())
    return service.get_nearby_addresses(center_lat, center_lon, max_km)