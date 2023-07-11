from sqlalchemy import Column, Integer, String, DATE, Boolean
from app.database.database import Base


class Tasks(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String)
    description = Column(String)
    priority = Column(String)
    start_date = Column(DATE)
    end_date = Column(DATE)
    status = Column(Boolean)
