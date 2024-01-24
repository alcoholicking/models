import requests

url = 'http://localhost:8080/wines?grape='
def get_wine_by_grapes(grape):

    url += grape
    return requests.get(url)