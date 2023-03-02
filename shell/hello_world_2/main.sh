#!/bin/sh

nc -p 8000 -lN << EOF > /dev/null &
HTTP/1.0 200 OK

Hello World!
EOF

curl http://127.0.0.1:8000
