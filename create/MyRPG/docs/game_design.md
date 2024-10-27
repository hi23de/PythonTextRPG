<!-- ゲーム設計書 -->
# 企画&仕様書

## 命名規則

- ファイル名
  - Pythonファイル(.py)
    - スネークケース
      - `main.py`, `data_loader.py`, `game_config.py`
  - テキストファイル(.txt, .md)
    - スネークケース or 小文字単語(短い場合)
      - `readme.md`, `changelog.txt`, `story_data.txt`
  - YAML, JSONファイル(.yaml, .json)
    - スネークケース
      - `config.yaml`, `game_data.json`, `enemy_stats.yaml`
  - READMEファイル
    - 大文字
      - `README.txt`
    - 慣習的に倣いつつ視認性を向上させるため
- ディレクトリ名
  - スネークケース(小文字のみ)
    - `src`, `data_files`, `assets`, `scripts`, `config_files`
    - 大文字はUnix系のファイルシステムで区別されるので、混乱を避けるために使用を控える
- プロジェクト名
  - パスカルケース
    - `MyGameProject`, `TextAdventureGame`

## ディレクトリ

- `data/`
  - `scenarios/`<br>シナリオデータのディレクトリ
    - `scenario1.json`<br>シナリオ管理用のJSONファイル
  - `yaml_scenarios/`<br>YAML形式のシナリオデータディレクトリ
    - `scenario1.yaml`<br>JSONに変換前のYAMLファイル
- `config/`
  - `config.yaml`<br>設定ファイル(ゲーム・システム設定)
- `tests/`<br>各ファイルのテストスクリプト用のディレクトリ
  - `test_battle_system.py`
  - `test_item_manager.py`
  - `test_character_manager.py`
- `logs/`<br>デバッグログのディレクトリ
- `assets/`<br>画像や音声データのディレクトリ
- `requirements.txt`<br>使用するPythonパッケージをリスト化

## マニュアル

### requirements.txtの記述方法

1. コマンドプロンプトMyRPGフォルダに移動<br>`cd Documents\private\vsCode\create\MyRPG`
2. インストール済みのパッケージをファイルに書き出し<br>`pip freeze > requirements.txt`

使用方法は`README.txt`に記載
