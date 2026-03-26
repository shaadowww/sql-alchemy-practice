from database_engines import engine, session_factory, Base
from models import UsersORM, TournamentsORM
from datetime import datetime

def create_tables():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

def insert_data_orm(
        table: str, *, user_name: str | None = None, level_arg: int | None = None, rating_arg: int | None = None, match_id_arg: int | None = None, stage_arg: int | None = None, 
        user1_id_arg: int | None = None, user2_id_arg: int | None = None, winner_id_arg: int | None = None, date_arg: datetime | None = None
        ):
    new_user = UsersORM(username=user_name,level=level_arg, rating=rating_arg)
    new_tournament = TournamentsORM(match_id=match_id_arg, stage=stage_arg, user1_id=user1_id_arg, user2_id=user2_id_arg, winner_id=winner_id_arg, date=date_arg)

    match table:
        case "users":
            with session_factory() as session:
                session.add(new_user)
                session.commit()
        case "tournaments":
            with session_factory() as session:
                session.add(new_tournament)
                session.commit()
        case _: 
            print("No such table")