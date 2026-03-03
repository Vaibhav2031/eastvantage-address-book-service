# address_service.py
# Service layer for Address operations

import logging
from app.repository.address_repository import AddressRepository
from app.dto.address_dto import AddressCreateDTO, AddressUpdateDTO
from app.entity.address_entity import Address
from app.service.distance_service import DistanceService

logger = logging.getLogger(__name__)

class AddressService:
    def __init__(self, repository: AddressRepository, distance_service: DistanceService):
        self.repository = repository
        self.distance_service = distance_service

    def create_address(self, dto: AddressCreateDTO):
        address = Address(**dto.dict())
        try:
            saved_address = self.repository.save(address)
            logger.info(f"Address created with ID: {saved_address.id}")
            return saved_address
        except Exception as e:
            logger.error(f"Failed to create address: {e}")
            raise

    def get_address_by_id(self, id: int):
        try:
            address = self.repository.find_by_id(id)
            if not address:
                logger.warning(f"Address with ID {id} not found.")
                raise ValueError(f"Address with ID {id} not found.")
            return address
        except Exception as e:
            logger.error(f"Failed to fetch address by ID {id}: {e}")
            raise

    def update_address(self, id: int, dto: AddressUpdateDTO):
        try:
            address = self.get_address_by_id(id)
            for key, value in dto.dict(exclude_unset=True).items():
                setattr(address, key, value)
            updated_address = self.repository.save(address)
            logger.info(f"Address with ID {id} updated.")
            return updated_address
        except Exception as e:
            logger.error(f"Failed to update address with ID {id}: {e}")
            raise

    def delete_address(self, id: int):
        try:
            address = self.get_address_by_id(id)
            self.repository.delete(address)
            logger.info(f"Address with ID {id} deleted.")
        except Exception as e:
            logger.error(f"Failed to delete address with ID {id}: {e}")
            raise

    def get_nearby_addresses(self, center_lat: float, center_lon: float, max_km: float):
        try:
            all_addresses = self.repository.find_all()
            nearby_addresses = self.distance_service.filter_nearby(all_addresses, center_lat, center_lon, max_km)
            logger.info(f"Nearby search executed for center ({center_lat}, {center_lon}) within {max_km} km.")
            return nearby_addresses
        except Exception as e:
            logger.error(f"Failed to execute nearby search: {e}")
            raise