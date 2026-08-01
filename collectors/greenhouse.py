import requests

def get_jobs(board_name):
    url = f"https://boards-api.greenhouse.io/v1/boards/{board_name}/jobs"

    response = requests.get(url)

    return response.json()