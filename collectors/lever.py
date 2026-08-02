import requests

def get_jobs(company):

    url = f"https://api.lever.co/v0/postings/{company['board']}?mode=json"

    response = requests.get(url, timeout=20)
    response.raise_for_status()

    return response.json()