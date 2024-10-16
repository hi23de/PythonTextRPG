import pygame
import sys
import json
from player import Player
from characters import Character
from item import Item
from combat import battle, draw_battle
from utils import draw_text

pygame.init()

# ウィンドウ設定
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Text-Based RPG")

# フォント設定
font = pygame.font.SysFont("Bizudgothic", 36)

# シナリオ読込
with open('../scenarios/scenario.json', 'r', encoding='utf-8') as file:
  scenarios = json.load(file)

current_scenario = "start"
in_battle = False

player = Player("プレイヤー", 100, 20)
enemy = Character("ドラゴン", 80, 15)

# メインループ
running = True
while running:
    if not in_battle:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_1, pygame.K_2, pygame.K_3]:
                    choices = list(scenarios[current_scenario]["choices"].values())
                    choice_index = event.key - pygame.K_1
                    if choice_index < len(choices):
                        current_scenario = choices[choice_index]
                        # アイテム取得チェック
                        if "item" in scenarios[current_scenario]:
                            item_data = scenarios[current_scenario]["item"]
                            new_item = Item(item_data["name"], item_data["effect"], item_data["value"])
                            player.inventory.append(new_item)
                            print(f"{new_item.name}を取得した！")
                        if current_scenario == "fight_dragon":
                            battle(screen, font, player, enemy)
                            in_battle = False

        #画面の更新
        screen.fill((0, 0, 0))
        draw_text(screen, font, scenarios[current_scenario]["text"], 20, 20, 760)
        choices = list(scenarios[current_scenario]["choices"].keys())
        for i, choice in enumerate(choices):
            draw_text(screen, font, f"{i + 1}. {choice}", 20, 100 + i * 40, 760)

        pygame.display.flip()
    else:
        battle(screen, font, player, enemy)