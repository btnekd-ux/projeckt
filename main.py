from fastapi import FastAPI

import uvicorn  # pyright: ignore[reportMissingImports]

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}





