import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from queries.core import create_tables, SynchCore, Test
from models import UserModel, TournamentModel

Misha = UserModel(username="Misha", level=2, rating=5, experience=890)
Vitya = UserModel(username="Vitya", level=1, rating=8, experience=970)
Ifmi = UserModel(username="IFMI", level=3, rating=7, experience=150)
tournament_1 = TournamentModel(match_id=3852, stage=2, user1_id=1, user2_id=2)

create_tables()
SynchCore.insert_data_orm("users",username=Misha.username, level=Misha.level, rating=Misha.rating)

SynchCore.insert_data_orm("users",username=Vitya.username, level=Vitya.level, rating=Vitya.rating)

SynchCore.insert_data_orm("users",username=Ifmi.username, level=Ifmi.level, rating=Ifmi.rating)

SynchCore.insert_data_orm("tournaments",match_id=tournament_1.match_id,stage=tournament_1.stage, user1_id=tournament_1.user1_id,user2_id=tournament_1.user2_id)

# print(SynchCore.select_data("users"))
# print(SynchCore.select_data("tournaments"))


Test.tournament_select()