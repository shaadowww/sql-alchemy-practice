from typing import Optional

from sqlalchemy import select, update
from database_engines import engine, session_factory, Base
from models import UsersORM, TournamentsORM

TABLE_MAP = {
    "users": UsersORM,
    "tournaments": TournamentsORM
}

def create_tables():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

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
            