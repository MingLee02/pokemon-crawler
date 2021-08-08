import requests


def checkUrl(base_url):
    response = requests.get(base_url)
    if response.status_code == 200:
        return response
    return 'Error'

