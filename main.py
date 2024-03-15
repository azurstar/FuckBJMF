import time
from config import Users, Localtion, Action
from utils import BJMF

for user in Users:
    name, cookie, classID, events = (
        user["name"],
        user["cookie"],
        user["classID"],
        user["events"],
    )

    bjmf = BJMF(cookie, classID)
