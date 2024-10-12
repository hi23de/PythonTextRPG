class Character:
  def __init__(self, name, hp, attack):
    self.name = name
    self.hp = hp
    self.attack = attack

  def take_damage(self, damage):
    self.hp -= damage
    if self.hp <= 0:
      self.hp = 0
      return True  # キャラクターが倒れる
    return False
