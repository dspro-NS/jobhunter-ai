from preprocessing.location import is_india_job
from scoring.relevance import is_relevant
from config.company_scores import COMPANY_SCORES


def score_job(job):

    if not is_india_job(job.location):
        return 0

    if not is_relevant(job.title):
        return 0

    score = COMPANY_SCORES.get(job.company.lower(), 40)

    location = job.location.lower()
    title = job.title.lower()

    if "remote" in location:
        score += 15

    if "staff" in title:
        score += 20
    elif "senior" in title:
        score += 10
    elif "lead" in title:
        score += 8

    return score