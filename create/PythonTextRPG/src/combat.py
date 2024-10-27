import pygame
import sys
from utils import draw_text

def draw_battle(screen, font, player, enemy):
    screen.fill((0, 0, 0))
    draw_text(screen, font, f"{player.name}のHP: {player.hp}", 20, 20, 760)
    draw_text(screen, font, f"{enemy.name}のHP: {enemy.hp}", 20, 60, 760)
    draw_text(screen, font, "行動を選んでください (1: 攻撃, 2: 防御, 3: アイテム)", 20, 100, 760)
    pygame.display.flip()

def battle(screen, font, player, enemy):
    in_battle = True
    draw_battle(screen, font, player, enemy)

    while player.hp > 0 and enemy.hp > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    enemy_defeated = enemy.take_damage(player.attack)
                    if enemy_defeated:
                        print(f"{enemy.name}を倒しました！")
                        in_battle = False
                        return
                elif event.key == pygame.K_2:
                    print(f"{player.name}は防御した！")
                elif event.key == pygame.K_3:
                    print("アイテムを使います（仮）")

                player_defeated = player.take_damage(enemy.attack)
                if player_defeated:
                    print(f"{player.name}が倒されました…")
                    in_battle = False
                    return

        draw_battle(screen, font, player, enemy)
