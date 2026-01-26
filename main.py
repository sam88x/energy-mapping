from core.config import config
from data_collection.eia import EIA_API

def test_eia_pull() -> None:
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
    data = eia.electric_operational(params)
    print(data[0])

def main():
    test_eia_pull()
    #print(config)

if __name__ == "__main__":
    main()
