#!/usr/bin/env python3

import os
import time
import threading
import requests
import psutil
import uvicorn
from fastapi import FastAPI

from multiprocessing import Process
import functools
from http.client import HTTPConnection
import time
import json

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

@app.get("/")
async def hello():
    t = threading.Thread(target=killer)
    t.start()
    print("Hello World!!")
    return "Hello World!!"
