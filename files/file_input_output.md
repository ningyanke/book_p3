## 文件流读写

> 文件流,类文件对象对象指的是能使用`read()` 和`write()` 方法的对象.

### 文件的基本操作

#### 1.打开文件

> ```python
> open(name[,mode[, buffering]])
> ```
>
> 打开文件有2种方式,
>
> 一种使用`open()` 函数打开文件,但是最后要关闭文件
>
> ```python
> f = open("./test1.txt","r")
> f.close()
> ```
>
> 另外一种是使用上下文管理器`with` ,这种方式不用显式的关闭文件.
>
> ```python
> with open("1.txt",'r') as f:
>     f.read()
>     f.readlines()
> ```

#### 2.文件模式

> | mode   | 描述                    |
> | ------ | --------------------- |
> | `"r" ` | 只读模式                  |
> | `"w"`  | 只写模式,如果文件存在内容,会删除文件内容 |
> | `"a"`  | 追加模式(可添加到其他模式中使用)     |
> | `"+"`  | 读写模式(可添加到其他模式中使用)     |
>
> 为什么要使用二进制
>
> ```python
> In text mode, the default when reading is to convert platform-specific line endings (\n on Unix, \r\n on Windows) to just \n. When writing in text mode, the default is to convert occurrences of \n back to platform-specific line endings. This behind-the-scenes modification to file data is fine for text files, but will corrupt binary data like that in JPEG or EXE files. Be very careful to use binary mode when reading and writing such files.
> ```
>
> 换行符在不同的平台下显示不同.

#### 3.缓冲`buffering`

> 如果参数是0,`I/O` 就是无缓冲的,所有的读写操作都是直接针对硬盘,
>
> 如果参数是1,`I/O` 就是缓冲的,写入到内存,只有`flush` 或者`close` 时候才会写入硬盘
>
> 如果参数大于1: 表示缓冲区的大小.

#### 4.基本文件方法

> | command                     | 解释                                     |
> | --------------------------- | -------------------------------------- |
> | `file.read()`               | 将文档全部读完,生成一个字符串                        |
> | `file.readline()`           | 生成一个迭代器,会以行为单位,迭代完文档,<br>生成一个字符串返回     |
> | `file.readlines()`          | 返回一个列表,文件每一行,为列表的一个元素<br />            |
> | `file.write(sting)`         | 所提供的的参数`string` 会追加到文件中已经存在的地方         |
> | `file.wirtelines(iterable)` | 将一个可迭代对象添加到写入文件<br />程序不会增加新行,需要自己手动添加 |
> | `file.seek(size)`           | 由当前位置移动到偏移量位置                          |
> | `file.tell()`               | 返回程序当前所在的位置                            |
>
> * 注意`file.write()` 和`file.writelines()` ,程序不会增加新行,需要自己手动添加,也就是,如果文件有内容,需要手动移动到文件的末尾,否则会覆盖文件中的内容

#### 5.fileinput

> 这个模块实现了一个辅助类和函数，可以在标准输入或文件列表上快速编写一个循环,可以轻松的遍历文本文件中的所有行:
>
> `fileinput.input()` 是其中最重要的函数,用于返回一个用于 `for` 循环的对象,可以通过使用for循环来读取一个或多个文本文件的所有行
>
> ```python
> fileinput.input(files=None, inplace=False, backup='', bufsize=0, mode='r', openhook=None)
> ```
>
> | 函数         | 描述                                       |
> | ---------- | ---------------------------------------- |
> | `files`    | 文件的路径列表，默认是stdin方式，多文件['1.txt','2.txt',...] |
> | `inplace`  | 是否将标准输出的结果写回文件，默认不取代<br />原地处理           |
> | `backup`   | 备份文件的扩展名，只指定扩展名，如.bak。<br />如果该文件的备份文件已存在，则会自动覆盖。<br />原地处理时,可选把结果写入到备份文件中 |
> | `mode`     | 默认是只读模式                                  |
> | `openhook` | 该钩子用于控制打开的所有文件，比如说编码方式等                  |
>
> `fileinput.filename()` 返回当前文件的名称
>
> `fileinput.lineno()` 返回当前(累积) 的行数
>
> `fileinput.filelineno()` 返回当前文件的行数
>
> `isfirstline()` 检查当前行是否是文件的第一行
>
> `isstdin()`  检查最后一行时候来自sys.stdin
>
> `nextfile()`  关闭当前文件,移动到下一个文件
>
> `close()`  关闭序列
>
> ##### 命令行下遍历
>
> ```bash
> # 执行如下命令,即可对多个文件依次进行遍历操作
> $ python3 some_script.py file1.txt file2.txt file3.txt
>
> # 还可以对提供标准输入的文本进行遍历
> $ cat file.txt | python3 somescript.py
> ```

