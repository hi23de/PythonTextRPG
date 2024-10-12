import pygame
import sys
import json
from combat import Character, battle

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

def draw_text(text, x, y):
  lines = text.split('\n')
  for i, line in enumerate(lines):
    screen.blit(font.render(line, True, (255, 255, 255)), (x, y + i * 40))

player = Character("プレイヤー", 100, 20)
enemy = Character("ドラゴン", 80, 15)

# メインループ
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_1:
        choices = list(scenarios[current_scenario]["choices"].values())
        if choices:
          current_scenario = choices[0]
          if current_scenario == "fight_dragon":
            battle(player, enemy)
      elif event.key == pygame.K_2:
        choices = list(scenarios[current_scenario]["choices"].values())
        if len(choices) > 1:
          current_scenario = choices[1]

  #画面の更新
  screen.fill((0, 0, 0))
  draw_text(scenarios[current_scenario]["text"], 20, 20)

  choices = list(scenarios[current_scenario]["choices"].keys())
  for i, choice in enumerate(choices):
    draw_text(f"{i + 1}.{choice}", 20, 100 + i * 40)

  pygame.display.flip()