from collectors import COLLECTORS


def collect_all_jobs(companies):

    all_jobs = []

    for company in companies:

        ats = company.ats

        collector = COLLECTORS.get(ats)

        if collector is None:
            print(f"Skipping {company.name} (Unsupported ATS: {ats})")
            continue

        print(f"Collecting from {company.name} ({ats})")

        try:
            jobs = collector(company)

            all_jobs.extend(jobs)

        except Exception as e:
            print(f"{company.name}: {e}")

    return all_jobs