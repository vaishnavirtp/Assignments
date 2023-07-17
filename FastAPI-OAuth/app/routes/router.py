from fastapi import HTTPException, Depends, APIRouter, Body, status, Request
from typing import Annotated
from app.auth.auth import *
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
import app.models.models as models
from app.database.database import get_db
from sqlalchemy.orm import Session
from decouple import config
from app.schemas.schema import *

from app.utils.exceptions import (
    InvalidIDError,
    InvalidDataError,
    ForbiddenUserError,
)
from fastapi.encoders import jsonable_encoder
from http import HTTPStatus
import bcrypt
from datetime import timedelta
from typing import Annotated
from jose import JWTError, jwt


router = APIRouter()


# ------------------------------ GET ALL SONGS---------------------------------------
@router.get("/")
def get_songs(db: Session = Depends(get_db)):
    return db.query(models.SongDetails).all()


# ------------------------------ GET SONG BY ID---------------------------------------
@router.get("/songs/{id}", tags=["songs"])
def get_song(id: int, db: Session = Depends(get_db)):
    try:
        song = db.query(models.SongDetails).filter(models.SongDetails.id == id).first()
        if song is None:
            raise InvalidIDError(id, "song")
        return song
    except InvalidIDError as e:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST, detail=str(e.get_message())
        )


allow_create_resource = RoleChecker(["admin"])


# ------------------------------CREATE A NEW SONG-----------------------------------------
@router.post(
    "/songs/create/",
    tags=["songs"],
    dependencies=[Depends(allow_create_resource)],
)
def create_song(song: SongDetailSchema, db: Session = Depends(get_db)):
    try:
        json_data = jsonable_encoder(song)
        song_model = models.SongDetails(**json_data)

        db.add(song_model)
        db.commit()
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content="Successfully created a song",
        )

    except ForbiddenUserError as e:
        raise HTTPException(status_code=e.status, detail=str(e.get_message()))


# ------------------------------UPDATE SONG BY ID-----------------------------------------


@router.put(
    "/songs/{song_id}", dependencies=[Depends(get_current_user)], tags=["songs"]
)
def update_song(song_id: str, song: SongUpdateSchema, db: Session = Depends(get_db)):
    try:
        song_model = (
            db.query(models.SongDetails)
            .filter(models.SongDetails.id == song_id)
            .first()
        )
        if song_model is None:
            raise InvalidIDError(song_id, "song")
        song_model.album = song.album
        song_model.title = song.title
        song_model.genre = song.genre

        db.add(song_model)
        db.commit()
        return JSONResponse(
            status_code=status.HTTP_200_OK, content="Successfully updated a song"
        )

    except InvalidIDError as e:
        raise HTTPException(status_code=e.status, detail=str(e.get_message()))


@router.delete(
    "/{song_id}", dependencies=[Depends(allow_create_resource)], tags=["songs"]
)
def delete_song(song_id: str, db: Session = Depends(get_db)):
    try:
        song_model = (
            db.query(models.SongDetails)
            .filter(models.SongDetails.id == song_id)
            .first()
        )
        if song_model is None:
            raise InvalidIDError(song_id, "song")

        db.query(models.SongDetails).filter(models.SongDetails.id == song_id).delete()
        db.commit()
        return JSONResponse(
            status_code=status.HTTP_200_OK, content="Successfully deleted the song."
        )
    except ForbiddenUserError as e:
        raise HTTPException(status_code=e.status, detail=str(e.get_message()))

    except InvalidIDError as e:
        raise HTTPException(status_code=e.status, detail=str(e.get_message()))


@router.delete(
    "/songs/delete-all/", tags=["songs"], dependencies=[Depends(allow_create_resource)]
)
def delete_all(db: Session = Depends(get_db)):
    try:
        db.query(models.SongDetails).delete()
        db.commit()
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content="Successfully deleted all the songs.",
        )
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail=str(e))


# -----------------------------REQUESTS for USER----------------------------------


# GET ALL USERS FROM THE DATABASE
@router.get("/user/", tags=["user"])
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()


@router.get("/user/{user_id}", tags=["user"])
def get_user_songs(user_id: str, db: Session = Depends(get_db)):
    try:
        user_model = db.query(models.User).filter(models.User.id == user_id).first()
        if user_model:
            return user_model.songs
        raise InvalidIDError(user_id, "user")
    except InvalidIDError as e:
        raise HTTPException(status_code=e.status, detail=str(e.get_message()))


#  LOGIN USER
@router.post("/token", response_model=Token, tags=["user"])
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db),
):
    user = (
        db.query(models.User).filter(models.User.username == form_data.username).first()
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not bcrypt.checkpw(form_data.password.encode("utf-8"), user.password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=int(config("ACCESS_TOKEN_EXPIRE_MINUTES")))
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


# SIGN UP OR REGISTER A USER
@router.post("/user/signup", tags=["user"])
def user_signup(user: UserInDB = Body(default=None), db: Session = Depends(get_db)):
    try:
        user_db = (
            db.query(models.User)
            .filter(
                models.User.email == user.email, models.User.username == user.username
            )
            .first()
        )

        if user_db:
            raise HTTPException(
                status_code=400, detail="User with the email and username "
            )
        password_hash = create_hash_password(user.hashed_password)

        user_model = models.User(
            email=user.email,
            password=password_hash,
            full_name=user.full_name,
            username=user.username,
        )
        db.add(user_model)
        db.commit()
        return JSONResponse(
            status_code=status.HTTP_201_CREATED, content=f"Welcome {user.email}"
        )
    except ValueError:
        raise HTTPException(
            status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
            detail="The password should contain minimum 5 charcters",
        )


# UPDATE USER ROLE (Only for admin users)
@router.put("/user/update-role/{user_id}}", tags=["user"])
def update_user_role(
    user_id: int, role: UserUpdateSchema, db: Session = Depends(get_db)
):
    try:
        if role.role not in ["user", "admin"]:
            raise InvalidDataError("The role should be either 'user' or 'admin' ")
        user = db.query(models.User).filter(models.User.id == user_id).first()
        if user:
            user.role = role.role
            db.add(user)
            db.commit()
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content="Successfully updated user role.",
            )
        raise InvalidIDError(user_id, "user")
    except InvalidDataError as e:
        raise HTTPException(status_code=e.status, detail=str(e.get_message()))
    except InvalidIDError as e:
        raise HTTPException(status_code=e.status, detail=str(e.get_message()))


# @router.delete("/user/delete-all/", tags=["user"])
# def delete_all_users(db: Session = Depends(get_db)):
#     try:
#         db.query(models.User).delete()
#         db.commit()
#         return JSONResponse(
#             status_code=status.HTTP_200_OK,
#             content="Successfully deleted all the users.",
#         )
#     except Exception as e:
#         raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail=str(e))