##### fileinput示例

> 1.原地操作替换并保持副本
>
> ```python
> #!/usr/bin/env python
> # -*- coding: utf-8 -*-
> import fileinput
>
> for line in fileinput.input("file_b.txt", backup='.bak', inplace=1):
>     print(line.replace("中", "zhong"))
> ```
>
> ```bash
> (python35) ningyanke@NYKpython:~/python3_learn/MOOC/week8/model/file$ cat file_b.txt.bak 
> 中国是个伟大国家
> (python35) ningyanke@NYKpython:~/python3_learn/MOOC/week8/model/file$ cat file_b.txt
> zhong国是个伟大国家
> ```
>
> 2.为python脚本添加行号
>
> ```python
> #!/usr/bin/env python
> # -*- coding: utf-8 -*-
> # fileinput_test.py
> import fileinput
>
> # for line in fileinput.input("file_b.txt", backup='.bak', inplace=1):
> #   print(line.replace("中", "zhong"))
>
>
> for line in fileinput(inplace=True):
>     line = line.rstrip()
>     num = fileinput.lineno()
>     print("%-40s # %2i" % (line, num))
> ```
>
> 对文件本身进行遍历操作
>
> ```bash
> # 注意 第二个fileinput.py 是要操作的文件
> $ python3 fileinput_test.py  fileinput_test.py 
> ```
>
> ```python
> #!/usr/bin/env python                    #  1
> # -*- coding: utf-8 -*-                  #  2
> import fileinput                         #  3
>                                          #  4
> # for line in fileinput.input("file_b.txt", backup='.bak', inplace=1): #  5
> #   print(line.replace("中", "zhong"))    #  6
>                                          #  7
>                                          #  8
> for line in fileinput.input(inplace=True): #  9
>     line = line.rstrip()                 # 10
>     num = fileinput.lineno()             # 11
>     print("%-40s # %2i" % (line, num))   # 12
> ```

#### 6.文件迭代器

> 文件对象是可迭代的,这意味着,可以直接对文件对象在for 循环中进行迭代
>
> ```python
> with open(filename) as f:
>     for line in f:
>         print(line)
>
> ```

#### 7.实例

##### 1.文件拷贝

> ```python
> #!/usr/bin/env python
> # coding=utf-8
>
> def main():
>     # 用户输入文件名
>     f1 = input("Enter a souce file:").strip()
>     f2 = input("Enter a souce file:").strip()
>
>     # 打开文件
>     infile = open(f1, 'r')
>     outfile = open(f2, "w")
>
>     # 拷贝数据
>     countLines = countChars = 0
>
>     for line in infile:
>         countLines += 1
>         countChars += len(line)
>         outfile.writelines(line)
>
>     print(countLines, "lines and", countChars, "chars copied")
>
>     infile.close()
>     outfile.close()
>
> if __name__ == "__main__":
>     main()
>
> ```
>
> 执行结果:默认是当前路径
>
> ```bash
> (python35) ningyanke@NYKpython:~/python3_learn/book_p3/files/code$ cat copyfile1.txt 
> I Love You so much
> (python35) ningyanke@NYKpython:~/python3_learn/book_p3/files/code$ cat copyfile2.txt 
> I Love You so much
> ```

##### 2.根据文本文件,绘制`turtle` 图形

