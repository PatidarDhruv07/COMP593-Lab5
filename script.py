from pastebin_api import post_new_paste
from poke_api import get_information_of_pokemon

#"While doing some reasearch I explore this "argparse" function from this website "https://docs.python.org/3/library/argparse.html#:~:text=The%20argparse%20module%20makes%20it,generates%20help%20and%20usage%20messages." so, I tried implement itand it worked."
import argparse

def main():
    
    parser_of_given_pokemon = argparse.ArgumentParser()
    parser_of_given_pokemon.add_argument('pokemon_name', help='Name of the Pokemon')
    args = parser_of_given_pokemon.parse_args()
    
    name = args.pokemon_name
    pokemon_details = get_information_of_pokemon(name)

    if pokemon_details:
        title, body_text = pokemon_details_paste(pokemon_details)
        paste_url = post_new_paste(title,body_text,'1M')
        print(paste_url)

def pokemon_details_paste(pokemon_details):
    name = pokemon_details['name'].capitalize()
    ability_names = [ability['ability']['name'] for ability in pokemon_details['abilities']]
    abilities_list = '* ' + '\n* '.join(ability_names)
    title = f"{name}'s Abilities"
    body = abilities_list

    return title, body

if __name__ == '__main__':
    main()