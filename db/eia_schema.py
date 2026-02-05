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

class EIAOperationalGeneratorCapacity(Base):
    __tablename__ = 'eia_operational_generator_capacity'

    period: Mapped[datetime]
    stateid: Mapped[str]
    stateName: Mapped[str]
    sector: Mapped[str]
    sectorName: Mapped[str]
    entityid: Mapped[str]
    entityName: Mapped[str | None]
    plantid: Mapped[str]
    plantName: Mapped[str]
    generatorid: Mapped[str]
    technology: Mapped[str]
    energy_source_code: Mapped[str | None]
    energy_source_desc: Mapped[str | None]
    prime_mover_code: Mapped[str | None]
    balancing_authority_code: Mapped[str | None]
    balancing_authority_name: Mapped[str | None]
    status: Mapped[str | None]
    statusDescription: Mapped[str | None]
    latitude: Mapped[float]
    longitude: Mapped[float]
    nameplate_capacity_mw: Mapped[float]
    operating_year_month: Mapped[datetime]
    unit: Mapped[str | None]
    nameplate_capacity_mw_units: Mapped[str | None]