from fastapi import FastAPI

main = FastAPI()

@main.get("/")
def index():
    return "this is the front page"