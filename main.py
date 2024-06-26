from croniter import croniter
import time, datetime, threading, sys
from config import Users, Localtion, Action, SearchTime, WriteLog, Offset
from utils import BJMF


def getSleepTime(cron: str):
    now = int(time.time()) + 8 * 60 * 60  # croniter默认utc时间
    iter = croniter(cron, now)
    return iter.get_next() - now


def wirteLog(msg: str):
    with open("run.log", "a", encoding="utf-8") as f:
        f.write(msg + "\n")


def printTimeMsg(msg: str):
    s = f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}"
    print(s)
    if WriteLog:
        wirteLog(s)


def thread(name: str, cron: str, event: str, classID, bjmf: BJMF, localtion: list):
    printTimeMsg(f"{name}({classID}) {event} 开始签到任务监测")
    while True:
        time.sleep(getSleepTime(cron))
        signID = bjmf.getSignID()
        if signID:
            printTimeMsg(f"{name}({classID}) {event} 发现签到任务 {signID}")
        for id in signID:
            msg = bjmf.sign(id, localtion)
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
            localtion[0] += Offset()
            localtion[1] += Offset()
            threading.Thread(
                target=thread, args=(name, cron, event, classID, bjmf, localtion)
            ).start()
            time.sleep(0.1)


def printBanner(msg="手动签到"):
    print("\033c", end="")
    print(msg)


def control():
    while True:
        printBanner()
        for user in Users:
            print(f"{Users.index(user)}.{user['name']}({user['classID']})")
        print("-1.退出")
        index = int(input("选择一个用户: "))
        if index == -1:
            exit()
        user = Users[index]
        name, cookie, classID = (
            user["name"],
            user["cookie"],
            user["classID"],
        )
        bjmf = BJMF(cookie, classID)
        signID = bjmf.getSignID()
        if signID:
            printTimeMsg(f"{name}({classID}) 发现签到任务。")
        else:
            printTimeMsg(f"{name}({classID}) 没有签到任务。")
            break
        printBanner()
        for id in signID:
            print(f"{signID.index(id)}.{user['name']}({user['classID']}): {id}")
        id = signID[int(input("选择一个签到任务: "))]
        printBanner()
        for localtion in Localtion:
            print(f"{list(Localtion.keys()).index(localtion)}: {localtion}")
        localtion = Localtion[list(Localtion.keys())[int(input("选择一个签到地点: "))]]
        localtion[0] += Offset()
        localtion[1] += Offset()
        pwd = input("输入签到密码(没有密码直接回车): ")
        msg = bjmf.sign(id, localtion, pwd)
        printTimeMsg(f"{name}({classID}) {id}: {msg}")
        input("按回车键继续...")


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) > 1:
        if argv[1] == "run":
            main()
    else:
        control()
