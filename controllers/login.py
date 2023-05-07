
from controllers.router import router
from fastapi import Depends
from services import user_service
from controllers.authentication import (
    get_password_hash,authenticate_user,create_access_token,verify_password
)
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


# User registration
@router.post("/api/v1/register",tags = ["LMS"])
def register_user(username: str, password: str, role: str):
    hashed_password = get_password_hash(password)
    return user_service.register_user(username, hashed_password, role)


# User login and generate JWT token

@router.post("/api/v1/token", tags=["LMS"])
def login_for_access_token(username:str, password:str):
    user = authenticate_user(username, password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@router.delete("/api/v1/delete",tags=["LMS"])
def delete_all_users():
    pass
    

