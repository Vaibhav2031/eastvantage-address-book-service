# main.py
# Entry point for the FastAPI application

import json
from fastapi import FastAPI
from app.controller.address_controller import router as address_router
from app.database.base import Base
from app.database.session import engine, SessionLocal
from app.entity.address_entity import Address
from app.repository.address_repository import AddressRepository
from app.utils.logger import get_logger, setup_logger  # Import AddressRepository

setup_logger()

logger = get_logger(__name__)

logger.info("Application starting")

app = FastAPI()

app.include_router(address_router)

# Create all tables
Base.metadata.create_all(bind=engine)

# Load initial data from address.json
with open("app/resources/address.json", "r") as file:
    data = json.load(file)
    db = SessionLocal()
    try:
        for record in data:
            address = Address(**record)
            db.add(address)
        db.commit()
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Address Book Service!"}