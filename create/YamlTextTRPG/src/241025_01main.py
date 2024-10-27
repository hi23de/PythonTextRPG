import json

# シナリオファイルの読み込み
with open('..\scenarios\scenario_poisonedSoup.json', 'r', encoding='utf-8') as file:
    scenarios = json.load(file)

# シナリオの開始
current_scene = "greet"

# メインループ
while True:
    scene = scenarios[current_scene]
    print(scene["text"])

    # 選択肢の表示
    for choice_text, next_scene in scene["choices"].items():
        print(f"- {choice_text}")

    # プレイヤーの選択
    player_choice = input("選択肢を入力してください: ")

    # 入力に対応する次のシーンへ移動
    if player_choice in scene["choices"]:
        current_scene = scene["choices"][player_choice]
    else:
        print("無効な選択肢です。もう一度入力してください。")
