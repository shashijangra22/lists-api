from collections import defaultdict
from models.Item import Item

class ItemService:
    def __init__(self) -> None:
        self.__items = defaultdict(list)
        self.__id = 0
        
    def get_items(self, id):
        print(f"getting items of: {id}")
        return self.__items[id]
    
    def add_item(self, req):
        self.__id+=1
        self.__items[req.user].append(Item(self.__id, req.content, req.added_by))