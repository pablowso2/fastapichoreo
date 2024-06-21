from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

@app.get("/items/")
async def read_item():
    return ["1", "2","3"]


