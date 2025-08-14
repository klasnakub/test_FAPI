from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI(title="Time API", description="Simple API to get current time")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Time API is running"}

@app.get("/time")
async def get_time():
    current_time = datetime.now()
    return {
        "current_time": current_time.isoformat(),
        "formatted_time": current_time.strftime("%Y-%m-%d %H:%M:%S"),
        "timestamp": current_time.timestamp()
    }

@app.get("/time/utc")
async def get_utc_time():
    from datetime import timezone
    utc_time = datetime.now(timezone.utc)
    return {
        "utc_time": utc_time.isoformat(),
        "formatted_utc_time": utc_time.strftime("%Y-%m-%d %H:%M:%S UTC"),
        "utc_timestamp": utc_time.timestamp()
    }
