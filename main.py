from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    print("hello")
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}