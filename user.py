import requests
import time
users = [123,123,123,123] # 设置目标的uid
cookie = "xxxxx" # 设置cookie
login_uid=937218 # 设置自己的UID
csrf-token = "" # 设置csef-token，直接使用getcsrf函数也可以获取
msg = "这是由_YuTian_制作的群发软件，基于了董乐山2020的Bot开源程序"  # 设置发送消息
login_cookie = '__client_id=' + cookie + '; login_referer=https%3A%2F%2Fwww.luogu.com.cn%2F; _uid=' + str(login_uid) # 初始化Login_cookie的值

def getcsrf(login_cookie):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE',
        '_contentOnly': 'WoXiHuanFanQianXing',
        'x-luogu-type': 'content-only',
        'cookie': login_cookie,
        'x-requested-with': 'XMLHttpRequest',
    }
    res2 = requests.get("https://www.luogu.com.cn/", headers=headers)
    res2 = res2.text
    csrftoken = res2.split(
        "<meta name=\"csrf-token\" content=\"")[-1].split("\">")[0]
    return csrftoken
def sendm2(ruid): # 发送程序，基于董乐山2020
    headers2 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        '_contentOnly': 'WoXiHuanFanQianXing',
        'x-luogu-type': 'content-only',
        'cookie': login_cookie,
        'x-requested-with': 'XMLHttpRequest',
        'referer': 'https://www.luogu.com.cn/',
        'x-csrf-token': csrf-token,
        "content-type": "application/json",
    }
    res_send = requests.post("https://www.luogu.com.cn/api/chat/new", headers=headers2, json={"user": ruid, "content": msg})
    if res_send.text != '{"_empty":true}':
        pass
    print('发送信息返回：', res_send.text)
    time.sleep(2)