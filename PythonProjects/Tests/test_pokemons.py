import requests
import pytest

url = 'https://api.pokemonbattle.ru/v2'
token = 'твой тренер токен'
header = {'Content-Type': 'application/json', 'trainer_token': token}
trainers_id = '7286'

def test_stasus_code():
    response = requests.get(url= f'{url}/trainers', params ={'trainer_id': trainers_id})
    assert response.status_code == 200