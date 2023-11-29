import requests
import random

# Open the necessary file containing a list of the favourite Pokémon.
with open('fav-pokemon.txt', 'r') as file:
    pokemon_list = [line.strip() for line in file]

# Using the `random` import library to sample six Pokémon from that list.
selected_pokemons = random.sample(pokemon_list, 6)

# Print a new line at the start of the code to improve formatting.
print("\n")

# Iterate over the selected Pokémon names.
for pokemon_name in selected_pokemons:
    # Dependent on the information within the list, the name is converted into
    # lowercase to better work with the API URL, and the link is constructed.
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}'

    # Send the 'GET' request to the API.
    response = requests.get(url)

    # Check to see if the request was successful.
    if response.status_code == 200:
        # Parse the JSON response.
        data = response.json()

        # Extract the Pokémon name and the types from the response.
        name = data['name']
        types = [t['type']['name'] for t in data['types']]
        abilities = [a['ability']['name'] for a in data['abilities']]
        height = data['height']
        weight = data['weight']

        # Display the Pokémon information, capitalising the start of the name.
        print(f"Pokémon: {name.capitalize()}")
        print(f"Type(s): {', '.join(types).capitalize()}")
        print(f"Abilities: {', '.join(abilities).capitalize()}")
        print(f"Weight: {weight}g")
        print(f"Height: {height}m")
        print("\n")
    else:
        # Display an error message if the request fails.
        print(f"Failed to retrieve data for {pokemon_name}.")
