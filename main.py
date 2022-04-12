from fastapi import FastAPI

app = FastAPI()

@app.get("/fast/{id}")
def fast(id:int):
    return {"id":id}

