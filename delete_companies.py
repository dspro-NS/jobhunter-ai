from database.db import Session
from database.company_models import Company

session = Session()

session.query(Company).delete()

session.commit()
session.close()

print("Companies deleted.")