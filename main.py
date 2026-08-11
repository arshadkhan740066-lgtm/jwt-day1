from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import model
import schema

from database import engine, get_db
from auth import hash_password


app = FastAPI()


# Create database tables
model.Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {
        "message": "JWT Authentication API"
    }


@app.post("/register")
def register(
    user: schema.UserCreate,
    db: Session = Depends(get_db)
):

    # Hash the user's password
    hashed_password = hash_password(user.password)

    # Create a new User object
    new_user = model.User(
        username=user.username,
        email=user.email,
        password=hashed_password
    )

    # Add user to database
    db.add(new_user)

    # Save changes
    db.commit()

    # Get the newly created user's data
    db.refresh(new_user)

    return {
        "message": "User registered successfully",
        "username": new_user.username,
        "email": new_user.email
    }