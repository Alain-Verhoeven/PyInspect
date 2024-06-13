from fastapi import APIRouter,Request
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="templates")

register_router = APIRouter()

@register_router.post("/register")
async def register(request:Request):
    print('<register>')
    return templates.TemplateResponse("views/index.html", {"request": request})
