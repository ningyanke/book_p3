###  `__name__`函数属性详解

#### `if __name__ == '__main__'`



> ```python
> '__main__' is the name of the scope in which top-level code executes. A module’s __name__ is set equal to '__main__' when read from standard input, a script, or from an interactive prompt.
>
> A module can discover whether or not it is running in the main scope by checking its own __name__, which allows a common idiom for conditionally executing code in a module when it is run as a script or with python -m but not when it is imported:
>
> if __name__ == "__main__":
>     # execute only if run as a script
>     main()
> For a package, the same effect can be achieved by including a __main__.py module, the contents of which will be executed when the module is run with -m.
> ```
>
> [官方文档](https://docs.python.org/3/library/__main__.html)

> ##### `if __name__ == "__main__"` 作用

> `if __name__ == "__main__"` 这句话,这是用来方便我们进行代码复用的,我们可以在其他脚本中方便的调用另外一个脚本里的函数.
>
> 模块是对象,并且所有的模块都有一个内置的属性`__name__` ,一个模块的`__name__`的值取决于你如何应用模块.如果`import`一个模块,那么模块的`__name__`的名字通常为模块的文件名,不带路径或者文件扩展名,但是你可以想一个标准模块一样直接运行,在这种情况下,`__name__`的值将是缺省名`__main__`
>
> #####   `__main__`
>
> 这个属性是顶级环境中的.比如我们我们运行Python解释器,它的顶级名就是`__main__`
>
> ```python
> ningyanke@ningpython:~/python3_file$ ipython3
> Python 3.5.2 (default, Sep 14 2017, 22:51:06) 
> Type "copyright", "credits" or "license" for more information.
>
> IPython 2.4.1 -- An enhanced Interactive Python.
> ?         -> Introduction and overview of IPython's features.
> %quickref -> Quick reference.
> help      -> Python's own help system.
> object?   -> Details about 'object', use 'object??' for extra details.
>
> In [1]: __name__
> Out[1]: '__main__'
> ```
>
> ####  示例解析
>
> 先看一个这样的问题,假设我有下面有一个Python代码.叫做:`pysysinfo.py`
>
> ```python
> #!/usr/bin/env python
> # coding=utf-8
> #pysysinfo.py
> # A system  information gathering script
>
> import subprocess
> #commond1
> #这段代码是用来查询系统信息的
> uname = 'uname'
> uname_arg = "-a"
> print("gathering system information with %s command:\n" % uname)
> subprocess.call([uname,uname_arg])
> #commond2
> #这段代码是查询磁盘分区使用情况的
> diskspace = "df"
> diskspace_arg = '-h'
> print("gathering diskpace information %s command:\n" % diskspace)
> subprocess.call([diskspace,diskspace_arg])
> ```
>
> 如果我们只想使用`command1`查询系统的信息,最好的方法是把上面的代码封装成一个模块,然后通过模块调用其中的函数.这样可以方便我们在不同的文件中多次调用这个模块,而又不用重新编写代码:
>
> ```python
> #!/usr/bin/env python
> # coding=utf-8
> #pysysinfo.py
> # A system  information gathering script
>
> import subprocess
> #commond1
> #这段代码是用来查询系统信息的
> #将其封装成为模块
> def uname_func():
>     uname = 'uname'
>     uname_arg = "-a"
>     print("gathering system information with %s command:\n" % uname)
>     subprocess.call([uname,uname_arg])
> #commond2
> #这段代码是查询磁盘分区使用情况的
> def disk_func():
>     diskspace = "df"
>     diskspace_arg = '-h'
>     print("gathering diskpace information %s command:\n" % diskspace)
>     subprocess.call([diskspace,diskspace_arg])
> #main function that call other functions
> def main():
>     uname_func()
>     disk_func()
>
> #main()
> ```
>
> 现在的问题是,我们如何让系统知道,我们到底是要这个文件直接运行的结果,还是只是作为一个模块引用到其他的脚本中呢?`.py`文件有两种使用方式,一种是直接运行,另外一种是作为模块导入其他的文件.这里引入`if __name__ == '__main__'` 这个判断条件:
>
> ```python
> #!/usr/bin/env python
> # coding=utf-8
> #pysysinfo.py
> # A system  information gathering script
>
> import subprocess
> #commond1
> #这段代码是用来查询系统信息的
> #将其封装成为模块
> def uname_func():
>     uname = 'uname'
>     uname_arg = "-a"
>     print("gathering system information with %s command:\n" % uname)
>     subprocess.call([uname,uname_arg])
> #commond2
> #这段代码是查询磁盘分区使用情况的
> def disk_func():
>     diskspace = "df"
>     diskspace_arg = '-h'
>     print("gathering diskpace information %s command:\n" % diskspace)
>     subprocess.call([diskspace,diskspace_arg])
> #main function that call other functions
> def main():
>     uname_func()
>     disk_func()
> if __name__ == '__main__':
>     main()
> ```
>
> 这样在模块应用到不同的情况下时:
>
> ```python
> #1作为文件直接运行,输出的结果,是因为文件的 __name__ 匹配了 __main__
> Linux ningpython 4.4.0-57-generic #78-Ubuntu SMP Fri Dec 9 23:46:51 UTC 2016 i686 i686 i686 GNU/Linux
> gathering diskpace information df command:
>
> 文件系统        容量  已用  可用 已用% 挂载点
> udev            990M     0  990M    0% /dev
> tmpfs           202M   22M  180M   11% /run
> /dev/sda1        57G  5.5G   49G   11% /
> tmpfs          1007M   14M  993M    2% /dev/shm
> tmpfs           5.0M  4.0K  5.0M    1% /run/lock
> tmpfs          1007M     0 1007M    0% /sys/fs/cgroup
> tmpfs           202M   60K  202M    1% /run/user/1000
> #作为模块直接导入, __name__ 显示的是自己的文件名
> ningyanke@ningpython:~/python3_file$ ipython3
> Python 3.5.2 (default, Sep 14 2017, 22:51:06) 
>
> In [1]: import pysysinfo
>
> In [2]: pysysinfo.__name__
> Out[2]: 'pysysinfo'
> ```

#### 参考链接`stackoverflow`

> [What does if __name__ == “__main__”: do?](https://stackoverflow.com/questions/419163/what-does-if-name-main-do/26369628#26369628)
>
> [What is  __main____.py](https://stackoverflow.com/questions/4042905/what-is-main-py)

