# Repository for Address entity
# Handles database operations for Address.

from sqlalchemy.orm import Session
from app.entity.address_entity import Address


class AddressRepository:
    def __init__(self, db: Session):
        """
        Initialize repository with database session.

        Args:
            db (Session): SQLAlchemy database session.
        """
        self.db = db

    def save(self, address: Address):
        """
        Save or update an address in the database.

        Args:
            address (Address): Address entity to persist.

        Returns:
            Address: Saved address with updated fields.
        """
        self.db.add(address)
        self.db.flush()
        self.db.refresh(address)
        return address

    def find_by_id(self, id: int):
        """
        Retrieve address by ID.

        Args:
            id (int): Address identifier.

        Returns:
            Address | None: Address if found, otherwise None.
        """
        return self.db.query(Address).filter(Address.id == id).first()

    def find_all(self):
        """
        Retrieve all addresses.

        Returns:
            list[Address]: List of all stored addresses.
        """
        return self.db.query(Address).all()

    def delete(self, address: Address):
        """
        Remove address from database.

        Args:
            address (Address): Address entity to delete.
        """
        self.db.delete(address)