# privateMaker

## ❓About
プライベートチャンネルを作成するためのDiscord Bot

## 🎮Command
### `/mkch`
コマンドの発信者と特定のロールのみ閲覧可能なテキストチャンネルを作成します。
#### 設定
##### CHANNEL_PREFIX
作成チャンネル名の先頭につける文字列
##### CHANNEL_CATEGORY
チャンネルを追加するカテゴリ
##### CHANNEL_READABLE_ROLES
チャンネルを閲覧可能なロール


## 🚗How to Run
1. Discord Botを作成し、チャンネルに招待します→[ドキュメント](https://discordpy.readthedocs.io/ja/latest/discord.html)
    - トークンを控えておきます
    - "**チャンネルの管理**", "**ロールの管理**"の権限が必要です
1. トークンを設定します
    1. Botの実行環境で、環境変数`DISCORD_TOKEN`の値を設定します
    1. または、プロジェクト直下の`.env.example`を`.env`にリネームし、`DISCORD_TOKEN`の値を設定します
1. 依存パッケージをインストールし、`main.py`を実行します
```shell
pip install -r requirements.txt
python ./main.py
```