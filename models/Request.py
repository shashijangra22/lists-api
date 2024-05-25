from pydantic import BaseModel

class Request(BaseModel):
    user: str
    content: str
    added_by: str