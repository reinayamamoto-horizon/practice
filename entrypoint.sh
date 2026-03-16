#!/bin/sh
set -e
# vite のときだけ npm install（web は Django のみなのでスキップ）
if [ "$1" = "npm" ]; then
  cd /code && npm install
fi
exec "$@"
