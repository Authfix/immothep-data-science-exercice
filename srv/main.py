from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def welcome_message():
    return { "welcome-message": "Hello World From Azure" }

@app.get("/api/estimates/{surface}")
def estimate(surface: int):
    return { "estimation": 2000, "surface": surface }