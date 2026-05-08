from typing import Sequence
from sqlalchemy import select, text, update
from sqlalchemy.orm import joinedload
from database_engines import engine, async_engine, session_factory, async_session_factory, Base
from models import UsersORM, TournamentsORM

TABLE_MAP = {
    "users": UsersORM,
    "tournaments": TournamentsORM
}

# def create_tables():
#     Base.metadata.drop_all(engine)
#     Base.metadata.create_all(engine)

# async def async_create_tables():
#     async with async_engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)

def tournament_select():
    with session_factory() as session:
        query = (
            select(TournamentsORM)
            .options(
                joinedload(TournamentsORM.user1),
                joinedload(TournamentsORM.user2),
                joinedload(TournamentsORM.winner)
            )
        )

        res = session.execute(query)
        result = res.scalars().all()

        for tour in result:
            print(f"Match {tour.match_id}: "
                    f"{tour.user1.username} vs {tour.user2.username}")
            if tour.winner: print(f"Winner is: {tour.winner.username}")

async def truncate_tables():
    async with async_engine.begin() as conn:
        tables = [
            table.name for table in Base.metadata.sorted_tables 
            if table.name != 'alembic_version'
        ]

        if tables:
            tables_str = ", ".join(tables)
            query = text(f"TRUNCATE TABLE {tables_str} RESTART IDENTITY CASCADE;")

            await conn.execute(query)
            print(f"{"-" * 8} Successfully truncated: {tables_str} {"-" * 8}")


async def async_tournament_select():
    async with async_session_factory() as session:
        query = (
            select(TournamentsORM)
            .options(
                joinedload(TournamentsORM.user1),
                joinedload(TournamentsORM.user2),
                joinedload(TournamentsORM.winner)
            )
        )

        res = await session.execute(query)
        result = res.scalars().all()

        for tour in result:
            print(f"{"-" * 25}\nMatch {tour.match_id}: "
                    f"{tour.user1.username} vs {tour.user2.username}")
            if tour.winner: print(f"Winner is: {tour.winner.username}")
        print("-" * 25)


class SynchCore:

    @staticmethod
    def _get_model(table_name: str):
        model = TABLE_MAP.get(table_name)
        if not model:
            raise ValueError(f"Таблица {table_name} не зарегистрирована в TABLE_MAP")
        return model
    

    @staticmethod
    def insert_data_orm(table_model: str, **data):
        '''Inserts the data into specified table'''
        model = SynchCore._get_model(table_model)
        with session_factory() as session:
            new_obj = model(**data)
            session.add(new_obj)
            session.commit()

        
    @staticmethod
    def select_data(table_model: str, **filters):
        '''Select all data'''
        model = SynchCore._get_model(table_model)
        with session_factory() as session:
            query = select(model) # SELECT * FROM table_name

            for key, val in filters.items():
                if val is not None:
                    query = query.where(getattr(model, key) == val)

            res = session.scalars(query).all()
            return res
            
            
    @staticmethod
    def update_data(table_name: str, filter_by: dict, **updates):
        model = SynchCore._get_model(table_name)
        with session_factory() as session:
            
            stmt = update(model)
            
            for key, value in filter_by.items():
                stmt = stmt.where(getattr(model, key) == value)
            stmt = stmt.values(**updates)
            
            session.execute(stmt)
            session.commit()

    @staticmethod
    def show_leaderboard():
        with session_factory() as session:
            query = (
                select(UsersORM)
                .order_by(
                    UsersORM.rating.desc(),
                    UsersORM.level.desc()
                )
                .limit(5)
            )
            execution = session.execute(query)
            leaderboard = execution.scalars().all()

            print(f"{leaderboard=}\n")
        

class AsynchCore:

    @staticmethod
    def _get_model(table_name: str):
        model = TABLE_MAP.get(table_name)
        if not model:
            raise ValueError(f"Таблица {table_name} не зарегистрирована в TABLE_MAP")
        return model
    
    @staticmethod
    async def insert_data_orm(table_model: str, **data):
        '''`Inserts the data into specified table`'''
        model = AsynchCore._get_model(table_model)
        async with async_session_factory() as session:
            new_obj = model(**data)
            session.add(new_obj)
            await session.commit()
    
    @staticmethod
    async def select_data(table_model: str, **filters):
        '''Select all data'''
        model = AsynchCore._get_model(table_model)
        async with async_session_factory() as session:
            query = select(model) # SELECT * FROM table_name

            for key, val in filters.items():
                if val is not None:
                    query = query.where(getattr(model, key) == val)

            result = await session.execute(query)
            res = result.scalars().all()
            return res
        
    @staticmethod
    async def update_data(table_name: str, filter_by: dict, **updates):
        model = AsynchCore._get_model(table_name)
        async with async_session_factory() as session:
            
            stmt = update(model)
            
            for key, value in filter_by.items():
                stmt = stmt.where(getattr(model, key) == value)
            stmt = stmt.values(**updates)
            
            await session.execute(stmt)
            await session.commit()

    @staticmethod
    async def show_leaderboard():
        async with async_session_factory() as session:
            query = (
                select(UsersORM)
                .order_by(
                    UsersORM.rating.desc(),
                    UsersORM.level.desc(),
                )
                .limit(5)
            )
            execution = await session.execute(query)
            leaderboard = execution.scalars().all()

            print(f"{leaderboard=}\n")

