from database.db import engine

from database.models import Base, JobModel
from database.company_models import Company

Base.metadata.create_all(engine)

print("Database initialized.")