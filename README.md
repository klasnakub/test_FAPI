# Time API

Simple FastAPI application that provides current time information.

## Installation

```bash
pip install -r requirements.txt
```

## Running the API

```bash
python main.py
```

Or with uvicorn directly:
```bash
uvicorn main:app --reload
```

## API Endpoints

- `GET /` - Health check
- `GET /time` - Get current local time
- `GET /time/utc` - Get current UTC time

## Access the API

- API will run on: http://localhost:8000
- Interactive docs: http://localhost:8000/docs
- Alternative docs: http://localhost:8000/redoc

## Example Response

```json
{
  "current_time": "2024-01-15T14:30:45.123456",
  "formatted_time": "2024-01-15 14:30:45",
  "timestamp": 1705324245.123456
}
```
