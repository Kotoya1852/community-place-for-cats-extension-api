# コントリビューター向けガイド

[![Python](https://img.shields.io/badge/python-3.10-blue?logo=python)](https://www.python.org/downloads/release/python-3100/)
[![GitHub](https://img.shields.io/github/license/Kotoya1852/community-place-for-cats-extension-api)](https://github.com/Kotoya1852/community-place-for-cats-extension-api/blob/main/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/Kotoya1852/community-place-for-cats-extension-api?logo=github)](https://github.com/Kotoya1852/community-place-for-cats-extension-api/issues?q=is%3Aissue+is%3Aopen+)
[![GitHub release (with filter)](https://img.shields.io/github/v/release/Kotoya1852/community-place-for-cats-extension-api)](https://github.com/Kotoya1852/community-place-for-cats-extension-api/releases/latest)
[![Static Badge](https://img.shields.io/badge/Visual_Stadio_Code-download-blue?logo=visual-studio-code)](https://azure.microsoft.com/ja-jp/products/visual-studio-code)
[![Static Badge](https://img.shields.io/badge/docker-not_upload-red?logo=docker)]()

> **Warning**<br>
> This document is only available in Japanese.

当ドキュメントはコントリビューター向けガイドです。

### 開発環境について
- [Visual Studio Code](https://azure.microsoft.com/ja-jp/products/visual-studio-code) : 最新バージョンを使用してください。
- [python](https://www.python.org/downloads/release/python-3100/) : v3.10.7
- [Django](https://docs.djangoproject.com/ja/4.2/) : [Pipfile](./Pipfile)に記載されているバージョン
- [Git](https://git-scm.com/downloads) : 最新バージョンを使用してください。

### クローンについて
以下のアプリケーションを使用することをお勧めします。
- [Tortoisegit](https://tortoisegit.org/) : 最新バージョンを使用してください。
- [Github Desktop](https://desktop.github.com/) : 最新バージョンを使用してください。

アプリケーションを使用している場合は、アプリケーションのマニュアル通りにクローンしてください。

クローンする場合、以下のコマンドを実行してください。
```
git clone https://github.com/Kotoya1852/community-place-for-cats-extension-api.git --branch <ブランチ名>
```

### 仮想環境構築について
以下ps1ファイルをpowershellで実行すると、仮想環境が構築出来ます。
```
./dev-setup.ps1
```

### 修正ブランチについて
ソースコードなどを修正する場合には必ず、developブランチから修正用ブランチを作成してください。
1. [developブランチ](https://github.com/Kotoya1852/community-place-for-cats-extension-api/tree/develop)を表示
2. 修正用ブランチ名を作成（命名規則：`feature-{Issue番号}-{Githubユーザー名}` 例：`feature-1-Kotoya1852`）
3. 修正用ブランチをクローン or プルをする。

### Issuesについて
Issuesに作成されたチケットを対応することになります。
対応する場合、ステータスラベルを付与してください。

### プルリクエストについて
developブランチにマージするには必ずレビューを実施してください。
レビューイ、レビュワーともに、プルリクエストにはステータスラベルを付与し、状況を管理してください。

### コミットメッセージについて
コミットメッセージは以下のルールに従って記載してください。
※コミット時にcommitlintが自動実行し、コミットメッセージがルールに従っているかをチェックします。

#### 接頭辞について（commitlintチェック対象）
[Conventional Commits](https://www.conventionalcommits.org/ja/v1.0.0/#%e6%a6%82%e8%a6%81)のルールに従ってください

- `feat:`は新機能を追加した際に使用するコミット接頭辞です。
- `fix:`はバグ修正した際に使用するコミット接頭辞です。
- `docs:`はドキュメントを修正した際に使用するコミット接頭辞です。
- `style:`はフォーマッターの適用、リンター対応を行った際に使用するコミット接頭辞です。
- `refactor:`はリファクタリング対応を行った際に使用するコミット接頭辞です。※テストコードは変更しない想定。テストコードのリファクタリングもこのコミット接頭辞に該当するが、`expect()`の引数が変更されることは無い。
- `perf:`はパフォーマンス改善対応を行った際に使用するコミット接頭辞です。
- `test:`はテストコードの追加、修正を行った際に使用するコミット接頭辞です。
- `build:`はビルドシステムや外部依存に関する変更を行った際に使用するコミット接頭辞です。（npm関係）
- `ci:`はCIの設定やスクリプトに関する変更を行った際に使用するコミット接頭辞です。
- `chore:`はその他の修正を行った際に使用するコミット接頭辞です。（例：開発ツールの追加、コマンドの追加等）

例１：
```
feat: #{Issue番号} ログインコンポーネントの新規作成
```

例２：
```
fix: #{Issue番号} 共通関数の不具合修正
```

例３：
```
style: #{Issue番号} 新フォーマッターの適用
```

### コミット時に以下の処理が実行されます
- コミットメッセージチェック（接頭辞チェック）
- フォーマッター適用
- リンターチェック

※コミットメッセージ、リンターでエラーが吐かれた場合、コミットエラーになるので確認してください。
