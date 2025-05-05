from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello, World!"}


@app.get("/about")
def about():
    return {"message": "This is the about page."}

@app.get("/blog/{id}")
def show(id: int):
    return {"message": f"This is blog post {id}."}