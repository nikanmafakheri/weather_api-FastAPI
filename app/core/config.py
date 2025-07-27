from pydantic import BaseSettings

class settings(BaseSettings):
  OPENWEATHER_API_KEY: str
  REDIS_HOST: str
  REDIS_PORT: int  
    
  POSTGRES_USER = str
  POSTGRES_PASSWORD = str 
  POSTGRES_DB = str
  POSTGRES_HOST = str
  POSTGRES_PORT = int
  
  class Config:
    env_file = ".env"


settings = settings()    