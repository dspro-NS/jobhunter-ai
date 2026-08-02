from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class JobModel(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)
    company = Column(String)
    title = Column(String)
    location = Column(String)
    url = Column(String, unique=True)
    published_at = Column(String)
    job_id = Column(Integer, unique=True)
    