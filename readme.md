# 即席蔵書管理アプリ

本アプリケーションは、2023年6月25日に富山IT勉強会で開発されたものです。このアプリケーションは、ChatGPTによって作成されたDjangoの即席アプリケーションで、主な機能として本の蔵書管理が可能です。

## 必要条件
- Docker
- Docker Compose
- Git

## インストールおよび起動手順

1. GitHubからプロジェクトをcloneします。

```bash
git clone git@github.com:smpi-un/ToyamaITBenkyokaiDjango.git
```

2. プロジェクトのルートディレクトリに移動します。

```bash
cd ToyamaITBenkyokaiDjango
```

3. Docker Composeを使用してアプリケーションとその依存関係を起動します。

```bash
docker-compose up
```

4. 新しいターミナルウィンドウを開き、Docker Composeを使用してDjangoコンテナのシェルにアクセスします。

```bash
docker-compose exec web bash
```

5. マイグレーションを適用します。

```bash
python manage.py migrate
```

6. Djangoの管理インターフェースを使用してユーザーを作成します。

```bash
python manage.py createsuperuser
```

その後、表示されるプロンプトに従ってユーザ名とパスワードを設定します。

7. ログインします。ブラウザを開き、`http://localhost:8000/admin/`にアクセスします。先ほど作成したスーパーユーザーのユーザー名とパスワードを入力してログインします。

これで、http://localhost:8000/hello/books/ にアクセスすると、アプリケーションの画面が表示されます。この画面表示はユーザがログインした状態を前提としています。

## 注意事項

本README.mdはAI（OpenAIのChatGPT）によって作成されました。具体的な操作手順や設定内容は、利用環境やプロジェクトの要件により適宜調整してください。