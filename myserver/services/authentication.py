from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import Optional

# In-memory storage for users and tokens (for demonstration purposes)
fake_users_db = {
    "Alain": {
        "username": "Alain",
        "full_name": "John Doe",
        "email": "alain.verhoeven1@gmail.com",
        "hashed_password": "fakehashed1234",
    },
    "Adriaan": {
        "username": "Adriaan",
        "full_name": "John Doe",
        "email": "user@example.com",
        "hashed_password": "fakehashed1234",
    }

}

class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

class UserInDB(User):
    hashed_password: str

# OAuth2 password flow
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def fake_hash_password(password: str):
    return "fakehashed" + password


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def fake_decode_token(token):
    # This doesn't provide any security at all
    # Check the next version
    user = get_user(fake_users_db, token)
    return user


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=400, detail="Invalid authentication credentials"
        )
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user




# fake_tokens_db = {}
#
# # OAuth2PasswordBearer instance for token retrieval
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
#
# # Utility functions for user verification
# def fake_hash_password(password: str):
#     return "fakehashed" + password
#
# def verify_password(plain_password, hashed_password):
#     print(fake_hash_password(plain_password))
#     print(hashed_password)
#     return fake_hash_password(plain_password) == hashed_password
#
# def get_user(db, username: str):
#     if username in db:
#         user_dict = db[username]
#         return UserInDB(**user_dict)
#
# def create_access_token(data: dict):
#     token = secrets.token_urlsafe(16)
#     print(f'token ={token}')
#     fake_tokens_db[token] = data
#     return token
#
# # User models
# class User(BaseModel):
#     username: str
#     email: str
#     full_name: Optional[str] = None
#
# class UserInDB(User):
#     hashed_password: str

