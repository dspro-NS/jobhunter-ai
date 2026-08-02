from database.db import Session
from database.models import JobModel
from schemas.job import Job
from utils.logger import logger
from database.company_models import Company


def save_jobs(jobs):
    session = Session()

    for job in jobs:

        existing = (
            session.query(JobModel)
            .filter_by(url=job.url)
            .first()
        )

        if existing:
            continue

        session.add(
            JobModel(
                company=job.company,
                title=job.title,
                location=job.location,
                url=job.url,
                published_at=job.posted_at,
                description=job.description,
            )
        )

    session.commit()
    session.close()

    logger.info(f"Saved {len(jobs)} jobs")

def get_jobs():
    session = Session()
    jobs = session.query(JobModel).all()
    session.close()
    return jobs

def add_company(name, careers_url, ats, board, country):

    session = Session()

    existing = (
        session.query(Company)
        .filter_by(careers_url=careers_url)
        .first()
    )

    if existing:
        existing.name = name
        existing.ats = ats
        existing.board = board
        existing.country = country
        existing.active = "Y"

        session.commit()
        session.close()
        return

    company = Company(
        name=name,
        careers_url=careers_url,
        ats=ats,
        board=board,
        country=country,
        active="Y",
    )

    session.add(company)

    session.commit()

    session.close()



def get_active_companies():
    session = Session()

    companies = (
        session.query(Company)
        .filter_by(active="Y")
        .all()
    )

    session.close()

    return companies