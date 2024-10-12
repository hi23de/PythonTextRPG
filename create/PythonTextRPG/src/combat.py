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

def battle(player, enemy):
  while player.hp > 0 and enemy.hp > 0:
    print(f"{player.name}のHP: {player.hp} | {enemy.name}のHP: {enemy.hp}")

    action = input("行動を選んでください (1: 攻撃, 2: 防御): ")

    if action == "1":
      enemy_defeated = enemy.take_damage(player.attack)
      if enemy_defeated:
        print(f"{enemy.name}を倒しました！")
        break

    player_defeated = player.take_damage(enemy.attack)
    if player_defeated:
      print(f"{player.name}が倒されました…")
      break
