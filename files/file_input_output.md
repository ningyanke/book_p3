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

> | command           | 解释                                 |
> | ----------------- | ---------------------------------- |
> | `file.read()`     | 将文档全部读完,生成一个字符串                    |
> | `file.readline()` | 生成一个迭代器,会以行为单位,迭代完文档,<br>生成一个字符串返回 |
>
> 

