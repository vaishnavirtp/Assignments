from pydantic import BaseModel, Field, EmailStr, SecretStr
from enum import Enum


class SongDetailSchema(BaseModel):
    artist_id: int
    album: str = Field(default=None)
    title: str = Field(default=None)
    genre: str = Field(default=None)

    class Config:
        schema_extra = {
            "song_demo": {
                "artist_id": 1,
                "album": "Purpose",
                "title": "What do you mean",
                "genre": "Acoustic Blues",
            }
        }


class SongUpdateSchema(BaseModel):
    title: str = Field(default=None)
    album: str = Field(default=None)
    genre: str = Field(default=None)


class User(BaseModel):
    username: str
    email: EmailStr = Field(default=None)
    full_name: str = Field(default=None)
    role: str


class UserInDB(User):
    password: str = Field(default=None, min_length=5)


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class UserUpdateSchema(BaseModel):
    role: str

    class Config:
        schema_extra = {"role": "user/admin"}
