## sys	

> | 模块                       | 内容                     |
> | ------------------------ | ---------------------- |
> | sys.argv                 | 生成一个列表,命令行参数           |
> | sys.exit()               | 退出整个程序                 |
> | sys.path                 | 生成一个列表,系统的library存放的目录 |
> | sys.stdin/stdout/stderro | 标准的输入输出,和错误            |
> | sys.models.keys()        | 查找已经导入的模块              |
> | sys.paltform             | 输出当前的平台                |
>
> 1.sys.argv
>
> ```python
> #!/usr/bin/env python
> # coding=utf-8
>
> import sys
>
> # 生成的是一个列表,可以按照索引取值,0位一般是文件名本身
> print('The filname is ', sys.argv[0])
> print('The number of arguments is ', len(sys.argv))
> print('The argument is', str(sys.argv))
>
> ```
>
> 2.sys.exit()
>
> ```python
> #!/usr/bin/env python
> # coding = utf-8
>
> import sys
>
> for i in range(10):
>     if i == 5:
>         #sys.exit()  # 返回systemexit异常,退出了整个程序,可以在exit中添加内容
>         sys.exit("baybay")
>     else:
>         print(i)
> ```
>
> 返回一个有意义的输出
>
> ```python
> import sys
>
> """
> 有意义的退出
> """
>
> for i in range(10):
>     if i == 5:
>         sys.exit("Sorry for exit")
>     else:
>         print(i)
>
> ```
>
> 3.sys.path
>
> 返回一个python查找标准库的列表,包含当前程序
>
> 4.stdout/stdin/stderror
>
> stdin , stdout , 以及 stderr 变量包含与标准 I/O 流对应的流对象. 如果需
> 要更好地控制输出,而 print 不能满足你的要求, 它们就是你所需要的. 你也
> 可以 替换 它们, 这时候你就可以重定向输出和输入到其它设备( device ), 或
> 者以非标准的方式处理它们
>
> ```python
> #!/usr/bin/env python
> # coding=utf-8
>
>
> import sys
>
> class Redirect:
>     def __init__(self, stdout):
>         self.stdout = stdout
>
>     def write(self, s):
>         self.stdout.write(s.lower())
>
> # 重定向标准输出(包括print语句)
> old_stdout = sys.stdout
> sys.stdout = Redirect(sys.stdout)
>
> print("HELLO WORLD")
>
> ```
>
> 也可以重定向输出到文件中
>
> ```python
> >>> f = open("stdout.md", "w")
> >>> sys.stdout = f
> >>> print "Learn Python: From Beginner to Master" #Python 3: print("Learn Pytho
> n: From Beginner to Master")
> >>> f.close()
> ```
>
> 