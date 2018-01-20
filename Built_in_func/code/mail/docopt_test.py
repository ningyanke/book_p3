"""发送文本邮件
Usage:
    test.py (-h| --help)
    test.py user <user> passwd <passwd> from <from> to <to>
    test.py (-u| --user)

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

import docopt


if __name__ == '__main__':
    arguments = docopt.docopt(__doc__)
    print(arguments['<user>'])
    print(arguments)
