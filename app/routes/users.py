
from fastapi import APIRouter, HTTPException, Header
from passlib.context import CryptContext
from jose import jwt

from app.schemas import UserCreate
from app.database import SessionLocal
from app.models import User

router = APIRouter()

SECRET_KEY = "mysecretkey123"
ALGORITHM = "HS256"

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

@router.post("/register")
def register(user: UserCreate):

    db = SessionLocal()

    hashed_password = pwd_context.hash(user.password)

    role = "user"

    if user.username == "admin":
        role = "admin"

    new_user = User(
        username=user.username,
        password=hashed_password,
        role=role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    db.close()

    return {
        "message": "User registered",
        "username": new_user.username
    }

@router.get("/users")
def get_users():

    db = SessionLocal()

    users = db.query(User).all()

    result = []

    for user in users:
        result.append({
            "id": user.id,
            "username": user.username
        })

    db.close()

    return result

@router.post("/login")
def login(user: UserCreate):

    db = SessionLocal()

    target = db.query(User).filter(
        User.username == user.username
    ).first()

    if not target:
        db.close()
        raise HTTPException(
            status_code=401,
            detail="Invalid username"
        )

    if not pwd_context.verify(
        user.password,
        target.password
    ):
        db.close()
        raise HTTPException(
            status_code=401,
            detail="Invalid password"
        )

    token = jwt.encode(
        {
            "sub": target.username,
            "role": target.role
        },
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    db.close()

    return {
        "access_token": token,
        "token_type": "bearer"
    }

@router.get("/me")
def me(authorization: str = Header(None)):

    if not authorization:
        raise HTTPException(
            status_code=401,
            detail="Missing token"
        )

    token = authorization.replace("Bearer ", "")

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username = payload["sub"]
        role = payload["role"]

        return {
            "username": username,
            "role": role
        }

    except:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

@router.delete("/users/{user_id}")
def delete_user(user_id: int):

    db = SessionLocal()

    target = db.query(User).filter(
        User.id == user_id
    ).first()

    if not target:
        db.close()
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    db.delete(target)
    db.commit()
    db.close()

    return {"message": "User deleted"}
