from discovery.discover import discover_companies
from collectors.manager import collect_all_jobs
from database.db import Session
from database.crud import add_company, get_active_companies, insert_jobs

def main():
    companies = discover_companies()
    for company in companies:
    add_company(
        name=company["name"],
        careers_url=company["careers_url"],
        board=company["board"],
        ats=company["ats"],
        country="India",
    )

    db_companies = get_active_companies()

    jobs = collect_all_jobs(db_companies)
    db = Session()

    insert_jobs(db, jobs)

    db.close()
    print(f"Companies: {len(companies)}")
    print(f"Jobs: {len(jobs)}")


if __name__ == "__main__":
    main()


