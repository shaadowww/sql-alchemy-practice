from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column
from pydantic import BaseModel, PositiveInt, Field
from database_engines import Base
from typing import Annotated
from datetime import datetime

class User(BaseModel):
    username: str = Field(max_length=15)
    level: PositiveInt
    rating: PositiveInt

class Tournament(BaseModel):

    match_id: PositiveInt = Field(ge=1000, le=9999)
    stage: PositiveInt = Field(ge=1, le=10)
    user1_id: int
    user2_id: int
    winner_id: PositiveInt | None = None
    

# imperative style
# users_table = Table(
#     "users",
#     metadata_obj,
#     Column("id", Integer, primary_key=True),
#     Column("username", String),
#     Column("level", Integer),
#     Column("rating", Integer)
# )
# declarative style
#-------------------------------------------------------------------------------

intforeign = Annotated[int, mapped_column(ForeignKey("users.id"))]

class UsersORM(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    level: Mapped[int]
    rating: Mapped[int]


class TournamentsORM(Base):
    __tablename__ = "tournaments"
    tournament_id: Mapped[int] = mapped_column(primary_key=True)
    match_id: Mapped[int]
    stage: Mapped[int]
    user1_id: Mapped[intforeign]
    user2_id: Mapped[intforeign]
    winner_id: Mapped[intforeign | None]
    date: Mapped[datetime | None] = mapped_column(server_default=text("TIMEZONE ('utc-2', now())"))