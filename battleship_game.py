import random

HORIZONT = 0
VERTICAL = 1

class Object:

    def __init__(self, position) -> None:
        self.position = position

    def get_body(self):
        pass

    def get_area(self):
        pass


class Ship(Object):

    def __init__(self, position: tuple, orient: int, size: int) -> None:
        super().__init__(position)
        self.size = size
        self.orient = orient
        self.health = size

    def get_body(self):
        body = []
        if self.orient == VERTICAL:
            for i in range(self.size):
                body.append((self.position[0] + i, self.position[1]))
        else:
            for i in range(self.size):
                body.append((self.position[0], self.position[1] + i))
        return body

    def get_area(self):
        body = self.get_body()
        area = set()
        for x, y in body:
            for x0 in [-1,0, 1]:
                for y0 in [-1, 0, 1]:
                    new_xy = (x + x0, y + y0)
                    if new_xy not in body:
                        area.add(new_xy)
        return area

    @classmethod
    def generate(cls, shape: tuple, size):
        max_x, max_y = shape
        x, y = random.randrange(max_x), random.randrange(max_y)
        orient = random.choice([HORIZONT, VERTICAL])
        return cls((x,y), orient=orient, size=size)

    def __repr__(self) -> str:
        return 'Ship'


class Mine(Object):

    def __init__(self, position):
        super().__init__(position)

    def get_body(self):
        body = [self.position]
        return body
    
    def get_area(self):
        body = self.get_body()
        area = set()
        for x, y in body:
            for x0 in [-1,0, 1]:
                for y0 in [-1, 0, 1]:
                    new_xy = (x + x0, y + y0)
                    if new_xy not in body:
                        area.add(new_xy)
        return area

    @classmethod
    def generate(cls, shape: tuple):
        max_x, max_y = shape
        x, y = random.randrange(max_x), random.randrange(max_y)
        return cls((x, y))

    def __repr__(self) -> str:
        return 'Mine'
    

class Map:

    config = {
        'ships': {
            1: 4,
            2: 3,
            3: 2,
            4: 1
        },
        'mine': {
            1: 2
        }
    }

    def __init__(self, shape) -> None:
        self.shape = shape
        self._list_objects = []
        self._objects = [[None] * self.shape[1] for _ in range(self.shape[0])]
        self._misses = [[0] * self.shape[1] for _ in range(self.shape[0])]
        self._areas = [[None] * self.shape[1] for _ in range(self.shape[0])]
        self._occupied = [[0] * self.shape[1] for _ in range(self.shape[0])]

    def add_ship(self, ship: Ship):
        for x, y in ship.get_body():
            if x < 0 or x >= self.shape[0]:
                raise ValueError("Ship out of map.")
            if y < 0 or y >= self.shape[1]:
                raise ValueError("Ship out of map.")
            if self._occupied[x][y]:
                raise ValueError("This position already occupied.")

        self._add_object(ship, area_occupied=True)

    def add_mine(self, mine: Mine):
        for x,y in mine.get_body():
            if x < 0 or x >= self.shape[0]:
                raise ValueError("Ship out of map.")
            if y < 0 or y >= self.shape[1]:
                raise ValueError("Ship out of map.")
            if self._occupied[x][y]:
                raise ValueError("This position already occupied.")

        self._add_object(mine, area_occupied=True)

    def _add_object(self, obj: Object, area_occupied=False):
        # метод відповідає за додавання об'єктів(у нашому випадку це корабель або міна) + він використовується всередині інших методів
        for x, y in obj.get_body():
            self._occupied[x][y] = 1
            self._objects[x][y] = obj
        for x,y in obj.get_area():
            if area_occupied:
                # area_occupied (точніше значення його) випливає з методів add_mine , add_ship
                # continue у циклі for == пропускає координати, які виходить за межі карти (пропускає ітерації, що не відповідають перевірці)
                if x < 0 or x >= self.shape[0]:
                    continue
                if y < 0 or y >= self.shape[1]: 
                    continue
                self._occupied[x][y] = 1
            self._areas[x][y] = obj
        self._list_objects.append(obj)

    @classmethod
    def generate(cls, shape, max_tries=100_000):
        res = cls(shape)

        for size, amount in cls.config['ships'].items():
            # cls.config['ships'] - кількість кораблів кожного розміру, які ми додати раніше(на початку класу)
            for _ in range(amount):
                for _ in range(max_tries):
                    try:
                        ship = Ship.generate(shape, size)
                        res.add_ship(ship)
                        break
                    except ValueError:
                        continue
                else:
                    raise ValueError("Couldn't generate map.")
                
        for size, amount in cls.config['mine'].items():
            for _ in range(amount):
                for _ in range(max_tries):
                    try:
                        mine = Mine.generate(shape)
                        res.add_mine(mine)
                        break
                    except ValueError:
                        continue
                else:
                    raise ValueError("Couldn't generate map.")
        return res

    def show(self):
        res = [[' '] * self.shape[1] for _ in range(self.shape[0])]

        for obj in self._list_objects:
            for (x, y) in obj.get_area():
                if 0 <= x < self.shape[0] and 0 <= y < self.shape[1]:
                    res[x][y] = '.'
            for (x, y) in obj.get_body():
                res[x][y] = 'x'
            if isinstance(obj, Mine):
                for (x, y) in obj.get_area():
                    if 0 <= x < self.shape[0] and 0 <= y < self.shape[1]:
                        res[x][y] = '.'
                for (x, y) in obj.get_body():
                    res[x][y] = 'o'

        print('-' * (self.shape[0] * 2 + 3))
        for row in res:
            print('|', *row, '|')
        print('-' * (self.shape[0] * 2 + 3))


