from sqlalchemy.orm import Session
from . import models, schemas


def get_user(db: Session, user_id: int):
    # Look up a single user by their unique ID
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    # Fetch a user by email (useful for login or checking duplicates)
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    # Get a list of users with simple pagination (skip N, take M)
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    # Create a new user object using the data from the request
    db_user = models.User(
        name=user.name,
        email=user.email,
        phone_number=user.phone_number,
        address=user.address
    )
    # Add the new user to the current database session
    db.add(db_user)
    # Commit = save changes to the database
    db.commit()
    # Refresh ensures we get updated fields (like auto-generated ID)
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: int, user_update: schemas.UserCreate):
    # First, check if the user actually exists
    db_user = get_user(db, user_id=user_id)
    if db_user:
        # Convert the incoming data to a dict, ignoring missing fields
        update_data = user_update.dict(exclude_unset=True)
        # Update each field dynamically
        for key, value in update_data.items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
        return db_user
    # If no user found, return None
    return None


def delete_user(db: Session, user_id: int):
    # Find the user first
    db_user = get_user(db, user_id=user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
        return db_user
    # Nothing to delete if user not found
    return None