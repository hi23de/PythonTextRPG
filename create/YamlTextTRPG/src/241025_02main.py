# -*- coding: utf-8 -*-
import pygame
import json
import sys

# シナリオファイルの読み込み
with open('..\scenarios\scenario_poisonedSoup.json', 'r', encoding='utf-8') as file:
    scenarios = json.load(file)

# 初期化
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("毒入りスープ")
font = pygame.font.SysFont("Bizudgothic", 36)

# 現在のシーン
current_scene = "greet"

# テキストを画面に描画
def draw_text(screen, text, position):
    for i, line in enumerate(text.splitlines()):
        rendered_text = font.render(line, True, (255, 255, 255))
        screen.blit(rendered_text, (position[0], position[1] + i * 40))

# 選択肢を画面に描画
def draw_choices(screen, choices):
    for i, choice_text in enumerate(choices, start=1):
        choice_text_render = font.render(f"{i}. {choice_text}", True, (255, 255, 255))
        screen.blit(choice_text_render, (50, 400 + i * 40))

# メインループ
running = True
while running:
    screen.fill((0, 0, 0))  # 画面を黒でクリア
    scene = scenarios[current_scene]

    # テキストと選択肢の描画
    draw_text(screen, scene["text"], (50, 50))
    draw_choices(screen, scene["choices"].keys())

    pygame.display.flip()

    # イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

        # キー入力処理
        if event.type == pygame.KEYDOWN:
            if pygame.K_1 <= event.key <= pygame.K_9:
                # 数字キーの入力を選択肢のインデックスに変換
                choice_index = event.key - pygame.K_1
                choices = list(scene["choices"].values())

                # 選択肢が有効な範囲内かを確認
                if choice_index < len(choices):
                    current_scene = choices[choice_index]

# 終了処理
pygame.quit()
