#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: chanafanghua
# @Date:   2018-01-21 00:40:37
# @Last Modified by:   chanafanghua
# @Last Modified time: 2018-01-21 02:49:16


"""发送文本邮件
Usage:
    发送文本邮件.py (-h| --help)
    发送文本邮件.py user <user> passwd <passwd> from <from> to <to>
    发送文本邮件.py (-u| --user)

Options:
    -h --help  # Python 对SMTP支持的有 smtplib 和 email
               # email 负责构造邮件, smtplib负责发送邮件
               # 使用基本的流程
               # 初始化服务器
               # 登录服务器
               # 操作服务器
               # 登出服务器
    user=None # 用户名
    passwd=None  # 密码
    from=None  # 发送者
    to=None    # 接收者,多个接收者之间用逗号分隔
"""

from docopt import docopt

import smtplib  # 导入发送邮件 smtplib
from email.mime.text import MIMEText  # 导入接收邮件 email
import sys


def plan1():
    '''设置服务器所需要的信息'''
    # gmail 服务器 smtp 地址
    mail_host = 'smtp.gmail.com'
    # gmail 用户名
    mail_user = input("User:")
    # gmail 密码(如果是qq邮箱则需要授权码)
    mail_passwd = input('Passwd')

    # 邮件发送方地址
    sender = input("From:")
    # 邮件接收方地址 注意需要[]包裹，这意味着可以写多个邮件地址群发
    receivers = input("To:")  # 可能有多个接收方,接受方之间用逗号分隔
    receivers = receivers.split(',')

    '''设置email的信息,邮件内容的设置'''
    # 纯文本发送
    text = "I love You"  # 指定发送的信息内容
    subtype = 'plain'  # 指定信息的类型
    charset = 'utf-8'  # 指定文字编码
    message = MIMEText(text, subtype, charset)

    # 邮件主题
    message['Subject'] = u'这是来自gmail的python测试邮件'
    # 发送方的信息
    message['From'] = sender
    # 接收方信息
    message['To'] = ', '.join(receivers)  # message['To'] 接收的是字符串,如果有多个,需要逗号隔开

    return mail_user, mail_passwd, mail_host, message, sender, receivers


def plan2():
    argments = docopt(__doc__)
    mail_user = argments['<user>']
    mail_passwd = argments['<passwd>']
    sender = argments['<from>']
    receivers = argments['<to>']

    mail_host = 'smtp.gmail.com'
    '''设置email的信息,邮件内容的设置'''
    # 纯文本发送
    text = "I love You"  # 指定发送的信息内容
    subtype = 'plain'  # 指定信息的类型
    charset = 'utf-8'  # 指定文字编码

    message = MIMEText(text, subtype, charset)

    # 邮件主题
    message['Subject'] = u'这是来自gmail的python测试邮件'
    # 发送方的信息
    message['From'] = sender
    # 接收方信息
    message['To'] = receivers  # message['To'] 接收的是字符串,如果有多个,需要逗号隔开
    # print(argments)
    return mail_passwd, mail_user, sender, receivers, \
        message, mail_host


'''
def main():
    plan_2 = plan2()
    mail_host = plan_2[5]
    mail_user = plan_2[1]
    mail_passwd = plan_2[0]
    sender = plan_2[2]
    receivers = plan_2[3]
    message = plan_2[4]
    print(mail_host, mail_user, mail_passwd,
          sender, receivers, message)
'''


def main():
    '''登录并发送邮件'''
    try:
        if sys.argv[1]:

            plan_2 = plan2()
            mail_host = plan_2[5]
            mail_user = plan_2[1]
            mail_passwd = plan_2[0]
            sender = plan_2[2]
            receivers = plan_2[3]
            message = plan_2[4]
            # print(mail_host, mail_user, mail_passwd,
            #      sender, receivers, message)
        else:
            print('start')
            plan_1 = plan1()
            mail_host = plan_1[2]
            mail_user = plan_1[0]
            mail_passwd = plan_1[1]
            sender = plan_1[4]
            receivers = plan_1[5]
            message = plan_1[3]
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 使用ssl加密传输
        smtpObj.login(mail_user, mail_passwd)  # 登录到服务器
        smtpObj.sendmail(
            sender,  # 发送者
            receivers,  # 接收者
            message.as_string()  # 发送的字符串
        )

        smtpObj.quit()
        print('发送成功')
    except Exception as e:
        print(e)  # 否则打印错误


if __name__ == '__main__':
    main()
