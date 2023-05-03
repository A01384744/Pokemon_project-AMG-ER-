import requests
import random

# Fetch Data

# Ask the user to enter the name of a Pokémon and store it as pokemon1_name.
pokemon1_name = input("Enter the name of a Pokémon (without caps): ")
print('--------------------------------------------------------------------------------------------')

# URL to access the Pokémon data, f-string is used to insert the pokemon1_name into the URL.
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon1_name}"
print(f'{pokemon1_name} stats:')

# Send a GET request to the PokeAPI using the URL, and store the response in the "response" variable.
response = requests.get(url)

# Check if the response status code is equal to 200 (successful).
if response.status_code == 200:
    # Convert the response to a Python object and extract the HP and weight of the Pokémon.
    data = response.json()
    hp = data["stats"][0]["base_stat"]
    weight = data["weight"]
    # Print out the name, HP, and weight of the Pokémon entered by the user.
    print(f"{pokemon1_name}'s HP is {hp} and its weight is {weight}.")
else:
    # If the response status code is not equal to 200, print an error message.
    print("Could not get information about the Pokémon.")

print('-----------------------------------------------------------------------------------------------------')

# Fetch Moves

# Send another GET request to the PokeAPI to fetch the moves of the Pokémon.
response = requests.get(url)

# Check if the response status code is equal to 200 (successful).
if response.status_code == 200:
    # Convert the response to a Python object and extract the moves of the Pokémon.
    data = response.json()
    moves_list = [move['move']['name'] for move in data['moves'][:5]]
    # Print out the name and moves of the Pokémon entered by the user.
    print(f"{pokemon1_name}'s moves are: {', '.join(moves_list)}.")
else:
    # If the response status code is not equal to 200, print an error message.
    print("Could not get information about the Pokémon.")

print('----------------------------------------------------------------------------------------------')

# Count Pokémon

# Send a GET request to the Pokemon API's Pokemon resource and store the response in the "response" variable.
response = requests.get("https://pokeapi.co/api/v2/pokemon/")

# Check if the response status code is equal to 200 (successful).
if response.status_code == 200:
    # Convert the response to a Python object and extract the "count" attribute, which tells us how many Pokémon exist.
    data = response.json()
    count = data["count"]
    print(f"There are {count} Pokémon in total.")
else:
    # If the response status code is not equal to 200, print an error message.
    print("Could not find information about the Pokémon.")

print('--------------------------------------------------------------------------------------')

# HP Fight

# Get a random Pokémon ID
random_pokemon_id = random.randint(1, count)

url = f"https://pokeapi.co/api/v2/pokemon/{random_pokemon_id}"
response = requests.get(url)

# Check if the response status code is equal to 200 (successful).
if response.status_code == 200:
    data = response.json()
    pokemon_name = data["name"]
    # Get the HP of the random Pokémon.
   
    random_pokemon_hp = data["stats"][0]["base_stat"]

    print(f"The random Pokémon is: {pokemon_name}")
    print(f"{pokemon_name}'s HP is: {random_pokemon_hp}, and {pokemon1_name}'s HP is: {hp}")

    if random_pokemon_hp > hp:
        print(f"{pokemon_name} is healthier than {pokemon1_name}.")
    elif random_pokemon_hp < hp:
        print(f"{pokemon1_name} is healthier than {pokemon_name}!")
    else:
        print(f"Both {pokemon1_name} and {pokemon_name} have the same HP.")
else:
    print("Could not find information about the Pokémon.")

print('--------------------------------------------------------------------------------------')

# How Many Pokémon Weigh More

# Send a GET request to fetch the weight of the specified Pokémon.
response = requests.get(url)

# Check if the response status code is equal to 200 (successful).
if response.status_code == 200:
    data = response.json()
    pokemon1_weight = data["weight"]

    print(f"{pokemon1_name}'s weight is: {pokemon1_weight}")
    print(f"Checking how many Pokémon are heavier than {pokemon1_name}. Please wait a moment...")

    offset = 0
    limit = count
    more_pokemons = True
    count_heavier = 0

    while more_pokemons:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/?offset={offset}&limit={limit}")

        if response.status_code == 200:
            pokemon_list_data = response.json()
            pokemon_list = pokemon_list_data["results"]

            for pokemon in pokemon_list:
                response = requests.get(pokemon["url"])

                if response.status_code == 200:
                    pokemon_data = response.json()
                    pokemon_weight = pokemon_data["weight"]

                    if pokemon_weight > pokemon1_weight:
                        count_heavier += 1
                else:
                    print(f"Failed to retrieve data for {pokemon['name']}")

            offset += limit

            if offset >= pokemon_list_data["count"]:
                more_pokemons = False
        else:
            print("Failed to retrieve Pokémon list")

    print(f"In total, there are {count_heavier} Pokémon that weigh more than {pokemon1_name}.")
else:
    print("Could not find information about the Pokémon.")