> 根据`data.txt` 文件中的内容来绘制图形
>
> ```bash
> # 300前进距离,0/1 向左偏/向右偏,144 角度,(1,0,0) 取色  
> $ cat data.txt 
> 300,0,144,1,0,0
> 300,0,144,0,1,0
> 300,0,144,0,0,1
> 300,0,144,1,1,0
> 300,0,108,0,1,1
> 184,0,72,1,0,1
> 184,0,72,0,0,0
> 184,0,72,0,0,0
> 184,0,72,0,0,0
> 184,0,72,0,0,0
> 184,0,72,0,0,0
> ```
>
> 程序代码
>
> ```python
> #!/usr/bin/env python
> # -*- coding: utf-8 -*-
>
> import turtle
>
> """
> 程序IPO
> I  输入文件中的坐标值
> P  turtle按照文件中的坐标值操作
> O  输出图形
>
> 自顶向下设计
> """
>
>
> class Draw_with_Turtle:
>
>     def __init__(self, color):
>         self.pen = turtle.Turtle()
>         self.color = color
>         pass
>
>     def forward(self, ptx, *color):
>         turtle.setup(800, 600, 0, 0)
>         self.pen.pensize(5)
>         self.pen.down()
>         self.pen.color(*color)
>         self.pen.speed(5)
>         self.pen.forward(ptx)
>
>     def turn(self, dirction, angle):
>         if dirction == 0:
>             self.pen.left(angle)
>         else:
>             self.pen.right(angle)
>
>
> class File_for_Turtle(Draw_with_Turtle):
>
>     def __init__(self, text, color):
>         self.text = open(text, 'r')
>         super(File_for_Turtle, self).__init__(color)
>
>     def file_option(self):
>         result = []
>         for line in self.text:
>             result.append(list(map(float, line.split(","))))
>
>         for i in result:
>             a1, a2, a3, a4, a5, a6 = i
>             self.forward(a1, (a4, a5, a6))
>             self.turn(a2, a3)
>         turtle.mainloop()
>
>     def file_close():
>         return self.text.close()
>
>
> if __name__ == "__main__":
>     file1 = File_for_Turtle("./data.txt", "red")
>     file1.file_option()
>     file1.file_close()
> ```

##### 3.将两个文件合并成一个

> ```bash
> # teleaddressbook.txt
> 姓名      电话号码
> 张三      13331017777
> 李四      13542154212
> 王麻子    13556549653
> 萝莉      13235652326
> 深度      13568265656
> 道康宁    13585659689
> ```
>
> ```bash
> # emialaddressbook.txt
> 姓名      邮箱
> 张三      13331017777@gmail.com
> 李四      13542154212@gmail.com
> 王麻子    13556549653@gmail.com
> 萝莉      13235652326@gmail.com
> 深度      13568265656@gmail.com
> 道康宁    13585659689@gmail.com 
> ```
>
> 合并效果
>
> ```bash
> # addressbook.txt
> 姓名      电话号码     邮箱
> 张三      13331017777     13331017777@gmail.com
> 李四      13542154212     13542154212@gmail.com
> 王麻子    13556549653   13556549653@gmail.com
> 萝莉      13235652326     13235652326@gmail.com
> 深度      13568265656     13568265656@gmail.com
> 道康宁    13585659689   13585659689@gmail.com 
> ```
>
> ```python
> # addressbook.py
> #!/usr/bin/env python 
> # coding=utf-8
>
> file1 = open("teleaddressbook.txt")
> file2 = open("emaladdressbook.txt")
> file3 = open("addressbook.txt", "w")
>
> list1 = file1.readlines()
> list2 = file2.readlines()
>
> mum = 0
> if len(list1) > len(list2):
>     num = len(list1)
> else:
>     num = len(list1)
>
> for i in range(num):
>     b = list2[i].split(" ")[1:]
>     bb = " ".join(b)
>     srt = list1[i].strip("\n") + bb
>
>     print(srt)
>     file3.writelines(iter(srt))
>
> file1.close()
> file2.close()
> file3.close()
> ```

##### 4.统计哈姆雷特中出现的词频最高的10个

