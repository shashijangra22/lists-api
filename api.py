from fastapi import FastAPI
from service.ItemService import ItemService
from models.Request import Request
import json

app = FastAPI()

service = ItemService()

@app.get("/{user_id}/items")
def get_items(user_id):
    items = service.get_items(user_id)
    return {
        "results": json.dumps([item.to_dict() for item in items]),
        "error": None
    }

@app.post("/items/send")
def send_item(req: Request):
    service.add_item(req)
    return {
        "error": None
    }