# address_controller.py
# Controller for Address endpoints

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.service.address_service import AddressService
from app.dto.address_dto import AddressCreateDTO, AddressUpdateDTO, AddressResponseDTO
from app.service.distance_service import DistanceService
from app.repository.address_repository import AddressRepository  # Import AddressRepository

router = APIRouter(prefix="/api/v1/addresses")

@router.post("/", response_model=AddressResponseDTO)
def create_address(dto: AddressCreateDTO, db: Session = Depends(get_db)):
    service = AddressService(AddressRepository(db), DistanceService())
    try:
        result = service.create_address(dto)
        db.commit()  # Commit the transaction
        return result
    except Exception as e:
        db.rollback()  # Rollback the transaction in case of an error
        raise HTTPException(status_code=500, detail=f"Failed to create address: {str(e)}")

@router.get("/", response_model=list[AddressResponseDTO])
def get_all_addresses(db: Session = Depends(get_db)):
    service = AddressService(AddressRepository(db), DistanceService())
    try:
        return service.get_all_addresses()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch addresses: {str(e)}")

@router.get("/nearby", response_model=list[AddressResponseDTO])
def get_nearby_addresses(center_lat: float, center_lon: float, max_km: float, db: Session = Depends(get_db)):
    service = AddressService(AddressRepository(db), DistanceService())
    try:
        return service.get_nearby_addresses(center_lat, center_lon, max_km)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch nearby addresses: {str(e)}")

@router.get("/{id}", response_model=AddressResponseDTO)
def get_address_by_id(id: int, db: Session = Depends(get_db)):
    service = AddressService(AddressRepository(db), DistanceService())
    try:
        return service.get_address_by_id(id)
    except ValueError as e:  # Custom exception for not found
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch address: {str(e)}")

@router.put("/{id}", response_model=AddressResponseDTO)
def update_address(id: int, dto: AddressUpdateDTO, db: Session = Depends(get_db)):
    service = AddressService(AddressRepository(db), DistanceService())
    try:
        return service.update_address(id, dto)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to update address: {str(e)}")

@router.delete("/{id}")
def delete_address(id: int, db: Session = Depends(get_db)):
    service = AddressService(AddressRepository(db), DistanceService())
    try:
        service.delete_address(id)
        return {"message": "Address deleted successfully."}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete address: {str(e)}")