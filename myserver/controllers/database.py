from fastapi import APIRouter,HTTPException

from myserver.services.database import *

database_router = APIRouter()

@database_router.post("/tokens/")
async def create_item(token: Token):
    tokendatabase.insert(token.dict())
    return {"message": "Item created successfully"}

@database_router.post("/items/")
async def create_item(item: Item):
    database.insert(item.dict())
    return {"message": "Item created successfully"}

@database_router.get("/items/{name}")
async def read_item(name: str):
    User = Query()
    item = database.search(User.name == name)
    if item:
        return item[0]
    raise HTTPException(status_code=404, detail="Item not found")

@database_router.put("/items/{name}")
async def update_item(name: str, item: Item):
    User = Query()
    updated = database.update(item.dict(), User.name == name)
    if updated:
        return {"message": "Item updated successfully"}
    raise HTTPException(status_code=404, detail="Item not found")

@database_router.delete("/items/{name}")
async def delete_item(name: str):
    User = Query()
    deleted = database.remove(User.name == name)
    if deleted:
        return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")

@database_router.get("/items/")
async def read_items():
    items = database.all()
    return items