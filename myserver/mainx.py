from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Mocking user data
fake_users_db = {
    "Alain": {
        "username": "Alain",
        "full_name": "Alain Verhoeven",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedpassword",
        "disabled": False,
    }
}

# Define models
class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

class UserInDB(User):
    hashed_password: str

# OAuth2 Password flow for authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Dependency to get current user
async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_users_db.get(token)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

# Mock CSRF token generation (you would use a more secure method)
def generate_csrf_token():
    return "fakecsrf_token"

# Dependency to verify CSRF token
async def verify_csrf_token(request: Request):
    csrf_token = request.headers.get("X-CSRF-Token")
    if not csrf_token or csrf_token != generate_csrf_token():
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="CSRF token missing or invalid",
        )

# Routes
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user = UserInDB(**user_dict)
    # Here you would validate the password, but for simplicity, I'm skipping it
    return {"access_token": user.username, "token_type": "bearer"}

@app.get("/users/me")
async def read_users_me(
    request: Request,
    current_user: User = Depends(get_current_user),
    csrf_token: str = Depends(verify_csrf_token)):
    return current_user
