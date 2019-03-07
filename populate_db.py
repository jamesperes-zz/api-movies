import json
from flask import url_for
import requests

with open('telecine_dataset.json') as json_file:  
    data = json.load(json_file)
    for movie in data['movies']:
        r = requests.post("http://127.0.0.1:5000/v1/movies/register", json=movie)