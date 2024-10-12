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
