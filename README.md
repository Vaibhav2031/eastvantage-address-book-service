# Address Book Service

This is a FastAPI-based Address Book Service that provides RESTful APIs for managing addresses.

## Features
- Add and retrieve addresses
- Calculate distances between addresses (placeholder)

## Project Structure
```
eastvantage-address-book-service/
│
├── app/                        # Application source code
│   ├── main.py                 # FastAPI application entry point
│   │
│   ├── config/                 # Application configuration
│   │
│   ├── controller/             # API controllers (FastAPI routers)
│   │
│   ├── service/                # Business logic layer
│   │
│   ├── repository/             # Data access layer (database operations)
│   │
│   ├── entity/                 # SQLAlchemy models (database entities)
│   │
│   ├── dto/                    # Data transfer objects (Pydantic schemas)
│   │
│   ├── database/               # Database configuration and session management
│   │
│   ├── utils/                  # Utility modules (e.g., logging)
│   │
│   └── resources/              # Additional resources or configurations
│
├── tests/                      # Unit and integration tests
│   └── test_address_api.py
│
├── logs/                       # Application logs
│   └── app.log
│
├── pytest.ini                  # Pytest configuration
├── pyproject.toml              # Project dependencies and metadata (uv)
├── uv.lock                     # Dependency lock file
├── .gitignore                  # Git ignore rules
├── .python-version             # Python version configuration
├── README.md                   # Project documentation
└── test.db                     # SQLite test database
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
uv run pytest
```