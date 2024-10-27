import sys
import json
import pygame

# JSONファイルの読み込み
def load_scenario(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

# テキストの描画（折り返し対応）
def draw_text(screen, font, text, x, y, max_width):
    lines = text.splitlines()
    rendered_lines = []

    for line in lines:
        current_line = ""
        
        for char in line:  # 各行を文字単位で処理
            test_line = current_line + char
            
            # 行の幅がmax_widthを超えないか確認
            if font.size(test_line)[0] <= max_width:
                current_line = test_line  # 行に文字を追加
            else:
                rendered_lines.append(current_line)  # 完成した行を追加
                current_line = char  # 新しい行のために現在の文字を開始
                
        # 最後の行を追加
        if current_line:
            rendered_lines.append(current_line)

    # 各行を描画
    for i, line in enumerate(rendered_lines):
        screen.blit(font.render(line, True, (255, 255, 255)), (x, y + i * 40))

# 画面の更新
def update_screen(screen, font, text, choices):
    screen.fill((0, 0, 0))
    draw_text(screen, font, text, 20, 20, 760)
    screen_height = screen.get_height()
    text_lines = text.splitlines()
    text_height = len(text_lines) * 40
    choice_start_y = screen_height - (len(choices) * 40) - 20
    for i, choice in enumerate(choices):
        draw_text(screen, font, f"{i + 1}. {choice}", 20, choice_start_y + i * 40, 760)
    pygame.display.flip()

# メイン関数
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Text Adventure")
    font = pygame.font.SysFont("Bizudgothic", 36)

    # シナリオの読み込み
    scenario = load_scenario('..\scenarios\scenario_poisonedSoup.json')
    current_scene = "greet"

    # メインループ
    running = True
    while running:
        # 現在のシーンのテキストと選択肢を取得
        scene_data = scenario[current_scene]
        current_text = scene_data["text"].replace("\\n", "\n")
        choices = scene_data["choices"]

        update_screen(screen, font, current_text, choices)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            # キー入力で選択肢を処理
            if event.type == pygame.KEYDOWN:
                if pygame.K_1 <= event.key <= pygame.K_9:
                    choice_index = event.key - pygame.K_1
                    if choice_index < len(choices):
                        selected_choice = list(choices.values())[choice_index]
                        if selected_choice in scenario:
                            current_scene = selected_choice
                        else:
                            print(f"シナリオ '{selected_choice}' が見つかりません")
    
    pygame.quit()

if __name__ == "__main__":
    main()
