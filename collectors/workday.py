import requests


def get_jobs(company):
    """
    company["board"] should contain the Workday tenant URL.

    Example:
    https://wd5.myworkdaysite.com/recruiting/company/jobs
    """

    url = company["board"]

    response = requests.get(url, timeout=20)
    response.raise_for_status()

    return response.json()