import requests
import json
import image_lib
import os

POKE_API_URL = r'https://pokeapi.co/api/v2/pokemon/'

def main():
    get_pokemon_info('giratina-origin')
    fetch_all_names()
    get_poke_image('giratina-origin')
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
    poke_list = []
    response = requests.get(r'https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0')
    resp_dict = json.loads(response.text)
    pokemon_names = [p["name"] for p in resp_dict['results']]
    #could also use comp like in lecture - pokemon_names = [p["name"] for p in resp_dict['results']]
    return(pokemon_names)

def get_poke_image(poke_name):
    
    url_to_use = POKE_API_URL + poke_name
    
    response = (requests.get(url_to_use))
    
    if response is None:
        return

    resp_dict = json.loads(response.text)
    
    img_url = resp_dict['sprites']['other']['official-artwork']['front_default']
    
    image_data = image_lib.download_image(img_url)

    if image_data is None:
        return
    
    dir_path = os.path.dirname(os.path.realpath('poke_api.py'))
    
    new_dir_path = dir_path + '\poke_images'
    
    if not os.path.exists(new_dir_path):
        os.makedirs(new_dir_path)
    
    poke_img_path = f'\{poke_name}.jpg'

    image_lib.save_image_file(image_data, new_dir_path + poke_img_path)

    return new_dir_path + poke_img_path
    

if __name__ == '__main__':
    main()