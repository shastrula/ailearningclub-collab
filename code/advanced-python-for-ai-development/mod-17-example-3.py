from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    model_path: str = 'model.pkl'
    batch_size: int = 32
    debug: bool = False
    
    class Config:
        env_file = '.env'

settings = Settings()