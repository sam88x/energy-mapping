import os
from typing import Any

import httpx
from pydantic import ValidationError
from sqlalchemy import insert

from core.config import config
from db.eia_schema import EIAElecPowerOperational as EEPO_db
from db.schema import SessionLocal
from models.eia_models import EIAElectricPowerOperational as EEPO_model

class EIA_API:
    """ Class for pulling data from the EIA API
    """
    def __init__(self):
        self.url_start: str = 'https://api.eia.gov/v2/'
        self.api_key: str = config.eia_api_key

        if self.api_key is None:
            print('No API key found for EIA in .env')
            raise SystemExit

    def electric_operational(self, params: dict[str, Any]) -> list[EEPO_model]:
        """ Data from the electricity/electric-power-operational-data
        endpoint.

        Example params:
            params = {
                'frequency': 'monthly',
                'data': [
                    'generation'
                ],
                'start': '2025-01',
                'end': '2025-12',
                'offset': 0,
                'length': 5000
            }
        """
        route = 'electricity/electric-power-operational-data/data'
        url = f'{self.url_start}{route}'
        params['api_key'] = self.api_key

        # Need to figure out if loop is needed for the offset/length params
        r = httpx.get(url, params=params, timeout=None)
        if r.status_code != 200:
            print('Crap')
        raw_data = r.json()['response']['data']

        # Validate Data
        try:
            data = [EEPO_model(**i) for i in raw_data]
        except ValidationError as err:
            for item in err.errors():
                loc = '.'.join(item['loc']) if len(item['loc']) > 1 \
                        else item['loc'][0]
                print(f'{loc} - {item["msg"]}')

        with SessionLocal() as session:
            for item in data:
                session.add(EEPO_db(**item.model_dump()))
                session.commit()
        
        return raw_data
