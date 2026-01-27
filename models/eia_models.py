from datetime import datetime
from typing import Literal

from pydantic import BaseModel, field_validator

class EIAEPOParams(BaseModel):
    """ PArameters class for EIA electrical-power-operational data
    (Incomplete)
    """
    frequency: Literal['monthly', 'annual', 'quarterly']
    data: list[str] = ['generation']
    start: str | None = None
    end: str | None = None
    offset: int
    length: int

    @field_validator('start', 'end')
    @classmethod
    def validate_dates(cls, v: str) -> str:
        for fmt in ['%Y-%m', '%Y']:
            try:
                datetime.strptime(v, fmt)
                FLAG = True
                break
            except:
                FLAG = False

        if FLAG:
            return v

        raise ValueError('Start and end must be in the format YYYY-mm or YYYY')

class EIAElectricPowerOperational(BaseModel):
    """ Pydantic class for validation of EIA
    electrical-power-operational data
    """
    period: str
    location: str
    stateDescription: str
    sectorid: str
    sectorDescription: str
    fueltypeid: str
    fuelTypeDescription: str

    @field_validator('period')
    @classmethod
    def to_datetime(cls, v: str) -> datetime:
        """ Convert period to datetime
        """
        try:
            return datetime.strptime(v, '%Y-%m')
        except ValueError:
            raise ValueError('Period is not of the format YYYY-mm')
