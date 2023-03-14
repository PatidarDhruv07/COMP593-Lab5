import requests

def main():
    pokemon_info = get_information_of_pokemon("1")
    print(pokemon_info)

def get_information_of_pokemon(name_of_pokemon):
    """Collectes the data of given pokemon name from PokeAPI

    Args:
        name (str): pokemon name

    Returns:
        dict: returns a dictionary of given pokemon and if its unsuccessfull it will return None
    """
    pokemon_name = str(name_of_pokemon).lower().strip()
    link_for_pastebin = f"https://pokeapi.co/api/v2/pokemon/{name_of_pokemon}"
    request_info = requests.get(link_for_pastebin)
    print(f"Getting information for {pokemon_name}...", end='')
    
    if request_info.ok:
        print('success')
        return request_info.json()
    else:
        print('failure')
        print("Response code: 404 (Not Found)")
        return None

if __name__ == '__main__':
    main()