from fastapi import HTTPException, Depends, APIRouter, Body, status, Request
from fastapi.responses import JSONResponse
import app.models.models as models
from app.database.database import get_db
from sqlalchemy.orm import Session
from app.schemas.schema import (
    SongDetailSchema,
    UserLogin,
    UserSchema,
    SongUpdateSchema,
    UserUpdateSchema,
)
from app.auth.jwt_handler import sign_jwt
from app.auth.jwt_bearer import JwtBearer
from app.utils.exceptions import (
    InvalidIDError,
    InvalidCredentailsError,
    InvalidDataError,
    ForbiddenUserError,
)
from fastapi.encoders import jsonable_encoder
from http import HTTPStatus
import bcrypt

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
        print(song)
        if song is None:
            raise InvalidIDError(id, "song")
        return song
    except InvalidIDError as e:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST, detail=str(e.get_message())
        )
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail=str(e))


# ------------------------------CREATE A NEW SONG-----------------------------------------
@router.post("/songs", dependencies=[Depends(JwtBearer())], tags=["songs"])
def create_song(song: SongDetailSchema, email: str, db: Session = Depends(get_db)):
    try:
        user = db.query(models.User).filter(models.User.email == email).first()
        if user.role != "admin":
            raise ForbiddenUserError(user.id, "create song")
        json_data = jsonable_encoder(song)
        song_model = models.SongDetails(**json_data)

        db.add(song_model)
        db.commit()
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content="Successfully created a song",
        )

    except ForbiddenUserError as e:
        raise HTTPException(status_code=e.set_status(), detail=str(e.get_message()))

    except Exception as e:
        print(e)
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail=str(e))


# ------------------------------UPDATE SONG BY ID-----------------------------------------


@router.put("/songs/{song_id}", dependencies=[Depends(JwtBearer())], tags=["songs"])
def update_song(song_id: str, song: SongUpdateSchema, db: Session = Depends(get_db)):
    try:
        song_model = (
            db.query(models.SongDetails)
            .filter(models.SongDetails.id == song_id)
            .first()
        )
        if song_model is None:
            print("Invalid id")
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
        raise HTTPException(status_code=e.set_status(), detail=str(e.get_message()))
    except Exception as e:
        print(e)
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail=str(e))


@router.delete("/{song_id}", dependencies=[Depends(JwtBearer())], tags=["songs"])
def delete_song(song_id: str, email: str, db: Session = Depends(get_db)):
    try:
        user = db.query(models.User).filter(models.User.email == email).first()
        if user.role != "admin":
            raise ForbiddenUserError(user.id, "create song")
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
        raise HTTPException(status_code=e.set_status(), detail=str(e.get_message()))

    except InvalidIDError as e:
        raise HTTPException(status_code=e.set_status(), detail=str(e.get_message()))
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail=str(e))


@router.delete("/delete-all/")
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
        raise HTTPException(status_code=e.set_status(), detail=str(e.get_message()))


# SIGN UP OR REGISTER A USER
@router.post("/user/signup", tags=["user"])
def user_signup(user: UserSchema = Body(default=None), db: Session = Depends(get_db)):
    try:
        byte_password = user.password.encode("utf-8")
        mySalt = bcrypt.gensalt()
        password_hash = bcrypt.hashpw(byte_password, mySalt)

        user_model = models.User(
            email=user.email, password=password_hash, fullname=user.fullname
        )
        db.add(user_model)
        db.commit()
        return sign_jwt(user.email)
    except ValueError:
        raise HTTPException(
            status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
            detail="The password should contain minimum 5 charcters",
        )
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail=str(e))


# CHECK IF THE USER EXIST OR NOT IN THE DATABASE
def check_user_exist(data: UserLogin, db: Session = Depends(get_db)):
    password = data.password.encode("utf-8")
    user_model = db.query(models.User).filter(models.User.email == data.email).first()
    if user_model and bcrypt.checkpw(password, user_model.password):
        return True
    return False


# LOGIN USER
@router.post("/user/login", tags=["user"])
def user_login(user: UserLogin = Body(default=None), db: Session = Depends(get_db)):
    try:
        if check_user_exist(user, db):
            return sign_jwt(user.email)
        raise InvalidCredentailsError(user.email, user.password)

    except InvalidCredentailsError as e:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED, detail=str(e.get_message())
        )
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail=str(e))


# UPDATE USER ROLE
@router.put("/user/update-role/{user_id}}", tags=["user"])
def update_user_role(
    user_id: int, role: UserUpdateSchema, db: Session = Depends(get_db)
):
    try:
        print(role.role)
        user = db.query(models.User).filter(models.User.id == user_id).first()
        if role.role not in ["user", "admin"]:
            print("in")
            raise InvalidDataError("The role should be either 'user' or 'admin' ")
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
        raise HTTPException(status_code=e.set_status(), detail=str(e.get_message()))
    except InvalidIDError as e:
        raise HTTPException(status_code=e.set_status(), detail=str(e.get_message()))
    except Exception as e:
        print(e)
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail=str(e))


@router.delete("/user/delete-all/", tags=["user"])
def delete_all_users(db: Session = Depends(get_db)):
    try:
        db.query(models.User).delete()
        db.commit()
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content="Successfully deleted all the users.",
        )
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail=str(e))
