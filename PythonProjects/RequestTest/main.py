import requests
import pytest

url = 'https://api.pokemonbattle.ru/v2'
token = 'твой тренер токен'
header = {'Content-Type': 'application/json', 'trainer_token': token}
body_sozdanie_pokemona =  {"name": "generate","photo_id": -1}
body_izmenenie_pokemona = {
    "pokemon_id": "122962",
    "name": "python",
    "photo_id": 6
}
body_poimka_pokemona = {
    "pokemon_id": "122965"
}

response = requests.post(url = f'{url}/pokemons', headers = header, json = body_sozdanie_pokemona)
print(response.json())


response = requests.put(url = f'{url}/pokemons', headers = header, json = body_izmenenie_pokemona)
print(response.json())


response = requests.post(url = f'{url}/trainers/add_pokeball', headers = header, json = body_poimka_pokemona)
print(response.json())