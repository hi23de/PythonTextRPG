import pygame
import sys
import json
from player import Player
from characters import Character
from item import Item
from combat import battle
from utils import draw_text, update_screen

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

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if not in_battle:
            if event.type == pygame.KEYDOWN:
                choices = list(scenarios[current_scenario]["choices"].values())
                choice_index = event.key - pygame.K_1
                if choice_index < len(choices):
                    current_scenario = choices[choice_index]
                    if "item" in scenarios[current_scenario]:
                        item_data = scenarios[current_scenario]["item"]
                        new_item = Item(item_data["name"], item_data["effect"], item_data["value"])
                        player.inventory.append(new_item)
                        print(f"{new_item.name}を取得した！")
                    if current_scenario == "fight_dragon":
                        in_battle = True
                        battle(screen, font, player, enemy)
                        in_battle = False

    if not in_battle:
        update_screen(screen, font, scenarios[current_scenario]["text"], list(scenarios[current_scenario]["choices"].keys()))
    else:
        battle(screen, font, player, enemy)
