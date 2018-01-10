## glob

> [官网解释](http://python.usyiyi.cn/translate/python_352/library/glob.html#glob.glob)
>
> glob模块使用一个Unix shell规则的字符串查找与其匹配的所有路径, 但返回的结果是无序的。用它可以查找符合特定规则的文件路径名。跟使用windows下的文件搜索差不多。查找文件只用到三个匹配符：`”*”, “?”, “[]“`。”*”匹配0个或多个字符；”?”匹配单个字符；”[]“匹配指定范围内的字符，如：[0-9]匹配数字。

### 常用方法

#### glob.glob

> ```python
> glob.glob(pathname,*,recursive=False)
> #返回一个与pathname匹配的路径组成的list，该list可能为空。
> #pathname可以是绝对路径，也可以是相对路径，
> #pathname包含shell风格的通配符
> #如果 recursive 设置为真，“**” 将匹配所有存在的目录和子目录和任何文件。如果匹配式以 os.sep 结尾, 只对目录和子目录进行匹配。
> ```
>
> ```python
> import glob
>  #获取指定目录下的所有图片
> print glob.glob(r"E:/Picture/*/*.jpg")
>  #获取上级目录的所有.py文件
> print glob.glob(r'../*.py') 
> #相对路径
> ```
>
> 

#### glob.iglob

> ```python 
> glob.iglob([atjma,e.recursive=False])
> #返回一个iterator迭代器，它产生与glob()相同的结果，但不会存储他们
> ```
>
> ```python
> import glob
> f = glob.iglob(r'.../*.py')
> for py in f:
> 	print f 
> ```
>

