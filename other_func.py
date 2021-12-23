import time
from db import *


def add_user(user_id, username):
    if username == None:
        username = ""
    data_about_user = select_db("*", "users", f"user_id = {user_id}")
    if data_about_user == []:
        insert_db("users", ("user_id", "username", "time_reg"), (user_id, username, int(time.time())))
    else:
        pass
