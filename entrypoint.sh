#!/bin/sh
set -e
# コンテナ内の /code/node_modules（ボリューム）に Linux 用依存を入れる
cd /code && npm install
exec "$@"
