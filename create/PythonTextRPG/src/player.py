from characters import Character
from item import Item

class Player(Character):
    def __init__(self, name, hp, attack):
        super().__init__(name, hp, attack)
        self.inventory = []

    def use_item(self, item):
        if item.effect == "heal":
            self.hp += item.value
            print(f"{self.name}は{item.value}HP回復した！")
        self.inventory.remove(item)
