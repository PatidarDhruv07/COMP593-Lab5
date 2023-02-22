from Pastebin import post_new_paste
from poke_api import get_information_of_pokemon
import sys

def main():
    
    
    name = get_pokemon_name()
    pokemon_details = get_information_of_pokemon(name)

    if pokemon_details:
        title, body_text = pokemon_details_paste(pokemon_details)
        paste_url = post_new_paste(title,body_text,'1M')
        print(paste_url)

       

def get_pokemon_name():
    num_params = len(sys.argv) - 1
    if num_params > 0:
        return sys.argv[1]
    else:
        print("Error: Missing Name of Pokemon!")
        sys.exit(1)
        
def pokemon_details_paste(pokemon_details):
    name = pokemon_details['name'].capitalize()
    ability_names = [ability['ability']['name'] for ability in pokemon_details['abilities']]
    abilities_list = '* ' + '\n* '.join(ability_names)
    title = f"{name}'s Abilities"
    body = abilities_list

    return title, body

if __name__ == '__main__':
    main()