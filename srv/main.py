from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def welcome_message():
    return { "welcome-message": "Hello World" }

@app.get("/api/estimates/{surface}")
def estimate(surface: int):
    return { "estimation": 2000, "surface": surface }