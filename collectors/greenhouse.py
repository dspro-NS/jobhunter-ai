import requests

from schemas.job import Job


def get_jobs(company):
    """
    Fetch all jobs from a Greenhouse board and convert them
    into the internal Job schema.
    """

    url = f"https://boards-api.greenhouse.io/v1/boards/{company.board}/jobs"

    response = requests.get(url, timeout=20)
    response.raise_for_status()

    data = response.json()
    print(Job)
    print(Job.__module__)
    print(Job.__annotations__)
    jobs = []

    for item in data.get("jobs", []):

        jobs.append(
            Job(
                title=item.get("title", ""),
                company=company.name,
                location=item.get("location", {}).get("name", ""),
                url=item.get("absolute_url", ""),
                description=item.get("content", ""),
                published_at=item.get("updated_at") or item.get("first_published"),
                source="greenhouse",
            )
        )

    return jobs