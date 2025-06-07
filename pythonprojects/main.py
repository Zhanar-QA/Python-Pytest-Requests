import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '0fb0110d221b69ce0f67847ba37c2b90'
HEADER = {'Content-Type': 'application/json','trainer_token': TOKEN}
body_create= {
   
    "name": "generate",
    "photo_id": 132
}
response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print (response_create.text)

message = response_create.json() ['message']
print (message)

body_change = {
    "pokemon_id": "332806",
    "name": "Bestie",
    "photo_id": 2
}
response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print (response_change.text)

body_catch = {
  "message": "Покемон пойман в покебол",
  "pokemon_id": "332806"
}
response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.text)