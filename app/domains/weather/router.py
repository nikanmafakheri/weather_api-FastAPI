from fastapi import APIRouter , Query 

router = APIRouter()

@router.get("/")
def get_weather(city : str = Query(..., description="City name to get weather for ")):
  return {
  "city": city,
  "temperature" : 30,
  "description":"(dummy data)"
}
