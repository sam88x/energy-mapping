from sqlalchemy import create_engine
from sqlalchemy.orm import (DeclarativeBase, Mapped,
                            mapped_column, sessionmaker)

from core.config import config

engine = create_engine(config.db_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False,
                            bind=engine)

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)
