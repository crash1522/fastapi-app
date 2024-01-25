from fastapi import APIRouter, HTTPException, status
from models.users import User, UserSignIn

user_router = APIRouter (
    tags=["User"],
)
users = {}

@user_router.post("/signup")
async def sign_new_user(data: User) -> dict:
    if data.email in users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username already exists"
        )
    users[data.email] = data
    return {
        "message": "User Successfully registered!"
    }

@user_router.post("/signin")
async def sign_user_in(user: UserSignIn) -> dict:
    if user.email not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exists"
        )
    if user.password != users[user.email].password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Wrong credential passed"
        )
    
    return {
        "message": "User signed in succssfully"
    }
