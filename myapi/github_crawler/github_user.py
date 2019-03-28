import requests


github_scraper_url = 'https://api.github.com/users/'


def get_github_user_data(username):
    response = requests.get(github_scraper_url + username)

    return response.json()
