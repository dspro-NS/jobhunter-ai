from database.crud import get_jobs
from scoring.score import score_job

jobs = get_jobs()

jobs = sorted(jobs, key=score_job, reverse=True)

for job in jobs[:20]:
    print(f"{score_job(job):3} | {job.company:12} | {job.title}")
    print(job.location)
    print(job.url)
    print("-" * 80)