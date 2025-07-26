import httpx , json
from app.core.config import settings
from app.db.redis import redis_client


async def get_weather(city: str):
  cache_key = f"weather:{city.lower()}"
  cached = await redis_client.get(cache_key)
  
  
  if cached :
    return json.loads(cached)
  

  url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.OPENWEATHER_API_KEY}&units=metric"
  
  async with httpx.AsyncClient() as client:
    response = await client.get(url)
    data = response.json()
    
  result = {
    "city": city,
    "temperature": data["main"]["temp"],
    "description": data["weather"][0]["description"],
  }
  
  await redis_client.set(cache_key, json.dumps(result), ex=600)
  return result
