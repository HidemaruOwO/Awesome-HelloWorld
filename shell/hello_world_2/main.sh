#!/usr/bin/env bash

nc -p 8000 -lN << EOF > /dev/null &
HTTP/1.0 200 OK

Hello World!
EOF

curl http://localhost:8000
