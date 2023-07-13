from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.database import Base, engine
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    email = Column(String)
    fullname = Column(String)
    password = Column(String)
    role = Column(String, default="user")

    songs = relationship("SongDetails", back_populates="artist", cascade="all, delete")


class SongDetails(Base):
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    album = Column(String)
    title = Column(String)
    genre = Column(String)
    artist_id = Column(Integer, ForeignKey("users.id"))

    artist = relationship("User", back_populates="songs")


# Create all tables
Base.metadata.create_all(bind=engine)
