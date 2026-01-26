from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

engine = create_engine('')

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

class EIAElecPowerOperational(Base):
    __tablename__ = 'eia_electric_power_operational'

    period: Mapped[datetime]
    location: Mapped[str]
    stateDescription: Mapped[str]
    sectorid: Mapped[str]
    sectorDescription: Mapped[str]
    fueltypeid: Mapped[str]
    fuelTypeDescription: Mapped[str]
