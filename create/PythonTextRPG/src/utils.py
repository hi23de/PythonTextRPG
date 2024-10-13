import sys
import pygame

def draw_text(screen, font, text, x, y, max_width):
    words = text
    lines = []
    current_line = ""

    for char in words:
        test_line = current_line + char
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = char
    lines.append(current_line)
    
    for i, line in enumerate(lines):
        screen.blit(font.render(line, True, (255, 255, 255)), (x, y + i * 40))

def update_screen(screen, font, text, choices):
    screen.fill((0, 0, 0))
    draw_text(screen, font, text, 20, 20, 760)
    for i, choice in enumerate(choices):
        draw_text(screen, font, f"{i + 1}. {choice}", 20, 100 + i * 40, 760)
    pygame.display.flip()
