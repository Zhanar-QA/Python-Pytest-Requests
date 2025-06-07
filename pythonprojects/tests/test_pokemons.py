import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '0fb0110d221b69ce0f67847ba37c2b90'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '33799'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

