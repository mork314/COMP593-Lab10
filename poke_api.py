import requests
import json

POKE_API_URL = r'https://pokeapi.co/api/v2/pokemon/'

def main():
    get_pokemon_info('giratina-origin')
    fetch_all_names()
    return


def get_pokemon_info(name_or_number):
    """Gets information about a specified pokemon

    Args:
        name_or_number (str): The name or pokedex number of the pokemon

    Returns:
        dict: The dictionary containing all the information for the specified pokemon. None if unsuccessful
    """
  
    name_or_number = str(name_or_number).strip().lower()
    url_to_use = POKE_API_URL + name_or_number
    try:
        number = int(name_or_number)
        print_desc = f'Pokemon #{number}'
    except:
        name = name_or_number
        print_desc = name
    
    print(f'Fetching information about {print_desc}...')
    response = (requests.get(url_to_use))

    #Check if request was successful
    if response.status_code == requests.codes.ok:
        print('success')
        return json.loads(response.text)
    else:
        raise ValueError('bad')
        print('failure')
        print(f'Response code {response.status_code} ({response.reason})')
        print(f"Error: {response.text}")

def fetch_all_names():
    """Gets a list of all pokemon names
    
    """
    for i in range(1, 1009):
        url_to_use = POKE_API_URL + str(i)
        poke_info = (requests.get(url_to_use))
        print(poke_info.text)

        

if __name__ == '__main__':
    main()