> ```python
> #!/usr/bin/env python
> # -*- coding:utf-8 -*-
> # file_name = count_words_10.py
> """
> 这个模块用于返回需要统计的txt文档中出现次数最多的10个单词
> 面向对象:
> 需求是返回一个txt文档中的前10个词频
> 首先,每个txt文档都是一个对象
> 这个文档应该具有方法 Print_txt 来打印出10个词频
> 面向对象也包含面向对象,但是更是工厂.
> 对于文件对象来说;
> 行为
> 方法:
> 打开文件得到全文字符串,
> 操作文件,
>     得到一个可操作字符串:
>         去除标点符号
>         去除大小写
>     生成单词和个数的对照表(字典)
>         对可操作字符串生成列表
>         对生成的列表统计到字典
>         字典是无序序列,转换为有序列表
>     对列表中的前10个元素取出
>
> 关闭文件,
> """
> import string
>
>
> class Cipin:
>     """
>     用于打开/关闭 需要读取的文件
>     """
>
>     def __init__(self, text):
>         """
>         打开文件
>         :param text:
>         """
>         self.text = open(text, 'r')
>
>     def openfile(self):
>         return self.text
>
>     def fileread(self):
>         """
>         返回全部文档的一个字符串
>         :return:
>         """
>         fileread = self.text.read()
>         return fileread
>
>     def closefile(self):
>         """
>         关闭文件
>         :return:
>         """
>         return self.text.close()
>
>         # def __all__(self):
>         #    return ['pptxt']
>
>
> class Cipin_str(Cipin):
>     """
>     用于处理文件: 移除标点符号,转换大小写,和同时移除标点转换大小写
>     """
>
>     def remove_biaodian(self, newsign=""):
>         """
>         移除标点
>         :param newsign:
>         :return:
>         """
>         signtext = string.punctuation + newsign
>         signrepl = "@" * len(signtext)
>         signtable = str.maketrans(signtext, signrepl)
>         return self.fileread().translate(signtable).replace("@", "")
>
>     def changecaptital(self):
>         """
>         转换大小写
>         :return:
>         """
>         return self.fileread().lower()
>
>     def biaodiancapital(self, newsign=""):
>         """
>         同时移除大小写和标点
>         :param newsign:
>         :return:
>         """
>         return self.remove_biaodian(newsign="").lower()
>
>
> class Dict_txt(Cipin_str):
>     """
>     生成单词和出现次数的字典
>     """
>     counts = {}
>
>     def __init__(self, text):
>         self.counts = Dict_txt.counts
>         super(Dict_txt, self).__init__(text)
>
>     def word_dict(self):
>         """
>         返回生成的字典
>         :return:
>         """
>         list_str = self.biaodiancapital(newsign="").split()
>         for word in list_str:
>             if word in Dict_txt.counts:
>                 Dict_txt.counts[word] += 1
>             else:
>                 Dict_txt.counts[word] = 1
>         return self.counts
>
>     def paixu_dict(self):
>         """
>         对生成的字典排序
>         :return:
>         """
>         a = list(self.word_dict().items())
>         print(a)
>         b = sorted(a, key=lambda x: x[1], reverse=True)
>         return b
>         # return list(Dict_txt.counts.items()).sort(key=lambda x: x[1], reverse=True)
>
>
> class Print_txt(Dict_txt):
>     """
>     取出字典中的前10个
>     """
>
>     def __init__(self, text):
>         super(Print_txt, self).__init__(text)
>
>     def pptxt(self):
>         """
>         返回前10个高发词频
>         :return:
>         """
>         # self.word_dict()
>         return "前10个高发词频为:", self.paixu_dict()[0:11]
>
>
> if __name__ == '__main__':
>     #    test1 = Cipin_str("./test1.txt")
>     #    print(test1.changecaptital())
>     #    test1.closefile()
>     #    test2 = Cipin_str("./test1.txt")
>     #    print(test2.biaodiancapital())
>     #    test2.closefile()
>     #    test3 = Dict_txt("./test1.txt")
>     #    print(test3.word_dict())
>     #    # test1.closefile()
>     #    # test1= Dict_txt("./test1.txt")
>     #    print("test3", test3.paixu_dict())
>     #    test3.closefile()
>
>     test4 = Print_txt("./test1.txt")
>     print(Dict_txt.counts)
>     print(test4.pptxt())
>     test4.closefile()
>     # test5 = Print_txt("./hamlet1.txt")
>     # print("test5", test5.pptxt())
>     # test5.closefile()
> ```