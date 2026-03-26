import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from queries.core import create_tables, insert_data_orm
from models import User, Tournament

user_1 = User(username="Misha", level=2, rating=5)
user_2 = User(username="Vitya", level=1, rating=8)
tournament_1 = Tournament(match_id=3852, stage=2, user1_id=1, user2_id=2)

create_tables()
insert_data_orm("users",user_name=user_1.username, level_arg=user_1.level, rating_arg=user_1.rating)

insert_data_orm("users",user_name=user_2.username, level_arg=user_2.level, rating_arg=user_2.rating)

insert_data_orm("tournaments",match_id_arg=tournament_1.match_id,stage_arg=tournament_1.stage, user1_id_arg=tournament_1.user1_id,user2_id_arg=tournament_1.user2_id)