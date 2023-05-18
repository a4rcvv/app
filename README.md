# DRF-Example

Django REST Frameworkのサンプルプロジェクト

## やっていること / やりたいこと

- [x] カスタムUserクラスの導入
- [x] サンプルモデルの追加
- [x] [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/index.html)によるトークン認証の導入
- [x] pytest-djangoの導入
- [x] django-filterの導入
- [x] django-configurationsの導入
- [x] 自動ドキュメント生成 (drf-spectacular)
- [x] DevContainerの導入
- [x] デプロイ用Docker環境 (django + gunicorn + nginx)
- [ ] Makefile整備
- [x] flake8などの整備

## 使い方

### ユーザー作成

APIドキュメント (/api/schema/redoc) を参考にしてください

### アクセストークンの取得

`/api/token`に次の内容をPOST

```json
{
  "email": "hoge@example.com",
  "password": "passpass"
}
```

こんな感じのレスポンスが帰ってくる
```json
{
  "access":"access token",
  "refresh":"refresh token"
}
```

アクセストークンはインメモリで保存，リフレッシュトークンはLocalStorageなどに保存
(LocalStorageへの保存はセキュリティ的にやばいけど...)

### アクセストークンのリフレッシュ

`/api/token/refresh`に次の内容をPOST

```json
{
  "refresh": "refresh token"
}
```

こんな感じのレスポンスが帰ってくる
```json
{
  "access":"access token",
  "refresh":"refresh token"
}
```

古いリフレッシュトークンを無効化する運用も可能(だけどやってない)

### トークンの使用

`Authorization`ヘッダに`Bearer <access token>`をつける

## 開発

### 環境変数

プロジェクトルートに`.env`を作成
```
DJANGO_SECRET_KEY=<任意のキー>
DJANGO_PAGINATION_LIMIT=<int>

POSTGRES_DB=DB名
POSTGRES_USER=DBユーザー
POSTGRES_PASSWORD=DBパスワード
POSTGRES_HOST=db
POSTGRES_PORT=5432

COMPOSE_PROJECT_NAME=drf-example-dev # DevContainerが開発用コンテナを開くようにするための設定
```

### VSCode Dev Container

1. `make build`を実行
2. devContainerを開く

macOSがホストの時にPermission Deniedと表示された場合は権限を見直すと良いかもしれない

参考: [macos - open /Users/[user]/.docker/buildx/current: permission denied on macbook? - Stack Overflow](https://stackoverflow.com/questions/75686903/open-users-user-docker-buildx-current-permission-denied-on-macbook)

### テスト

django通常のテストではなくpytestを使っています．`pytest`で実行できます

### パッケージバージョン

- 今のところ`django=4.1.9`，`djangorestframework=3.14.0`
- DRF`3.15.0`がリリースされたらdjango`4.2`(LTS)をインストールできそう

### よくわかってないこと / 既知の不具合

- devcontainer上でrunserverすると`127.0.0.1:8000`でアクセス可能
- macからwebコンテナにアクセスしてrunserverすると`127.0.0.1:8000`でアクセスできない
  - `runserver 0.0.0.0:8000` で立ち上げる必要がある

## 参考資料

- [Django REST Frameworkでユーザ認証周りのAPIを作る - Qiita](https://qiita.com/xKxAxKx/items/60e8fb93d6bbeebcf065#%E3%83%A2%E3%83%87%E3%83%AB%E3%81%AE%E4%BD%9C%E6%88%90)
- [Docker+Django+Nginx+MySQL+Gunicornで環境構築\~M1Mac対応 - Qiita](https://qiita.com/shun198/items/f6864ef381ed658b5aba#%E5%89%8D%E6%8F%90)
- [djangorestframework - くろのて](https://note.crohaco.net/tags/djangorestframework/page/1/)