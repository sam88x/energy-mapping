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
        
class EIAGeneratorCapacity(BaseModel):
    """ Pydantic class for validation of EIA
    operation-generator-capacity data
    """
    period: str
    stateid: str
    stateName: str
    sector: str
    sectorName: str
    entityid: str
    entityName: str | None
    plantid: str
    plantName: str
    generatorid: str
    technology: str
    energy_source_code: str | None
    energy_source_desc: str | None
    prime_mover_code: str | None
    balancing_authority_code: str | None
    balancing_authority_name: str | None
    status: str | None
    statusDescription: str | None
    latitude: str
    longitude: str
    nameplate_capacity_mw: str
    operating_year_month: str
    unit: str | None
    nameplate_capacity_mw_units: str | None

    @field_validator('period')
    @classmethod
    def to_datetime_period(cls, v: str) -> datetime:
        """ Convert period to datetime
        """
        try:
            return datetime.strptime(v, '%Y-%m')
        except ValueError:
            raise ValueError('Period is not of the format YYYY-mm')
        
    @field_validator('operating_year_month')
    @classmethod
    def to_datetime_op_time(cls, v: str) -> datetime:
        """ Convert operating_year_month to datetime
        """
        try:
            return datetime.strptime(v, '%Y-%m')
        except ValueError:
            raise ValueError('operating_year_month is not of the format YYYY-mm')
        
    @field_validator('latitude')
    @classmethod
    def to_float_lat(cls, v: str) -> float:
        """ Convert latitude to float
        """
        try:
            return float(v)
        except ValueError:
            raise ValueError('latitude cannot be turned to float')
        
    @field_validator('longitude')
    @classmethod
    def to_float_long(cls, v: str) -> float:
        """ Convert longitude to float
        """
        try:
            return float(v)
        except ValueError:
            raise ValueError('longitude cannot be turned to float')
        
    @field_validator('nameplate_capacity_mw')
    @classmethod
    def to_float_capacity(cls, v: str) -> float:
        """ Convert nameplate_capacity_mw to float
        """
        try:
            return float(v)
        except ValueError:
            raise ValueError('nameplate_capacity_mw cannot be turned to float')
