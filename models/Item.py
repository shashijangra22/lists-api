class Item:
    def __init__(self, id, content, added_by):
        self.__id = id
        self.__content = content
        self.__state = "UNREAD"
        self.__from = added_by
    
    def __mark_as_read(self):
        self.__state = "READ"
        
    def to_dict(self):
        return {
            'id': self.__id,
            'content': self.__content,
            'state': self.__state,
            'from': self.__from
        }
