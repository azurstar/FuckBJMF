# FuckBJMF
## SO BJMF(班级魔方), FUCK YOU!
我们导员最近在搞一些反人类的神秘集会，所以这个仓库就诞生了
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
    cron: "* * 7 * * *" # cron表达式(若与当前时间匹配就会进行签到)
  上课签到:
    localtion: 一号教学楼
    cron: "* * 8-17 * * *"
  晚自习签到:
    localtion: 一号教学楼
    cron: "* * 19-20 * * *"

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
```
# 获取classID和cookie
![039f37ceeffaf8153097b1fdefbc2770](https://github.com/azurstar/FuckBJMF/assets/91844313/0f491389-9f03-4f0c-a3a2-9a23d35f609d)

# 已解决
- GPS签到
- 扫码签到
- 多用户
# 待解决
- 密码签到
- 完善README
