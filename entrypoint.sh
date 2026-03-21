#!/bin/sh
set -e
if [ "$1" = "npm" ]; then
  cd /code && npm install
fi
exec "$@"

