# SO BJMF, FUCK YOU!
我们导员最近在搞一些反人类的神秘集会，所以这个仓库就诞生了

# 功能
- [x] GPS签到
- [x] 扫码签到
- [x] 密码签到(仅手动)
- [x] 多用户
- [x] 定位随机偏移

# 使用
- 安装依赖 `pip install -r requirements.txt`
- [配置](#配置) `config/config.yaml`
- 运行程序
  - 手动签到 `python3 main.py`
  - 自动签到 `python3 main.py run`

# 配置
```yaml
Localtion: # 位置信息
  操场: [1, 2, 3] # 纬度，经度，海拔
  一号教学楼: [1, 2, 3]

Action: # 任务列表(用于自动签到)
  早操签到: # 任务名
    localtion: 操场 # 对应Localtion中的位置信息
    cron: "* 7 * * *" # cron表达式(若与当前时间匹配就会进行签到)
    # 分 时 日 月 星期(croniter不支持秒级)
  上课签到:
    localtion: 一号教学楼
    cron: "* 8-17 * * *"
  晚自习签到:
    localtion: 一号教学楼
    cron: "* 19-20 * * *"

Users: #  用户列表
  - name: 张三 # 用户名(可自定义)
    cookie: "123456" # 微信中班级魔方抓包获得的Cookie(其实就是微信Cookie)
    classID: "123456" # 班级ID(同样是抓包获取)
    events: # 需要执行的事件列表
      - 早操签到
      - 上课签到
  - name: 李四
    cookie: "123456"
    classID: "123456"
    events:
      - 上课签到
      - 晚自习签到

SearchTime: 60 # 获取签到任务的时间间隔(单位:秒)
WriteLog: True # 是否输出日志
Offset: 0.0005 # 经纬度最大偏移量(正实数)
```

# 获取classID和cookie
- 班级魔方尚未使用上先进的https仍然使用着http，所以可以在未配置证书的情况下直接使用httpcanary等手机抓包软件。在微信中打开班级魔方后，在抓包软件里面找到`k8n.cn`即可。

<img src="https://github.com/azurstar/FuckBJMF/assets/91844313/0f491389-9f03-4f0c-a3a2-9a23d35f609d" width="400">
