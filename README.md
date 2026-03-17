# practice

Django と MySQL を使った Web アプリケーションの練習用プロジェクトです。


## ブランチ運用

### stagingブランチからチェックしてください
`staging　→ git checkout -b add_new_branch`

### pushは自分で作成したブランチに向かって行ってください
`push origin add_new_branch`

**mainブランチには反映しないでください！**

### プルリクを作成したら他の人にレビューをもらいましょう！
プルリクはstagingに向かって行いましょう

## 技術スタック

- Python 3.12
- Django 5.0+
- MySQL 8.0（Docker 利用時）
- Docker / Docker Compose

## ディレクトリ概要

- `config/` — Django のプロジェクト設定（settings, urls, wsgi, asgi）
- `manage.py` — Django の管理用 CLI エントリポイント

## 必要環境

- Python 3.12
- （Docker 利用時）Docker / Docker Compose
- （ローカルで MySQL を使う場合）MySQL 8.0

## 環境変数

Docker の DB サービス用に、`.env.example` をコピーして `.env` を作成し、以下を設定してください。

| 変数名 | 説明 |
|--------|------|
| `MYSQL_DATABASE` | データベース名 |
| `MYSQL_USER` | DB ユーザー名 |
| `MYSQL_PASSWORD` | DB パスワード |
| `MYSQL_ROOT_PASSWORD` | root パスワード |

```bash
cp .env.example .env
# .env を編集して値を設定
```

## 操作コマンド

### Docker で起動する場合

```bash
# バックグラウンドで DB + Web 起動
docker compose up -d

# ビルドして起動
docker compose up --build

# イメージを再ビルドして起動
docker compose build --no-cache

# 停止・削除
docker compose down
```

- アプリ: http://localhost:8000
- 管理画面: http://localhost:8000/admin/

### Docker 内で Django コマンドを実行する場合

```bash
# マイグレーション適用
docker compose exec web python manage.py migrate

# 管理ユーザー作成
docker compose exec web python manage.py createsuperuser

# マイグレーション作成（アプリ追加後など）
docker compose exec web python manage.py makemigrations

# 新しいアプリを作成する際に使用するコマンド
docker compose exec web python manage.py startapp アプリ名
```

### Vite 開発サーバー（別コンテナ）

`vite` サービスで Vite が常時起動します。`docker compose up` で Django (9000) と Vite (5173) が両方動きます。

```bash
# 通常の起動で OK（web + vite が立ち上がる）
docker compose up -d

# 初回または @rollup/rollup-linux-arm64-gnu エラーが出た場合のみ:
docker compose down
docker volume rm practice_web_node_modules 2>/dev/null || true
docker compose build --no-cache
docker compose up -d
```

- Django: http://localhost:9000/
- Vite: http://localhost:5173/

### ローカルで実行する場合（venv + SQLite）

```bash
# 仮想環境の作成と有効化
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 依存関係インストール
pip install -r requirements.txt

# マイグレーション適用
python manage.py migrate

# 開発サーバー起動
python manage.py runserver

```

- アプリ: http://127.0.0.1:8000/

### よく使う Django コマンド

| コマンド | 説明 |
|----------|------|
| `python manage.py runserver` | 開発サーバー起動 |
| `python manage.py migrate` | マイグレーション適用 |
| `python manage.py makemigrations` | マイグレーション作成 |
| `python manage.py createsuperuser` | 管理ユーザー作成 |
| `python manage.py shell` | Django shell |

Docker 利用時は `python manage.py` の前に `docker-compose exec web` を付けて実行してください。



## 注意点

- 現在の `config/settings.py` では `DATABASES` に SQLite が指定されています。Docker で MySQL を使う場合は、`python-dotenv` で `.env` を読み込み、環境変数から `DATABASES` を組み立てるように設定を変更する必要があります。


## エイリアスの設定

`nano ~/.zshrc`
または、
`nano ~/.bashrc`
に以下を指定すると`dcu` `dcm` などのコマンドが使用できる

```
alias dcu='docker compose up -d'
alias dcw='docker compose exec web'
alias dcm='docker compose exec web python manage.py'
```
