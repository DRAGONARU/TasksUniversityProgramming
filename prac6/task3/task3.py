import requests


class Pokemon:
    """
    Класс, описывающий отдельного покемона и его характеристики.

    Атрибуты:
        name (str): Имя покемона.
        abilities (list[str]): Список способностей покемона.
        weight (int): Вес покемона.
        height (int): Рост покемона.
        p_types (list[str]): Типы покемона (например, 'fire', 'water').
        hp_stat (int): Показатель здоровья.
        attack_stat (int): Показатель атаки.
        defense_stat (int): Показатель защиты.
        speed_stat (int): Показатель скорости.
        power_stat (int): Комплексная сила покемона (вычисляется автоматически).
    """

    def __init__(
        self,
        name,
        abilities,
        weight,
        height,
        p_types,
        hp_stat,
        attack_stat,
        defense_stat,
        speed_stat,
    ):
        self.name = name
        self.abilities = abilities
        self.weight = weight
        self.height = height
        self.p_types = p_types
        self.hp_stat = hp_stat
        self.attack_stat = attack_stat
        self.defense_stat = defense_stat
        self.speed_stat = speed_stat
        self.power_stat = (
            len(abilities) * len(p_types) * hp_stat * attack_stat * defense_stat * speed_stat - height * weight
        )

    def get_pokemon_info(self):
        """Выводит подробную информацию о покемоне."""
        print(f'Имя: {self.name}')
        print('Способности:', *self.abilities)
        print(f'Вес: {self.weight}')
        print(f'Рост: {self.height}')
        print('Типы покемона:', *self.p_types)
        print(f'Здоровье: {self.hp_stat}')
        print(f'Атака: {self.attack_stat}')
        print(f'Защита: {self.defense_stat}')
        print(f'Скорость: {self.speed_stat}')


class PokemonTeam:
    """
    Класс, описывающий команду покемонов.

    Атрибуты:
        name (str): Название команды.
        pokemon_list (list[Pokemon]): Список покемонов в команде.
    """

    def __init__(self, name, pokemon_list):
        self.name = name
        self.pokemon_list = pokemon_list

    def add_pokemon(self, pokemon):
        """
        Добавляет нового покемона в команду, если он ещё не присутствует.
        """
        for item in self.pokemon_list:
            if item.name == pokemon.name:
                print(f'Покемон {pokemon.name} уже есть в команде.')
                return
        self.pokemon_list.append(pokemon)
        print(f'Покемон {pokemon.name} добавлен в команду.')

    def delete_pokemon(self, pokemon_name):
        """
        Удаляет покемона из команды по имени.
        """
        for item in self.pokemon_list:
            if item.name == pokemon_name:
                self.pokemon_list.remove(item)
                print(f'Покемон {pokemon_name} удалён из команды.')
                return
        print(f'Покемон {pokemon_name} не найден в команде.')

    def show_pokemon_list(self):
        """Выводит список имён покемонов в команде."""
        if not self.pokemon_list:
            print('Команда пуста.')
            return
        print('Список покемонов команды:')
        for i, pokemon in enumerate(self.pokemon_list, 1):
            print(f'{i}. {pokemon.name}')

    def get_pokemon_info(self, pokemon_name):
        """Выводит информацию о покемоне по его имени."""
        for item in self.pokemon_list:
            if item.name == pokemon_name:
                item.get_pokemon_info()
                return
        print(f'Покемон {pokemon_name} не найден в команде.')

    def show_team_info(self):
        """Выводит полную информацию о всех покемонах в команде."""
        if not self.pokemon_list:
            print('Команда пуста.')
            return
        for i, pokemon in enumerate(self.pokemon_list, 1):
            print(f'№{i}')
            pokemon.get_pokemon_info()
            print('-' * 30)

    def training_battle(self, name1, name2):
        """
        Проводит тренировочный бой между двумя покемонами команды по именам.
        """
        p1 = next((p for p in self.pokemon_list if p.name.lower() == name1.lower()), None)
        p2 = next((p for p in self.pokemon_list if p.name.lower() == name2.lower()), None)

        if not p1 or not p2:
            print('Один или оба покемона не найдены в команде.')
            if not p1:
                print(f'Не найден: {name1}')
            if not p2:
                print(f'Не найден: {name2}')
            return

        print(f'Бой: {p1.name} vs {p2.name}')
        if p1.power_stat > p2.power_stat:
            print(f'Победил покемон {p1.name}!')
        elif p2.power_stat > p1.power_stat:
            print(f'Победил покемон {p2.name}!')
        else:
            print('Ничья!')


def main():
    """Главная функция программы с интерактивным интерфейсом."""
    team = PokemonTeam('Команда 1', [])
    flag_to_end = False

    while not flag_to_end:
        command = input('Введите команду: ').strip().lower()

        if command == 'help':
            print('''Доступные команды:
help - показать список команд
add_pokemon - добавить покемона в команду
delete_pokemon - удалить покемона из команды
show_pokemon_list - показать список покемонов в команде
get_pokemon_info - показать информацию о покемоне
show_team_info - показать информацию о всех покемонах команды
training_battle - устроить тренировочный бой
exit - выход''')

        elif command == 'add_pokemon':
            pokemon_name = input('Введите имя покемона: ')
            try:
                response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}')
                response.raise_for_status()
                pokemon_data = response.json()
            except requests.RequestException:
                print('Ошибка при получении данных о покемоне.')
                continue

            abilities = [a['ability']['name'] for a in pokemon_data['abilities']]
            p_types = [t['type']['name'] for t in pokemon_data['types']]
            pokemon = Pokemon(
                name=pokemon_data['name'],
                abilities=abilities,
                weight=pokemon_data['weight'],
                height=pokemon_data['height'],
                p_types=p_types,
                hp_stat=pokemon_data['stats'][0]['base_stat'],
                attack_stat=pokemon_data['stats'][1]['base_stat'],
                defense_stat=pokemon_data['stats'][2]['base_stat'],
                speed_stat=pokemon_data['stats'][5]['base_stat'],
            )
            team.add_pokemon(pokemon)

        elif command == 'delete_pokemon':
            name = input('Введите имя покемона: ')
            team.delete_pokemon(name)

        elif command == 'show_pokemon_list':
            team.show_pokemon_list()

        elif command == 'get_pokemon_info':
            name = input('Введите имя покемона: ')
            team.get_pokemon_info(name)

        elif command == 'show_team_info':
            team.show_team_info()

        elif command == 'training_battle':
            name1 = input('Введите имя первого покемона: ')
            name2 = input('Введите имя второго покемона: ')
            team.training_battle(name1, name2)

        elif command == 'exit':
            flag_to_end = True
        else:
            print('Неверная команда. Введите "help" для списка доступных команд.')


if __name__ == '__main__':
    main()