class Game:
    def __init__(self, map_shape: tuple, map: Map) -> None:
        self.map_bot = Map.generate(map_shape)
        self.map_person = map
        self.bots_moves = []
                
    def generate_moves_for_bot(self, map_shape: tuple):
        x, y = random.randrange(map_shape[0]), random.randrange(map_shape[1])
        self.bots_moves.append((x, y))
        return x,y
    
    def moves_of_person(self):
        x = int(input("Enter row: ")) 
        y = int(input("Enter column: ")) 
        return x,y

    def shoots(self, position: tuple, opponent_map: Map, attack_map: Map):
        # attack_map - мапа, на якій будуть відображатися moves 
        x, y = position
        obj = opponent_map._objects[x][y]

        if obj is None:
            attack_map._misses[x][y] = '.'
            return 'Missed!'
        
        if isinstance(obj, Ship):
            obj.health -= 1
            attack_map._misses[x][y] = 'x'
            if obj.health == 0:
                for el in obj.get_area():
                    x0, y0 = el
                    if 0 <= x0 < attack_map.shape[0] and 0 <= y0 < attack_map.shape[1]:
                        attack_map._misses[x0][y0] = '.'
                return f'Ship sunk!'
            else:
                return 'Hit!'
        
        if isinstance(obj, Mine):
            attack_map._misses[x][y] = 'o'
            self.explode_mine(position, attack_map)
            return 'Mine exploded!'
        
    def explode_mine(self, position: tuple, attack_map: Map):
        area_expl = list(Mine(position).get_area())
        for x0, y0 in area_expl:
            if 0 <= x0 < attack_map.shape[0] and 0 <= y0 < attack_map.shape[1]:
                attack_map._misses[x0][y0] = '.'

    def show_map(self, map: Map):
        res = [[' '] * map.shape[1] for _ in range(map.shape[0])]

        for x in range(map.shape[0]):
            for y in range(map.shape[1]): 
                if map._misses[x][y] == '.':
                    res[x][y] = '\033[0;31m.\033[0m'
                elif map._misses[x][y] == 'x':
                    res[x][y] = '\033[0;31mx\033[0m'
                elif map._misses[x][y] == 'o':
                    res[x][y] = '\033[0;31mo\033[0m'

        print('-' * (map.shape[1] * 2 + 3))
        for row in res:
            print('|', *row, '|')
        print('-' * (map.shape[1] * 2 + 3))

    def is_game_over(self, map: Map):
        for el in map._objects:
            for obj in el:
                if isinstance(obj, Ship) and obj.health > 0:
                    return False
        return True

    def game_algorithm(self):
        while not self.is_game_over(self.map_bot):
            while True:
                print('Your map:')
                self.map_person.show()
                print("Player's turn")
                x, y = self.moves_of_person()
                res = self.shoots((x, y), self.map_bot, self.map_person)
                print(res)
                self.show_map(self.map_person)
                if res == 'Missed!':
                    break
                if self.is_game_over(self.map_bot):
                    print('Game over! You win!')
                    return
            while True:
                print("Bot's turn")
                x, y = self.generate_moves_for_bot(self.map_bot.shape)
                res = self.shoots((x, y), self.map_person, self.map_bot)
                print("Bot's move: ", (x, y))
                print(res)
                self.show_map(self.map_bot)
                if res == "Missed!":
                    break
                elif self.is_game_over(self.map_person):
                    print("Game over! You lost.")
                    return


map_shape = (10, 10)
player_map = Map(map_shape)
ships = [
    ((3, 6), HORIZONT, 4),
    ((2, 1), VERTICAL, 3),
    ((6, 1), HORIZONT, 3),
    ((4, 3), HORIZONT, 2),
    ((8, 1), HORIZONT, 2),
    ((6, 9), VERTICAL, 2),
    ((1, 5), HORIZONT, 1),
    ((6, 6), VERTICAL, 1),
    ((9, 9), VERTICAL, 1),
    ((1, 8), VERTICAL, 1)
]
for el in ships:
    ship = Ship(el[0], el[1], el[2])
    player_map.add_ship(ship)
mines = [(8, 5),(2, 3)]
for el in mines:
    mine = Mine(el)
    player_map.add_mine(mine)

game = Game(map_shape, player_map)
game.game_algorithm()