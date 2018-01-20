## docopt

> [项目地址](https://github.com/docopt/docopt)
>
> 使用python创建一个偏亮的命令行的界面

### 一个简单的例子

> ```python
> # docopt_test2.py
> """Naval Fate.
>  
> Usage:
>   naval_fate.py ship new <name>...
>   naval_fate.py ship <name> move <x> <y> [--speed=<kn>]
>   naval_fate.py ship shoot <x> <y>
>   naval_fate.py mine (set|remove) <x> <y> [--moored | --drifting]
>   naval_fate.py (-h | --help)
>   naval_fate.py --version
>  
> Options:
>   -h --help     Show this screen.
>   --version     Show version.
>   --speed=<kn>  Speed in knots [default: 10].
>   --moored      Moored (anchored) mine.
>   --drifting    Drifting mine.
>  
> """
> from docopt import docopt
>  
> if __name__ == '__main__':
>     arguments = docopt(__doc__, version='Naval Fate 2.0')
>     print(arguments)
> ```

### API

> ```python
> from docopt import docopt
> docopt(doc, argv=None, help=True, version=None, options_first=False)
> ```
>
> `docopt` 需要一个必要和4个可选的参数
>
> - `doc` 可以是一个模块的docstring(`__doc__`) ,或者其他的包含帮助消息的**字符串**,将被`dcoopt` 解析以创建选项解析器,下面是这样的**字符串** 的简单例子
>
>   ```python
>   """Usage: my_program.py [-hso FILE] [--quiet | --verbose] [INPUT ...]
>
>   -h --help    show this
>   -s --sorted  sorted output
>   -o FILE      specify output file [default: ./test.txt]
>   --quiet      print less text
>   --verbose    print more text
>
>   """
>   ```
>
> - `argv` 提供一个可选参数,默认情况下,`docopt` 使用传递给程序的是`sys.arg[1:]` 的参数.
>
> - `help` 默认情况下为`True` ,指定解析器是否应该自动打印帮助消息（以doc形式提供）并终止，以防遇到-h或--help选项（选项应该存在于`usage`模式中）。如果要手动处理-h或--help选项（如其他选项），请设置help = False
>
> - `version` 默认为None，是一个可选的参数，用于指定程序的版本.如果提供了.那么(假设--version 在`Usage`中 提到) 解析器在遇到`--version` 会打印出来并结束.可以是任意可打印对象,一般为字符串.请注意，当docopt设置为自动处理-h，--help和--version选项时，您仍然需要在`Usage` 模式中提及它们以使其工作。此外，为您的用户了解他们。
>
> - options_first，默认为False。如果设置为True将禁止混合选项和位置参数。即在第一个位置参数之后，所有参数将被解释为位置，即使看起来像选项。这可以用于与POSIX的严格兼容性，或者如果你想分配你的参数到其他程序。
>
> 返回值是一个简单的字典,字典的键包含了`options, arguments, commands` ,比如上面的例子
>
> ```bash
> (python35) $ python docopt_test2.py ship Guardian move 100 150 --speed=15
> {'--drifting': False,
>  '--help': False,
>  '--moored': False,
>  '--speed': '15',
>  '--version': False,
>  '<name>': ['Guardian'],
>  '<x>': '100',
>  '<y>': '150',
>  'mine': False,
>  'move': True,
>  'new': False,
>  'remove': False,
>  'set': False,
>  'ship': True,
>  'shoot': False}
> $ python docopt_test2.py --version
> Naval Fate 2.0
>
> ```

### 帮助信息的格式

> 由2部分组成
>
> - `Usage`
>
>   - `Usage: my_program.py [-hso FILE][--quiet | --verbose] [INPUT ...]`
>
> - `Option`
>
>   - ```python
>     -h --help    show this
>     -s --sorted  sorted output
>     -o FILE      specify output file [default: ./test.txt]
>     --quiet      print less text
>     --verbose    print more text
>     ```
>
> 格式如下所示
>
> `Usage` 格式
>
> `Usage` 是`doc` 的子字符串,
>
> - 以`Usage` 开始(不区分大小写,以空行结束),
> - `Usage` 后接的第一个单词,是程序的名字
> - 可以多次指定程序名,使用多个模式(parrerns),每个模式包含以下元素
>   - `<arguments>，ARGUMENTS`。参数被指定为大写字母，例如`my_program.py CONTENT-PATH`或括号括起来的单词：`my_program.py <content-path>`。
>   - `--options`. 选项是以短划线开始的单词(`-`),例如:`--output`, `-o`. 可以几个选项写在一起.例如`-oiv` 等同于`-o -i -v` ,选项可以有参数,比如`--input=FILE` 但是，如果您希望您的选项具有参数，默认值或指定选项的同义短/长版本，则指定选项描述非常重要
>   - `commands` 是不遵循上述的`--options <arguments> ARGUMENTS`惯例的单词 
>
> ```python
> """
> Usage: 
> 	xxx.py FILE
> 	xxx.py  COUNT  FILE
> """
> ```
>
> - 使用以下结构来指定模式：
>   - `[]` 描述可选元素（可选）
>   - `（） `描述必要元素（必需）
>   - `|` 描述互斥元素（互斥）
>   - `......` 描述重复元素（重复）
>
> `Option` 
>
> 由在`Usage`模式下放置的选项列表组成
>
> 有必要列出选项说明，以便指定： 
>
> - 选项是否有长/短形式，如-h，--help
> - 选项后面是否带参数，如--speed =
> - 选项是否有默认值，如[default: 10]
>
> `Example`
>
> 可以指定一个实例来说明

### 自己写一个简单的例子

> ```python
> #!/usr/bin/env python
> # -*- coding: utf-8 -*-
> # @Author: chanafanghua
> # @Date:   2018-01-21 00:40:37
> # @Last Modified by:   chanafanghua
> # @Last Modified time: 2018-01-21 02:49:16
>
>
> """发送文本邮件
> Usage:
>     发送文本邮件.py (-h| --help)
>     发送文本邮件.py user <user> passwd <passwd> from <from> to <to>
>     发送文本邮件.py (-u| --user)
>
> Options:
>     -h --help  # Python 对SMTP支持的有 smtplib 和 email
>                # email 负责构造邮件, smtplib负责发送邮件
>                # 使用基本的流程
>                # 初始化服务器
>                # 登录服务器
>                # 操作服务器
>                # 登出服务器
>     user=None # 用户名
>     passwd=None  # 密码
>     from=None  # 发送者
>     to=None    # 接收者,多个接收者之间用逗号分隔
> """
>
> from docopt import docopt
>
> import smtplib  # 导入发送邮件 smtplib
> from email.mime.text import MIMEText  # 导入接收邮件 email
> import sys
>
>
> def plan1():
>     '''设置服务器所需要的信息'''
>     # gmail 服务器 smtp 地址
>     mail_host = 'smtp.gmail.com'
>     # gmail 用户名
>     mail_user = input("User:")
>     # gmail 密码(如果是qq邮箱则需要授权码)
>     mail_passwd = input('Passwd')
>
>     # 邮件发送方地址
>     sender = input("From:")
>     # 邮件接收方地址 注意需要[]包裹，这意味着可以写多个邮件地址群发
>     receivers = input("To:")  # 可能有多个接收方,接受方之间用逗号分隔
>     receivers = receivers.split(',')
>
>     '''设置email的信息,邮件内容的设置'''
>     # 纯文本发送
>     text = "I love You"  # 指定发送的信息内容
>     subtype = 'plain'  # 指定信息的类型
>     charset = 'utf-8'  # 指定文字编码
>     message = MIMEText(text, subtype, charset)
>
>     # 邮件主题
>     message['Subject'] = u'这是来自gmail的python测试邮件'
>     # 发送方的信息
>     message['From'] = sender
>     # 接收方信息
>     message['To'] = ', '.join(receivers)  # message['To'] 接收的是字符串,如果有多个,需要逗号隔开
>
>     return mail_user, mail_passwd, mail_host, message, sender, receivers
>
>
> def plan2():
>     argments = docopt(__doc__)
>     mail_user = argments['<user>']
>     mail_passwd = argments['<passwd>']
>     sender = argments['<from>']
>     receivers = argments['<to>']
>
>     mail_host = 'smtp.gmail.com'
>     '''设置email的信息,邮件内容的设置'''
>     # 纯文本发送
>     text = "I love You"  # 指定发送的信息内容
>     subtype = 'plain'  # 指定信息的类型
>     charset = 'utf-8'  # 指定文字编码
>
>     message = MIMEText(text, subtype, charset)
>
>     # 邮件主题
>     message['Subject'] = u'这是来自gmail的python测试邮件'
>     # 发送方的信息
>     message['From'] = sender
>     # 接收方信息
>     message['To'] = receivers  # message['To'] 接收的是字符串,如果有多个,需要逗号隔开
>     # print(argments)
>     return mail_passwd, mail_user, sender, receivers, \
>         message, mail_host
>
>
> '''
> def main():
>     plan_2 = plan2()
>     mail_host = plan_2[5]
>     mail_user = plan_2[1]
>     mail_passwd = plan_2[0]
>     sender = plan_2[2]
>     receivers = plan_2[3]
>     message = plan_2[4]
>     print(mail_host, mail_user, mail_passwd,
>           sender, receivers, message)
> '''
>
>
> def main():
>     '''登录并发送邮件'''
>     try:
>         if sys.argv[1]:
>
>             plan_2 = plan2()
>             mail_host = plan_2[5]
>             mail_user = plan_2[1]
>             mail_passwd = plan_2[0]
>             sender = plan_2[2]
>             receivers = plan_2[3]
>             message = plan_2[4]
>             # print(mail_host, mail_user, mail_passwd,
>             #      sender, receivers, message)
>         else:
>             print('start')
>             plan_1 = plan1()
>             mail_host = plan_1[2]
>             mail_user = plan_1[0]
>             mail_passwd = plan_1[1]
>             sender = plan_1[4]
>             receivers = plan_1[5]
>             message = plan_1[3]
>         smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 使用ssl加密传输
>         smtpObj.login(mail_user, mail_passwd)  # 登录到服务器
>         smtpObj.sendmail(
>             sender,  # 发送者
>             receivers,  # 接收者
>             message.as_string()  # 发送的字符串
>         )
>
>         smtpObj.quit()
>         print('发送成功')
>     except Exception as e:
>         print(e)  # 否则打印错误
>
>
> if __name__ == '__main__':
>     main()
>
> ```
>
> 测试文件,可以看出,所有的`arguments`全都可以从字典中获取出来,这就要求
>
> **在Usage 中把想要的参数写全,argument可以写入默认值** ,这只是一种情况

