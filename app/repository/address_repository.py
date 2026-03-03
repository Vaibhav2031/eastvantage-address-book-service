# address_repository.py
# Repository for Address entity

from sqlalchemy.orm import Session
from app.entity.address_entity import Address

class AddressRepository:
    def __init__(self, db: Session):
        self.db = db

    def save(self, address: Address):
        self.db.add(address)
        self.db.commit()
        self.db.refresh(address)
        return address

    def find_by_id(self, id: int):
        return self.db.query(Address).filter(Address.id == id).first()

    def find_all(self):
        return self.db.query(Address).all()

    def update(self, address: Address):
        self.db.merge(address)
        self.db.commit()
        return address

    def delete(self, address: Address):
        self.db.delete(address)
        self.db.commit()