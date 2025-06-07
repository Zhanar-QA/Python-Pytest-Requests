import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '0fb0110d221b69ce0f67847ba37c2b90'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '33799'

def test_my_trainer():
    response_get = requests.get(url = f'{URL}/trainers', params= {'trainer_id': TRAINER_ID})
    assert response_get.json()["data"][0] ["trainer_name"] == 'Jenny Jenkins'