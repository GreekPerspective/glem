#!/bin/sh

# This script is meant to be invoked via runit (installed in /etc/service/uwsgi/run), not directly

uwsgi --plugin python3 \
      --uid ${UWSGI_UID:100} \
      --gid ${UWSGI_GID:100} \
      --master \
      --socket "127.0.0.1:8888" \
      --wsgi-file /etc/webglem.wsgi \
      --processes ${UWSGI_PROCESSES:-2} \
      --threads ${UWSGI_THREADS:-2} \
      --manage-script-name

