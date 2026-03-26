from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DB_HOST: str
    DB_NAME: str
    DB_PORT: int
    DB_USERNAME: str
    DB_PASS: str

    @property
    def DB_URL_psycopg(self):
        # synchrounous
        # postgresql+psycopg://USER:PASSWORD@HOST:PORT/DATABASE
        return f"postgresql+psycopg://{self.DB_USERNAME}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()