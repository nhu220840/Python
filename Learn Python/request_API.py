# How to connect to an API using Python
import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    # print(response)

    # HTTPS response 200: means connect successful
    if response.status_code == 200:
        # convert data to json format (key: value) pairs (dictionary)
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Fail to retrieve data {response.status_code}")


pokemon_name = "ditto"
pokemon_info = get_pokemon_info(pokemon_name)

# using single quotes instead of double quotes in []
if pokemon_info:
    print(f"Name: {pokemon_info['name'].capitalize()}")
    print(f"ID: {pokemon_info['id']}")
    print(f"Height: {pokemon_info['height']}")
    print(f"Weight: {pokemon_info['weight']}")
