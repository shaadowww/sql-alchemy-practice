import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from queries.core import create_tables, SynchCore, Test
from models import UserModel, TournamentModel

Misha = UserModel(username="Misha", level=2, rating=9, experience=890)
Vitya = UserModel(username="Vitya", level=5, rating=8, experience=970)
Ifmi = UserModel(username="IFMI", level=10, rating=5, experience=150)
artyom = UserModel(username="Artyom", level=3, rating=15, experience=540)
tournament_1 = TournamentModel(match_id=3852, stage=2, user1_id=1, user2_id=2)

create_tables()
SynchCore.insert_data_orm("users",username=Misha.username, level=Misha.level, rating=Misha.rating, experience=Misha.experience)

SynchCore.insert_data_orm("users",username=Vitya.username, level=Vitya.level, rating=Vitya.rating, experience=Vitya.experience)

SynchCore.insert_data_orm("users",username=Ifmi.username, level=Ifmi.level, rating=Ifmi.rating, experience=Ifmi.experience)

SynchCore.insert_data_orm("users",username=artyom.username, level=artyom.level, rating=artyom.rating, experience=artyom.experience)

SynchCore.insert_data_orm("tournaments",match_id=tournament_1.match_id,stage=tournament_1.stage, user1_id=tournament_1.user1_id,user2_id=tournament_1.user2_id)


SynchCore.show_leaderboard()
Test.tournament_select()