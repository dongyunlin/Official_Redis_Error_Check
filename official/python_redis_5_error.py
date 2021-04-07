# coding:utf-8
# file: python_redis_5_error.py
import zmail
import redis

r = redis.Redis(
    host="47.108.150.133",
    password="pdOfredis@miss",
    db=5,
    port=6379
)

redis_05_keys = r.keys()
save_data = set()

for key in redis_05_keys:
    key2 = key.decode().strip()
    data = r.get(key2)

    value = eval(data.decode('utf-8'))  # 将获取到的str转为dict

    redis_Fibonacci = value.get("Client-Fibonacci")  # 获取Client-Fibonacci
    # Fibonacci_dict = value["Client-Fibonacci"]  # 获取Client-Fibonacci
    redis_msg = value.get("msg")  # 获取msg

    save_data.add(redis_msg)

    if redis_Fibonacci == "" or redis_msg == "error:参数'Client-Fibonacci'的值为空":
        pass
    else:
        print(f"{key2}:{redis_msg, redis_Fibonacci}")

print(save_data)

# 邮件内容
msg_content = {
    "subject": "线上监控:斐波拉契值是否存在异常",
    "content_text": f"{save_data}",
}

# 收件人
receiver = 'cloudyl_yo@163.com'

# 发件人
sender = {'username': '775260452@qq.com', 'pwd': "xzkybuajdstcbfic"}
name = sender.get('username')
pwd = sender.get('pwd')

# 发送邮件
server = zmail.server(name, pwd)
server.send_mail(receiver, msg_content)  # 收件人，发送内容
