import os
from typing import Any

from dotenv import load_dotenv
import httpx

load_dotenv()

class EIA_API:
    """ Class for pulling data from the EIA API
    """
    def __init__(self):
        self.url_start: str = 'https://api.eia.gov/v2/'
        self.api_key: str = os.getenv('EIA_API_KEY')

        if self.api_key is None:
            print('No API key found for EIA in .env')
            raise SystemExit

    def electric_operational(self, params: dict[str, Any]) -> dict:
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
        r = httpx.get(url, params=params, timeout=10.0)
        if r.status_code != 200:
            print('Crap')
        print(r.json()['response']['data'])

if __name__ == '__main__':
    params = {
        'frequency': 'monthly',
        'data': [
            'generation'
        ],
        'start': '2025-01',
        'end': '2025-01',
        'offset': 0,
        'length': 5000
    }
    
    eia = EIA_API()
    eia.electric_operational(params)
