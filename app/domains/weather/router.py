from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import SessionLocal
from app.domains.weather.schemas import WeatherResponse
from app.services.weather_service import get_weather

router = APIRouter()

async def get_db():
    async with SessionLocal() as session:
        yield session

@router.get("/", response_model=WeatherResponse)
async def weather(
    city: str = Query(..., description="City name to get weather for"),
    db: AsyncSession = Depends(get_db),
):
    return await get_weather(city, db)

