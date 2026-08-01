import requests


def get_jobs():
    url = "https://api.lever.co/v0/postings/netflix?mode=json"

    response = requests.get(url)

    return response.json()