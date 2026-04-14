from fastapi import FastAPI

app = FastAPI()

def add(a: int, b: int) -> int:
    return a + b

@app.get("/")
def read_root():
    return {"message": "Hello CI/CD 🚀, please be nice."}

@app.get("/add/{a}/{b}")
def add_endpoint(a: int, b: int):
    result = add(a, b)
    return {"result": result}