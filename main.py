from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse,JSONResponse
from starlette.middleware.sessions import SessionMiddleware
import os
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from myserver.communication.email import email_router
from myserver.controllers.authentication import auth_router
from myserver.controllers.register import register_router

origins = [
    "http://127.0.0.1:8000/protected",
    "http://0.0.0.0:8000",
    "http://192.168.68.52:8000",
    "http://192.168.68.52:8000",
    "http://tvsistop.duckdns.org:8000/protected"
    ]

templates = Jinja2Templates(directory="templates")
app = FastAPI()#docs_url=None,redoc_url=None)


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)
app.mount("/static", StaticFiles(directory="templates"), name="static")

# Middleware for sessions
app.add_middleware(SessionMiddleware, secret_key=os.urandom(24))

app.include_router(auth_router, prefix="", tags=["Communication"])
app.include_router(register_router, prefix="", tags=["Register"])
app.include_router(email_router, prefix="", tags=["Communication"])


# Index
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    request.session.clear()
    return templates.TemplateResponse("views/index.html", {"request": request})

@app.exception_handler(404)
async def custom_404_handler(request: Request, exc):
    return JSONResponse(
        status_code=404,
        content={"message": "Page not found. Please check the URL and try again."},
    )




# db = NanoDB('mydatabase.db')
# db.insert({'name': 'John', 'age': 30})
#
# db.insert_many([
#     {'name': 'Alice', 'age': 25},
#     {'name': 'Bob', 'age': 35}
# ])
#
# result = db.find_one({'name': 'John'})
# print(result)
#
# results = db.find({'age': {'$gt': 25}})
# for doc in results:
#     print(doc)









# @app.get('/a')
# def home(request: Request):
#     print('>/')
#     user = request.session.get('user')
#     if user:
#         return JSONResponse(content=user)
#     return RedirectResponse(url='/login')





# @app.get('/abcprotected')
# async def protected():
#     print('abcprotected')

# async def protected(token: str = Depends(oauth2_scheme)):
#     print('>protected')
#     print(f'token {token}')
#     if token not in fake_tokens_db:
#         raise HTTPException(status_code=401, detail="Invalid token")
#     user_data = fake_tokens_db[token]
#     print(f'data :{user_data.get("sub")}')
#     print(f'email: {user_data.get("email")}')
#     return {"Uitdaging": f'Probeer deze site maar te kraken {user_data.get("sub")}',
#             "email": f'{user_data.get("email")}'}

# @app.get('/logout')
# def logout(request: Request):
#     request.session.clear()
#     print(request.session)
#     return RedirectResponse(url='/')


# @app.get("/protected", response_class=HTMLResponse)
# async def protected(request: Request):
#     print(request.session)
#     return templates.TemplateResponse("protected.html", {"request": request})

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
