import requests

class Pokemon:
    '''
    Класс покемона
    :param name: имя покемона
    :param p_type: тип покемона
    :param weight: вес покемона
    :param height: рост покемона    
    :param abilities: способности покемона    
    '''
    def __init__(self, name, p_type, weight, height, abilities):
        self.name = name
        self.p_type = p_type
        self.weight = weight
        self.height = height
        self.abilities = abilities

def get_pokemon_name(pokemon_id):
    '''
    Функция получает имя покемона по его id/имени
    :param pokemon_id: id/имя покемона
    :return: имя покемона
    '''
    response = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(pokemon_id))
    pokemon_name = response.json()['name']
    return pokemon_name

list_of_pokemon_names = []

for i in range(1, 21):
    list_of_pokemon_names.append(get_pokemon_name(i))

print(*list_of_pokemon_names)

while True:
    pokemon_id = input('Введите имя покемона или 0, чтобы выйти: ')
    if pokemon_id == '0':
        break
    else:
        pokemon_response = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(pokemon_id))
        current_pokemon = Pokemon(pokemon_response.json()['name'], pokemon_response.json()['types'],
                                  pokemon_response.json()['weight'], pokemon_response.json()['height'],
                                  pokemon_response.json()['abilities'])
        print(current_pokemon.name)
        print(*[item['type']['name'] for item in current_pokemon.p_type])
        print(current_pokemon.weight)
        print(current_pokemon.height)
        print(*[item['ability']['name'] for item in current_pokemon.abilities])
