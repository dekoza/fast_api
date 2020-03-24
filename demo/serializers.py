from pydantic import BaseModel


class Item(BaseModel):
    external_id: str
    name: str = None
    value: int = None
