from myserver.services.authentication import *
from fastapi import Request,APIRouter

auth_router = APIRouter()


@auth_router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if hashed_password != user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}

@auth_router.post('/auth')
async def auth(request: Request,token = Depends(oauth2_scheme)):
    print(f'>auth toke={token}')
    print(request.headers)



# @auth_router.post("/token")
# async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
#     print('>login_for_access_token')
#     user = get_user(fake_users_db, form_data.username)
#     if not user or not verify_password(form_data.password, user.hashed_password):
#         raise HTTPException(status_code=400, detail="Incorrect username or password")
#     access_token = create_access_token(data={"sub": user.username,"email":user.email})
#     print(f'access_token:{access_token}')
#     return {"access_token": access_token, "token_type": "bearer"}




# @app.post('/auth')
# async def auth(request: Request, username: str = Form(), password: str = Form(), csrf_token: str = Form()):
#     print('>auth')
#     stored_csrf_token = request.session.get('csrf_token')
#     print(f'stored_csrf_token:{stored_csrf_token}')
#     if not stored_csrf_token or stored_csrf_token != csrf_token:
#         raise HTTPException(status_code=400, detail="CSRF token mismatch")
#     user = get_user(fake_users_db, username)
#     print(user)
#     if not user or not verify_password(password, user.hashed_password):
#         raise HTTPException(status_code=400, detail="Incorrect username or password")
#     access_token = create_access_token(data={"sub": user.username})
#     print(f'access_token:{access_token}')
#     request.session['user'] = {"username": user.username, "email": user.email, "full_name": user.full_name, "token": access_token}
#     headers = {
#         'Authorization': f'Bearer {access_token}'
#     }
#     async with httpx.AsyncClient() as client:
#         protected_response = await client.get(url="http://127.0.0.1:8000/protected", headers=headers)
#
#     return {"msg":"data"}
#     #return RedirectResponse(url='/protected', headers=headers)