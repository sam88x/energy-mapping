from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from db.schema import Base

class EIAElecPowerOperational(Base):
    """ Table for the EIA Electric Power Operational data
    """
    __tablename__ = 'eia_electric_power_operational'

    period: Mapped[datetime]
    location: Mapped[str]
    stateDescription: Mapped[str]
    sectorid: Mapped[str]
    sectorDescription: Mapped[str]
    fueltypeid: Mapped[str]
    fuelTypeDescription: Mapped[str]
