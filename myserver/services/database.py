from tinydb import TinyDB, Query
from pydantic import BaseModel

database = TinyDB('database.json')
tokendatabase = TinyDB('tokens.json')

class Item(BaseModel):
    name: str
    age: int

class Token(BaseModel):
    token: str