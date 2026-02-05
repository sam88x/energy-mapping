from core.config import config
from data_collection.eia import EIA_API
from db.schema import Base, engine
from db import eia_schema
from display.create_map import generate_heat_map
import warnings
import pandas as pd

def test_eia_pull() -> None:
    states = [
        "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", 
        "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
        "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
        "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
        "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
    ]
    
    data = pd.DataFrame()

    for state in states:
        params = { 
            'frequency': 'monthly',
            'start': '2025-01',
            'end': '2025-01',
            'state_code': state,
            'offset': 0,
            'length': 5000
        }   
        
        eia = EIA_API()
        # data = eia.electric_operational(params)
        # print(data[0])

        state_data = pd.DataFrame(eia.get_generators_by_state(params))
        state_data = state_data[state_data['sector'] == 'electric-utility']
        state_data = state_data[['latitude', 'longitude', 'nameplate-capacity-mw', 'plantName', 'technology']]
        data = pd.concat([data, state_data])
        
    plot_df = data
    for col in plot_df.columns[:3]:
        plot_df[col] = plot_df[col].astype('float64')

    generate_heat_map(plot_df, 'nameplate-capacity-mw', 'plantName', 'technology')

def main():
    # Set up db
    Base.metadata.create_all(bind=engine)

    test_eia_pull()
    #print(config)

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    main()
