from objects.gameobject import GameObject
from objects.rocks.mineral import Mineral
from objects.mysteryman import MysteryMan
from GUI.scene import ShopScene
from objects.ladder import Ladder
from objects.surface.water import Water
from eq.pickaxe import Pickaxe
from eq.weapon import Weapon
from eq.clothing import Clothing
from eq.lantern import Lantern


class Player(GameObject):
    # GOLD = 0
    # COPPER = 1
    # EMERALD = 2
    # DIAMOND = 3
    # BEDROCK = 4
    def __init__(self, game, health, gas):
        super().__init__(game, False)
        self.gas = gas  # paliwo
        self.health = health
        self.crystals_count = 0
        self.crystals = [0] * 5
        self.crystals[0] = 15
        self.inventory = []
        self.current_pickaxe = Pickaxe(10, self.game.graphics.cobelstone_pickaxe, 0)
        self.current_weapon = Weapon(5, self.game.graphics.sword_texture, 0)
        self.current_clothing = Clothing(1, self.game.graphics.armor1_texture, 0)
        self.current_lantern = Lantern(10, self.game.graphics.lantern_texture, 0)
        self.inventory.append(self.current_pickaxe)
        self.inventory.append(self.current_weapon)
        self.inventory.append(self.current_clothing)
        self.inventory.append(self.current_lantern)
        self.generate_score_image()
        self.generate_level_image()
        # jednostki w okreslonym czasie //1sekunda
        self.velocity_x = 0
        self.velocity_y = 0
        # aby niszczyc skały kilof
        self.pressed_axe = False
        # aby walczyc w przeciwnikami
        self.pressed_weapon = False
        # do handlu
        self.pressed_handel = False
        # do_przejscia_na_nastepny_poziom
        self.pressed_enter_next_level = False
        self.pressed_drink = False

    def increment_mineral(self, mineral_type):
        self.crystals[mineral_type] += 1
        self.generate_score_image()

    def draw(self, screen, x_center, y_center):
        screen.blit(self.game.graphics.miner_texture, (x_center - 24, y_center - 24))
        screen.blit(self.scores_image, (0, 0))
        screen.blit(self.health_image, (1040, 0))
        screen.blit(self.level_image, (500, 0))

    # elapsed w milisekundach
    # przemieszczanie

    def update(self, elapsed):
        if self.health <= 0:
            print("NO HP")
            self.game.end_game()

        if self.pressed_axe or self.pressed_weapon:
            # prawo
            if self.velocity_x > 0:
                offset_x = 1
            elif self.velocity_x < 0:
                offset_x = -1
            else:
                offset_x = 0

            if self.velocity_y > 0:
                offset_y = 1
            elif self.velocity_y < 0:
                offset_y = -1
            else:
                offset_y = 0

            if offset_x != 0 or offset_y != 0:
                # wspólrzedne gracza
                field_x = self.field.x + offset_x
                field_y = self.field.y + offset_y
                # wyjscie za mape
                if 0 <= field_x < self.game.map.width and 0 <= field_y < self.game.map.height:
                    for obj in self.game.map.fields[field_x][field_y].objects:

                        if self.pressed_axe:
                            obj.hit_by_axe()
                        elif self.pressed_weapon:
                            obj.hit_by_weapon()

        elif self.pressed_handel:

            for i in range(3):
                for j in range(3):
                    # wyliczam pozycje
                    x_position = int(self.x + i - 1)
                    y_position = int(self.y + j - 1)
                    if self.x == x_position or self.y == y_position:
                        continue
                    for obj in self.game.map.fields[x_position][y_position].objects:
                        if isinstance(obj, MysteryMan):
                            self.game.pop_up = ShopScene(self.game, obj)
        elif self.pressed_enter_next_level:
            for i in range(3):
                for j in range(3):
                    # wyliczam pozycje
                    x_position = int(self.x + i - 1)
                    y_position = int(self.y + j - 1)
                    if self.x == x_position or self.y == y_position:
                        continue
                    for obj in self.game.map.fields[x_position][y_position].objects:
                        if isinstance(obj, Ladder):
                            # nowa plansza
                            self.game.next_level()

        elif self.pressed_drink:

            dx = [0, 0, -1, 1, 0]
            dy = [-1, 0, 0, 0, 1]

            for i in dx:
                for j in dy:
                    for obj in self.game.map.fields[int(self.x) + i][int(self.y) + j].objects:
                        if isinstance(obj, Water):
                            obj.is_drunk(self)

        else:
            new_x = self.x + self.velocity_x * elapsed / 1000
            new_y = self.y + self.velocity_y * elapsed / 1000

            # nie wychodzi pozaplansze
            if new_x < 0:
                new_x = int(self.x)

            elif new_x >= self.game.map.width:
                new_x = int(self.x)

            if new_y < 0:
                new_y = int(self.y)

            elif new_y >= self.game.map.height:
                new_y = int(self.y)

            for obj in self.game.map.fields[int(new_x)][int(new_y)].objects:
                if self is obj:
                    continue
                if not obj.isCollectible:
                    return
            self.game.map.set_position(self, new_x, new_y)
            self.collect_collectibles()
            self.generate_health_image()
            self.generate_level_image()

    def destroy_rocks(self, x, y):

        for obj in self.game.map.fields[x][y].objects:

            if not obj.isCollectible:
                pass

    def collect_collectibles(self):

        for obj in self.field.objects:
            if isinstance(obj, Mineral):
                self.crystals_count += 1
                self.increment_mineral(obj.mineral_type)
                self.game.map.remove_game_object(obj)
                break

    def generate_score_image(self):
        string = ''
        for i in self.crystals:
            if len(string) > 0:
                string += ','
            string += str(i)
        self.scores_image = self.game.graphics.font.render(string, True, (255, 0, 0), (0, 0, 255))

    def generate_health_image(self):
        string = 'health: '
        string += str(self.health)
        self.health_image = self.game.graphics.font.render(string, True, (255, 0, 0), (0, 0, 255))

    def generate_level_image(self):
        string = "level: "
        string += str(self.game.level)
        self.level_image = self.game.graphics.font.render(string, True, (255, 0, 0), (0, 0, 255))

    def buy_item(self, index):
        item = self.game.map.MysteryMan.goods[index]
        price = self.game.map.MysteryMan.goods[index].price
        if self.crystals[Mineral.GOLD] >= price:
            self.inventory.append(self.game.map.MysteryMan.goods[index])
            self.game.map.MysteryMan.goods.remove(item)
            self.crystals[Mineral.GOLD] -= price
        self.update_inventory()

    def update_inventory(self):
        for i in self.inventory:
            if isinstance(i, Pickaxe):
                if self.current_pickaxe.power <= i.power:
                    self.current_pickaxe = i
            if isinstance(i, Weapon):
                if self.current_weapon.damage <= i.damage:
                    self.current_weapon = i
            if isinstance(i, Clothing):
                if self.current_clothing.defence <= i.defence:
                    self.current_clothing = i

    def use_item(self, item):
        if isinstance(item, Weapon):
            self.current_weapon = item
        elif isinstance(item, Clothing):
            self.current_clothing = item
        elif isinstance(item, Lantern):
            self.current_lantern = item
        elif isinstance(item, Pickaxe):
            self.current_pickaxe = item

    def is_item_used(self, item):
        if item is self.current_weapon:
            return True
        elif item is self.current_clothing:
            return True
        elif item is self.current_lantern:
            return True
        elif item is self.current_pickaxe:
            return True
        return False
