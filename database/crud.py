from database.db import Session
from database.models import Job
from utils.logger import logger
from database.company_models import Company


def save_jobs(board, jobs):
    session = Session()

    for job in jobs:

        existing = (
            session.query(Job)
            .filter_by(url=job["absolute_url"])
            .first()
        )

        if existing:
            continue

        session.add(
            Job(
                company=board,
                title=job["title"],
                location=job.get("location", {}).get("name", ""),
                url=job.get("absolute_url", ""),
                published_at=job.get("updated_at") or job.get("first_published"),
                job_id=job["id"],
                description=job.get("content", "")
            )
        )

    session.commit()
    session.close()

    logger.info(f"Saved jobs for {board}")

def get_jobs():
    session = Session()
    jobs = session.query(Job).all()
    session.close()
    return jobs



def add_company(name, careers_url, ats, board,country):

    session = Session()

    existing = (
        session.query(Company)
        .filter_by(careers_url=careers_url)
        .first()
    )

    if existing:
        session.close()
        return

    company = Company(
    name=name,
    careers_url=careers_url,
    ats=ats,
    board=board,
    country=country,
    active="Y"
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