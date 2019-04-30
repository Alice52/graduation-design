from django.core.mail import send_mail
from users.models import EmailVerifyCode
from random import choice
from zcEducation.settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_PORT, EMAIL_HOST
import random
import time
from smtplib import SMTP, SMTP_SSL
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


def get_random_code(code_length):
    code_source = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM'
    code = ''
    for i in range(code_length):
        code += choice(code_source)
    return code


def send_email_code(email, send_type):
    # save the info of email and code
    code = get_random_code(20)
    table_email = EmailVerifyCode()
    table_email.email = email
    table_email.send_type = send_type
    table_email.code = code
    table_email.save()

    # send email
    send_title = ''
    send_body = ''
    if send_type == 1:
        send_title = '欢迎注册617室 ZC在线学习平台：'
        receiverlist = [email]
        send_body = '请点击以下链接进行激活您的账号：\n http://www.zc-education.top:8000/users/user_active/' + code + """
                <br>
                <img src="https://t1.hddhhn.com/uploads/tu/201903/195/4554fds.jpg"  alt="美女" />
                """
        send_email1 = SendEmail(subject=send_title, content=send_body, receiver_list=receiverlist)
        send_email1.send_email()

    if send_type == 2:
        receiverlist = [email]
        send_title = '617室 ZC在线学习平台重置密码系统：'
        send_body = '请点击以下链接进行重置您的密码：\n http://127.0.0.1:8000/users/user_reset/' + code + """
                <br>
                <img src="https://t1.hddhhn.com/uploads/tu/201903/195/4554fds.jpg"  alt="美女" />
                """
        send_email1 = SendEmail(subject=send_title, content=send_body, receiver_list=receiverlist)
        send_email1.send_email()

    if send_type == 3:
        receiverlist = [email]
        send_title = '617室 ZC在线学习平台修改邮箱验证码：'
        send_body = '您的验证码是：' + code + """
                <br>
                <img src="https://t1.hddhhn.com/uploads/tu/201903/195/4554fds.jpg"  alt="美女" />
                """
        send_email1 = SendEmail(subject=send_title, content=send_body, receiver_list=receiverlist)
        send_email1.send_email()


class SendEmail(object):
    def __init__(self, receiver_list=None, subject=None, content=None):
        self.stm_server = EMAIL_HOST
        self.send_addr = EMAIL_HOST_USER
        self.password = EMAIL_HOST_PASSWORD
        self.receiver_list = receiver_list
        self.subject = subject
        self.content = content

    def send_email(self):
        email_client = SMTP_SSL(self.stm_server, EMAIL_PORT)
        email_client.login(self.send_addr, self.password)

        try:
            for reveiver in self.receiver_list:
                message = MIMEMultipart()
                message['From'] = self.send_addr
                message['To'] = reveiver
                # subject
                message['Subject'] = Header(self.subject, 'utf-8')
                # content
                message.attach(MIMEText(self.content, 'html', 'utf-8'))

                email_client.sendmail(self.send_addr, reveiver, message.as_string())
                time.sleep(random.randint(1, 3))
        except Exception as e:
            print(e)

        email_client.quit()

#
# from users.models import EmailVerifyCode
# # from random import choice
# from random import randrange, randint
# from django.core.mail import send_mail
# from zcEdocationNoVue.settings import EMAIL_FROM
#
#
# def get_random_code(code_length):
#     code_source = '2134567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
#     code = ''
#     for i in range(code_length):
#         # 随机选择一个字符
#         str = code_source[randrange(0, len(code_source))]
#         code += str
#         # code += choice(code_source)
#     return code
#
#
# def send_email_code(email, send_type):
#     # 第一步：创建邮箱验证码对象，保存数据库，用来以后做对比
#     code = get_random_code(8)
#     a = EmailVerifyCode()
#     a.email = email
#     a.send_type = send_type
#     a.code = code
#     a.save()
#
#     # 第二步：正式的发邮件功能
#     send_title = ''
#     send_body = ''
#     if send_type == 1:
#         send_title = '欢迎注册617室 ZC在线学习平台网站：'
#         send_body = '请点击以下链接进行激活您的账号：\n http://127.0.0.1:8000/users/user_active/' + code
#         send_mail(send_title, send_body, EMAIL_FROM, [email])
#
#     if send_type == 2:
#         send_title = '617室 ZC在线学习平台重置密码系统：'
#         send_body = '请点击以下链接进行重置您的密码：\n http://127.0.0.1:8000/users/user_reset/' + code
#         send_mail(send_title, send_body, EMAIL_FROM, [email])
#
#     if send_type == 3:
#         send_title = '617室 ZC在线学习平台修改邮箱验证码：'
#         send_body = '您的验证码是：' + code
#         send_mail(send_title, send_body, EMAIL_FROM, [email])
