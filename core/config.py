import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Config(BaseSettings):
    app_name: str = 'energy-mapper'
    db_name: str = 'energy_map.sqlite3'
    eia_api_key: str = os.getenv('EIA_API_KEY')

    @property
    def db_url(self):
        return f'sqlite:///./{self.db_name}'

config = Config()
