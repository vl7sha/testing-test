import requests
import os
import json
# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values
# loading variables from .env file
load_dotenv()

token = os.getenv("MY_KEY")
name_repository = os.getenv("NAME_REPOSITORY")
name_owner = os.getenv("NAME_OWNER")
url = "https://api.github.com/user/repos"
json_headers = {
    'Authorization': token ,
    'Accept': 'application/vnd.github+json',
    'X-GitHub-Api-Version': '2022-11-28'
}

def test_create_repos():
    data_repository = {
        "name": name_repository,
        "description":"This is your first repo!",
        "homepage":"https://github.com",
        "private":"false",
        "is_template":"true"
    }

    r = requests.post(url = url, data = json.dumps(data_repository), headers = json_headers)
    assert 201 == r.status_code

def test_created_repos():
    page = 1
    while():
        new_url = url + f'"?page={page}"'
        r = requests.get(new_url, headers = json_headers)
        for i in r.json():
            if i['name'] == name_repository:
                assert True
        page = page + 1

def test_delete_repos():
    url_delete_repos = 'https://api.github.com/repos/' + str(name_owner) + '/' + str(name_repository)
    r = requests.delete(url_delete_repos, headers = json_headers)
    assert 204 == r.status_code
