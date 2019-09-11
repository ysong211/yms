import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import redis
import time
import json


def redis_db2():

    # 实现一个连接池,无需重新新建数据库连接
    pool = redis.ConnectionPool(host='192.168.5.11', db=2)
    redis_pool = redis.Redis(connection_pool=pool)
    # 返回当前循环开始时间
    time1 = int(redis_pool.hget("product", "当前循环开始时间").decode('utf-8')) / 1000
    time1 = int(time1)
    getall = redis_pool.hgetall("product")
    print(time1)
    localtime = int(time.time())
    print(localtime)
    if localtime - time1 >= 600:
        print("报错")
        print(getall)


redis_db2()



# def redis_time():
#     l1 = []
#     l2 = []
#     # 实现一个连接池,无需重新新建数据库连接
#     pool = redis.ConnectionPool(host='192.168.5.11', db=2)
#     ip_pool = redis.Redis(connection_pool=pool)
#     # 返回当前循环开始时间
#     time1 = (ip_pool.hget("product", "当前循环开始时间").decode('utf-8'))
#     vals = ip_pool.hvals("product")
#     keys = ip_pool.hkeys("product")
#
#     for val in vals:
#         l1.append(val.decode('utf-8'))
#     for key in keys:
#         l2.append(key.decode('utf-8'))
#     d = dict(zip(l2, l1))
#     return d
#
#
# redis_time()

# # 创建一个带附件的实例
# message = MIMEMultipart()
# # 设置服务器所需信息, 163邮箱服务器地址
# mail_host = 'smtp.163.com'
# # 163用户名
# mail_user = 'ysong211@163.com'
# # 密码(部分邮箱为授权码)
# mail_pass = 'ys15007017422'
# # 邮件发送方邮箱地址
# sender = 'ysong211@163.com'
# # 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
# receivers = ['409643876@qq.com']
# # 设置email信息,邮件正文内容
# message.attach(MIMEText('这里是报错的内容', 'plain', 'utf-8'))
# # 邮件主题
# message['Subject'] = '亚马逊项目报错警告'
# # 发送方信息
# message['From'] = Header("茵卓尔")
# # 接受方信息
# message['To'] = receivers[0]
#
#
# # 构造附件2，传送当前目录下的 runoob.txt 文件
# att2 = MIMEText(open('runoob.txt', 'rb').read(), 'base64', 'utf-8')
# att2["Content-Type"] = 'application/octet-stream'
# att2["Content-Disposition"] = 'attachment; filename="runoob.txt"'
# message.attach(att2)
#
# a = 0
# # 登录并发送邮件
#
# try:
#     if a == 1:
#         smtpObj = smtplib.SMTP()
#         # 连接到服务器
#         smtpObj.connect(mail_host, 25)
#         # 登录到服务器
#         smtpObj.login(mail_user, mail_pass)
#         # 发送
#         smtpObj.sendmail(sender, receivers, message.as_string())
#         # 退出
#         smtpObj.quit()
#         print('success')
#     else:
#         print("+++++++")
# except smtplib.SMTPException as e:
#     # 打印错误
#     print('error', e)