from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    print("hello")
    return {"greeting": "BYE", "message": "Welcome to FastAPI!"}