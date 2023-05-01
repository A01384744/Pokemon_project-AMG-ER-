import requests
import random
# Fetch Data
pokemon1_name = input("Enter the name of a Pokémon (without caps): ")
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon1_name}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    hp = data["stats"][0]["base_stat"]
    weight = data["weight"]
    print(f"{pokemon1_name}'s HP is {hp} and its weight is {weight}.")
else:
    print("Could not retrieve information about the Pokémon.")

# Count
response = requests.get("https://pokeapi.co/api/v2/pokemon/")
if response.status_code == 200:
    data = response.json()
    count = data["count"]
    print(f"There are {count} Pokémon in total.")
else:
    print("Could not retrieve information about the Pokémon.")

import requests

import requests

pokemon_name = input("Enter the name of a Pokémon (without caps): ")

# Fetch data
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    species_url = data["species"]["url"]

    # Retrieve species data
    species_response = requests.get(species_url)
    if species_response.status_code == 200:
        species_data = species_response.json()

        # Retrieve evolution chain URL
        evolution_chain_url = species_data["evolution_chain"]["url"]

        # Retrieve evolution chain data
        evolution_chain_response = requests.get(evolution_chain_url)
        if evolution_chain_response.status_code == 200:
            evolution_chain_data = evolution_chain_response.json()

            # Find the current Pokémon in the evolution chain
            chain = evolution_chain_data["chain"]
            current_pokemon = None
            for evolution in chain["evolves_to"]:
                if evolution["species"]["name"] == pokemon_name:
                    current_pokemon = evolution
                    break

            # If the current Pokémon exists in the chain, calculate and list the benefits of its evolution
            if current_pokemon:
                benefits = []
                evolves_to = current_pokemon["evolves_to"]
                while evolves_to:
                    next_evolution = evolves_to[0]
                    evolution_name = next_evolution["species"]["name"]

                    # Calculate the differences in HP, height, and weight
                    old_hp = data["stats"][0]["base_stat"]
                    new_response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{evolution_name}")
                    if new_response.status_code == 200:
                        new_data = new_response.json()
                        new_hp = new_data["stats"][0]["base_stat"]
                        hp_difference = new_hp - old_hp

                        old_height = data["height"]
                        new_height = new_data["height"]
                        height_difference = new_height - old_height

                        old_weight = data["weight"]
                        new_weight = new_data["weight"]
                        weight_difference = new_weight - old_weight

                        benefits.append(f"Evolution: {evolution_name}")
                        benefits.append(f"HP increased by {hp_difference}, height by {height_difference}, and weight by {weight_difference}.")
                    else:
                        print(f"Failed to retrieve data for {evolution_name}")

                    evolves_to = next_evolution["evolves_to"]

                # Print the benefits of evolution
                print("Benefits of Evolution:")
                for benefit in benefits:
                    print(benefit)
            else:
                print("There is no evolution for this Pokémon.")
        else:
            print("Failed to retrieve evolution chain data.")
    else:
        print("Failed to retrieve species data.")
else:
    print("Could not retrieve information about the Pokémon.")
