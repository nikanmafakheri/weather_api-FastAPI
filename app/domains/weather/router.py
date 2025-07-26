from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_weather():
  return {"msg": "weather endpoint"}
