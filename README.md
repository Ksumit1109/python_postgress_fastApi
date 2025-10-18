# Python FastAPI Project

A simple FastAPI web application with file upload functionality.

## Project Structure

```
Python/
├── main.py              # Main FastAPI application
├── app.py               # Additional application file
├── venv/                # Virtual environment
├── README.md            # This file
└── requirements.txt     # Project dependencies
```

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Setup Instructions

### 1. Clone or Download the Project

```bash
# If using git
git clone <repository-url>
cd Python

# Or simply navigate to the project directory
cd path/to/your/Python/project
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
# Install required packages
pip install fastapi uvicorn python-multipart

# Or install from requirements.txt (if available)
pip install -r requirements.txt
```

### 4. Run the Application

```bash
# Run the FastAPI application
python main.py

# Or using uvicorn directly
uvicorn main:app --reload
```

The application will be available at: `http://localhost:8000`

## API Endpoints

### GET /
- **Description**: Welcome page
- **Response**: `{"message": "Welcome to main page user"}`

### GET /contact
- **Description**: Contact page
- **Response**: `{"Message": "Welcome to Contact page"}`

### POST /upload
- **Description**: File upload endpoint
- **Parameters**: `files` (list of uploaded files)
- **Response**: `{"status": "File received"}`

## API Documentation

Once the server is running, you can access:

- **Interactive API docs (Swagger UI)**: `http://localhost:8000/docs`
- **Alternative API docs (ReDoc)**: `http://localhost:8000/redoc`

## Development

### Virtual Environment Management

```bash
# Activate virtual environment
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Deactivate virtual environment
deactivate

# Remove virtual environment (if needed)
rm -rf venv  # macOS/Linux
rmdir /s venv  # Windows
```

### Adding New Dependencies

```bash
# Install new package
pip install package-name

# Save dependencies to requirements.txt
pip freeze > requirements.txt
```

### Running in Development Mode

```bash
# Run with auto-reload for development
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Troubleshooting

### Common Issues

1. **Command not found error when activating venv**
   - Make sure you're using the correct path separator (`\` for Windows, `/` for Unix)
   - Ensure you're in the correct directory

2. **Module not found errors**
   - Make sure the virtual environment is activated
   - Install required dependencies with `pip install`

3. **Port already in use**
   - Change the port: `uvicorn main:app --reload --port 8001`
   - Or kill the process using the port

### Getting Help

- Check the [FastAPI documentation](https://fastapi.tiangolo.com/)
- Review the [Uvicorn documentation](https://www.uvicorn.org/)

## License

This project is open source and available under the [MIT License](LICENSE).
