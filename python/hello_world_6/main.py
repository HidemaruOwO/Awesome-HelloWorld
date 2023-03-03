import uvicorn
from fastapi import FastAPI

from multiprocessing import Process
import functools
from http.client import HTTPConnection
import time
import json

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

host = '127.0.0.1'
port = 8000

@app.get("/")
async def hello():
    return "Hello World!!"

p = Process(target=functools.partial(uvicorn.run, app, host=host, port=port, log_level='error'))

p.start()
time.sleep(1)

conn = HTTPConnection(host=host, port=port)
conn.request('GET', '/')
response = conn.getresponse()
data = json.loads(response.read().decode())

print(data)

p.kill()

