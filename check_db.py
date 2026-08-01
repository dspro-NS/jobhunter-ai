from database.crud import get_jobs
from scoring.score import score_job

jobs = get_jobs()

for job in jobs:

    score = score_job(job)

    if score == 0:
        continue

    print("=" * 100)
    print(f"Score     : {score}")
    print(f"Company   : {job.company}")
    print(f"Title     : {job.title}")
    print(f"Location  : {job.location}")
    print(f"URL       : {job.url}")
    print(f"Published : {job.published_at}")

    print("\nDescription:\n")
    print(job.description[:500])      # First 500 characters
    print("=" * 100)