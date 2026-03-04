# Service layer for Address operations.
# Contains business logic for managing addresses.

from app.utils.logger import get_logger
from app.repository.address_repository import AddressRepository
from app.dto.address_dto import AddressCreateDTO, AddressUpdateDTO
from app.entity.address_entity import Address
from app.service.distance_service import DistanceService

logger = get_logger(__name__)


class AddressService:
    def __init__(self, repository: AddressRepository, distance_service: DistanceService):
        """
        Initialize AddressService.

        Args:
            repository (AddressRepository): Data access layer.
            distance_service (DistanceService): Distance calculation service.
        """
        self.repository = repository
        self.distance_service = distance_service

    def create_address(self, dto: AddressCreateDTO):
        """
        Create a new address.

        Args:
            dto (AddressCreateDTO): Address creation data.

        Returns:
            Address: Newly created address.
        """
        address = Address(**dto.dict())

        saved_address = self.repository.save(address)

        logger.info(f"Address created with ID: {saved_address.id}")

        return saved_address

    def get_address_by_id(self, id: int):
        """
        Retrieve address by ID.

        Args:
            id (int): Address identifier.

        Returns:
            Address: Address entity.

        Raises:
            ValueError: If address not found.
        """
        address = self.repository.find_by_id(id)

        if not address:
            logger.warning(f"Address with ID {id} not found.")
            raise ValueError(f"Address with ID {id} not found.")

        return address

    def update_address(self, id: int, dto: AddressUpdateDTO):
        """
        Update an existing address.

        Args:
            id (int): Address identifier.
            dto (AddressUpdateDTO): Updated address fields.

        Returns:
            Address: Updated address entity.
        """
        address = self.get_address_by_id(id)

        for key, value in dto.dict(exclude_unset=True).items():
            setattr(address, key, value)

        updated_address = self.repository.save(address)

        logger.info(f"Address with ID {id} updated.")

        return updated_address

    def delete_address(self, id: int):
        """
        Delete address by ID.

        Args:
            id (int): Address identifier.
        """
        address = self.get_address_by_id(id)

        self.repository.delete(address)

        logger.info(f"Address with ID {id} deleted.")

    def get_all_addresses(self):
        """
        Retrieve all addresses.

        Returns:
            list[Address]: List of all stored addresses.
        """
        addresses = self.repository.find_all()

        logger.info("Fetched all addresses.")

        return addresses

    def get_nearby_addresses(self, center_lat: float, center_lon: float, max_km: float):
        """
        Retrieve addresses within a distance.

        Args:
            center_lat (float): Center latitude.
            center_lon (float): Center longitude.
            max_km (float): Maximum distance in kilometers.

        Returns:
            list[Address]: Nearby addresses.
        """
        all_addresses = self.repository.find_all()

        nearby_addresses = self.distance_service.filter_nearby(
            all_addresses,
            center_lat,
            center_lon,
            max_km
        )

        logger.info(
            f"Nearby search executed for center ({center_lat}, {center_lon}) within {max_km} km."
        )

        return nearby_addresses