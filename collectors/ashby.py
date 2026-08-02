import requests


def get_jobs(company):

    url = "https://jobs.ashbyhq.com/api/non-user-graphql"

    payload = {
        "operationName": "ApiJobBoardWithTeams",
        "variables": {
            "organizationHostedJobsPageName": company["board"]
        },
        "query": ""
    }

    response = requests.post(url, json=payload, timeout=20)
    response.raise_for_status()

    return response.json()