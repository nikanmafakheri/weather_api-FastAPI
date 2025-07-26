from pydantic import BaseSettings

class settings(BaseSettings):
  OPENWEATHER_API_KEY: str
  REDIS_HOST: str
  REDIS_PORT: int  
  
  class Config:
    env_file = ".env"


settings = settings()    