#!/bin/sh
set -e
nginx -g 'daemon off;' &
exec python main.py