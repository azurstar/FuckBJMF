from croniter import croniter
import time, datetime, threading
from config import Users, Localtion, Action, SearchTime
from utils import BJMF


def getSleepTime(cron: str):
    now = int(time.time())
    iter = croniter(cron, now)
    return iter.get_next() - now


def printTimeMsg(msg: str):
    print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}")


def thread(name: str, cron: str, event: str, classID: str, bjmf: BJMF, localtion: list):
    printTimeMsg(f"{name}({classID}) {event} 开始签到任务监测")
    while True:
        time.sleep(getSleepTime(cron))
        signID = bjmf.getSignID()
        if signID:
            printTimeMsg(f"{name}({classID}) {event} 发现签到任务 {signID}")
        for id in signID:
            msg = bjmf.signGPS_QR(id, localtion)
            printTimeMsg(f"{name}({classID}) {event} {id}: {msg}")
        time.sleep(SearchTime)


def main():
    for user in Users:
        name, cookie, classID, events = (
            user["name"],
            user["cookie"],
            user["classID"],
            user["events"],
        )
        bjmf = BJMF(cookie, classID)
        for event in events:
            act = Action[event]
            localtion, cron = Localtion[act["localtion"]], act["cron"]
            threading.Thread(target=thread, args=(name, cron, event, classID, bjmf, localtion)).start()
            time.sleep(0.1)


if __name__ == "__main__":
    main()
