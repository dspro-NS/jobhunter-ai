from discovery.discover import discover_companies
from database.crud import add_company, get_active_companies, save_jobs
from collectors.manager import collect_all_jobs


def main():

    print("\n===== DISCOVERY =====")
    companies = discover_companies()
    print(companies)

    print("\n===== SAVING COMPANIES =====")
    for company in companies:
        add_company(
            name=company["name"],
            careers_url=company["careers_url"],
            ats=company["ats"],
            board=company["board"],
            country="India",
        )

    print("\n===== DATABASE =====")
    db_companies = get_active_companies()
    print(f"Companies in DB: {len(db_companies)}")

    for c in db_companies:
        print(c.name, c.ats, c.board)

    print("\n===== COLLECTORS =====")
    jobs = collect_all_jobs(db_companies)
    print(f"Collected {len(jobs)} jobs")

    if jobs:
        print(jobs[0])

    print("\n===== SAVE JOBS =====")
    save_jobs(jobs)

    print("\nPipeline completed successfully!")


if __name__ == "__main__":
    main()