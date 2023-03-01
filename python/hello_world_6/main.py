#!/usr/bin/env python3

import uvicorn
from fastapi import FastAPI

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

@app.get("/")
async def hello():
    return "Hello World!!"

uvicorn.run(app, host="127.0.0.1", port=8000)
