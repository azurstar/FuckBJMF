import requests
from bs4 import BeautifulSoup


class BJMF:
    server = "k8n.cn"
    UA = "Mozilla/5.0 (Linux; Android 12; PAL-AL00 Build/HUAWEIPAL-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160065 MMWEBSDK/20231202 MMWEBID/1136 MicroMessenger/8.0.47.2560(0x28002F35) WeChat/arm64 Weixin NetType/4G Language/zh_CN ABI/arm64"

    def __init__(self, cookie, classID):
        self.cookie = cookie
        self.classID = classID
        self.headers = self.get_headers(cookie, classID)

    def get_headers(self, cookie, classID):
        return {
            "User-Agent": self.UA,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/wxpic,image/tpg,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "X-Requested-With": "com.tencent.mm",
            "Referer": f"http://k8n.cn/student/course/{classID}",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh-SG;q=0.9,zh;q=0.8,en-SG;q=0.7,en-US;q=0.6,en;q=0.5",
            "Cookie": cookie,
        }

    def getSignID(self):
        url = f"http://{self.server}/student/course/{self.classID}/punchs"
        r = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(r.text, "html.parser")
        soup.findAll("div", "card")
        signID = []
        for i in soup.findAll("div", "card"):
            try: signID.append(i.get("onclick")[10:-1:1])
            except: pass
        return signID

    def signGPS(self, signID, location: list) -> bool:
        url = f"http://{self.server}/student/punchs/course/{self.classID}/{signID}"
        data = {
            "id": signID,
            "lat": location[0],  # 纬度
            "lng": location[1],  # 经度
            "acc": location[2],  # 海拔
            "res": "",
            "gps_addr": "",
        }
        r = requests.post(url, headers=self.headers, data=data)
        print(r.text)
        return "签到成功" in r.text
