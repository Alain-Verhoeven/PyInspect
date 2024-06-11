from fastapi import APIRouter,Request
from fastapi.templating import Jinja2Templates

from server.services.register import *

templates = Jinja2Templates(directory="templates")

register_router = APIRouter()

@register_router.post("/register")
async def register(request:Request):
    print('<register>')
    return templates.TemplateResponse("views/register.html", {"request": request})
