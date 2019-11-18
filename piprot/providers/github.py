"""Functions to interact with github API."""
import json
import re
from io import StringIO

import requests

GITHUB_API_BASE = 'https://api.github.com'


def build_github_url(
    repo,
    branch=None,
    path='requirements.txt',
    token=None
):
    """Builds a URL to a file inside a Github repository."""
    repo = re.sub(r"^http(s)?://github.com/", "", repo).strip('/')

    # args come is as 'None' instead of not being provided
    if not path:
        path = 'requirements.txt'

    if not branch:
        branch = get_default_branch(repo)

    url = 'https://raw.githubusercontent.com/{}/{}/{}'.format(
        repo, branch, path
    )

    if token:
        url = '{}?token={}'.format(url, token)

    return url


def get_default_branch(repo):
    """Returns the name of the default branch of the repo."""
    url = "{}/repos/{}".format(GITHUB_API_BASE, repo)
    response = requests.get(url)
    if response.status_code == 200:
        api_response = json.loads(response.text)
        return api_response['default_branch']
    else:
        return 'master'


def get_requirements_file_from_url(url):
    """Fetches the requiremets from the url."""
    response = requests.get(url)

    if response.status_code == 200:
        return StringIO(response.text)
    else:
        return StringIO("")
