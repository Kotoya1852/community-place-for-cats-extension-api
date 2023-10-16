# 仮想開発環境構築スクリプト（PowerShell用）

# このps1ファイルのフルパスのうち親ディレクトリまでのフルパスを取得して、カレントディレクトリを移動する
$path = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $path

# 仮想開発環境構築
pipenv sync --dev
# pre-commitを有効にする
pipenv run pre-commit install --hook-type commit-msg -f
