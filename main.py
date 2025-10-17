from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World!"}

print("This is a sample FastAPI application.")