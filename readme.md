# 即席蔵書管理アプリ

このリポジトリは、6/25(日)に富山IT勉強会で開発したChatGPTによるDjangoの即席アプリケーションのコードです。アプリケーションの主な機能は本の蔵書管理です。

## 機能

- 本の蔵書管理：新しい本を追加、蔵書一覧を表示、既存の本を更新または削除できます。

## インストールと起動

このアプリケーションはDockerを使用しています。Dockerがローカルマシンにインストールされていることを確認してください。Dockerがインストールされていない場合は、公式の[Dockerインストールガイド](https://docs.docker.com/get-docker/)に従って設定してください。

1. リポジトリをクローンします：

    ```
    git clone git@github.com:smpi-un/ToyamaITBenkyokaiDjango.git
    ```

2. Docker Composeを使ってアプリケーションを起動します：

    ```
    cd ChatGPT-Django-Book-Manager
    docker-compose up
    ```

3. ブラウザで[http://localhost:8000/hello/books/](http://localhost:8000/hello/books/)にアクセスします。ここでアプリケーションの蔵書管理インターフェースを見ることができます。

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細については、[LICENSE](LICENSE)を参照してください。
