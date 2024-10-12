class Item:
    def __init__(self, name, effect, value):
        self.name = name
        self.effect = effect
        self.value = value

class Player:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.inventory = []

    def use_item(self, item):
        if item.effect == "heal":
            self.hp += item.value
            print(f"{self.name}は{item.value}HP回復した！")
        # アイテムをインベントリから削除
        self.inventory.remove(item)
