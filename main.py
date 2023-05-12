import requests
import random

#1 Fetch Data

# ask user to enter the pokemon and stores it as pokemon_name.
pokemon1_name = input("Enter the name of a Pokémon (without caps): ")
print('--------------------------------------------------------------------------------------------')

# url to acces the pokemon data, f is to be able to insert the pokemon_name to the url
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon1_name}"
print(f'{pokemon1_name} stats:')
# Send a GET(get the info) request to the PokeAPI using the URL, and store the response in the "response" variable.
response = requests.get(url)

# Check if the response status code is equal to 200, 200=sucseful.
if response.status_code == 200:
    # since the PokeApi send its info in JSON we change it to Python object stored it in the "data" variable.
    data = response.json()
    # Extract the HP (health points) of the Pokémon from the "data" dictionary by accessing the first element of the "stats" list and then the "base_stat" key.
    hp = data["stats"][0]["base_stat"]
    # Extract the weight of the Pokémon from the "data" dictionary by accessing the "weight" key.
    weight = data["weight"]
    # Print out the name of the Pokémon entered by the user along with its HP and weight using an f-string.
    print(f"{pokemon1_name}'s HP is {hp} and its weight is {weight}.")
else:
    # If the response status code is not equal to 200, print an error message.
    print("Could not retrieve information about the Pokémon.")

#2b moves

# url to access the pokemon data, f is to be able to insert the pokemon_name to the url
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon1_name}"

# Send a GET(get the info) request to the PokeAPI using the URL, and store the response in the "response" variable.
response = requests.get(url)

# Check if the response status code is equal to 200, 200=sucseful.
if response.status_code == 200:
    # since the PokeApi send its info in JSON we change it to Python object stored it in the "data" variable.
    data = response.json()
    # Extract the HP (health points) of the Pokémon from the "data" dictionary by accessing the first element of the "stats" list and then the "base_stat" key.
    hp = data["stats"][0]["base_stat"]
    # Extract the weight of the Pokémon from the "data" dictionary by accessing the "weight" key.
    weight = data["weight"]
    # Extract the moves of the Pokémon from the "data" dictionary by accessing the "moves" list and then the "name" key.}
    moves_list = []
    for move in data['moves'][:5]:
        move_name = move['move']['name']
        moves_list.append(move_name)

    # Print out the name of the Pokémon entered by the user along with its HP, weight and moves using an f-string.
    print(f"{pokemon1_name}'s moves are: {', '.join(moves_list)}.")
else:
    # If the response status code is not equal to 200, print an error message.
    print("Could not get information of the Pokémon.")



print('-----------------------------------------------------------------------------------------------------')

#2a Count 
print('Pokemon count')
# Send a GET request to the Pokemon API's Pokemon resource and store the response in the "response" variable
response = requests.get("https://pokeapi.co/api/v2/pokemon/")
# Check if the response status code is equal to 200 (successful)
if response.status_code == 200:
    # Convert the response to a Python object and extract the "count" attribute, which tells us how many Pokemon exist
    data = response.json()
    count = data["count"]
    print(f"There are {count} Pokémon in total.")
else:
    # If the response status code is not equal to 200, print an error message.
    print("Could not retrieve information about the Pokémon.")

print('----------------------------------------------------------------------------------------------')

#2c Healthier
print('HP fight')
# Get a random Pokemon name
random_pokemon_id = random.randint(1, count)

url = f"https://pokeapi.co/api/v2/pokemon/{random_pokemon_id}"
response = requests.get(url)

# Check if the response status code is equal to 200, 200=sucseful.
if response.status_code == 200:
    data = response.json()
    pokemon_name = data["name"] 
    # Get a random Pokémon from the list
    random_pokemon = random.choice(data["stats"])
    random_pokemon_hp = random_pokemon["base_stat"]
    
    print(f"The random Pokémon is: {pokemon_name}")
    print(f"{pokemon_name} hp is: {random_pokemon_hp}, and {pokemon1_name} hp is: {hp}")

    if random_pokemon_hp > hp:
        print(f"{pokemon_name} is healthier than {pokemon1_name}")
    else:
      if hp>random_pokemon_hp:
       print(f"{pokemon1_name} is healthier than {pokemon_name}!")
      else:
         print(f"both {pokemon1_name} and {pokemon_name} have the same hp {hp}")
else:
    print("Could not retrieve information about the Pokémon.")

print('--------------------------------------------------------------------------------------')


#3a how many pokemons weight more
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon1_name}"
response = requests.get(url)

# Check if the response status code is equal to 200, 200=successful.
if response.status_code == 200:
    data = response.json()
    pokemon1_weight = data["weight"]
    
    print(f"{pokemon1_name}'s weight is: {pokemon1_weight}")
    print(f"checking for how many pokemons are heavier than {pokemon1_name}, please wait a minute :)")
    
    offset = 0 #is set to 0, which means the program will start fetching data from the first item in a list.
    limit = count #the program will retrieve data up to count number of items from the list.
    more_pokemons = True #its true so that it loops and fetches more pokemon

    # Loop until all pokemon have been searched
    while more_pokemons:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/?offset={offset}&limit={limit}")   # Send a request to the PokeAPI with the current offset and limit
        if response.status_code == 200:  # If the request is successful, get the list of pokemon from the response
            pokemon_list_data = response.json()
            pokemon_list = pokemon_list_data["results"]
            count_heavier = 0
  # Loop through each pokemon in the list
            for pokemon in pokemon_list:
                response = requests.get(pokemon["url"])   # Send a request to the PokeAPI for details about the current pokemon
                if response.status_code == 200:  # If the request is successful, get the pokemon's name and weight
                    pokemon_data = response.json()
                    pokemon_name = pokemon_data["name"]
                    pokemon_weight = pokemon_data["weight"]
                       # If the pokemon's weight is greater than the first pokemon's weight, increment the count_heavier variable
                    if pokemon_weight > pokemon1_weight:
                        count_heavier = count_heavier + 1
                else:
                    print(f"Failed to retrieve data for {pokemon['name']}")

            offset = offset + limit # adding a limit to the offset

            if offset >= pokemon_list_data["count"]:
                more_pokemons = False
        else: 
            print("Failed to retrieve Pokémon list")
    print(f'In total there are {count_heavier} pokemons heavier than {pokemon1_name}')
else:
    print("Could not retrieve information about the Pokémon.")
