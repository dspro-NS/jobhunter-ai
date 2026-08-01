from preprocessing.location import is_india_job
from scoring.relevance import is_relevant


def filter_jobs(jobs):
    filtered = []

    for job in jobs:

        if not is_india_job(job.location):
            continue

        if not is_relevant(job.title):
            continue

        filtered.append(job)

    return filtered