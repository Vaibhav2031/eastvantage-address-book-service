# Address Book Service

This is a FastAPI-based Address Book Service that provides RESTful APIs for managing addresses.

## Features
- Add and retrieve addresses
- Calculate distances between addresses (placeholder)

## Project Structure
```
app/
├── main.py               # Entry point for the application
├── config/settings.py    # Configuration settings
├── entity/               # Database entities
├── dto/                  # Data Transfer Objects
├── repository/           # Data Access Layer
├── service/              # Business Logic Layer
├── controller/           # API Endpoints
├── database/             # Database setup
```

## Requirements
- Python 3.13+

## Installation
1. Install `uv` if not already installed:
   ```bash
   pip install uv
   ```
2. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
3. Navigate to the project directory:
   ```bash
   cd eastvantage-address-book-service
   ```
4. Initialize the project (if not already initialized):
   ```bash
   uv init
   ```

## Running the Application
1. Sync dependencies:
   ```bash
   uv sync
   ```
2. Start the FastAPI server:
   ```bash
   uv run uvicorn app.main:app --reload
   ```

Server will start at:
- API Root: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Interactive API documentation: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Testing
Run tests using pytest:
```bash
pytest
```