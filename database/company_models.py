from sqlalchemy import Column, Integer, String
from database.models import Base


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True)

    name = Column(String)
    careers_url = Column(String, unique=True)

    board = Column(String)   
    ats = Column(String)

    country = Column(String)

    active = Column(String)