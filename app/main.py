from fastapi import FastAPI
from app.domains.weather.router import router as weather_router

app = FastAPI(
  title = "weather API",
  version = "1.0",
  description = "A RESTful API to fetch weather data with Redis and Postgresql ",
)



app.include_router(weather_router, prefix="/weather" , tags=["weather"])

@app.get("/")
def root():
  return {"message": "weather API is running!"}

