import pygame
import sys

pygame.init()

#ウィンドウ設定
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Text-Based RPG")

#メインループ
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  #画面の更新
  screen.fill((0, 0, 0))
  pygame.display.flip()