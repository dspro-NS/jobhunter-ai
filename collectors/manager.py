from collectors.greenhouse import get_jobs as greenhouse_jobs
from config.companies import GREENHOUSE_BOARDS
def collect_all_jobs():

    all_jobs = []

    greenhouse_boards = [
        "stripe",
        "databricks",
        "airbnb",
        "figma",
    ]

    for board in GREENHOUSE_BOARDS:

        try:
            jobs = greenhouse_jobs(board)

            if "jobs" in jobs:
                all_jobs.extend(jobs["jobs"])

                print(f"{board}: {len(jobs['jobs'])} jobs")

        except Exception as e:
            print(board, e)

    return all_jobs