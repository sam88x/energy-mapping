import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Config(BaseSettings):
    """ Config class to hold all configuration data. Some data
    is read from a .env file as needed.
    """
    app_name: str = 'energy-mapper'
    db_name: str = 'energy_map.sqlite3'
    eia_api_key: str = os.getenv('EIA_API_KEY')

    @property
    def db_url(self):
        return f'sqlite:///./{self.db_name}'

config = Config()
