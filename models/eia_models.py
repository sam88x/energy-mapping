from datetime import datetime
from pydantic import BaseModel, field_validator

class EIAElectricPowerOperational(BaseModel):
    period: str
    location: str
    stateDescription: str
    sectorid: str
    sectorDescription: str
    fueltypeid: str
    fuelTypeDescription: str

    @field_validator('period')
    @classmethod
    def to_datetime(cls, v) -> datetime:
        """ Convert period to datetime
        """
        try:
            return datetime.strptime(v, '%Y-%m')
        except ValueError:
            raise ValueError('Period is not of the format YYYY-mm')
