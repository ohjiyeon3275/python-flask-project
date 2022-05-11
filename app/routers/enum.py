from fastapi import FastAPI
from enum import Enum

class MyName(str, Enum):
    uh = "oh"
    ah = "yeah"
    oh = "jiyeon"


app = FastAPI()

@app.get("/models/{my_name}", tags=["myNames"])
async def get_model(my_name: MyName):
    if my_name == MyName.oh:
        return {"name": my_name, "message": "key"}

    if my_name.value == "yeah":
        return {"yeahee": my_name, "message": "No Way!"}

    return {"model_name": my_name, "message": "Have some fun"}