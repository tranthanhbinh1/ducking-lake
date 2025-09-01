from sqlalchemy import Column, String, DECIMAL, ARRAY, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Network(Base):
    __tablename__ = "networks"

    id = Column(String, primary_key=True)  # from API network_id
    name = Column(String, nullable=False)
    city = Column(String)
    country = Column(String(2))  # ISO country code
    latitude = Column(DECIMAL(10, 7))
    longitude = Column(DECIMAL(10, 7))
    company = Column(ARRAY(String))  # PostgreSQL array for companies
    href = Column(String)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

    def __repr__(self):
        return f"<Network(id='{self.id}', name='{self.name}', city='{self.city}')>"